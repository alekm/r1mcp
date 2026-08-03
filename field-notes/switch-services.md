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

## AAA servers: query per venue, not tenant-wide

`POST /venues/aaaServers/query` takes **`venueId` — singular**, not the `venueIds`
array that the neighbouring wifiNetworks query uses:

```jsonc
POST /venues/aaaServers/query   {"venueId": "<venueId>"}
```

Without it: 500 `SWITCH-10000` "an unknown error occurred". The standard
`fields`/`page`/`sortField` envelope may be added but does not substitute for it.

The venue-scoped path also works and is unfussy — envelope, flat, or even `{}`:

```
POST /venues/{venueId}/aaaServers/query   {}
```

`POST /templates/venues/aaaServers/query` works tenant-wide with any body.

**Two lessons:** singular vs plural id keys differ between adjacent endpoints, so
read each `requestBody` in the spec; and when a tenant-wide aggregate fails, the
venue-scoped path is a separate implementation worth trying.

### ⚠ This endpoint returns switch admin credentials

```jsonc
{"id": "…", "name": "admin", "username": "admin", "password": "<in cleartext>",
 "purpose": "DEFAULT", "level": "READ_WRITE", "serverType": "LOCAL",
 "authPort": 0, "switchCountInVenue": 5, "syncedPasswordSwitchCount": 5}
```

`password` comes back in the response body. **Do not echo this into chat output,
logs, tickets or commits.** Read the fields you need and drop the rest.

`syncedPasswordSwitchCount` vs `switchCountInVenue` is the useful signal — a
mismatch means some switches never took the credential change.
