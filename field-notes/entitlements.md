# Entitlements — field notes

## License utilization is one call — do not count devices

```jsonc
POST /entitlements/utilizations/query   {"page": 1, "pageSize": 20}
-> {"licenseType": "APSW", "quantity": 338, "usedQuantity": 329,
    "remainingQuantity": 9, "assignedQuantity": 338}
```

Inventorying devices and subtracting is the obvious approach and it is both
laborious and wrong.

- `GET /entitlements` — per-SKU detail: SKU name, tier, quantity,
  effective/expiration dates, trial vs assigned, grace end
- `GET /assignments/summaries` — MSP assignment

## Body shapes — verified 2026-08-02

`banners` and `compliances` were previously recorded as broken. They are not —
they take **only** a `filters` object, and an empty one is enough. Omitting the
key is a 500 `ENTITLEMENT-10000`.

```jsonc
POST /entitlements/banners/query      {"filters": {}}   -> 200 {"data": []}
POST /entitlements/compliances/query  {"filters": {}}   -> 200 {"compliances": [null]}
```

Note `compliances` returns its rows under a `compliances` key, not `data`, and can
contain `null` entries — guard before dereferencing.

`GET /entitlements/licenseUsageReports` returns 400 `"Not a MSP"` on a non-MSP
tenant. That is a permission boundary rather than a fault; it has also been seen
returning a raw Java stack trace.

Endpoints that need extra fields rather than being broken:

- `POST /entitlements/availabilityReports/query` — requires `effectiveDate`,
  which must be today or later (`ENTITLEMENT-10200`)
- `POST /entitlements/mileageReports/query` — requires `usageType`
