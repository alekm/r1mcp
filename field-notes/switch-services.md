# Switch Services — field notes

## Switch objects use `deviceStatus`, not `status`

`.get("status")` returns `None` and reads like an API gap. Switches carry
`deviceStatus` (`ONLINE`), plus `model`, `family`, `firmwareVersion`,
`numOfPorts`, `cloudPort`, `switchMac`, `ipAddress`, `uptime`.

## `id` is the MAC — and `PUT` will not accept a serial

`GET /venues/{venueId}/switches/{switchId}` accepts **either** serial or MAC.
`PUT` accepts **only the MAC**:

```
PUT with a serial -> 400 SWITCH-10462 "ID in payload does not match switchId in URL"
```

Same fact behind both behaviors: the switch's `id` field is its MAC address.

## Port settings are usually empty

`GET /switches/{id}/portSettings` returns configured *overrides* only — typically
empty, which does not mean the ports are unconfigured. For the actual port ↔
device map use `POST /venues/switches/clients/query` (see
view-model-resources.md).

## Broken as of 2026-08-02

`POST /venues/aaaServers/query` returns 500 `SWITCH-10000` ("an unknown error
occurred") even with paging and sort supplied.
