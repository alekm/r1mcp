# Wi-Fi Services

## Whole-object `PUT`s clobber omitted fields

**`PUT /venues/{venueId}/aps/{serialNumber}`** carries a per-AP `loginPassword`.
GET first and echo it back or you may reset the AP admin credential. Returns 202,
so the status code is not proof the change landed (GENERAL.md §1).

The matching GET returns almost nothing (`name`, `loginPassword`), so you cannot
round-trip a full object from it — AP state is on `POST /venues/aps/query`.

**`PUT /venues/{venueId}/apGroups/{apGroupId}`** — `apSerialNumbers` replaces the
entire membership list. Always send the full intended set, never a delta.

Floorplan `PUT` has the same shape — see venues.md.

## `POST /venues/wifiNetworks/query` takes a flat body

Not the standard envelope, which this endpoint does not accept:

```jsonc
{"venueIds": ["<venueId>"], "networkIds": ["<networkId>"]}   // networkIds optional
```

`venueIds` is required; `networkIds` alone is not sufficient. Same for
`/templates/venues/wifiNetworks/query`.

This is the **network-to-venue activation map** — which SSIDs are live at a venue,
on which AP groups, on which radios:

```jsonc
{"data": [{"venueId": "<venueId>",
           "networks": [{"networkId": "<networkId>", "isAllApGroups": false,
                         "allApGroupsRadioTypes": ["2.4-GHz","5-GHz"],
                         "apGroups": [{"apGroupId": "<id>",
                                       "radioTypes": ["2.4-GHz","5-GHz","6-GHz"]}]}]}]}
```

The tenant-level `POST /wifiNetworks/query` lists networks but not where they are
deployed. `GET /wifiNetworks` is 405.

## PoE mode is a per-model venue setting

```
PUT /venues/{venueId}/apModels/{apModel}/lanPortSpecificSettings   {"poeMode": "802.3at"}
```

Covers every AP of that model running `useVenueSettings: true`, no reboot. Prefer
it over `PUT /venues/{venueId}/apModelLanPortSettings`, which takes the whole
~50-model list and rewrites every model.

`poeMode`: `Auto | 802.3af | 802.3at | 802.3bt-Class_5…8`

On models where the second ethernet port is unavailable at `802.3af`, a downstream
bind succeeds but the port does not come up — which presents as a binding problem.
Check `poeMode` before investigating the bind.
