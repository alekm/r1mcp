# Venues

## `PUT /venues/{venueId}/floorplans/{floorPlanId}` is a whole-object write

Requires `floorNumber`, `imageId`, `imageName`, `name` — omitted fields are lost.

Floor numbers are **0-indexed** and appear to need to be unique per venue, so
renumbering a stack requires an order that avoids collisions mid-sequence.

## Venue AP settings only reach APs with `useVenueSettings: true`

Binding an AP to a Property Management unit flips that flag to `false` and can
leave `poeMode` unset, after which venue LAN-port settings silently stop applying.
See property-management.md.

PoE mode is set per AP model — see wi-fi-services.md.

## AP state does not live here

`POST /venues/aps/query` (view-model-resources) carries AP state.
`GET /venues/{venueId}/aps/{serialNumber}` returns roughly two fields.
