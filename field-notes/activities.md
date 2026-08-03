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

The only working change history — `/events/query` is broken and `/alarms/query`
holds active alarms only. Durable; observed 1,026 records on one tenant.

```jsonc
{"page": 1, "pageSize": 500, "sortField": "startDatetime", "sortOrder": "DESC"}
```

Carries a `useCase` taxonomy (`ADD_UNIT`, `DELETE_UNIT`, `UpdateAp`, `AddSwitch`,
`DeleteAp`, `UpdateFloorPlan`, `UpdateApRadioSettings`, `SUBMIT_BULK_ACTION`, …)
plus `totalSuccessSteps` / `totalFailSteps`.

**It attributes every change to an actor.** Console users appear by name, API
integrations as `Application <name>`, platform automation under its own identity.
`Application rai-token` performing `UpdateApRadioSettings` is RUCKUS AI changing
radio settings autonomously — so "was this even a human?" is answerable.

Pagination is `page`/`pageSize`, 1-indexed.
