# Wi-Fi Services — field notes

## Whole-object `PUT`s that clobber omitted fields

### `PUT /venues/{venueId}/aps/{serialNumber}`

Carries a per-AP `loginPassword`. **GET first and echo it back** or you may reset
the AP's admin credential. Returns **202** — a success code is not proof the
change landed; poll the activity (GENERAL.md §1).

Note the asymmetry: the `GET` returns almost nothing (`name`, `loginPassword`), so
you cannot round-trip a full object from it. AP state lives on
`POST /venues/aps/query` — see view-model-resources.md.

### `PUT /venues/{venueId}/apGroups/{apGroupId}`

`apSerialNumbers` **replaces** the entire membership list. Always send the full
intended set, never a delta.

(Floorplan `PUT` has the same clobbering shape — see venues.md.)

## PoE mode is a per-model venue setting

```
PUT /venues/{venueId}/apModels/{apModel}/lanPortSpecificSettings   {"poeMode": "802.3at"}
```

Covers every AP of that model running `useVenueSettings: true`, no reboot.
**Prefer it over `PUT /venues/{venueId}/apModelLanPortSettings`**, which takes the
whole ~50-model list and rewrites every model.

`poeMode` enum: `Auto | 802.3af | 802.3at | 802.3bt-Class_5…8`

On models where the second ethernet port is suppressed at `802.3af`, a downstream
bind succeeds but the port stays dead — this presents as a binding failure and
sends you chasing the wrong thing.

## Broken as of 2026-08-02

| Endpoint | Behavior |
|---|---|
| `POST /venues/wifiNetworks/query` | 500 `WIFI-10000`, with paging and sort supplied |
| `POST /templates/venues/wifiNetworks/query` | 500 `WIFI-10000` |

Both are the **venue-scoped** network query endpoints. The tenant-level
`POST /wifiNetworks/query` works — use it and filter client-side.

Note `GET /wifiNetworks` is **405**, not a collection endpoint; the tenant-level
list is only reachable through `/query`.

`GET /venues/aps/importResults` requires a `requestId` **query parameter**
(422 `WIFI-10008` without it), so it is only usable after an import.
