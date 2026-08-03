# Guest Service

## `POST /portalServiceProfiles/query` needs `filters` and rejects `fields`

```jsonc
{"filters": {}}   -> 200
```

An empty `filters` object is the whole requirement. Sending `fields` returns
`400 GUEST-400000`; sending paging or sort keys without `filters` returns
`500 GUEST-500999`.

This endpoint declares a shared generic query schema advertising ~24 properties it
does not accept — see GENERAL.md §7.

Response is `content` + `paging`, with the total nested at `paging.totalCount`.

`GET /portalServiceProfiles` returns the same shape with no body.
`GET /portalServiceProfiles/networks` and `/tags` return bare arrays.
