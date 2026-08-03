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


@mcp.tool()
def r1_call(
    method: str,
    path: str,
    query_params: dict | None = None,
    body: dict | None = None,
    target_tenant_id: str | None = None,
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

    Returns:
        JSON response as a formatted string, or an error message.
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
        with httpx.Client(timeout=30) as client:
            response = client.request(
                method=method,
                url=url,
                headers=headers,
                params=query_params or {},
                json=body,
            )

        status = response.status_code
        data = None
        try:
            data = response.json()
            body_text = json.dumps(data, indent=2)
        except Exception:
            body_text = response.text

        return f"HTTP {status} {method} {url}\n\n{body_text}{_async_hint(status, data)}"

    except httpx.ConnectError as e:
        return f"ERROR: Could not connect to {url}: {e}"
    except httpx.TimeoutException:
        return f"ERROR: Request timed out after 30s — {method} {url}"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


if __name__ == "__main__":
    mcp.run()
