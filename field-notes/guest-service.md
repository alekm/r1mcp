# Guest Service — field notes

## `POST /portalServiceProfiles/query` needs `filters`, and rejects `fields`

Previously recorded as broken. It is not:

```jsonc
POST /portalServiceProfiles/query   {"filters": {}}   -> 200
```

An empty `filters` object is enough. Every other shape fails, and the two failure
modes are worth telling apart:

| Body | Result |
|---|---|
| `{"filters": {}}` | **200** |
| `{}`, `{"page":1,"pageSize":5}`, `{"searchString":""}`, `{…,"sortField":"name"}` | 500 `GUEST-500999` |
| `{"fields":["name"]}` or `{"fields":["id"]}` | **400 `GUEST-400000`** "Invalid attribute value" |

**The spec is actively misleading here.** This endpoint's `requestBody` is the
shared `View_Model_Resources_DynamicQueryPayloadDto`, which advertises 24
properties — `fields`, `page`, `sortField`, `groupBy`, `search_after` and so on.
The endpoint rejects `fields` outright and 500s on the paging keys. So for shared
generic DTOs, reading the schema is **not** enough: it lists what the DTO can
express, not what this endpoint accepts.

The 400 vs 500 split is the useful signal — 400 means the key was understood and
refused, 500 means the body shape was wrong.

## Response shape: `content` + `paging`

```jsonc
{"content": [], "paging": {"page": 1, "pageSize": 256, "totalCount": 0}}
```

Rows under **`content`**, and the total nested under **`paging.totalCount`** — not
at the top level. Code checking `response["totalCount"]` finds nothing and cannot
verify completeness.

`GET /portalServiceProfiles` returns the same shape without a body.
`GET /portalServiceProfiles/networks` and `/tags` return bare arrays.
