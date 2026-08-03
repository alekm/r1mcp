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

## Broken

`GET /entitlements/licenseUsageReports` returns **400 with a raw Java stack
trace**. Do not route around it — there is no working variant.
