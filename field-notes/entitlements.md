# Entitlements

## License utilization is one call

```jsonc
POST /entitlements/utilizations/query   {"page": 1, "pageSize": 20}
-> {"licenseType": "APSW", "quantity": 338, "usedQuantity": 329,
    "remainingQuantity": 9, "assignedQuantity": 338}
```

Do not inventory devices and subtract — it is laborious and wrong.

- `GET /entitlements` — per-SKU detail: name, tier, quantity, effective and
  expiration dates, trial vs assigned, grace end
- `GET /assignments/summaries` — MSP assignment

## Body shapes

| Endpoint | Body |
|---|---|
| `/entitlements/banners/query` | `{"filters": {}}` — empty object is enough |
| `/entitlements/compliances/query` | `{"filters": {}}` |
| `/entitlements/availabilityReports/query` | requires `effectiveDate`, today or later |
| `/entitlements/mileageReports/query` | requires `usageType` |

`compliances` returns rows under a `compliances` key, not `data`, and can contain
`null` entries — guard before dereferencing.

`GET /entitlements/licenseUsageReports` returns 400 `"Not a MSP"` on a non-MSP
tenant.
