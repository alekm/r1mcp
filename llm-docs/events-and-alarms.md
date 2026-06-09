# Events and Alarms

> RUCKUS One API Reference

---


## Event

*APIs for retrieving and managing event data.*


*6 endpoints*


### `GET` `/events/adminGroups/{adminGroupId}/latestLogins`

**Get Admin Members Last Logins**

Get admin members last logins.

operationId: `adminGroupMemberLastLogin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `adminGroupId` | path | ✓ | `string` | Admin Group Id |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Last Login Response`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `POST` `/events/csvFiles`

**Export Events Within Date Range**

Export specific events within a date range.

operationId: `exportEvents`


**Request Body:** `Events_and_Alarms_Dynamic Query Payload`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `clientDateFormat` | `string` |  | Client date format. |
| `clientTimeZone` | `string` |  | Client time zone. |
| `detailLevel` | `string` |  | Detail level of the event data. |
| `eventsPeriodForExport` | `object` |  | Events period for export. |
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Filters for the query. |
| `groupBy` | `string` |  | Group by field. |
| `isSupport` | `boolean` |  | Is support user or not. |
| `matchFields` | `array` |  | Match fields for the query. |
| `mustNotMatchFields` | `array` |  | Must not match fields for the query. |
| `page` | `integer` |  | Page number for pagination. |
| `pageSize` | `integer` |  | Number of records per page. |
| `rangeFilter` | `Events_and_Alarms_Range Filter` |  | Range filter for the query. |
| `searchString` | `string` |  | Search string provided by user. |
| `searchTargetFields` | `array` |  | Fields to be searched. |
| `sortField` | `string` |  | Field to sort the results on. |
| `sortOrder` | `string` |  | The order in which results should be sorted. |
| `support` | `boolean` |  | Is support user or not. |
| `tenantId` | `string` |  | The unique identifier for the tenant. |
| `termField` | `Events_and_Alarms_Term Field` |  | Term field for the query. |


**Responses:**

- `200` successful operation
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `POST` `/events/details/query`

**Get Events Details Data**

Get events details with venue, access point and network data.

operationId: `getEventDetails`


**Request Body:** `Events_and_Alarms_Metas request`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Filters alarm metadata by ids. Must provide 'ids' in the filters as a key, whether value of the filters is empty or not. |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Event data`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `POST` `/events/metas/query`

**Get Events Meta Data**

Get events with venue, access point and network data.

operationId: `getEventListMetaData`


**Request Body:** `Events_and_Alarms_Metas request`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Filters alarm metadata by ids. Must provide 'ids' in the filters as a key, whether value of the filters is empty or not. |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Event data`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `POST` `/events/query`

**Get Events**

Get event list information.

operationId: `getEventList`


**Request Body:** `Events_and_Alarms_Event request`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `detailLevel` | `string` |  | Detail level of the event data. |
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Users need to pass a list of string or string as map values. |
| `page` | `integer` |  | Page number for pagination. |
| `pageSize` | `integer` |  | Number of records per page. |
| `searchString` | `string` |  | Search string provided by user. |
| `searchTargetFields` | `array` |  | Fields to be searched. |
| `sortField` | `string` |  | Field to sort the results on. |
| `sortOrder` | `string` |  | The order in which results should be sorted. |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Event data`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `POST` `/historicalClients/query`

**Get Historical Clients**

Get historical client list information grouped by client MAC address.

operationId: `getEventAggList`


**Request Body:** `Events_and_Alarms_Event request`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `detailLevel` | `string` |  | Detail level of the event data. |
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Users need to pass a list of string or string as map values. |
| `page` | `integer` |  | Page number for pagination. |
| `pageSize` | `integer` |  | Number of records per page. |
| `searchString` | `string` |  | Search string provided by user. |
| `searchTargetFields` | `array` |  | Fields to be searched. |
| `sortField` | `string` |  | Field to sort the results on. |
| `sortOrder` | `string` |  | The order in which results should be sorted. |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Event data`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---



## Alarm

*APIs for retrieving and managing alarm data.*


*3 endpoints*


### `POST` `/alarms/metas/query`

**Get Alarms Meta Data**

Get all alarms filtered by the query. Includes venue, access point and network data.

operationId: `getAlarmListMetaData`


**Request Body:** `Events_and_Alarms_Metas request`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Filters alarm metadata by ids. Must provide 'ids' in the filters as a key, whether value of the filters is empty or not. |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Alarm Data`
- `400` Invalid payload supplied
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `POST` `/alarms/query`

**Get Alarms**

Returns the set of alarms. Added the support for MSP tenant. For MSP tenant need to pass tenant ids and sort order.

operationId: `getAlarmList`


**Request Body:** `Events_and_Alarms_Alarm Request`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Fields to be returned in response. |
| `filters` | `object` |  | Filters for the query. |
| `mspEcTenants` | `array` |  | MSP EC tenants filter for the query. |
| `page` | `integer` |  | Page number for pagination. |
| `pageSize` | `integer` |  | Page size for pagination. |
| `sortField` | `string` |  | Field to sort the results on. |
| `sortOrder` | `string` |  | The order in which results should be sorted. |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Alarm Data`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---

### `PATCH` `/alarms/{alarmId}`

**Clear Alarm**

Clear the alarm.

operationId: `clearAlarm`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `alarmId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `204` successful operation
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---



## Group Members Last login Event

*1 endpoint*


### `GET` `/events/adminGroups/{adminGroupId}/latestLogins`

**Get Admin Members Last Logins**

Get admin members last logins.

operationId: `adminGroupMemberLastLogin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `adminGroupId` | path | ✓ | `string` | Admin Group Id |


**Responses:**

- `200` successful operation → `Events_and_Alarms_Last Login Response`
- `400` Invalid payload supplied → `Events_and_Alarms_Error Response`
- `500` Internal Server Error → `Events_and_Alarms_Error Response`
- `501` not implemented


---


