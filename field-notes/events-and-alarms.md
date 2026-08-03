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

Known field names, from the console's own request:

```
event_datetime severity entity_type product entity_id message dpName apMac
clientMac macAddress apName switchName serialNumber networkName serviceName
networkId ssid radio raw_event sourceType adminName clientName userName hostname
adminEmail administratorEmail venueName venueId apGroupId apGroupName
floorPlanName recipientName transactionId name ipAddress detailedDescription
duration remoteEdgeId apModel clientMldMac portList authenticationType
profileName action macOui lldpTlv macAcl ethPort successCount failureCount
```

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

## Genuinely broken — verified 2026-08-02 with fields, paging and sort supplied

| Endpoint | Code |
|---|---|
| `POST /events/metas/query` | 500 `EVENT-10001` |
| `POST /events/details/query` | 500 `EVENT-10005` |
| `POST /alarms/metas/query` | 500 |

These resisted every payload variant that fixed `/events/query`. You can read
events and alarms but cannot enumerate their type metadata.

## Never-contacted devices cannot alarm

An AP that has not yet checked in reports only `1_01_NeverContactedCloud` and
generates no alarms — including through a firmware pull that can last a long
while. Silence here is not health.
