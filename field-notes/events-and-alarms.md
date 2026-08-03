# Events and Alarms — field notes

## `POST /events/query` WORKS — it requires `fields`

Corrects an earlier finding. This endpoint was recorded as persistently broken
because a bare query returns `500 EVENT-10002 "Something went wrong… please wait
a few minutes and try again"`. It is not broken and the wait does nothing.

**It requires a `fields` list containing at least one recognized field name.**
Nothing else is mandatory — not paging, not sort, not filters.

```jsonc
POST /events/query
{"fields": ["event_datetime","severity","entity_type","message","apName","venueName"],
 "page": 1, "pageSize": 100, "sortField": "event_datetime", "sortOrder": "DESC",
 "filters": {"fromTime": "2026-07-27T00:00:00Z", "toTime": "2026-08-03T23:59:59Z"}}
```

Verified 2026-08-02: 5,342 events over one week on a live tenant.

Behavior of `fields` here matches the general rule (GENERAL.md §3) — unrecognized
names are silently dropped, so a bogus field mixed with valid ones is harmless. A
list containing **only** unrecognized names leaves zero valid selections and
returns the same 500. So the 500 really means "no valid field selected".

Sort field is `event_datetime`, not `startDatetime`. `filters.fromTime`/`toTime`
are ISO-8601 strings. `filters.entity_type` accepts
`["AP","SECURITY","CLIENT","SWITCH","NETWORK","EDGE","IOT","PROFILE","OPTICAL"]`.
`detailLevel: "debug"` is accepted and optional.

### Only 20 of the 56 accepted fields ever return data

The console sends 56 field names. Measured over 200 events on a live tenant, these
**20** came back:

```
event_datetime severity entity_type product entity_id message name
apMac clientMac macAddress serialNumber venueId
networkName ssid radio adminName clientName userName hostname ethPort
```

`id` and `indexName` come back **without being requested** — convenient, since
`id` is what the `/metas` lookups need.

The other 36 returned nothing across the whole sample:

```
dpName apName switchName serviceName networkId raw_event sourceType adminEmail
administratorEmail venueName apGroupId apGroupName floorPlanName recipientName
transactionId ipAddress detailedDescription Persona-ID duration remoteEdgeId
apModel minimumRequiredVersion clientMldMac turnOnTimestamp turnOffTimestamp
portList authenticationType profileName action macOui lldpTlv macAcl
rodanAvProfileTemplate cleanupNote successCount failureCount
```

**This is by design, not a gap — and it is why `/metas` exists.** Nine of those
absent fields (`apName`, `switchName`, `venueName`, `apGroupId`, `apGroupName`,
`floorPlanName`, `networkId`, `recipientName`, `administratorEmail`) are exactly
what `/events/metas/query` resolves. `/events/query` hands you **ids and MACs**;
names come from the second call. Asking `/events/query` for `apName` returns
nothing and looks like missing data (GENERAL.md §3) rather than a routing
decision.

Caveat on the sample: it covered `CLIENT` (167), `SECURITY` (22) and `AP` (11)
events only. Fields specific to switch, edge or IoT events may populate where this
sample could not show it. Absence here means "not for these event types", not
"never".

`message` comes back as a **JSON-encoded string**, not prose — it holds a
`message_template` with `@@placeholder` / `%%placeholder` markers plus a `data`
object of entity references. Render it yourself; do not show it raw.

## `POST /alarms/query` returns active alarms only

Alarms clear on recovery, so alarm history does not exist here. Absence of an
alarm is not evidence a problem never occurred — use events or activities.

Known-good fields — anything else is silently dropped (GENERAL.md §3):

```
startTime, severity, serialNumber, entityType, entityId, name, message, venueId
```

`startTime` is epoch **milliseconds** here, while events uses ISO-8601 strings.

## The `/metas` and `/details` endpoints are ID-keyed lookups, not lists

**Generalizable rule.** A `/query` endpoint ending in `/metas` or `/details` does
not list anything. It takes ids you already have and returns extra columns for
them. All of them require **`fields` plus `filters.id`**, and every one returns
500 without both — which is why the whole set was written off as broken.

| Endpoint | Needs | Returns |
|---|---|---|
| `POST /alarms/metas/query` | `fields` + `filters.id` | names behind each alarm |
| `POST /events/metas/query` | `fields` + `filters.id` | names behind each event |
| `POST /events/details/query` | `fields` + `filters.id` | detail rows (often empty) |

Get the ids from `/alarms/query` or `/events/query` first. Those return ids,
serials and timestamps but **no venue, AP, switch or network names** — resolving
them is a deliberate second call, and this is it.

`filters.fromTime`/`toTime` are accepted inside `filters` here and are optional
when ids are supplied.

`/events/details/query` returns 200 with zero rows for ordinary client-connect
events; detail rows appear only for event types that carry them. Zero rows is a
valid answer, not a failure.

## `POST /alarms/metas/query` WORKS — it resolves names for alarm IDs

Also previously recorded as broken. It is not a catalogue of alarm types; it is a
**lookup keyed by alarm ID** that returns the human-readable names behind an
alarm. It requires **both** `fields` and `filters.id`, and 500s (`ALARM-10003`)
without either.

```jsonc
POST /alarms/metas/query
{"fields": ["venueName","apName","switchName","edgeName","oltName"],
 "filters": {"id": ["<alarmId>", "<alarmId>"]}}
```

Returns per id: `venueName`, `apName`, `switchName`, `edgeName`, `oltName`, plus
`isSwitchExists` / `isEdgeExists` booleans — useful for telling "no name" apart
from "entity is gone". `filters.alarmType: ["new"]` is accepted and optional.

Get the ids from `POST /alarms/query` first. This is a second call by design: the
alarm objects carry ids and serials, not venue or device names.

## Nothing in this group is broken

Every endpoint here that was previously recorded as a persistent 500 —
`/events/query`, `/events/metas/query`, `/events/details/query`,
`/alarms/metas/query` — works once the required body fields are supplied. The
"please wait a few minutes and try again" text is misleading: waiting changes
nothing, and the request was never going to succeed as sent.

## Never-contacted devices cannot alarm

An AP that has not yet checked in reports only `1_01_NeverContactedCloud` and
generates no alarms — including through a firmware pull that can last a long
while. Silence here is not health.
