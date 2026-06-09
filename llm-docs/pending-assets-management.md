# Pending Assets Management

> RUCKUS One API Reference

---


## Pending Assets Management

*Device provisioning and management APIs for access points and switches.*


*6 endpoints*


### `PATCH` `/deviceProvisions/aps`

**Update Access Points Status**

Updates the operational status of access points.

operationId: `addHiddenAccessPoints`


**Request Body:** `Pending_Assets_Management_DeviceManagementRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `serials` | `array` | ✓ | List of device serial numbers to perform the action on. |
| `status` | `string` | ✓ | Management action to perform on the specified devices. |


**Responses:**

- `200` Access Points status updated successfully → `Pending_Assets_Management_DeviceManagementResponse`
- `400` Bad/malformed request. → `Pending_Assets_Management_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Management_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Management_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Management_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Management_ErrorResponse`


---

### `GET` `/deviceProvisions/aps/statusReports`

**Get AP Refresh Status**

Retrieve latest refresh status for access points. Returns filtered status report based on requested fields.

operationId: `getApRefreshJob`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fields` | query |  | `array` | Fields to include in response. Only refreshedTime is currently supported. If omitted, refreshedTime will be returned by default. |


**Responses:**

- `200` Successfully retrieved latest refresh status → `Pending_Assets_Management_FilteredRefreshJobResponse`
- `400` Bad/malformed request. → `Pending_Assets_Management_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Management_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Management_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Management_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Management_ErrorResponse`


---

### `PATCH` `/deviceProvisions/aps/statusReports`

**Refresh Access Points**

Initiates a refresh operation for access points and synchronizes the latest access point data to the database.

operationId: `triggerApRefreshAction`


**Request Body:** `Pending_Assets_Management_ActionStatusRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `status` | `string` | ✓ |  |


**Responses:**

- `200` Refresh action triggered successfully → `Pending_Assets_Management_RefreshStatusReportResponse`
- `400` Bad/malformed request. → `Pending_Assets_Management_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Management_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Management_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Management_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Management_ErrorResponse`


---

### `PATCH` `/deviceProvisions/switches`

**Update Switch Status**

Updates the operational status of switches.

operationId: `addHiddenSwitches`


**Request Body:** `Pending_Assets_Management_DeviceManagementRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `serials` | `array` | ✓ | List of device serial numbers to perform the action on. |
| `status` | `string` | ✓ | Management action to perform on the specified devices. |


**Responses:**

- `200` Switch status updated successfully → `Pending_Assets_Management_DeviceManagementResponse`
- `400` Bad/malformed request. → `Pending_Assets_Management_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Management_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Management_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Management_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Management_ErrorResponse`


---

### `GET` `/deviceProvisions/switches/statusReports`

**Get Switch Refresh Status**

Retrieve latest refresh status for switches. Returns filtered status report based on requested fields.

operationId: `getSwitchRefreshJob`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fields` | query |  | `array` | Fields to include in response. Only refreshedTime is currently supported. If omitted, refreshedTime will be returned by default. |


**Responses:**

- `200` Successfully retrieved latest refresh status → `Pending_Assets_Management_FilteredRefreshJobResponse`
- `400` Bad/malformed request. → `Pending_Assets_Management_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Management_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Management_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Management_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Management_ErrorResponse`


---

### `PATCH` `/deviceProvisions/switches/statusReports`

**Refresh Switches**

Initiates a refresh operation for switches and synchronizes the latest switches data to the database.

operationId: `triggerSwitchRefreshAction`


**Request Body:** `Pending_Assets_Management_ActionStatusRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `status` | `string` | ✓ |  |


**Responses:**

- `200` Refresh action triggered successfully → `Pending_Assets_Management_RefreshStatusReportResponse`
- `400` Bad/malformed request. → `Pending_Assets_Management_ErrorResponse`
- `401` Unauthorized → `Pending_Assets_Management_ErrorResponse`
- `403` Forbidden → `Pending_Assets_Management_ErrorResponse`
- `404` Requested resource or related entity not found. → `Pending_Assets_Management_ErrorResponse`
- `500` Internal Server Error → `Pending_Assets_Management_ErrorResponse`


---


