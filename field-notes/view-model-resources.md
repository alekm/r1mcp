# View Model Resources

Holds the query endpoints that carry actual device state.

## `POST /venues/aps/query` is where AP state lives

Not the detail endpoint — `GET /venues/{venueId}/aps/{serialNumber}` returns
roughly `{"name": ..., "loginPassword": ...}`.

Fields are absent rather than null on APs that have never contacted the cloud, so
`model`, `macAddress`, `firmwareVersion`, `lanPortStatuses`, `switchSerialNumber`,
`uptime` and `clientCount` are simply missing. `networkStatus` is always present.
**You cannot inventory models or MACs of staged-but-uninstalled gear.**

During onboarding `status` reaches `2_00_Operational` *before* `macAddress`
publishes, so reconciliation keyed on MAC undercounts. Key on `status`.

## `POST /venues/switches/clients/query` — model and firmware before onboarding

Returns a `clientDesc` per learned MAC:

```
"Ruckus R550 Multimedia Hotzone Wireless AP/SW Version: 7.2.0.610.1360"
```

The only way to see a device's model and running firmware before it checks in to
R1, which makes it the way to tell "mid-upgrade" from "stuck" — an AP pulls venue
firmware before appearing healthy, and reports only `1_01_NeverContactedCloud`
throughout.

Also the practical switch-port to device map. Shows only ports with a device
**currently learned**, so a blank port means "nothing learned", not "nothing
connected".
