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
identities use `GET /identityGroups/{groupId}/identities?page=0&size=500`, which
pages correctly. (The path parameter is `{groupId}` — searching for
`{identityGroupId}` finds nothing and makes it look undocumented.)

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

## 7. A 500 almost always means the wrong request body — not a broken endpoint

**This is the most expensive mistake to make against this API.** A tenant-wide
sweep produced eleven endpoints that returned `500` and looked dead. Every one of
them works. Not a single confirmed-broken endpoint remains.

The 500s say "something went wrong, please wait a few minutes and try again".
Waiting never helps: the request was never going to succeed as sent.

### The spec has the property names. It does not say they are required.

Read each endpoint's `requestBody` properties in `llm-docs` — they are accurate,
and they differ per endpoint. There is no universal query envelope.

What the spec will not tell you, and what actually causes the 500s:

- **Only 11 of 196 `/query` operations declare any required body field.** The
  other 185 declare nothing and still refuse to work. Treat every documented
  property as potentially mandatory.
- **No `fields` array anywhere has an enum**, so valid field names are
  undiscoverable. Send a name the endpoint does not know and it is silently
  dropped (§3); send *only* unknown names and you get a 500.
- **Shared DTOs lie by omission.** Several endpoints declare a generic schema
  advertising properties they reject — `/portalServiceProfiles/query` uses one
  with 24 properties and refuses `fields` with a 400.

Required-in-practice, declared-optional-in-spec:

| Endpoint | Minimum body |
|---|---|
| `/events/query` | `{"fields": [...]}` |
| `/activities/query` | `page`, `pageSize`, `sortField`, `sortOrder` — all four |
| `/*/metas/query`, `/events/details/query` | `{"fields": [...], "filters": {"id": [...]}}` |
| `/venues/wifiNetworks/query` | `{"venueIds": [...]}` |
| `/venues/aaaServers/query` | `{"venueId": "..."}` — singular |
| `/entitlements/{banners,compliances}/query`, `/portalServiceProfiles/query` | `{"filters": {}}` |
| `/macRegistrationPools/query` | `{"searchCriteriaList": []}` |

### Procedure when a `/query` returns 500

1. Look up the endpoint's `requestBody` properties in the spec and send **those**
   keys, not the envelope that worked elsewhere.
2. If the path ends in `/metas` or `/details`, supply `fields` + `filters.id`.
3. If a tenant-wide aggregate fails, try the venue-scoped path
   (`/venues/{venueId}/…`) — they are separate implementations.
4. Only after all of that is a 500 evidence of anything.

**Caveat on reading the spec:** some endpoints share a generic DTO — e.g.
`/portalServiceProfiles/query` uses `View_Model_Resources_DynamicQueryPayloadDto`,
which advertises 24 properties. That endpoint rejects `fields` with a 400 and 500s
on the paging keys. The schema describes what the DTO can express, not what the
endpoint accepts. A **400** means a key was understood and refused; a **500**
means the shape was wrong.

The only endpoint still returning an error is
`GET /entitlements/licenseUsageReports` (`"Not a MSP"`) — a permission boundary on
a non-MSP tenant, not a fault.

## Totals are not always at the top level

The spec documents which response shape each endpoint returns, so check there
rather than guessing. The trap it does not flag: in two of the three shapes the
row count is **nested**, under `paging.totalCount` or `pageable`. Code reading
`response["totalCount"]` finds nothing, skips the completeness check, and reports
truncated data as complete — the §2 failure with a different cause.

`pageable.pageNumber` is also **0-indexed** where the standard shape is 1-indexed.

Sweep scope: 237 read-only endpoints with no path parameters across all 31 groups;
212 returned 200.
