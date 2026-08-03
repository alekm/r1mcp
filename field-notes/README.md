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

Keep `GENERAL.md` short. It is in every context window, so it earns its place only
with cross-cutting traps that a model cannot know to look up — by the time it
would think to check, it has already been given a wrong answer silently.

All content here is original observation, not derived from the RUCKUS spec, and is
covered by this repository's MIT license — unlike `llm-docs/` (see
`llm-docs/NOTICE`).
