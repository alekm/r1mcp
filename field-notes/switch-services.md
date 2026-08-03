# Switch Services

## Switch objects use `deviceStatus`, not `status`

`.get("status")` returns `None` and reads like an API gap. Switches carry
`deviceStatus` (`ONLINE`), plus `model`, `family`, `firmwareVersion`,
`numOfPorts`, `cloudPort`, `switchMac`, `ipAddress`, `uptime`.

## `id` is the MAC, and `PUT` will not accept a serial

`GET /venues/{venueId}/switches/{switchId}` accepts either serial or MAC.
`PUT` accepts only the MAC — a serial returns
`400 SWITCH-10462 "ID in payload does not match switchId in URL"`.

## Port settings are usually empty

`GET /switches/{id}/portSettings` returns configured overrides only, which does
not mean the ports are unconfigured. For the actual port-to-device map use
`POST /venues/switches/clients/query` (see view-model-resources.md).

## AAA servers

`POST /venues/aaaServers/query` takes **`venueId` singular**, not the `venueIds`
array the neighbouring wifiNetworks query uses. The request is rejected without it.

The venue-scoped path works with any body, including `{}`:

```
POST /venues/{venueId}/aaaServers/query   {}
```

Responses include a `password` field. **Do not echo it into output, logs or
tickets** — read the fields you need and drop the rest.

`syncedPasswordSwitchCount` against `switchCountInVenue` shows switches that never
took a credential change.
