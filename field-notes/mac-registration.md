# MAC Registration

## `POST /macRegistrationPools/query` uses a Spring-style body and response

No `fields`, no `filters`, no `sortField`:

```jsonc
{"searchCriteriaList": [], "dataOption": "SUMMARY"}   // dataOption optional
```

Omitting `searchCriteriaList` returns 500.

The response is a Spring page:

```jsonc
{"content": [...], "pageable": {"pageNumber": 0, "pageSize": 20}, "totalElements": 0}
```

Rows under `content`; `pageable.pageNumber` is **0-indexed**. Code reaching for
`data` finds nothing and reports an empty pool list.

`GET /macRegistrationPools` returns the plain collection — simpler when you do not
need search criteria.
