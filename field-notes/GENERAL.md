# RUCKUS One — behavior the API spec does not describe

Apply these to every call. They cover cases where a response is misleading — 2xx
with incomplete data, or a 5xx that means the request needs changing.

## 1. A 202 is not a completed write

Mutating calls return `202` with a `requestId`. **That `requestId` is an activity
ID** — poll it before verifying state or reporting success:

```
GET /activities/{requestId}   ->  status: SUCCESS | FAIL | ...
```

`status` is the only outcome signal. Two traps, both verified 2026-09-04:

**`errors[]` can be non-empty on a `SUCCESS`.** A DPSK passphrase update that
stored the value verbatim and kept its bound devices still returned
`errors: [{"code": "DPSK-10032"}]` at both step and top level, alongside
`totalFailSteps: 0`. The *same* code appears on the failure case, there with a
populated `message`. So branch on `status` (cross-check `totalFailSteps`), never
on the presence of `errors`. Treat an error code as diagnostic, not determinative.

**`progressSummary` is not always there.** It appears only on steps with
`progressType: "DEVICE"` — a config push fanning out to hardware. Where it
exists, `pending`/`inProgress`/`success`/`fail`/`offline` separates "cloud
accepted the config" from "config reached the device", and a SUCCESS with a
non-zero `offline` count means those devices never got it. But a DPSK passphrase
update produces a single `progressType: "REQUEST"` step with **no
`progressSummary` at all**, so code that reaches for it unconditionally will
break on the write you most want to verify. Per-device detail, where a DEVICE
step exists: `POST /activities/{activityId}/devices/query`.

**A 202 can be followed by an asynchronous FAIL that changes nothing.** A
passphrase longer than 63 characters returns 202, resolves to `status: FAIL` with
`DPSK-10032`, and leaves the prior value in place. Read the object back and
compare before reporting success — a terminal status alone does not tell you what
the stored state is.

Validation detail arrives as a **JSON document encoded in a string** in
`errors[].message`, not in any HTTP error body:

```
errors[0].message = "{\"message\":\"Validation Error\",\"subErrors\":[{
                       \"field\":\"passphrase\",\"rejectedValue\":\"…\",
                       \"message\":\"Size must be between 8 and 63\"}]}"
```

Parse it to get the reason. Note `rejectedValue` can contain the submitted
secret.

## 2. Four pagination conventions, all failing silently

| Convention | Where |
|---|---|
| `page` / `pageSize`, **base varies — probe it** | most `POST /…/query` |
| `page` / `size`, 0-indexed | identity and Property Management `GET`s |
| paging is fatal | `POST /dpskServices/query` — any `page`/`pageSize` returns 500 |
| paging ignored | `POST /identities/query` — same 20 rows forever |

An unrecognized paging parameter is ignored, the default page size applies, and
the total still reports correctly — so truncated data looks complete.

```
GET /venues/{venueId}/units?page=0&pageSize=500  ->  20 rows, totalElements 290
GET /venues/{venueId}/units?page=0&size=500      -> 290 rows, totalElements 290
```

**The index base is not a property of the key names.** Two endpoints use
`page`/`pageSize` with *different* bases, so there is no rule to memorize —
verified 2026-09-04:

| Endpoint | Base | Rows key | Total key |
|---|:---:|---|---|
| `POST /dpskServices/{poolId}/passphrases/query` | **1** | `data` | `totalCount` |
| `POST /dpskServices/{poolId}/passphrases/{id}/devices/query` | **0** | `content` | `totalElements` |

`/passphrases/query` rejects `page: 0` with a **500** — which is a rejected
*value*, not the wrong body shape (see §7). `/devices/query` returns a Spring
`Page` and is 0-indexed like every Spring pageable. That correlation — flat
envelope vs Spring `Page` — is a useful guess for an endpoint you have not
probed, but it is a guess.

Sending base 1 to a 0-indexed endpoint is the dangerous case: you get a full
page back, so the convention looks honored, and you have silently skipped the
first page. `r1_fetch_all` probes the base per endpoint rather than assuming it.

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

## 7. Treat a 500 from `/query` as "fix the request", not only "fix the shape"

Retrying unchanged will not help — correct the request instead. The cause is
usually the body shape, but it can equally be a rejected **value**: `page: 0`
against `/dpskServices/{poolId}/passphrases/query` returns 500 on a body the
endpoint otherwise accepts, and the same body with `page: 1` succeeds (§2).

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

A **400** usually means a key was understood and refused; a **500** usually means
the shape needs changing. Neither is reliable enough to diagnose from the status
alone — the DPSK device endpoints return **400** for a wrong body shape, and
`/passphrases/query` returns **500** for a correctly-shaped body carrying a bad
paging value. Read the response body. Note also that some endpoints declare a
shared generic schema and accept only a subset of the properties it advertises.

To tell a shape problem from a value problem, re-send with the suspect key
removed: if that succeeds, the shape was never wrong.

**Bare-array bodies.** Some DPSK collection endpoints take a bare JSON array of
identifiers rather than an object — an object gets 400, or
`GENERAL-003 "Malformed JSON request."` Verified 2026-09-04:

| Endpoint | Body |
|---|---|
| `POST /dpskServices/{poolId}/passphrases/{passphraseId}/devices` | `["aa:bb:cc:dd:ee:ff"]` |
| `DELETE /dpskServices/{poolId}/passphrases/{passphraseId}/devices` | `["aa:bb:cc:dd:ee:ff"]` |
| `DELETE /dpskServices/{poolId}/passphrases` | `["<passphraseId>"]` |

## 8. Totals are not always top-level

Rows arrive under `data` or `content`; the total may be nested under
`paging.totalCount` or `pageable`. Reading `response["totalCount"]` finds nothing,
skips the completeness check, and reports truncated data as complete.
`pageable.pageNumber` is 0-indexed.

## 9. Path parameters are not named what you expect

`/activities/{activityId}` (not `{requestId}`), `/identityGroups/{groupId}/…`
(not `{identityGroupId}`). Guessing wrong makes a documented endpoint look
missing.
