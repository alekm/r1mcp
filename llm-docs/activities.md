# Activities

> RUCKUS One API Reference

---


## View Activities

*View platform information. Note: this group of endpoints is used to view activities data. They don't provide the means to manage configuration.*


*4 endpoints*


### `POST` `/activities/query`

**Query Activities**

Get activities by query criteria.

operationId: `findActivityList`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `rks-scopes` | header |  | `string` |  |


**Request Body:** `Activities_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Available fields |
| `filters` | `object` |  | Filters |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Page size |
| `searchString` | `string` |  | Target string for search |
| `searchTargetFields` | `array` |  | Target fields for search |
| `sortField` | `string` |  | Sort fields |
| `sortOrder` | `string` |  | Sort order |


**Responses:**

- `200` Successful operation → `Activities_QueryResponseActivityDto`
- `400` Invalid payload supplied → `Activities_ActivityErrorResponse`
- `404` Tenant ID not found → `Activities_ActivityErrorResponse`
- `501` Not implemented → `Activities_ActivityErrorResponse`


---

### `GET` `/activities/{activityId}`

**Access Activity by ID**

Get activity details.

operationId: `getDetails`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `activityId` | path | ✓ | `string` |  |
| `rks-scopes` | header |  | `string` |  |


**Responses:**

- `200` Successful operation → `Activities_ActivityDto`
- `400` Invalid payload supplied → `Activities_ActivityErrorResponse`
- `404` Tenant ID not found → `Activities_ActivityErrorResponse`
- `501` Not implemented → `Activities_ActivityErrorResponse`


---

### `POST` `/activities/{activityId}/devices/query`

**Query Device Activities**

Get device activities by query criteria.

operationId: `findActivityDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `activityId` | path | ✓ | `string` |  |


**Request Body:** `Activities_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Available fields |
| `filters` | `object` |  | Filters |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Page size |
| `searchString` | `string` |  | Target string for search |
| `searchTargetFields` | `array` |  | Target fields for search |
| `sortField` | `string` |  | Sort fields |
| `sortOrder` | `string` |  | Sort order |


**Responses:**

- `200` Successful operation → `Activities_QueryResponseDeviceDto`
- `400` Invalid payload supplied → `Activities_ActivityErrorResponse`
- `404` Tenant ID not found → `Activities_ActivityErrorResponse`
- `501` Not implemented → `Activities_ActivityErrorResponse`


---

### `PUT` `/activities/{activityId}/notifications`

**Replace Activity Notification**

Update activity notification options.

operationId: `updateActivityNotification`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `activityId` | path | ✓ | `string` |  |


**Request Body:** `Activities_NotificationData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  | Checked if its enabled. |
| `endpoint` | `string` |  | Notification endpoint |
| `type` | `string` |  |  |


**Responses:**

- `200` Successful operation → `Activities_ActivityDto`
- `400` Invalid payload supplied → `Activities_ActivityErrorResponse`
- `404` Tenant ID not found → `Activities_ActivityErrorResponse`
- `501` Not implemented → `Activities_ActivityErrorResponse`


---


