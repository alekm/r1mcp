#!/usr/bin/env python3
"""RUCKUS One MCP Server — exposes R1 API docs and live API calls as tools."""

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv(Path(__file__).parent / ".env")

API_KEY = os.environ.get("R1_API_KEY", "")
REGION = os.environ.get("R1_REGION", "na").lower()
DOCS_PATH = Path(os.environ.get("R1_DOCS_PATH", "/home/alek/R1API/llm-docs"))

REGION_HOSTS = {
    "na": "https://api.ruckus.cloud",
    "eu": "https://api.eu.ruckus.cloud",
    "asia": "https://api.asia.ruckus.cloud",
}
BASE_URL = REGION_HOSTS.get(REGION, REGION_HOSTS["na"])

mcp = FastMCP("ruckus-one")


@mcp.tool()
def r1_list_groups() -> str:
    """
    List all available RUCKUS One API groups and their endpoint counts.
    Use this first to understand what parts of the API exist before diving deeper.
    """
    index = DOCS_PATH / "INDEX.md"
    if not index.exists():
        return f"ERROR: INDEX.md not found at {index}"
    return index.read_text()


@mcp.tool()
def r1_get_docs(group: str) -> str:
    """
    Get full API documentation for a specific RUCKUS One API group.
    Use r1_list_groups first to see available group names.

    Args:
        group: The group slug, e.g. 'wifi-services', 'switch-services', 'venues',
               'tenant-management', 'events-and-alarms', etc.
    """
    # Normalize: allow spaces or underscores, lowercase
    slug = group.strip().lower().replace(" ", "-").replace("_", "-")
    doc_file = DOCS_PATH / f"{slug}.md"
    if not doc_file.exists():
        available = sorted(p.stem for p in DOCS_PATH.glob("*.md") if p.stem != "INDEX")
        return (
            f"ERROR: No docs found for '{group}' (tried {doc_file.name}).\n"
            f"Available groups: {', '.join(available)}"
        )
    return doc_file.read_text()


@mcp.tool()
def r1_call(
    method: str,
    path: str,
    query_params: dict | None = None,
    body: dict | None = None,
) -> str:
    """
    Make an authenticated API call to RUCKUS One and return the response.

    Args:
        method: HTTP method — GET, POST, PUT, PATCH, DELETE
        path: API path, e.g. '/venues' or '/venues/{venueId}/wifiNetworks'
              (include the leading slash; do NOT include the base URL)
        query_params: Optional dict of query string parameters
        body: Optional dict for the request body (POST/PUT/PATCH)

    Returns:
        JSON response as a formatted string, or an error message.
    """
    if not API_KEY:
        return "ERROR: R1_API_KEY is not set. Add it to your .env file."

    method = method.upper()
    if method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
        return f"ERROR: Unsupported HTTP method '{method}'"

    url = BASE_URL + path
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

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
        try:
            data = response.json()
            body_text = json.dumps(data, indent=2)
        except Exception:
            body_text = response.text

        return f"HTTP {status} {method} {url}\n\n{body_text}"

    except httpx.ConnectError as e:
        return f"ERROR: Could not connect to {url}: {e}"
    except httpx.TimeoutException:
        return f"ERROR: Request timed out after 30s — {method} {url}"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


if __name__ == "__main__":
    mcp.run()
