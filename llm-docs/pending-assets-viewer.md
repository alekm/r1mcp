# Pending Assets Viewer

> RUCKUS One API Reference

---


## Pending Assets Viewer

*Retrieve pending asset information including access points and switches.*


*4 endpoints*


### `GET` `/deviceProvisions/aps/models`

**Get Access Point Device Models**

Retrieve list of available access point device models.

operationId: `getApDeviceAssetModels`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `includeHidden` | query |  | `boolean` | Whether to include hidden device models in the response. Default is false to show only non hidden models. |


**Responses:**

- `200` Successfully retrieved AP device models
- `400` Bad/malformed request. → `Pending_Assets_Viewer_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Viewer_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Viewer_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Viewer_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Viewer_ErrorResponse`


---

### `POST` `/deviceProvisions/aps/query`

**Query Access Point Device Assets**

Retrieve access point device assets based on search criteria with pagination support.

operationId: `getApDeviceAssets`


**Request Body:** `Pending_Assets_Viewer_DeviceSearchRequestDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `createdDateFrom` | `string` |  | Start date for device creation filter. |
| `createdDateTo` | `string` |  | End date for device creation filter. |
| `dayRange` | `string` |  | Date range filter for device creation. |
| `filterModels` | `array` |  | List of model names to filter by. |
| `includeHidden` | `boolean` |  | Whether to include hidden devices in the results. |
| `order` | `string` |  |  |
| `page` | `integer` | ✓ | Page number for pagination (0-based). |
| `searchText` | `string` |  | Text to search for in device information. |
| `size` | `integer` | ✓ | Number of items per page. |
| `sortColumn` | `string` |  | Column name to sort by. |


**Responses:**

- `200` Successfully retrieved AP device assets → `Pending_Assets_Viewer_DevicePageResponseView`
- `400` Bad/malformed request. → `Pending_Assets_Viewer_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Viewer_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Viewer_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Viewer_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Viewer_ErrorResponse`


---

### `GET` `/deviceProvisions/switches/models`

**Get Switch Device Models**

Retrieve list of available switch device models.

operationId: `getSwitchDeviceAssetModels`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `includeHidden` | query |  | `boolean` | Whether to include hidden device models in the response. Default is false to show only non hidden models. |


**Responses:**

- `200` Successfully retrieved Switch device models
- `400` Bad/malformed request. → `Pending_Assets_Viewer_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Viewer_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Viewer_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Viewer_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Viewer_ErrorResponse`


---

### `POST` `/deviceProvisions/switches/query`

**Query Switch Device Assets**

Retrieve switch device assets based on search criteria with pagination support.

operationId: `getSwitchDeviceAssets`


**Request Body:** `Pending_Assets_Viewer_DeviceSearchRequestDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `createdDateFrom` | `string` |  | Start date for device creation filter. |
| `createdDateTo` | `string` |  | End date for device creation filter. |
| `dayRange` | `string` |  | Date range filter for device creation. |
| `filterModels` | `array` |  | List of model names to filter by. |
| `includeHidden` | `boolean` |  | Whether to include hidden devices in the results. |
| `order` | `string` |  |  |
| `page` | `integer` | ✓ | Page number for pagination (0-based). |
| `searchText` | `string` |  | Text to search for in device information. |
| `size` | `integer` | ✓ | Number of items per page. |
| `sortColumn` | `string` |  | Column name to sort by. |


**Responses:**

- `200` Successfully retrieved Switch device assets → `Pending_Assets_Viewer_DevicePageResponseView`
- `400` Bad/malformed request. → `Pending_Assets_Viewer_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Viewer_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Viewer_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Viewer_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Viewer_ErrorResponse`


---


