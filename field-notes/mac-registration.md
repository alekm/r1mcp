# MAC Registration — field notes

## `POST /macRegistrationPools/query` uses a Spring-style body and response

Previously recorded as broken. It is not — it shares nothing with the usual query
envelope. No `fields`, no `filters`, no `sortField`:

```jsonc
POST /macRegistrationPools/query
{"searchCriteriaList": [], "dataOption": "SUMMARY"}   // dataOption optional
```

Omitting `searchCriteriaList` returns a 500 with a bare Spring error body.

The **response** is a Spring page, not the usual `data` + `totalCount`:

```jsonc
{"content": [...],
 "pageable": {"pageNumber": 0, "pageSize": 20, "sort": {...}},
 "totalElements": 0}
```

Rows are under **`content`**, and `pageable.pageNumber` is **0-indexed**. Code
that reaches for `data` finds nothing and reports an empty pool list.

`GET /macRegistrationPools` also works and returns the plain collection — simpler
when you do not need search criteria.
