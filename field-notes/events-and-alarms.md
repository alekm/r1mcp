# Events and Alarms

## `POST /events/query` requires `fields`

A `fields` list holding at least one recognized name is required; without it the
request is rejected. Nothing else is mandatory.

```jsonc
{"fields": ["event_datetime","severity","entity_type","message","apMac","venueId"],
 "page": 1, "pageSize": 100, "sortField": "event_datetime", "sortOrder": "DESC",
 "filters": {"fromTime": "2026-07-27T00:00:00Z", "toTime": "2026-08-03T23:59:59Z"}}
```

Sort on `event_datetime`, not `startDatetime`. Times here are ISO-8601;
`alarms/query` uses epoch milliseconds. `filters.entity_type` accepts
`AP SECURITY CLIENT SWITCH NETWORK EDGE IOT PROFILE OPTICAL`.

Fields that return data:

```
event_datetime severity entity_type product entity_id message name
apMac clientMac macAddress serialNumber venueId
networkName ssid radio adminName clientName userName hostname ethPort
```

`id` arrives unrequested — it is what the `/metas` lookups need.

**Entity names are not available here.** `apName`, `switchName`, `venueName`,
`apGroupName`, `floorPlanName` and `networkId` never populate on this endpoint;
they come from `/events/metas/query`. Requesting them returns nothing, which looks
like missing data (GENERAL.md §3).

`message` is a JSON-encoded string, not prose — a `message_template` with
`@@` / `%%` placeholders plus a `data` object of entity references. Render it
rather than printing it raw.

## `/metas` and `/details` are ID-keyed lookups, not lists

They take ids you already hold and return extra columns. All require `fields`
**and** `filters.id`; the request is rejected without both.

| Endpoint | Returns |
|---|---|
| `POST /alarms/metas/query` | `venueName`, `apName`, `switchName`, `edgeName`, `oltName`, `isSwitchExists`, `isEdgeExists` |
| `POST /events/metas/query` | the entity names `/events/query` omits |
| `POST /events/details/query` | detail rows; 200 with zero rows for ordinary client events |

`isSwitchExists` / `isEdgeExists` distinguish "no name recorded" from "entity
deleted". Time filters are optional when ids are supplied.

## `POST /alarms/query` returns active alarms only

Alarms clear on recovery, so no history exists here — absence of an alarm is not
evidence a problem never occurred. Use events or activities.

Known-good fields, anything else silently dropped: `startTime, severity,
serialNumber, entityType, entityId, name, message, venueId`. `startTime` is epoch
milliseconds.

## Never-contacted devices cannot alarm

An AP that has not checked in reports only `1_01_NeverContactedCloud` and raises
no alarms, including through a firmware pull that can run a long while. Silence is
not health.
