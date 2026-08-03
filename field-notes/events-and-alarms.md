# Events and Alarms — field notes

## `POST /events/query` is broken

Returns **HTTP 500 `EVENT-10002`**, persistently — not a transient failure. There
is no working variant to fall back to.

For change history use `POST /activities/query` (see activities.md). It is the
only durable option.

## `POST /alarms/query` returns active alarms only

Alarms clear on recovery, so alarm history does not exist here. Absence of an
alarm is not evidence a problem never occurred.

Known-good fields — anything else is **silently dropped** (GENERAL.md §3):

```
startTime, severity, serialNumber, entityType, entityId, name, message, venueId
```

`startTime` is epoch **milliseconds**.

## Never-contacted devices cannot alarm

An AP that has not yet checked in reports only `1_01_NeverContactedCloud` and
generates no alarms — including through a firmware pull that can last a long
while. Silence here is not health.
