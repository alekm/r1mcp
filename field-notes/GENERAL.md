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

## 7. A 500 usually means an under-specified body, not a broken endpoint

**This is the most expensive mistake to make against this API.** Several `/query`
endpoints return **500 when a required body field is missing**, where a 400 would
be correct — and the message reads like an outage ("something went wrong, please
wait a few minutes and try again"). Waiting does nothing. Every endpoint in the
events and alarms group was written off as broken on this basis, and none of them
are. Two illustrative cases:

```
POST /events/query      {"page":1,"pageSize":10}                        -> 500
POST /events/query      {"fields":["event_datetime","severity","message"]}
                                                                        -> 200

POST /activities/query  {"page":1,"pageSize":50}                        -> 500
POST /activities/query  {"page":1,"pageSize":50,
                         "sortField":"startDatetime","sortOrder":"DESC"} -> 200
```

- `/events/query` needs **`fields`** with at least one recognized name. Nothing
  else is mandatory.
- `/activities/query` needs **all four** of `page`, `pageSize`, `sortField`,
  `sortOrder`. An unrecognized `sortField` is also a 500.
- Any `/query` path ending in **`/metas` or `/details`** is an ID-keyed lookup,
  not a list. It needs **`fields` + `filters.id`** and 500s without both. Covers
  `/alarms/metas/query`, `/events/metas/query`, `/events/details/query`.

**Five** endpoints written off as broken turned out to be under-specified —
the entire events and alarms surface. Before recording a sixth, retry with a
`fields` list, full paging, both sort keys, and `filters.id` if the path ends in
`/metas` or `/details`. Only then is a 500 evidence of anything.

## Known-broken endpoints — verified 2026-08-02

Confirmed 500 across every payload variant that fixed the five above, including
`fields`, `filters.id`, `filters.venueIds`, paging and sort:

| Endpoint | Code |
|---|---|
| `POST /venues/wifiNetworks/query` | `WIFI-10000` — tenant-level `POST /wifiNetworks/query` works |
| `POST /templates/venues/wifiNetworks/query` | `WIFI-10000` |
| `POST /venues/aaaServers/query` | `SWITCH-10000` |
| `POST /macRegistrationPools/query` | 500 — use `GET /macRegistrationPools` |
| `POST /entitlements/banners/query` | `ENTITLEMENT-10000` |
| `POST /entitlements/compliances/query` | `ENTITLEMENT-10000` |
| `GET /entitlements/licenseUsageReports` | 400 |

Where a plain collection `GET` exists alongside a broken `/query`, the `GET` works
— that is the workaround, not a retry. `POST /portalServiceProfiles/query` is
field-sensitive rather than broken: a wrong `fields` list returns
`400 GUEST-400000`, so it wants the right names, which are not yet known.

For change history, **both** `/events/query` and `/activities/query` work — events
for what happened on the network, activities for who changed what. `/alarms/query`
returns active alarms only; history is lost on recovery. Neither alarms nor events
carry entity *names* — resolve those through the `/metas` lookups above.

Sweep scope: 237 read-only endpoints with no path parameters across all 31 groups;
212 returned 200.
