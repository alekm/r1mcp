# RUCKUS One — field-verified behavior

Verified against a live tenant. These are silent-failure modes: the API returns
2xx and plausible data while giving you the wrong answer. None of this is in the
OpenAPI spec.

## 1. A 202 is not a completed write — poll the activity

Mutating calls return `202 Accepted` with a `requestId`. **That `requestId` is an
activity ID**, though nothing in the spec says so (653 operations return 202;
two mention activities).

```
PUT /venues/{venueId}/aps/{serialNumber}   -> 202 {"requestId": "<uuid>"}
GET /activities/<uuid>                     -> 200  status: SUCCESS | FAIL | ...
```

Poll `GET /activities/{requestId}` to a terminal `status` before verifying state.
Do not sleep-and-re-GET the resource.

`steps[].progressSummary` (`pending`/`inProgress`/`success`/`fail`/`offline`)
separates "cloud accepted the config" from "config reached the device" — an
`offline` count is why a SUCCESS can still leave a device unchanged. Per-device
detail: `POST /activities/{activityId}/devices/query`.

## 2. Three incompatible pagination conventions, all failing silently

| Convention | Where |
|---|---|
| `page` / `pageSize`, **1**-indexed | most `POST /…/query` |
| `page` / `size`, **0**-indexed | identity + Property Management `GET`s (spec says 1-indexed; it is not) |
| paging **ignored** | `POST /identities/query` — same 20 rows forever |

An unrecognized paging parameter is ignored, the default page size applies, and
`totalElements` still reports the true count — so truncated data looks complete.

```
GET /venues/{venueId}/units?page=0&pageSize=500  ->  20 items, totalElements: 290
GET /venues/{venueId}/units?page=0&size=500      -> 290 items, totalElements: 290
```

**Always compare returned length against `totalElements`/`totalCount`.** For
identities use `GET /identityGroups/{identityGroupId}/identities?page=0&size=500`
(not in the spec, but it works and pages correctly).

## 3. Query endpoints silently drop unrecognized `fields` and filters

Confirmed on `POST /venues/aps/query` and `POST /alarms/query`. Ask for a field
the endpoint doesn't know and it simply doesn't come back — no error. A typo is
indistinguishable from "the API has no such data". Verify a field exists before
concluding anything from its absence.

## 4. Objects are sparse, and fields are absent rather than null

On APs that have never contacted the cloud, `model`, `macAddress`,
`firmwareVersion`, `lanPortStatuses`, `switchSerialNumber`, `uptime` and
`clientCount` are **missing entirely** (0/269 present in one venue, vs 57/57 on
operational APs). `networkStatus` is always present.

`.get("model") is None` is normal, not an error. Never assume a stable schema
across a mixed fleet.

## 5. Status fields lag reality by ~3 minutes

APs report on roughly a 3-minute cycle. Every status field — `poeUnderPowered`,
`lanPortStatuses`, binding state — can be that stale. A stale value is not a
stuck device.

## 6. Read the error code, not just the status

Errors carry real codes (`PROPERTY-MANAGEMENT-001`, `SWITCH-10462`,
`EVENT-10002`) plus a `requestId`. The code identifies the cause; the HTTP status
usually does not.

## Known-broken endpoints — do not retry, do not work around

| Endpoint | Behavior |
|---|---|
| `POST /events/query` | **HTTP 500** `EVENT-10002`, persistent |
| `GET /entitlements/licenseUsageReports` | **400** with a raw Java stack trace |

For change history use `POST /activities/query` — it is the only working option
(`/alarms/query` returns active alarms only; history is lost on recovery).
