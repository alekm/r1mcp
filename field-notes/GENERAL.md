# RUCKUS One — behavior the API spec does not describe

Apply these to every call. They cover cases where a response is misleading — 2xx
with incomplete data, or a 5xx that means the request needs changing.

## 1. A 202 is not a completed write

Mutating calls return `202` with a `requestId`. **That `requestId` is an activity
ID** — poll it before verifying state or reporting success:

```
GET /activities/{requestId}   ->  status: SUCCESS | FAIL | ...
```

`steps[].progressSummary` (`pending`/`inProgress`/`success`/`fail`/`offline`)
separates "cloud accepted the config" from "config reached the device". A SUCCESS
with a non-zero `offline` count means those devices never got it. Per-device
detail: `POST /activities/{activityId}/devices/query`.

## 2. Three pagination conventions, all failing silently

| Convention | Where |
|---|---|
| `page` / `pageSize`, 1-indexed | most `POST /…/query` |
| `page` / `size`, 0-indexed | identity and Property Management `GET`s |
| paging ignored | `POST /identities/query` — same 20 rows forever |

An unrecognized paging parameter is ignored, the default page size applies, and
the total still reports correctly — so truncated data looks complete.

```
GET /venues/{venueId}/units?page=0&pageSize=500  ->  20 rows, totalElements 290
GET /venues/{venueId}/units?page=0&size=500      -> 290 rows, totalElements 290
```

**Always compare returned row count against the declared total.** For identities
use `GET /identityGroups/{groupId}/identities?page=0&size=500`.

## 3. Unrecognized `fields` and filters are silently dropped

Ask for a field an endpoint does not know and it simply does not come back — no
error. A typo is indistinguishable from "no such data". Never conclude data is
missing from its absence alone.

## 4. Fields are absent, not null

On APs that have never contacted the cloud, `model`, `macAddress`,
`firmwareVersion`, `lanPortStatuses`, `switchSerialNumber`, `uptime` and
`clientCount` are missing entirely. `networkStatus` is always present. A missing
key is normal; do not assume a stable schema across a mixed fleet.

## 5. Status lags reality by ~3 minutes

APs report on roughly a 3-minute cycle. `poeUnderPowered`, `lanPortStatuses` and
binding state can all be that stale. A stale value is not a stuck device.

## 6. Read the error code, not the status

Errors carry codes (`PROPERTY-MANAGEMENT-001`, `SWITCH-10462`, `EVENT-10002`).
The code identifies the cause; the HTTP status usually does not.

## 7. Treat a 500 from `/query` as a body-shape problem

Retrying unchanged will not help — correct the request instead.

Each `/query` endpoint has its own body shape. The spec lists the correct
properties per endpoint but marks almost nothing required, so treat every
documented property as potentially mandatory. Minimum bodies that work:

| Endpoint | Body |
|---|---|
| `/events/query` | `{"fields": [...]}` |
| `/activities/query` | `page`, `pageSize`, `sortField`, `sortOrder` — all four |
| `/*/metas/query`, `/events/details/query` | `{"fields": [...], "filters": {"id": [...]}}` |
| `/venues/wifiNetworks/query` | `{"venueIds": [...]}` |
| `/venues/aaaServers/query` | `{"venueId": "..."}` — singular |
| `/entitlements/{banners,compliances}/query`, `/portalServiceProfiles/query` | `{"filters": {}}` |
| `/macRegistrationPools/query` | `{"searchCriteriaList": []}` |

When one fails:

1. Send the properties the spec lists for **that** endpoint, not the envelope that
   worked elsewhere.
2. Path ends in `/metas` or `/details` — supply `fields` + `filters.id`.
3. Tenant-wide aggregate failing — try the venue-scoped path
   (`/venues/{venueId}/…`); they are separate implementations.

A **400** means a key was understood and refused; a **500** means the shape needs
changing. Note that some endpoints declare a shared generic schema and accept only
a subset of the properties it advertises.

## 8. Totals are not always top-level

Rows arrive under `data` or `content`; the total may be nested under
`paging.totalCount` or `pageable`. Reading `response["totalCount"]` finds nothing,
skips the completeness check, and reports truncated data as complete.
`pageable.pageNumber` is 0-indexed.

## 9. Path parameters are not named what you expect

`/activities/{activityId}` (not `{requestId}`), `/identityGroups/{groupId}/…`
(not `{identityGroupId}`). Guessing wrong makes a documented endpoint look
missing.
