# Activities

## The activity ID is the `requestId` from any 202

`GET /activities/{activityId}` accepts the `requestId` returned by a mutating
call. A terminal `status` plus `steps[].progressSummary` is the only reliable
confirmation a write landed. See GENERAL.md §1.

```jsonc
{"requestId": "<uuid>", "status": "SUCCESS", "useCase": "UpdateAp",
 "admin": {"name": "Application <app-name>"},
 "steps": [{"id": "ApplyConfigToImpactedDevices", "status": "SUCCESS",
            "progressType": "DEVICE",
            "progressSummary": {"pending": 0, "inProgress": 0, "success": 0,
                                "fail": 0, "offline": 0}}]}
```

## `POST /activities/query` is the configuration change log

Requires all four of `page`, `pageSize`, `sortField`, `sortOrder`. Any missing —
or an unrecognized `sortField` — returns 500.

```jsonc
{"page": 1, "pageSize": 500, "sortField": "startDatetime", "sortOrder": "DESC"}
```

Optional: `fields`, `searchString`, `searchTargetFields`, and
`filters.fromTime`/`toTime` as ISO-8601 strings. Omit `filters` for full history.

Carries a `useCase` taxonomy (`ADD_UNIT`, `DELETE_UNIT`, `UpdateAp`, `AddSwitch`,
`DeleteAp`, `UpdateFloorPlan`, `UpdateApRadioSettings`, `SUBMIT_BULK_ACTION`, …)
plus `totalSuccessSteps` / `totalFailSteps`.

**Every change is attributed.** Console users appear by name, API integrations as
`Application <name>`, and platform automation under its own identity — including
RUCKUS AI adjusting radio settings on its own. So "who changed this, and was it a
person?" is answerable.

Pick the right log: **activities** = configuration changes and who made them;
**`/events/query`** = what happened on the network; **`/alarms/query`** = active
alarms only, not a history.
