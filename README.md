# r1mcp

An [MCP](https://modelcontextprotocol.io) server that connects Claude to the [RUCKUS One](https://www.ruckusnetworks.com/products/ruckus-one/) cloud WiFi management platform. Ask natural-language questions and make live API calls against your R1 tenant directly from Claude Code or any MCP-capable client.

## How it works

The server exposes three tools that follow a deliberate discovery flow:

| Tool | Purpose |
|------|---------|
| `r1_list_groups` | Returns the full API surface (30 groups, 1592 endpoints) from a local index — no network call |
| `r1_get_docs(group)` | Returns full endpoint documentation for a group (parameters, request/response schemas) |
| `r1_call(method, path, ...)` | Makes an authenticated live API call and returns the JSON response |

Authentication uses OAuth2 client credentials with automatic token caching and refresh. MSP tenants can pass `target_tenant_id` to `r1_call` to operate on a customer tenant.

## Setup

**1. Install dependencies**

```bash
pip install "mcp[cli]" httpx python-dotenv
```

**2. Configure credentials**

```bash
cp .env.example .env
```

Edit `.env` with your RUCKUS One OAuth2 credentials (from the R1 console under API Keys / OAuth2 Applications):

```
R1_CLIENT_ID=your_client_id
R1_CLIENT_SECRET=your_client_secret
R1_TENANT_ID=your_tenant_id
R1_REGION=na          # na, eu, or asia
# R1_MSP_ID=...       # uncomment if this is an MSP account
```

**3. Register with Claude Code**

Add to `~/.claude.json` under `mcpServers`:

```json
"ruckus-one": {
  "type": "stdio",
  "command": "python3",
  "args": ["/path/to/r1mcp/server.py"]
}
```

Restart Claude Code to pick up the new server.

**4. Verify**

```bash
python3 server.py          # should exit cleanly
mcp dev server.py          # interactive smoke test
```

## Usage examples

```
List all venues in my tenant
Show me the wifi-services API docs
Create a new SSID named "CorpWiFi" with WPA3 on venue abc123
List all switches in venue xyz and show their port status
```

## Configuration reference

| Variable | Required | Default | Description |
|----------|:--------:|---------|-------------|
| `R1_CLIENT_ID` | ✓ | — | OAuth2 client ID |
| `R1_CLIENT_SECRET` | ✓ | — | OAuth2 client secret |
| `R1_TENANT_ID` | ✓ | — | Your R1 tenant ID |
| `R1_REGION` | | `na` | API region: `na`, `eu`, or `asia` |
| `R1_MSP_ID` | | — | MSP tenant ID (if operating as an MSP) |
| `R1_DOCS_PATH` | | `./llm-docs` | Path to the markdown docs directory |

## API docs

The `llm-docs/` directory contains pre-generated markdown reference files for all 30 API groups (1592 endpoints, from the June 2026 spec). If you have access to an updated OpenAPI spec, regenerate them with the companion `generate.py` tool.

## License

MIT — see [LICENSE](LICENSE).
