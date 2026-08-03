# field-notes/

Hand-written, permanent. **Not generated — never overwritten by a spec regen.**

`llm-docs/` is regenerated from the RUCKUS One OpenAPI spec and says what
endpoints exist. This directory says what the spec does not: which calls fail
silently, which need a body the spec marks optional, and how endpoints relate.

## How it reaches the model

| File | Surfaced as |
|---|---|
| `GENERAL.md` | injected into the MCP server instructions — always in context |
| `<group>.md` | appended to `r1_get_docs("<group>")`, below the generated docs |
| any | returned by `r1_field_notes()` |

Filenames match `llm-docs/` group slugs exactly (e.g. `wi-fi-services.md`).

## What belongs here

Operational guidance for making calls against RUCKUS One. Nothing else — this is
not a notebook, a changelog, or a record of what was tried.

Include only behavior **verified against a live tenant** that a caller cannot get
from `llm-docs/`:

- constraints the spec omits — required fields it marks optional, valid values it
  gives no enum for
- silent failures — dropped fields, ignored paging, absent keys, stale reads
- consequences a schema cannot express — writes that clobber, deletes that reissue
  credentials, totals that lie
- relationships between endpoints — which call resolves what another withholds
- endpoints missing from the spec entirely

Leave out anything `llm-docs/` already carries: property names, response shapes,
paths, methods, status codes. The line is finer than "documented or not" — for
`/venues/aaaServers/query` the spec shows `venueId`; what it omits is that the
call fails without it. **Record the constraint, not the property list.**

Keep `GENERAL.md` short. It is in every context window, so it earns its place only
with cross-cutting traps a caller cannot know to look up.

All content here is original observation, not derived from the RUCKUS spec, and is
covered by this repository's MIT license — unlike `llm-docs/` (see
`llm-docs/NOTICE`).
