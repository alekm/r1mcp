# Identity Management (Personal Identity Network)

The identity group is the join point binding DPSK, MAC registration, certificates
and policy to a set of people or devices — it carries `personalIdentityNetworkId`,
`dpskPoolId`, `macRegistrationPoolId`, `certificateTemplateId`, `policySetId` and
`propertyId`.

## `POST /identities/query` ignores paging entirely

It returns the same first 20 rows regardless of what you send. A paging loop
re-collects them and **inflates** the result, which reads as data rather than an
error. This is the worst pagination failure in the API.

Use instead:

```
GET /identityGroups/{groupId}/identities?page=0&size=500
```

Pages correctly with `page`/`size`, **0-indexed**, rows under `content`. The path
parameter is `{groupId}` — searching the spec for `{identityGroupId}` finds
nothing and makes a documented endpoint look missing.

## Identities carry the AP binding for Property Management units

`ethernetPorts` on the identity is the readable form of a unit's AP binding, which
Property Management itself does not expose:

```jsonc
"ethernetPorts": [{"macAddress": "<AA-BB-CC-DD-EE-FF>", "portIndex": 1, "name": "<apName>"}]
```

Populated means bound, empty means not. Immediate, unlike the AP-side signal
(`lanPortStatuses[id="0"].wanConnectivity` flipping `"WAN"` to `"Not Applicable"`),
which lags a reporting cycle.

**MACs are hyphen-separated here and colon-separated on the AP object** —
normalize before comparing.

## Unit identities are created and destroyed with the unit

Property Management units mint an identity named `UNIT_<name>-<epoch>` holding the
unit's `dpskPassphrase` and `vni`. Deleting the unit destroys it; recreating mints
a **new passphrase**, silently breaking every device already onboarded.
