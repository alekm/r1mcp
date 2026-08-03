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

## Broken — verified 2026-08-02

| Endpoint | Behavior |
|---|---|
| `POST /entitlements/banners/query` | 500 `ENTITLEMENT-10000` |
| `POST /entitlements/compliances/query` | 500 `ENTITLEMENT-10000` |
| `GET /entitlements/licenseUsageReports` | 400 |

`licenseUsageReports` has been seen two ways: a raw Java stack trace, and a plain
`"Not a MSP"` on a non-MSP tenant. Either way there is no working variant — do not
route around it.

Endpoints that need extra fields rather than being broken:

- `POST /entitlements/availabilityReports/query` — requires `effectiveDate`,
  which must be today or later (`ENTITLEMENT-10200`)
- `POST /entitlements/mileageReports/query` — requires `usageType`
