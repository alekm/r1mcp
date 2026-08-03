# field-notes/

Hand-written, permanent. **Not generated — never overwritten by a spec regen.**

This is the counterpart to `llm-docs/`, which is mechanically regenerated from the
RUCKUS One OpenAPI spec and wiped each time. `llm-docs/` says what endpoints
*exist*; this directory says which ones lie, which are broken, and how they relate
to each other — none of which is derivable from the spec.

## How it reaches the model

| File | Surfaced as |
|---|---|
| `GENERAL.md` | Injected into the MCP server instructions — always in context, no tool call |
| `<group>.md` | Appended to `r1_get_docs("<group>")` output, below the generated docs |
| any | Returned wholesale by `r1_field_notes()` |

Filenames match `llm-docs/` group slugs exactly (e.g. `wi-fi-services.md`). A file
here with no matching group is still readable via `r1_field_notes` but will never
be appended to anything — check the slug.

## Adding a note

Only record behavior **verified against a live tenant** that the spec does not
capture, or contradicts. Prefer relationships between endpoints over restating
signatures — the generated docs already have signatures.

### The test: is the fact already in the spec?

If yes, leave it out — `llm-docs/` already carries it and a second copy just goes
stale. Checked against the August 2026 spec:

| Already in the spec — **do not duplicate** | |
|---|---|
| Request body property names per endpoint | under `requestBody`, and accurate |
| Which response shape an endpoint uses | `data` ×145, `content`+`pageable` ×34, `content`+`paging` ×28 |
| Paths, methods, path parameters, response codes | all of it |

| Not in the spec — **this is what belongs here** | |
|---|---|
| Which body fields are **required** | only 11 of 196 `/query` ops declare any; the rest say nothing and still refuse to work |
| Valid values for `fields` | 0 of 196 have an enum |
| That a 202's `requestId` is an activity ID | 651 ops return 202; 2 mention activities |
| Endpoints missing altogether | `POST /edgeDhcpServices/dhcpClientLeases/query` — verified absent |
| Path parameters named differently than you expect | `/activities/{activityId}` not `{requestId}`; `/identityGroups/{groupId}/…` not `{identityGroupId}` — a wrong guess makes a documented endpoint look missing |
| Anything a schema cannot express | silent truncation, clobbering writes, DPSK reissue, staleness, credential exposure |

The line is finer than "documented or not". For `/venues/aaaServers/query` the
spec **does** show `venueId`; what it does not show is that the call fails without
it. Record the constraint, not the property list.

Shared DTOs are the exception worth naming: several endpoints declare a generic
schema advertising properties they actually reject, so "it is in the spec" does
not mean "this endpoint accepts it".

Keep `GENERAL.md` short. It is in every context window, so it earns its place only
with cross-cutting traps that a model cannot know to look up — by the time it
would think to check, it has already been given a wrong answer silently.

All content here is original observation, not derived from the RUCKUS spec, and is
covered by this repository's MIT license — unlike `llm-docs/` (see
`llm-docs/NOTICE`).
