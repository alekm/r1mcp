# Property Management

## Recreating a unit reissues its DPSK

Each unit gets an auto-created identity (`UNIT_<name>-<epoch>`) holding its
`dpskPassphrase` and `vni`. **Deleting the unit destroys that identity; recreating
mints a new passphrase** — every device already onboarded to that unit silently
stops connecting.

The `resident` object survives if echoed back on the re-POST. The credential does
not. Deleting a unit also releases its bound AP; that port reverts to `WAN`.

## AP-to-unit binding is creation-only

```
PATCH /venues/{venueId}/units/{unitId}  with accessPoint
  -> 400 PROPERTY-MANAGEMENT-001 "Changing accessPoint not supported"
```

The AP can only be attached in the `POST` that creates the unit, so rebinding an
existing unit requires DELETE + re-POST — which triggers the DPSK reissue above.

## `identityCount` is not an occupancy signal

It counts only non-system identities and reads 0 even for units with a named
resident and email address. Anything using it to guard a destructive operation is
unguarded. **Check the `resident` object instead.**

## The AP binding is not readable here

No Property Management endpoint returns `accessPoint` — not `GET /units/{unitId}`,
not the list, not `/units/query`. Read it from the identity instead — see
identity-management.md.

## Assorted

- `UnitAp` binds by **AP name**, not serial. Bind an unnamed AP and it is recorded
  under its serial string, which cannot be resolved later. Name APs before binding.
- `selectedPorts[].portIndex` must be positive, and is 1-indexed while
  `lanPortStatuses` ids are 0-indexed: `portIndex: 1` is the port reported as
  `id: "0"`.
- Binding sets the AP's `useVenueSettings` to `false` and can leave `poeMode`
  unset, so venue LAN-port settings stop reaching it. Set `poeMode` explicitly
  after binding.
- `sortOrder` is required on every query in this group — `/units/query`,
  `/venues/propertyConfigs/query`, `/residentPortals/query` — though none mark it
  required. Omitting it returns `400 PROPERTY-MANAGEMENT-007`.
- `resident` is required on a unit but `resident.email` is not. Omitting the
  address means no resident notification can fire.
- These `GET`s use `page`/`size`, **0-indexed**.
