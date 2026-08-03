# RUCKUS Edge — field notes

## `POST /edgeDhcpServices/dhcpClientLeases/query` — not in the spec at all

Backs the console's Edge → DHCP page and is the only way to read Edge leases.
Absent from the OpenAPI spec entirely, so it will never appear in `llm-docs/`.

```jsonc
{"sortField": "name", "sortOrder": "ASC", "page": 1, "pageSize": 100,
 "filters": {"edgeClusterId": ["<edgeClusterId>"]}}
```

Returns `hostMac, hostIpAddr, hostName, hostStatus, hostRemainingTime,
hostExpireDate, isReserved, dhcpPoolName, segmentId, segmentGroupId, edgeId,
edgeClusterId, venueId`.

`hostRemainingTime` counts **down** from lease duration, so lease age =
duration − remaining — a decent proxy for when a device last booted or renewed.

**Known issue:** observed returning `totalCount: 0` while the Edge was
demonstrably serving ~55 leases (vendor case open). **A zero here does not mean
DHCP is broken** — do not report an outage on this alone.

## Edge query endpoints require explicit filters

Verified 2026-08-02 — these reject an unfiltered query rather than returning
everything:

- `POST /venues/edgeCompatibilities/query` — 400, needs `filters.venueIds`
- `POST /edgeDhcpServices/edgeCompatibilities/query` — 422 `EDGE-10001`, needs
  `filters.serviceIds`

Get the IDs first; there is no "list all" form.
