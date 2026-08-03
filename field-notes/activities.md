# Activities — field notes

## The activity ID is the `requestId` returned by any 202

`GET /activities/{activityId}` accepts the `requestId` handed back by a mutating
call. The spec documents the two independently and never links them, so activities
reads as a passive "view" group when it is actually the completion-tracking
mechanism for every write in the API. See GENERAL.md §1.

A terminal `status` plus `steps[].progressSummary` is the only reliable
confirmation that a write landed.

```jsonc
{
  "requestId": "<uuid>",
  "status": "SUCCESS",
  "useCase": "UpdateAp",
  "admin": {"name": "Application <app-name>"},
  "steps": [
    {"id": "ApplyConfigToImpactedDevices", "status": "SUCCESS", "progressType": "DEVICE",
     "progressSummary": {"pending": 0, "inProgress": 0, "success": 0, "fail": 0, "offline": 0}},
    {"id": "UpdateAp", "status": "SUCCESS", "progressType": "REQUEST"}
  ],
  "descriptionTemplate": "AP \"@@apName\" (SN:\"@@serialNumber\") was updated"
}
```

## `POST /activities/query` is the tenant change-history / audit log

Durable; observed 1,026 records on one tenant.

**Pick the right log.** `activities` records *configuration changes and who made
them*. `/events/query` records *what happened on the network* — client joins, AP
state, security — and it works too (it needs a `fields` list; see
events-and-alarms.md). An earlier version of these notes said events was broken
and activities was the only option. That was wrong. `/alarms/query` holds active
alarms only, so it is not a history at all.

**All four of `page`, `pageSize`, `sortField` and `sortOrder` are required.**
Omit any one and the endpoint returns **500**, not 400 — so it reads as broken
rather than under-specified. An unrecognized `sortField` is also a 500.

```jsonc
{"page": 1, "pageSize": 500, "sortField": "startDatetime", "sortOrder": "DESC"}
```

Optional additions, taken from the console's own request:

```jsonc
{"fields": ["startDatetime","endDatetime","status","product","admin",
            "descriptionTemplate","descriptionData","severity"],
 "searchTargetFields": ["description","source"], "searchString": "",
 "filters": {"fromTime": "2026-08-02T02:27:00Z", "toTime": "2026-08-03T02:27:00Z"}}
```

`filters.fromTime`/`toTime` are **ISO-8601 strings** here — note the contrast with
`alarms/query`, where `startTime` is epoch milliseconds. Omit `filters` entirely
and you get the full history. `fields`, `searchString`, `defaultPageSize` and
`total` are all optional; the console sends them but the API does not need them.

Carries a `useCase` taxonomy (`ADD_UNIT`, `DELETE_UNIT`, `UpdateAp`, `AddSwitch`,
`DeleteAp`, `UpdateFloorPlan`, `UpdateApRadioSettings`, `SUBMIT_BULK_ACTION`, …)
plus `totalSuccessSteps` / `totalFailSteps`.

**It attributes every change to an actor.** Console users appear by name, API
integrations as `Application <name>`, platform automation under its own identity.
`Application rai-token` performing `UpdateApRadioSettings` is RUCKUS AI changing
radio settings autonomously — so "was this even a human?" is answerable.

Pagination is `page`/`pageSize`, 1-indexed.
