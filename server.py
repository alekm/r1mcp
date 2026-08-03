#!/usr/bin/env python3
"""RUCKUS One MCP Server — exposes R1 API docs and live API calls as tools."""

import base64
import json
import os
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv(Path(__file__).parent / ".env")

CLIENT_ID = os.environ.get("R1_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("R1_CLIENT_SECRET", "")
TENANT_ID = os.environ.get("R1_TENANT_ID", "")
REGION = os.environ.get("R1_REGION", "na").lower()
MSP_ID = os.environ.get("R1_MSP_ID", "")
DOCS_PATH = Path(os.environ.get("R1_DOCS_PATH", Path(__file__).parent / "llm-docs"))
NOTES_PATH = Path(os.environ.get("R1_NOTES_PATH", Path(__file__).parent / "field-notes"))

# A fleet-scale query is hundreds of KB and will swallow a context window.
MAX_RESPONSE_CHARS = int(os.environ.get("R1_MAX_RESPONSE_CHARS", "40000"))
TIMEOUT = float(os.environ.get("R1_TIMEOUT", "30"))
MAX_RETRIES = int(os.environ.get("R1_MAX_RETRIES", "3"))

# The two paging conventions that work. Which one an endpoint wants is not
# derivable from the spec, and sending the wrong one fails silently.
_CONVENTIONS = (("page", "pageSize", 1), ("page", "size", 0))

# Keys R1 uses for the row list and the true total across its query endpoints.
_LIST_KEYS = ("data", "content", "items", "results", "list")
_TOTAL_KEYS = ("totalCount", "totalElements", "total", "totalRows")

REGION_HOSTS = {
    "na": "https://api.ruckus.cloud",
    "eu": "https://api.eu.ruckus.cloud",
    "asia": "https://api.asia.ruckus.cloud",
}
BASE_URL = REGION_HOSTS.get(REGION, REGION_HOSTS["na"])


def _general_notes() -> str:
    """Cross-cutting field notes, injected into the server instructions."""
    general = NOTES_PATH / "GENERAL.md"
    return general.read_text() if general.exists() else ""


# field-notes/GENERAL.md rides in the server instructions so the silent-failure
# modes are in context before the model makes its first call — by the time it
# would think to look them up, it has already been handed a wrong answer.
_INSTRUCTIONS = """\
Tools for the RUCKUS One cloud WiFi management API.

Discovery flow: r1_list_groups -> r1_get_docs(group) -> r1_call(...).

The notes below are verified against a live tenant and are NOT in the API spec.
They describe failures that return 2xx with plausible but wrong data. Apply them
to every call. Per-group notes come back with r1_get_docs, or via r1_field_notes.

"""


def _group_notes(slug: str) -> str:
    """Field notes for one API group, or '' if none exist."""
    f = NOTES_PATH / f"{slug}.md"
    if slug in {"GENERAL", "README"} or not f.exists():
        return ""
    return f.read_text()


mcp = FastMCP("ruckus-one", instructions=_INSTRUCTIONS + _general_notes())

# In-process token cache: (access_token, expires_at)
_token_cache: tuple[str, float] = ("", 0.0)


def _request_token(client: httpx.Client, path: str, data: dict, headers: dict) -> tuple[str, int]:
    """Make one token request attempt. Returns (access_token, expires_in)."""
    resp = client.post(
        BASE_URL + path,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded", **headers},
    )
    # Some R1 deployments return the token in a response header instead of the body
    header_token = resp.headers.get("login-token") or resp.headers.get("Login-Token")
    if resp.status_code == 200 and header_token:
        return header_token, 3600
    resp.raise_for_status()
    payload = resp.json()
    return payload["access_token"], int(payload.get("expires_in", 3600))


def _get_token() -> str:
    """Return a valid Bearer token, fetching a new one via OAuth2 if needed."""
    global _token_cache
    token, expires_at = _token_cache
    if token and time.time() < expires_at - 30:
        return token

    if not all([CLIENT_ID, CLIENT_SECRET, TENANT_ID]):
        raise RuntimeError("R1_CLIENT_ID, R1_CLIENT_SECRET, and R1_TENANT_ID must all be set in .env")

    tenant_path = f"/oauth2/token/{TENANT_ID}"
    basic = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    attempts = [
        # Preferred: credentials in form body, tenant-scoped endpoint
        (tenant_path, {"grant_type": "client_credentials", "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}, {}),
        # Fallback: HTTP Basic auth, tenant-scoped endpoint
        (tenant_path, {"grant_type": "client_credentials"}, {"Authorization": f"Basic {basic}"}),
        # Alternative: credentials in form body, bare endpoint (no tenant in path)
        ("/oauth2/token", {"grant_type": "client_credentials", "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}, {}),
    ]

    last_err: Exception = RuntimeError("No attempts made")
    with httpx.Client(timeout=15) as client:
        for path, data, headers in attempts:
            try:
                access_token, expires_in = _request_token(client, path, data, headers)
                expires_in = max(60, expires_in)
                _token_cache = (access_token, time.time() + expires_in - 30)
                return access_token
            except Exception as e:
                last_err = e
                continue

    raise RuntimeError(f"Authentication failed: {last_err}")


@mcp.tool()
def r1_list_groups() -> str:
    """
    List all available RUCKUS One API groups and their endpoint counts.
    Use this first to understand what parts of the API exist before diving deeper.
    """
    index = DOCS_PATH / "INDEX.md"
    if not index.exists():
        return f"ERROR: INDEX.md not found at {index}"

    annotated = sorted(
        p.stem for p in NOTES_PATH.glob("*.md") if p.stem not in {"GENERAL", "README"}
    )
    footer = ""
    if annotated:
        footer = (
            "\n\n---\n\n## Groups with field notes\n\n"
            "These have verified real-world behavior that the generated docs above do not "
            "capture — broken endpoints, silent failures, destructive semantics. "
            "`r1_get_docs` returns them automatically:\n\n"
            + "\n".join(f"- `{g}`" for g in annotated)
        )
    return index.read_text() + footer


@mcp.tool()
def r1_get_docs(group: str) -> str:
    """
    Get full API documentation for a specific RUCKUS One API group.
    Use r1_list_groups first to see available group names.

    Args:
        group: The group slug, e.g. 'wifi-services', 'switch-services', 'venues',
               'tenant-management', 'events-and-alarms', etc.
    """
    slug = group.strip().lower().replace(" ", "-").replace("_", "-")
    doc_file = DOCS_PATH / f"{slug}.md"
    if not doc_file.exists():
        available = sorted(p.stem for p in DOCS_PATH.glob("*.md") if p.stem != "INDEX")
        return (
            f"ERROR: No docs found for '{group}' (tried {doc_file.name}).\n"
            f"Available groups: {', '.join(available)}"
        )

    text = doc_file.read_text()
    notes = _group_notes(slug)
    if notes:
        text += (
            "\n\n---\n\n"
            "# ⚠ FIELD NOTES — verified against a live tenant\n\n"
            "Not in the API spec. Where these contradict the generated documentation "
            "above, **the field notes are correct** — they were observed on a real "
            "system.\n\n"
            + notes
        )
    return text


def _async_hint(status: int, data) -> str:
    """
    A 202 means the write was accepted, not applied. The returned requestId is an
    activity ID — undocumented, and true of ~653 operations in the spec. Point the
    caller at the follow-up rather than letting it assume success.
    """
    if status != 202 or not isinstance(data, dict):
        return ""
    request_id = data.get("requestId") or data.get("id")
    if not request_id:
        return ""
    return (
        f"\n\n⚠ NOT YET APPLIED — this 202 means accepted, not done.\n"
        f"'{request_id}' is an activity ID. Confirm before reporting success or "
        f"re-reading state:\n"
        f"  r1_call('GET', '/activities/{request_id}')\n"
        f"Poll until status is terminal (SUCCESS/FAIL). Check "
        f"steps[].progressSummary — a SUCCESS with a non-zero 'offline' count "
        f"means the config never reached those devices."
    )


def _should_retry(method: str, path: str, response) -> bool:
    """
    429 is always safe to retry — rate limiting means the request was rejected,
    not processed. 5xx is only safe when the call cannot have changed anything:
    a retried DELETE here can destroy a unit's DPSK twice (see field notes), and
    R1 gives no idempotency key to protect against that.
    """
    if response.status_code == 429:
        return True
    if response.status_code < 500:
        return False
    return method == "GET" or (method == "POST" and path.rstrip("/").endswith("/query"))


def _retry_delay(response, attempt: int) -> float:
    """Honor Retry-After when R1 sends one, else exponential backoff."""
    header = response.headers.get("Retry-After")
    if header:
        try:
            return min(float(header), 30.0)
        except ValueError:
            pass
    return min(1.0 * (2 ** attempt), 8.0)


def _error_detail(status: int, data) -> str:
    """
    R1 returns real error codes. Lead with the code rather than making the caller
    dig — the code identifies the cause where the HTTP status usually does not.
    """
    if not isinstance(data, dict):
        return ""
    err = data
    for k in ("errors", "error"):
        v = data.get(k)
        if isinstance(v, list) and v and isinstance(v[0], dict):
            err = v[0]
            break
        if isinstance(v, dict):
            err = v
            break
    code = err.get("code") or err.get("errorCode") or data.get("code")
    msg = err.get("message") or err.get("errorMessage") or data.get("message")
    if not code and not msg:
        return ""
    lead = f"HTTP {status}" + (f" {code}" if code else "") + (f": {msg}" if msg else "")
    return f"{lead}\n\n{json.dumps(data, indent=2)}"


def _rows(data):
    """Return (key, list) for the row list in a query response, or (None, None)."""
    if isinstance(data, list):
        return "", data
    if isinstance(data, dict):
        for k in _LIST_KEYS:
            if isinstance(data.get(k), list):
                return k, data[k]
    return None, None


def _declared_total(data):
    """The count R1 claims exists, which is not always the count it returned."""
    if isinstance(data, dict):
        for k in _TOTAL_KEYS:
            if isinstance(data.get(k), int):
                return k, data[k]
    return None, None


def _summarize(data) -> str:
    """count_only: shape and totals, without the payload."""
    key, rows = _rows(data)
    total_key, total = _declared_total(data)

    if rows is None:
        if isinstance(data, dict):
            return "Not a list response. Top-level keys: " + ", ".join(sorted(data))
        return f"Not a list response (got {type(data).__name__})."

    lines = [f"returned: {len(rows)} rows" + (f" (under '{key}')" if key else "")]
    if total is not None:
        lines.append(f"{total_key}: {total}")
        if total > len(rows):
            lines.append(
                f"\n⚠ INCOMPLETE — {total - len(rows)} rows were not returned. This is "
                f"the silent-truncation trap: the wrong paging parameter is ignored, the "
                f"default page size applies, and the total still reports correctly. "
                f"Check whether this endpoint wants page/pageSize (1-indexed) or "
                f"page/size (0-indexed)."
            )
    if rows and isinstance(rows[0], dict):
        lines.append("\nfields on first row: " + ", ".join(sorted(rows[0])))
        lines.append(
            "(fields are absent rather than null when unpopulated — a missing key "
            "is normal, not an error)"
        )
    return "\n".join(lines)


def _shrink(data, body_text: str, limit: int) -> tuple[str, str]:
    """
    Cap an oversized response. Returns (text, notice). Trims the row list rather
    than slicing mid-JSON, so what comes back is still valid and still labelled.
    """
    if len(body_text) <= limit:
        return body_text, ""

    key, rows = _rows(data)
    if rows:
        kept = rows
        while kept:
            kept = kept[: max(1, len(kept) * 2 // 3)]
            trial = dict(data) if isinstance(data, dict) else None
            sample = kept if trial is None else {**trial, key: kept}
            text = json.dumps(sample, indent=2)
            if len(text) <= limit:
                notice = (
                    f"\n\n⚠ TRUNCATED — showing {len(kept)} of {len(rows)} returned rows "
                    f"({len(body_text):,} chars exceeded the {limit:,} limit).\n"
                    f"The omitted rows were NOT examined. Do not describe this as the "
                    f"full set. Narrow it: count_only=True for totals and field names, "
                    f"a smaller pageSize, or a filter."
                )
                return text, notice
            if len(kept) == 1:
                break

    return body_text[:limit], (
        f"\n\n⚠ TRUNCATED at {limit:,} of {len(body_text):,} chars — this is a hard cut "
        f"and the JSON above is incomplete. Re-run with count_only=True or a narrower "
        f"query."
    )


@mcp.tool()
def r1_field_notes(group: str = "") -> str:
    """
    Verified real-world RUCKUS One behavior that the API spec does not document —
    broken endpoints, silent failures, and destructive semantics.

    Args:
        group: An API group slug (e.g. 'property-management'). Omit to get
               everything, including the cross-cutting notes.
    """
    if not NOTES_PATH.exists():
        return f"ERROR: field-notes directory not found at {NOTES_PATH}"

    if group:
        slug = group.strip().lower().replace(" ", "-").replace("_", "-")
        notes = _group_notes(slug)
        if not notes:
            have = sorted(
                p.stem for p in NOTES_PATH.glob("*.md")
                if p.stem not in {"GENERAL", "README"}
            )
            return (
                f"No field notes for '{group}'. This means nothing has been recorded "
                f"for it yet — not that it is free of surprises.\n"
                f"Groups with notes: {', '.join(have)}"
            )
        return notes

    parts = [_general_notes()]
    for f in sorted(NOTES_PATH.glob("*.md")):
        if f.stem in {"GENERAL", "README"}:
            continue
        parts.append(f"\n\n---\n\n# {f.stem}\n\n{f.read_text()}")
    return "".join(parts)


# Anything not obviously still running is treated as terminal, so an unknown
# status ends the poll rather than looping until timeout.
_PENDING_STATES = {"INPROGRESS", "IN_PROGRESS", "PENDING", "STARTED", "RUNNING", "QUEUED"}


def _activity_report(activity: dict, elapsed: float, polls: int) -> str:
    status = str(activity.get("status", "UNKNOWN"))
    lines = [
        f"Activity {activity.get('requestId', '?')} — {status}",
        f"useCase: {activity.get('useCase', '?')}"
        f" | polled {polls}x over {elapsed:.0f}s",
    ]
    if activity.get("admin", {}).get("name"):
        lines.append(f"actor: {activity['admin']['name']}")

    stalled = []
    for step in activity.get("steps", []) or []:
        summary = step.get("progressSummary") or {}
        detail = " ".join(f"{k}={v}" for k, v in summary.items() if v)
        lines.append(f"  - {step.get('id', '?')}: {step.get('status', '?')}"
                     + (f" ({detail})" if detail else ""))
        if summary.get("offline") or summary.get("fail"):
            stalled.append(step.get("id", "?"))

    if stalled:
        lines.append(
            f"\n⚠ The cloud accepted this, but it did NOT reach every device — "
            f"{', '.join(stalled)} reports offline or failed devices. Do not report "
            f"this as fully applied."
        )
    if status.upper() in _PENDING_STATES:
        lines.append(
            f"\n⚠ STILL RUNNING at timeout — not a failure, just unfinished. "
            f"Poll again; do not re-issue the original write."
        )
    return "\n".join(lines)


def _fetch_page(method, path, query_params, body, conv, page, size, tenant):
    """One page under a given convention. Paging goes in the body for POST."""
    page_key, size_key, base = conv
    paging = {page_key: base + page, size_key: size}
    if method == "POST":
        payload = {**(body or {}), **paging}
        params = query_params
    else:
        payload = body
        params = {**(query_params or {}), **paging}

    raw = r1_call(method, path, query_params=params, body=payload,
                  target_tenant_id=tenant, max_chars=10_000_000)
    if raw.startswith("ERROR") or not raw.startswith("HTTP 2"):
        return None, raw
    try:
        return json.loads(raw.split("\n\n", 1)[1]), ""
    except Exception:
        return None, raw


def _row_key(row):
    """A stable-enough identity for detecting a page that repeats itself."""
    if not isinstance(row, dict):
        return json.dumps(row, sort_keys=True)[:200]
    for k in ("id", "serialNumber", "mac", "macAddress", "name", "requestId"):
        if row.get(k):
            return f"{k}={row[k]}"
    return json.dumps(row, sort_keys=True)[:200]


@mcp.tool()
def r1_fetch_all(
    method: str,
    path: str,
    query_params: dict | None = None,
    body: dict | None = None,
    page_size: int = 500,
    max_pages: int = 40,
    target_tenant_id: str | None = None,
) -> str:
    """
    Fetch every row from a paginated endpoint, working out which paging
    convention it wants and verifying the result is actually complete.

    Use this instead of r1_call for any list you intend to count, reconcile or
    report on. RUCKUS One has three paging behaviors and picking the wrong one
    fails silently — you get the default page size back while the total still
    reports correctly, so short data looks complete.

    Args:
        method: GET or POST (POST for '/…/query' endpoints)
        path: API path
        query_params: Query parameters, excluding paging
        body: Request body, excluding paging
        page_size: Rows per page (default 500)
        max_pages: Safety stop (default 40)
        target_tenant_id: For MSP operations

    Returns:
        A completeness report, then the rows — trimmed with a notice if large.
    """
    method = method.upper()
    if method not in {"GET", "POST"}:
        return "ERROR: r1_fetch_all supports GET and POST only"

    # Probe both conventions and keep whichever actually honors page_size.
    chosen, first, probe_note = None, None, ""
    for conv in _CONVENTIONS:
        data, err = _fetch_page(method, path, query_params, body, conv, 0,
                                page_size, target_tenant_id)
        if data is None:
            return f"ERROR while probing paging convention {conv[0]}/{conv[1]}:\n\n{err}"
        _, rows = _rows(data)
        if rows is None:
            return f"Not a paginated list response.\n\n{json.dumps(data, indent=2)[:4000]}"
        _, total = _declared_total(data)
        chosen, first = conv, data
        # Honored if it filled the page, or returned everything there is.
        if len(rows) > 20 or (total is not None and len(rows) >= total):
            break
        probe_note += (f"'{conv[1]}' returned only {len(rows)} rows"
                       f"{f' of {total}' if total is not None else ''}; ")

    _, rows = _rows(first)
    _, total = _declared_total(first)
    key, _ = _rows(first)
    collected, seen, pages, stopped = list(rows), {_row_key(r) for r in rows}, 1, ""

    while total is not None and len(collected) < total and pages < max_pages:
        data, err = _fetch_page(method, path, query_params, body, chosen, pages,
                                page_size, target_tenant_id)
        if data is None:
            stopped = f"stopped after page {pages}: {err.splitlines()[0]}"
            break
        _, page_rows = _rows(data)
        if not page_rows:
            stopped = f"page {pages + 1} came back empty before reaching {total}"
            break

        fresh = [r for r in page_rows if _row_key(r) not in seen]
        if not fresh:
            stopped = (
                f"page {pages + 1} repeated rows already seen — this endpoint ignores "
                f"paging. Collecting further pages would INFLATE the result with "
                f"duplicates rather than extend it. Known true of POST /identities/query; "
                f"use GET /identityGroups/{{identityGroupId}}/identities instead."
            )
            break
        seen.update(_row_key(r) for r in fresh)
        collected.extend(fresh)
        pages += 1

    head = [
        f"{len(collected)} rows collected over {pages} page(s) "
        f"using {chosen[0]}/{chosen[1]} ({chosen[2]}-indexed)"
    ]
    if total is not None:
        head.append(f"endpoint reports {total}")
        if len(collected) == total:
            head.append("✓ COMPLETE")
        else:
            head.append(f"⚠ INCOMPLETE — {total - len(collected)} rows missing. "
                        f"Do not treat this as the full set.")
    else:
        head.append("⚠ endpoint declared no total, so completeness cannot be verified")
    if stopped:
        head.append(f"⚠ {stopped}")
    if probe_note:
        head.append(f"(probe: {probe_note.strip('; ')})")
    if pages >= max_pages and total is not None and len(collected) < total:
        head.append(f"⚠ hit the {max_pages}-page safety stop")

    payload = {**first, key: collected} if key and isinstance(first, dict) else collected
    text = json.dumps(payload, indent=2)
    text, notice = _shrink(payload, text, MAX_RESPONSE_CHARS)
    return "\n".join(head) + "\n\n" + text + notice


@mcp.tool()
def r1_wait_for_activity(
    request_id: str,
    timeout_seconds: float = 120.0,
    target_tenant_id: str | None = None,
) -> str:
    """
    Poll a RUCKUS One activity to completion and report what actually happened.

    Mutating calls return 202 with a requestId, which IS an activity ID. A 202
    means accepted, not applied — pass its requestId here before verifying state
    or reporting success.

    Args:
        request_id: The requestId from a 202 response
        timeout_seconds: Give up after this long (default 120)
        target_tenant_id: For MSP operations — the customer tenant to poll in

    Returns:
        Terminal status, per-step progress, and a warning when a SUCCESS still
        left devices offline or failed.
    """
    started = time.time()
    delay, polls = 2.0, 0

    while True:
        polls += 1
        raw = r1_call("GET", f"/activities/{request_id}",
                      target_tenant_id=target_tenant_id, max_chars=20000)
        if raw.startswith("ERROR"):
            return f"{raw}\n\n(while polling activity {request_id})"

        try:
            activity = json.loads(raw.split("\n\n", 1)[1])
        except Exception:
            return f"Could not parse activity response:\n\n{raw}"

        elapsed = time.time() - started
        status = str(activity.get("status", "")).upper()
        if status not in _PENDING_STATES:
            return _activity_report(activity, elapsed, polls)

        if elapsed + delay >= timeout_seconds:
            return _activity_report(activity, elapsed, polls)

        time.sleep(delay)
        delay = min(delay * 1.5, 10.0)


@mcp.tool()
def r1_call(
    method: str,
    path: str,
    query_params: dict | None = None,
    body: dict | None = None,
    target_tenant_id: str | None = None,
    count_only: bool = False,
    max_chars: int | None = None,
) -> str:
    """
    Make an authenticated API call to RUCKUS One and return the response.

    Args:
        method: HTTP method — GET, POST, PUT, PATCH, DELETE
        path: API path, e.g. '/venues' or '/venues/{venueId}/wifiNetworks'
              (include the leading slash; do NOT include the base URL)
        query_params: Optional dict of query string parameters
        body: Optional dict for the request body (POST/PUT/PATCH)
        target_tenant_id: For MSP operations — the customer tenant ID to operate on
                          (sets x-rks-tenantid header; R1_MSP_ID must also be set in .env)
        count_only: Return row counts, declared totals and field names instead of
                    the rows. Use this FIRST on any fleet-scale query — it is cheap
                    and it reveals silent truncation.
        max_chars: Cap the response body (default R1_MAX_RESPONSE_CHARS, 40000).

    Returns:
        JSON response as a formatted string, or an error message. Large list
        responses are trimmed with an explicit notice — never silently.
    """
    method = method.upper()
    if method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
        return f"ERROR: Unsupported HTTP method '{method}'"

    try:
        token = _get_token()
    except Exception as e:
        return f"ERROR: {e}"

    headers: dict[str, str] = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # MSP headers — set when operating on a customer tenant via an MSP account
    if target_tenant_id:
        headers["x-rks-tenantid"] = target_tenant_id
        if MSP_ID:
            headers["X-MSP-ID"] = MSP_ID
    elif MSP_ID:
        headers["X-MSP-ID"] = MSP_ID

    url = BASE_URL + path
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            for attempt in range(MAX_RETRIES + 1):
                response = client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=query_params or {},
                    json=body,
                )
                if attempt == MAX_RETRIES or not _should_retry(method, path, response):
                    break
                time.sleep(_retry_delay(response, attempt))

        status = response.status_code
        data = None
        try:
            data = response.json()
            body_text = json.dumps(data, indent=2)
        except Exception:
            body_text = response.text

        head = f"HTTP {status} {method} {url}"
        notice = ""

        if status >= 400:
            body_text = _error_detail(status, data) or body_text
        elif count_only:
            body_text = _summarize(data)
        else:
            limit = max_chars if max_chars is not None else MAX_RESPONSE_CHARS
            body_text, notice = _shrink(data, body_text, limit)
            _, rows = _rows(data)
            _, total = _declared_total(data)
            if rows is not None and total is not None and total > len(rows) and not notice:
                notice = (
                    f"\n\n⚠ INCOMPLETE — {len(rows)} rows returned but the endpoint "
                    f"reports {total}. The paging parameter was likely ignored; the "
                    f"total is still accurate, so this looks complete but is not."
                )

        return f"{head}\n\n{body_text}{notice}{_async_hint(status, data)}"

    except httpx.ConnectError as e:
        return f"ERROR: Could not connect to {url}: {e}"
    except httpx.TimeoutException:
        return (
            f"ERROR: Request timed out after {TIMEOUT:g}s — {method} {url}\n"
            f"Fleet-scale queries routinely need 60-90s; raise R1_TIMEOUT."
        )
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


if __name__ == "__main__":
    mcp.run()
