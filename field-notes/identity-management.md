# Identity Management — field notes

RUCKUS calls this surface the **Personal Identity Network (PIN)**. The identity
group object carries a `personalIdentityNetworkId`, and it is the join point for
DPSK, MAC registration, certificates and policy: `dpskPoolId`,
`macRegistrationPoolId`, `certificateTemplateId`, `policySetId`, `propertyId`.
A group is how those services are bound to a set of people or devices.

## `POST /identities/query` ignores paging entirely

It returns the same first 20 rows regardless of what you send. A paging loop
re-collects those rows and **inflates** the result — which reads as data rather
than as an error. This is the worst pagination failure in the API.

**Use instead:**

```
GET /identityGroups/{groupId}/identities?page=0&size=500
```

This is in the spec — note the path parameter is `{groupId}`, not
`{identityGroupId}` as earlier notes had it. Searching for the wrong name makes it
look undocumented. Same trap as `/activities/{activityId}` vs `{requestId}`.

It works and pages correctly, using `page`/`size` **0-indexed**. Rows arrive under
`content`, not `data`.

## Identities carry the AP binding for Property Management units

`ethernetPorts` on the identity is the readable form of a unit's AP binding,
which Property Management itself does not expose:

```jsonc
"ethernetPorts": [{"macAddress": "<AA-BB-CC-DD-EE-FF>", "portIndex": 1, "name": "<apName>"}]
```

MACs are **hyphen-separated** here and colon-separated on the AP object.
See property-management.md.

## Unit identities are auto-created and destroyed with the unit

Property Management units mint an identity named `UNIT_<name>-<epoch>` holding the
unit's `dpskPassphrase` and `vni`. Deleting the unit destroys it; recreating mints
a **new passphrase**, silently breaking every device already onboarded.
