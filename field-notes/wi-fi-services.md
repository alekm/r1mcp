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

## `POST /venues/wifiNetworks/query` takes a flat body, not the usual envelope

Previously recorded as broken. It is not — it rejects the standard
`fields`/`page`/`pageSize`/`sortField`/`filters` envelope with `500 WIFI-10000`,
and takes a flat body instead:

```jsonc
POST /venues/wifiNetworks/query
{"venueIds": ["<venueId>"],
 "networkIds": ["<networkId>", "<networkId>"]}   // optional narrowing
```

**`venueIds` is required**; `networkIds` alone is still a 500, as is an empty
body. Same shape for `/templates/venues/wifiNetworks/query`.

This is the **network-to-venue activation map**, which nothing else gives you:

```jsonc
{"data": [{"venueId": "<venueId>",
           "networks": [{"networkId": "<networkId>",
                         "isAllApGroups": false,
                         "allApGroupsRadioTypes": ["2.4-GHz","5-GHz"],
                         "apGroups": [{"apGroupId": "<apGroupId>",
                                       "radioTypes": ["2.4-GHz","5-GHz","6-GHz"]}],
                         "dual5gEnabled": false, "tripleBandEnabled": false,
                         "urlFilteringPolicyEnabled": false, "isEnforced": false}]}]}
```

So it answers "which SSIDs are live at this venue, on which AP groups, on which
radios" — including the per-AP-group radio overrides. The tenant-level
`POST /wifiNetworks/query` lists networks but says nothing about where they are
deployed.

Note `GET /wifiNetworks` is **405**; the tenant-level list is only reachable
through `/query`.

`GET /venues/aps/importResults` requires a `requestId` **query parameter**
(422 `WIFI-10008` without it), so it is only usable after an import.
