# View Model Resources — field notes

This group holds the query endpoints that actually carry device state.

## `POST /venues/aps/query` is where AP state lives

Not the detail endpoint. `GET /venues/{venueId}/aps/{serialNumber}` returns
essentially nothing — observed `{"name": ..., "loginPassword": ...}`, two fields.

Fields are **absent, not null**, on APs that have never contacted the cloud.
Measured across one venue (57 operational / 269 never-contacted):

| Field | Operational | Never-contacted |
|---|---|---|
| `model`, `macAddress`, `firmwareVersion`, `lanPortStatuses`, `switchSerialNumber`, `uptime`, `clientCount` | 57/57 | **0/269** |
| `networkStatus` | 57/57 | 269/269 |

So you **cannot inventory models or MACs of staged-but-uninstalled gear** from R1.

**Ordering trap:** during onboarding `status` reaches `2_00_Operational` *before*
`macAddress` publishes. Any reconciliation keyed on MAC undercounts — key on
`status`, or accept a lag.

Unrecognized entries in `fields` are silently dropped (GENERAL.md §3).

## `POST /venues/switches/clients/query` — model + firmware before onboarding

Returns a `clientDesc` per learned MAC:

```
"Ruckus R550 Multimedia Hotzone Wireless AP/SW Version: 7.2.0.610.1360"
```

This is the **only** way to see a device's model and running firmware before it
has checked in to R1 — which makes it the way to distinguish "mid-upgrade" from
"stuck". APs ship on a factory image and pull venue firmware before ever appearing
healthy; through that whole window R1 reports only `1_01_NeverContactedCloud` and
cannot alarm.

Also the practical switch-port ↔ device map — `GET /switches/{id}/portSettings`
returns configured overrides only and is usually empty.

**Caveat:** shows only ports with a device *currently learned*. Patched-but-idle
ports are invisible, so a blank port means "nothing learned", not "nothing
connected".
