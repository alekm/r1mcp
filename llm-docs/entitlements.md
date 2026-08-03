# Entitlements

> RUCKUS One API Reference

---


## Entitlement

*Entitlement management and license operations.*


*16 endpoints*


### `DELETE` `/assignments`

**Revoke Bulk Assignments**

Revoke multiple license assignments for MSP. This method will be removed no sooner than 08/31/2026. The following endpoint '/tenants/{tenantId}/entitlements/assignments/query' can be used for this content.

operationId: `revokeBulkAssignment`


**Request Body:** Yes


**Responses:**

- `204` No Content → `Entitlements_AssignmentOperationResponse`


---

### `GET` `/assignments/summaries`

**Get Assignment Summaries**

Get summaries of MSP license assignments by device type and device subtype. This method will be removed no sooner than 08/31/2026. The following endpoint '/entitlements/utilizations/query' can be used for this content.

operationId: `getAssignmentsSummary`


**Responses:**

- `200` OK


---

### `GET` `/banners`

**Get Banners**

Retrieves entitlement banner notifications for the authenticated tenant. This method will be removed no sooner than 08/31/2026. The following endpoint '/entitlements/banners/query' can be used for this content.

operationId: `getBanners_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `type` | query |  | `string` | Filter by device type (Optional). If device agnostic sku feature is enabled, all device types will be treated as APSW except ANALYTICS. |
| `licenseType` | query |  | `string` | Filter by license type (optional) |


**Responses:**

- `200` OK


---

### `GET` `/entitlements`

**Get Entitlements**

Retrieves the list of device entitlements for the authenticated tenant. This method will be removed no sooner than 08/31/2026.  The following '/entitlements/query' can be used for this content.

operationId: `getEntitlements_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `type` | query |  | `string` | Filter by device type (optional). If device agnostic sku feature is enabled, all device types will be treated as APSW except ANALYTICS. |
| `licenseType` | query |  | `string` | Filter by license type (optional) |


**Responses:**

- `200` Returns the entitlements.
- `404` This tenant does not exist. → `Entitlements_RestApiErrorDto`
- `417` Entitlement ID is missing. → `Entitlements_RestApiErrorDto`


---

### `PATCH` `/entitlements`

**Update Entitlements**

Synchronizes entitlements by triggering a refresh of license data from external licensing systems. This operation fetches the latest license purchases, renewals, and modifications, then updates the local entitlement cache to reflect current entitlements.

**What is synchronized**:  new license purchases, license quantity changes, expiration date updates, license type modifications, subscription renewals.

**Prerequisites**:  the tenant must have an active entitlement ID and at least one active s

operationId: `syncEntitlements`


**Request Body:** `Entitlements_SyncEntitlementRequestDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `refreshType` | `string` |  | Type of refresh operation to perform during synchronization, determining the scope and method of the entitlement data refresh. |
| `status` | `string` |  |  |
| `usageType` | `string` |  | Usage type for entitlement synchronization, specifying the context of the sync operation; deprecated and not used in V2. |


**Responses:**

- `202` Sync entitlements → `Entitlements_AcceptedDto`
- `404` Tenant not found. → `Entitlements_RestApiErrorDto`
- `417` Entitlement ID is missing. At least one tenant subscription must be active. → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `POST` `/entitlements/attentionNotes/query`

**Query License Attention Notes**

Queries license attention notes, which are alerts and notifications related to license status that require administrator attention. Attention notes are automatically generated for important license events such as upcoming change in licensing system.

operationId: `queryAttentionNote`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Entitlements_AttentionNoteQueryDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | Fields to return, all fields will be returned if missing. |
| `filters` | `Entitlements_AttentionNoteQueryFilterDto` |  | Filter criteria for attention note queries, containing type, tenant type, status, and other filtering options to narrow down search results. |
| `page` | `integer` |  | Page number, 1 based, default is 1 if missing. |
| `pageSize` | `integer` |  | Page size, default is 20 if missing. |
| `sortField` | `string` |  | Sorting field, it can be any of the fields of attention notes. |
| `sortOrder` | `string` |  | Sorting order, default is ascending order if missing. |


**Responses:**

- `200` Success → `Entitlements_QueryResponseMapStringObject`
- `403` Access Denied → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `POST` `/entitlements/availabilityReports/query`

**Query Availability Reports**

This endpoint allows you to query availability reports for entitlements.

operationId: `licenseAvailabilityReports`


**Request Body:** `Entitlements_CalculatorRequestDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `effectiveDate` | `string` | ✓ | Start date from which the license is valid. |
| `expirationDate` | `string` |  | End date until which the license is valid. Required if operator max quantity is selected. |
| `filters` | `Entitlements_CalculatorFilterRequestDto` | ✓ | Filter criteria for the request. |
| `operator` | `string` | ✓ | Operator to be used. |
| `quantity` | `integer` |  | Number of licenses available. Required if operator max period is selected. |


**Responses:**

- `200` Success → `Entitlements_CalculatorResponseDto`
- `403` Access Denied → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `POST` `/entitlements/banners/query`

**Get Entitlements Banners**

Retrieve entitlement banner data for display in the user interface. Banners are visual notifications that alert administrators about critical license conditions requiring attention. They provide information about entitlements that are either near their expiry or have expired, helping prevent service disruptions. Version application/vnd.ruckus.v1+JSON will be removed no sooner than 08/31/2026. application/JSON and application/vnd.ruckus.v1.1+JSON are now available.

operationId: `getBanners`


**Request Body:** `Entitlements_EntitlementBannerRequestDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Entitlements_Filters` |  | Filter criteria for determining which entitlement banners to display, containing license type specifications and usage type preferences. |


**Responses:**

- `200` success → `Entitlements_EntitlementBannerResponseDto`
- `404` This tenant does not exist. → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `POST` `/entitlements/compliances/query`

**Get Compliance**

Retrieve detailed license availability reports that calculate how many licenses are currently available for assignment or consumption. This endpoint performs real-time calculations to determine remaining license capacity by analyzing purchased entitlements, active assignments, expired licenses, and reserved allocations. Availability reports are essential for capacity planning and preventing over allocation.

operationId: `getCompliances`


**Request Body:** `Entitlements_LicenseComplianceRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Entitlements_LicenseComplianceFilter` |  | Filter criteria object containing parameters to narrow down compliance query results based on license types and status. |


**Responses:**

- `200` success → `Entitlements_LicenseComplianceResponse`
- `404` This tenant does not exist. → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `GET` `/entitlements/licenseUsageReports`

**Get Entitlement Usage Report**

Get the entitlement usage report.

operationId: `getUsageReport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `licenseType` | query |  | `string` | Specific license type if the tenant is an ALM tenant, valid value: MSP_APSW (default), MSP_URLF, MSP_EDGE_SECS, MSP_EDGE_SECL |
| `startDate` | query |  | `string` | The first date included in the usage report, for example, startDate=2024-01-15; if omitted, the startDate is set to last month's first date. |
| `endDate` | query |  | `string` | The end date included in the usage report, for example, endDate=2024-01-31; if omitted, the endDate is set to last month's last date. |
| `month` | query |  | `string` | month=MM |
| `year` | query |  | `string` | year=YYYY |
| `mspEcTenantId` | query |  | `string` | Specific MSP EC tenant ID |
| `deviceDetails` | query |  | `boolean` | True to include device detail in the report. False to exclude device detail in the report. |
| `page` | query |  | `integer` | Page number for the daily reports. If missing or value 0 means no pagination, all daily reports will be returned. |
| `pageSize` | query |  | `integer` | Page size for the daily reports, default is 5, valid only if page is given |
| `Content-Type` | header | ✓ | `string` |  |


**Responses:**

- `200` Success → `Entitlements_UsageReport`
- `404` Tenant not found. → `Entitlements_EntitlementAssignmentRestException`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `POST` `/entitlements/mileageReports/query`

**Query License Mileage Report**

Mileage reports offer clear insights into how licenses have been consumed and released across different periods.

**Request payload structure:**
accepts a mileage request object containing:
- license type filters
- pagination parameters (`page size`, `page number`)

**Available filters:**
- filter by specific license types
- filter by date range (if applicable)
- additional filters based on business requirements

**Response format:**
returns a mileage response containing a list of mileage report

operationId: `licenseMileageReports`


**Request Body:** `Entitlements_MileageRequestDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Entitlements_CalculatorFilterRequestDto` | ✓ | Filter criteria for the request. |
| `page` | `integer` |  | The page number to be returned, 1 based, default 1. |
| `pageSize` | `integer` |  | The page number to be returned, default 20. |


**Responses:**

- `200` Success → `Entitlements_MileageResponseDto`
- `403` Access Denied → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `POST` `/entitlements/query`

**Get Entitlements**

Retrieves all purchased entitlements for the authenticated tenant. Purchased entitlements represent the licenses, subscriptions, and service rights that an organization has acquired through purchases, contracts, or promotions. Each entitlement includes details about the license type, stock keeping unit (SKU), quantity, effective dates, expiration dates, device compatibility, and current usage status. 

**What constitutes a purchased entitlement**: subscription licenses with defined quantities an

operationId: `getEntitlements`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Entitlements_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultPageSize` | `integer` |  | Default number of records per page to use when pageSize is not explicitly specified or is invalid. |
| `fields` | `array` |  | Set of specific field names to include in the query response, enabling selective data retrieval. |
| `filters` | `Entitlements_DynamicQueryPayloadFilterDto` |  | Filter criteria object containing various conditions to narrow down query results based on specific parameters. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of records to return per page for pagination, with automatic fallback to default if invalid. |
| `sortField` | `string` |  | Field name to use for sorting the query results in ascending or descending order. |
| `sortOrder` | `string` |  | Sort order direction for the specified sort field, typically 'ASC' for ascending or 'DESC' for descending. |


**Responses:**

- `200` success. → `Entitlements_QueryResponse`
- `404` Tenant not found. → `Entitlements_RestApiErrorDto`
- `417` Cannot display subscription data: entitlement ID is missing. At least one tenant subscription must be active. → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `GET` `/entitlements/summaries`

**Get Entitlement Summaries**

Retrieves summarized entitlement utilization data for the authenticated tenant, providing an overview of license usage and availability. This method will be removed no sooner than 08/31/2026. The following endpoint '/entitlements/utilizations/query' can be used for this content.

operationId: `getSummary_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `refresh` | query |  | `boolean` |  |
| `type` | query |  | `string` | Filter by device type (optional). If device agnostic sku feature is enabled, all device types will be treated as APSW except ANALYTICS. |
| `licenseType` | query |  | `string` | Filter by license type (optional) |


**Responses:**

- `200` Returns the entitlement summary. The response is actual in case when the refresh request parameter value is false → `Entitlements_InternalRefreshLicensesResponse`
- `202` Returns Use activity link in the Location header to track the refresh status. The response is actual in case when the refresh request parameter value is true → `Entitlements_AcceptedDto`
- `404` This tenant does not exist. → `Entitlements_RestApiErrorDto`
- `417` This tenant does not have Entitlement ID. → `Entitlements_RestApiErrorDto`


---

### `POST` `/entitlements/utilizations/query`

**Get Entitlements Utilization Summaries**

Retrieve entitlement usage details. Usage summaries provide information on the number of entitlements used and active devices.

operationId: `getSummary`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `Content-Type` | header | ✓ | `string` |  |


**Request Body:** `Entitlements_EntitlementUtilizationQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Entitlements_DynamicQueryPayloadFilterDto` |  | Filter criteria for querying entitlement utilization. |


**Responses:**

- `200` Returns entitlement utilization query response for SELF usage type or assigned entitlement summaries response for ASSIGNED usage type. → `Entitlements_AssignedEntitlementSummariesResponse`
- `404` Tenant not found. → `Entitlements_RestApiErrorDto`
- `417` Cannot display subscription data: entitlement ID is missing. At least one tenant subscription must be active. → `Entitlements_RestApiErrorDto`
- `500` Internal Server Error → `Entitlements_ErrorDto`


---

### `GET` `/mspEntitlements`

**Retrieve MSP bulk license pools**

Retrieves all MSPs bulk entitlements for the authenticated tenant. MSP bulk entitlements are large license pools that MSPs purchase and can then allocate to their customer tenants through assignments. Each entitlement includes details such as device type, SKUs, quantity, effective date, expiration date, and trial status. The response returns a list of MspEntitlement objects containing all bulk licenses available to the MSP. This method will be removed no sooner than 08/31/2026. The following end

operationId: `getMspEntitlements`


**Responses:**

- `200` OK


---

### `GET` `/mspEntitlements/summaries`

**Sync MSP entitlement summaries**

Retrieves MSPs entitlement summaries with an optional refresh capability. When called without the 'refresh' parameter or with 'refresh=false', returns cached summary data including all MSPs bulk entitlements, expiration banners, and aggregated summaries by device type. When called with 'refresh=true', initiates a synchronization with external licensing systems to update entitlement data from the source, then returns a 202 accepted response with an activity tracking link to monitor the refresh pr

operationId: `syncMspEntitlements`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `refresh` | query |  | `boolean` |  |


**Responses:**

- `200` Success → `Entitlements_MspEntitlementsRefreshData`
- `202` Accepted - refresh request submitted → `Entitlements_AcceptedDto`


---



## Manage Entitlements

*5 endpoints*


### `POST` `/tenants/self/entitlements/assignments`

**Create a Self Assignment**

Creates a self assignment by allocating licenses from the MSP's bulk entitlement pool to their own tenant account. Self assignments allow MSPs to assign licenses to their own devices rather than to customer tenants. This is useful when the MSP needs to manage and license their own device separately from customer allocations.

operationId: `createEntitlementAssignment`


**Request Body:** `Entitlements_CreateAssignmentReq`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `effectiveDate` | `string` | ✓ | Effective date of the entitlement assignment. |
| `expirationDate` | `string` | ✓ | Expiration date of the entitlement assignment. |
| `licenseType` | `string` | ✓ | Type of entitlement license being assigned. |
| `quantity` | `integer` | ✓ | Quantity of entitlements assigned. |
| `trial` | `boolean` |  | Flag indicating whether this assignment is for a trial period with limited duration and features. |


**Responses:**

- `201` Created a self assignment → `Entitlements_EntitlementAssignmentResp`
- `400` Bad input, such as missing required fields. → `Entitlements_ErrorDto`
- `500` Internal server error. → `Entitlements_ErrorDto`


---

### `POST` `/tenants/self/entitlements/assignments/query`

**Get MSP Self Assignments**

Retrieves self assignments, which are entitlement allocations where the tenant manages their own license distribution for internal use.
An MSP uses self assignments to allocate licenses from their bulk license pool to their own tenant account, rather than assigning them to customer tenants.
Self assignments represent licenses that the provider reserves for managing their own devices.
This allows providers to separate their internal license consumption from customer allocations for better trackin

operationId: `getSelfEntitlementAssignments`


**Request Body:** `Entitlements_QueryAssignmentReq`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | A list of assignment data fields to be returned. |
| `filters` | `Entitlements_QueryAssignmentFilters` |  | Filter criteria for querying assignments. |
| `page` | `integer` |  | The page number to be returned, 1 based, default 1. |
| `pageSize` | `integer` |  | The page number to be returned, default 20. |
| `sortField` | `string` |  | The data filed name which will be used for sorting the query result. |
| `sortOrder` | `string` |  | The sorting order, default is ascending order. |


**Responses:**

- `200` OK → `Entitlements_QueryResponse`
- `400` Bad input, missing tenant ID. → `Entitlements_ErrorDto`
- `500` Internal server error. → `Entitlements_ErrorDto`


---

### `DELETE` `/tenants/self/entitlements/assignments/{id}`

**Delete Self Assignment**

Deletes an active self assignment by marking it as revoked. When a license is deleted, it is not physically removed from the system but instead marked as revoked and can no longer be used. The assignment record is preserved for audit purposes. Returns a 204 no content status code on successful deletion, or a 409 conflict if the assignment has already expired or been revoked.

operationId: `deleteEntitlementAssignment`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `integer` |  |


**Responses:**

- `204` Assignment deleted successfully
- `400` Bad input, such as missing required fields. → `Entitlements_ErrorDto`
- `409` If the assignment already have been revoked. → `Entitlements_ErrorDto`
- `500` Internal server error. → `Entitlements_ErrorDto`


---

### `PATCH` `/tenants/self/entitlements/assignments/{id}`

**Update a Self Assignment**

Updates an existing self assignment where the MSPs has allocated licenses to their own tenant account. Quantity and expiry date can be modified for self assignments. When updating assignments, existing assignments will be revoked and new assignments will be created with the updated fields. This allows MSPs to adjust the number of licenses allocated to their own infrastructure as their needs change.

operationId: `updateEntitlementAssignment`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `integer` |  |


**Request Body:** `Entitlements_UpdateAssignmentReq`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `expirationDate` | `string` | ✓ | Expiration date of the entitlement assignment. |
| `quantity` | `integer` | ✓ | Quantity of entitlements assigned. |
| `valid` | `boolean` |  | Indicates whether the assignment request contains valid data with at least one non null field (expirationDate or quantity). |


**Responses:**

- `200` Assignment updated successfully → `Entitlements_EntitlementAssignmentResp`
- `400` Bad input, such as missing required fields. → `Entitlements_ErrorDto`
- `402` Insufficient license → `Entitlements_ErrorDto`
- `409` If the assignment has already expired. → `Entitlements_ErrorDto`
- `500` Internal server error. → `Entitlements_ErrorDto`


---

### `POST` `/tenants/{tenantId}/entitlements/assignments/query`

**Get Tenant Entitlement Assignments**

Retrieves entitlement assignments allocated to a specific customer tenant by an MSP.
Entitlement assignments represent the allocation of licenses from a provider's bulk license pool to individual MSP_EC tenants, enabling customers to use specific products and services based on the assigned license quantities and types.
This endpoint allows providers to view which licenses have been assigned to a tenant, and monitor assignment details including quantities, expiration dates, and current status.

U

operationId: `getEntitlementAssignments`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Request Body:** `Entitlements_QueryAssignmentReq`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | A list of assignment data fields to be returned. |
| `filters` | `Entitlements_QueryAssignmentFilters` |  | Filter criteria for querying assignments. |
| `page` | `integer` |  | The page number to be returned, 1 based, default 1. |
| `pageSize` | `integer` |  | The page number to be returned, default 20. |
| `sortField` | `string` |  | The data filed name which will be used for sorting the query result. |
| `sortOrder` | `string` |  | The sorting order, default is ascending order. |


**Responses:**

- `200` OK → `Entitlements_QueryResponse`
- `400` Bad input, missing tenant ID. → `Entitlements_ErrorDto`
- `500` Internal server error. → `Entitlements_ErrorDto`


---


