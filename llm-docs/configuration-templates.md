# Configuration Templates

> RUCKUS One API Reference

---


## Configuration Template

*Manage the configuration templates.*


*6 endpoints*


### `POST` `/templates/{templateId}/dependencies/query`

**Query Template Dependency**

Query template dependency (direct children only) for a specific template with pagination and sorting. Add prefix '/rec' for REC templates.

operationId: `queryDependency`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Configuration_Templates_HierarchyQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |


**Responses:**

- `200` OK → `Configuration_Templates_HierarchyQueryResponse`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `PUT` `/templates/{templateId}/enforcementSettings`

**Update Template Enforcement Settings**

Update template enforcement settings.  Add prefix '/rec' for REC templates.

operationId: `enforcementSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |
| `Authorization` | header | ✓ | `string` |  |


**Request Body:** `Configuration_Templates_EnforceRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `isEnforced` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Configuration_Templates_EnforceResponse`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/{templateId}/instances/query`

**Query Drift Instances**

Query drift instances with filter for template. Add prefix '/rec' for REC templates.

operationId: `queryInstances`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |
| `page` | query |  | `integer` |  |
| `pageSize` | query |  | `integer` |  |


**Request Body:** `Configuration_Templates_QueryTemplateInstanceRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filter` | `Configuration_Templates_QueryTemplateInstanceFilter` |  |  |


**Responses:**

- `200` OK → `Configuration_Templates_DriftInstanceResponse`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/{templateId}/tenants/{tenantId}`

**Apply Template**

Apply a template to the target tenant for creating instances. Add prefix '/rec' for REC templates.

operationId: `applyTemplateV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |
| `tenantId` | path | ✓ | `string` |  |
| `Authorization` | header | ✓ | `string` |  |


**Request Body:** `Configuration_Templates_ApplyRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `overrides` | `array` |  | List of key value pairs to override the template. Only venue template is supported with overriding the following attributes: name, description, address.addressLine, address.city, address.country, address.countryCode, address.latitude, address.longitu |


**Responses:**

- `200` OK → `Configuration_Templates_ApplyTemplateResponse`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `GET` `/templates/{templateId}/tenants/{tenantId}/diffReports`

**Retrieve Diff Reports**

Retrieve diff reports from drift tenant.

operationId: `getDiffReport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `PATCH` `/templates/{templateId}/tenants/{tenantId}/diffReports`

**Sync Template**

Sync the configuration template to a drift tenant.

operationId: `sync`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |
| `tenantId` | path | ✓ | `string` |  |
| `Authorization` | header | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Configuration_Templates_SyncResponse`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---


