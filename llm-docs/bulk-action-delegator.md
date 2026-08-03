# Bulk Action Delegator

> RUCKUS One API Reference

---


## Bulk Actions

*APIs for submitting and querying bulk action requests.*


*3 endpoints*


### `POST` `/bulkActions`

**Submit a bulk action request**

Accepts a bulk action request that runs the same downstream API call for each item (up to 10,000). The targetApi object must match one of the allowed TargetApi variants. Returns a requestId for tracking; processing happens asynchronously, so use the summary and detail endpoints to monitor progress.

operationId: `submitBulkAction`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `Authorization` | header | ✓ | `string` |  |


**Request Body:** `Bulk_Action_Delegator_BulkActionRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `actions` | `array` | ✓ | List of actions to be executed (max 10000). |
| `targetApi` | `Bulk_Action_Delegator_TargetApi` | ✓ | Definition of the downstream API to call for every item. Must match exactly one allowed TargetApi variant. |


**Responses:**

- `200` OK → `Bulk_Action_Delegator_OperationResponseRequestIdOnly`
- `400` Bad/malformed request → `Bulk_Action_Delegator_ErrorResponse`
- `401` Unauthorized → `Bulk_Action_Delegator_ErrorResponse`
- `403` Forbidden → `Bulk_Action_Delegator_ErrorResponse`
- `404` Requested resource or related entity not found → `Bulk_Action_Delegator_ErrorResponse`
- `422` Validation error → `Bulk_Action_Delegator_ErrorResponse`
- `423` Locked → `Bulk_Action_Delegator_ErrorResponse`
- `500` Internal Server Error → `Bulk_Action_Delegator_ErrorResponse`


---

### `GET` `/bulkActions/{requestId}`

**Get bulk action summary**

Retrieves the overall status, timing, and progress statistics for the bulk action identified by the requestId returned from submit. Use it to poll until the request reaches a terminal state.

operationId: `getBulkActionSummary`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `requestId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Bulk_Action_Delegator_BulkActionSummaryResponse`
- `400` Bad/malformed request → `Bulk_Action_Delegator_ErrorResponse`
- `401` Unauthorized → `Bulk_Action_Delegator_ErrorResponse`
- `403` Forbidden → `Bulk_Action_Delegator_ErrorResponse`
- `404` Requested resource or related entity not found → `Bulk_Action_Delegator_ErrorResponse`
- `422` Validation error → `Bulk_Action_Delegator_ErrorResponse`
- `423` Locked → `Bulk_Action_Delegator_ErrorResponse`
- `500` Internal Server Error → `Bulk_Action_Delegator_ErrorResponse`


---

### `POST` `/bulkActions/{requestId}/query`

**Query bulk action details**

Retrieves execution results for each action item in a bulk action, with pagination, optional filtering by status, and keyword search on description.

operationId: `queryBulkActionDetails`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `requestId` | path | ✓ | `string` |  |


**Request Body:** `Bulk_Action_Delegator_BulkActionDetailRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | Optional filters to apply on action details. Supported fields: status. |
| `page` | `integer` | ✓ | 1-based page index |
| `pageSize` | `integer` | ✓ | Number of actions per page. |
| `searchString` | `string` |  | Optional search keyword used to match results within the specified target fields. |
| `searchTargetFields` | `array` |  | Optional target fields to search against. Supported field: description. |


**Responses:**

- `200` OK → `Bulk_Action_Delegator_BulkActionDetailResponse`
- `400` Bad/malformed request → `Bulk_Action_Delegator_ErrorResponse`
- `401` Unauthorized → `Bulk_Action_Delegator_ErrorResponse`
- `403` Forbidden → `Bulk_Action_Delegator_ErrorResponse`
- `404` Requested resource or related entity not found → `Bulk_Action_Delegator_ErrorResponse`
- `422` Validation error → `Bulk_Action_Delegator_ErrorResponse`
- `423` Locked → `Bulk_Action_Delegator_ErrorResponse`
- `500` Internal Server Error → `Bulk_Action_Delegator_ErrorResponse`


---


