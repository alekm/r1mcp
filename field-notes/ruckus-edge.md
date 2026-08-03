# RUCKUS Edge

## `POST /edgeDhcpServices/dhcpClientLeases/query` — not in the spec

The only way to read Edge DHCP leases, and absent from the OpenAPI spec entirely,
so it will never appear in `llm-docs/`.

```jsonc
{"sortField": "name", "sortOrder": "ASC", "page": 1, "pageSize": 100,
 "filters": {"edgeClusterId": ["<edgeClusterId>"]}}
```

Returns `hostMac, hostIpAddr, hostName, hostStatus, hostRemainingTime,
hostExpireDate, isReserved, dhcpPoolName, segmentId, segmentGroupId, edgeId,
edgeClusterId, venueId`.

`hostRemainingTime` counts **down** from lease duration, so lease age =
duration − remaining — a usable proxy for when a device last booted or renewed.

**A `totalCount` of 0 here does not mean DHCP is broken.** It has been observed
returning zero while the Edge was serving ~55 leases. Do not report an outage on
this alone.

## Edge compatibility queries require explicit filters

- `POST /venues/edgeCompatibilities/query` — needs `filters.venueIds`
- `POST /edgeDhcpServices/edgeCompatibilities/query` — needs `filters.serviceIds`

There is no "list all" form; get the ids first.
