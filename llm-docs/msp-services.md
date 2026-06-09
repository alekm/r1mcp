# MSP Services

> RUCKUS One API Reference

---


## Tenant Activation Management

*Supports the activation and deactivation of a managed tenant. Control support team access for managed tenants.*


*9 endpoints*


### `GET` `/mspCustomers/{customerId}/activationStatus`

**Get Tenant Activation Status**

Check whether a tenant account is currently activated or deactivated. 
This method will be removed no sooner than 06/30/2026.

operationId: `getMspEcActivationStatus`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the tenant to get MSP data. |


**Responses:**

- `200` Ok → `MSP_Services_MspEc`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/mspCustomers/{customerId}/delegations`

**Disable Support Access**

Revoke support team access to the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL DELETE /tenantActivations/supportStatus/{tenantId} can be used for this content.

operationId: `disableRuckusSupport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant Id  |


**Responses:**

- `204` No Content → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/delegations`

**Get Support Access Status**

Check whether support team access is currently enabled or disabled for the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenantActivations/supportStatus/{tenantId} can be used for this content.

operationId: `getRuckusSupportStatus_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant Id  |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers/{customerId}/delegations`

**Enable Support Access**

Grant support team access to assist with tenant account issues. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenantActivations/supportStatus/{tenantId} can be used for this content.

operationId: `enableRuckusSupport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant Id  |


**Responses:**

- `201` Created → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/tenantActivations/supportStatus/{tenantId}`

**Disable Support Access**

Revoke support team access to the tenant account, removing their ability to view or modify tenant settings.

operationId: `disableSupport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenantActivations/supportStatus/{tenantId}`

**Get Support Access Status**

Check whether support team access is currently enabled or disabled for the tenant account.

operationId: `getRuckusSupportStatus`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenantActivations/supportStatus/{tenantId}`

**Enable Support Access**

Grant support team access to assist with tenant account issues, allowing them to troubleshoot and resolve technical problems.

operationId: `enableSupport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/tenantActivations/{tenantId}`

**Deactivate Tenant**

Suspend login access and disable all operations for a tenant account.

operationId: `deActivateTenant`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenantActivations/{tenantId}`

**Reactivate Tenant**

Restore login access and enable all operations for a previously deactivated tenant.

operationId: `reActivateTenant`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---



## View MSP

*View MSP and VAR information. Note: this group of endpoints is used to view operational data. They don't provide the means to manage configuration.*


*5 endpoints*


### `POST` `/delegations`

**Get Delegations**

Get the list of customer delegations. This method will be removed no sooner than 06/30/2026. The following URL POST /delegations/query can be used for this content.

operationId: `getDelegationsForViewLegacy`


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_DelegationData`
- `400` Bad request. → `MSP_Services_QueryResponseDelegationData`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseDelegationData`


---

### `POST` `/mspecs/query`

**Query Customer Data for MSP-EC**

Retrieves customer details for managed service providers end customers. This method will be removed no sooner than 06/30/2026. The following URL POST /tenants/query can be used for this content.

operationId: `queryMSPECs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegation` | query |  | `string` |  |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspEcDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspEcDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspEcDto`


---

### `POST` `/msps/{mspTenantId}/ecInventories/query`

**Query Inventory for MSP**

View the list of networking devices installed in end customers venues. This method will be removed no sooner than 06/30/2026. The following URL POST /tenants/inventories/query can be used for this content.

operationId: `getDeviceInventory`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mspTenantId` | path | ✓ | `string` | Tenant Id of the MSP. |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspInventoryDeviceDto`


---

### `POST` `/msps/{mspTenantId}/ecInventories/query/csvFiles`

**Export End Customer Inventory**

Export the list of networking devices installed in our end customers venues.

operationId: `exportDeviceInventory_MSP`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mspTenantId` | path | ✓ | `string` | Tenant Id of the MSP. |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_StreamingResponseBody`
- `400` Bad request. → `MSP_Services_StreamingResponseBody`
- `404` Requested resource or related entity not found. → `MSP_Services_StreamingResponseBody`


---

### `POST` `/techpartners/mspecs/query`

**Query Technology Partners**

Retrieves the list of managed service providers end customers for technology partners based on the provided query parameters. This method will be removed no sooner than 06/30/2026. The following URL POST /tenants/query can be used for this content.

operationId: `getMSPECs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegation` | query |  | `string` |  |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspEcDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspEcDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspEcDto`


---



## Firmware Upgrade Scheduling

*Manages firmware upgrade schedules for access points and switches. Supports recurring automated upgrades and one time manual scheduling options.*


*2 endpoints*


### `POST` `/firmwareUpgradeSchedules`

**Schedule Firmware Upgrade**

Create or update firmware upgrade schedules with automatic or manual timing options.

operationId: `setScheduleForFirmwareUpgrades`


**Request Body:** `MSP_Services_FirmwareUpgradeRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `data` | `MSP_Services_DataRequest` |  | The bulk operation data. |
| `operation` | `string` | ✓ | The bulk operation type. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers/firmwareUpgradeSchedules`

**Schedule Firmware Upgrade**

Create or update firmware upgrade schedules with automatic or manual timing options. 
This method will be removed no sooner than 06/30/2026. 
The following URL POST /firmwareUpgradeSchedules can be used for this content.

operationId: `mspFirmwareUpgrade`


**Request Body:** `MSP_Services_FirmwareUpgradeRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `data` | `MSP_Services_DataRequest` |  | The bulk operation data. |
| `operation` | `string` | ✓ | The bulk operation type. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---



## Query MSP Customer Information V3

*Retrieves customer information with support for service mode filtering. These endpoints are specifically designed for viewing operational data and do not facilitate configuration management.*


*0 endpoints*




## Query Inventory Information

*Retrieves inventory information. These endpoints are specifically designed for viewing operational data and do not facilitate configuration management.*


*1 endpoint*


### `POST` `/tenants/inventories/query`

**Query Device Inventory Data**

Retrieves customer device inventory data.

operationId: `queryDeviceInventoryData`


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `403` Forbidden no relation between MSP and JWT tenant. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `500` Internal server error. → `MSP_Services_QueryResponseMspInventoryDeviceDto`


---



## Query Delegation Information

*Retrieves delegation information. These endpoints are specifically designed for viewing operational data and do not facilitate configuration management.*


*1 endpoint*


### `POST` `/delegations/query`

**Query Delegation Data**

Retrieves customer delegation data.

operationId: `queryCustomerDelegationData`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `inclEntitlements` | query |  | `boolean` |  |
| `inclPGFilter` | query |  | `boolean` |  |
| `eetMail` | query |  | `string` |  |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_DelegationData`
- `500` Internal server error. → `MSP_Services_QueryResponseDelegationData`


---



## Query MSP Customer Information

*Retrieves customer information. These endpoints are specifically designed for viewing operational data and do not facilitate configuration management.*


*1 endpoint*


### `POST` `/tenants/query`

**Query Tenant Accounts**

Retrieve a list of managed tenant accounts including customer and tech partner information.

operationId: `queryCustomerOrTechPartnerDataV3`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `Content-Type` | header |  | `string` |  |
| `delegation` | query |  | `string` |  |
| `includeDelegations` | query |  | `boolean` |  |
| `type` | query |  | `string` |  |
| `eetMail` | query |  | `string` |  |
| `includeTpBasic` | query |  | `boolean` |  |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` successful operation → `MSP_Services_QueryResponseMspEcDto`
- `400` Invalid tenant_id supplied → `MSP_Services_QueryResponseMspEcDto`
- `404` tenant_id not found → `MSP_Services_QueryResponseMspEcDto`
- `415` Unsupported Media Type - service mode filter requires V3 content type and feature flag → `MSP_Services_QueryResponseMspEcDto`
- `501` not implemented → `MSP_Services_QueryResponseMspEcDto`


---



## Tenant Delegation Management

*Manages delegation relationships between service provider accounts, technology partners, installers, and tenant accounts. Supports assigning tenant accounts to technology partners and controlling organizational access permissions.*


*6 endpoints*


### `PATCH` `/mspCustomers/delegations`

**Add Designated Tenant Accounts**

Add or update MSP-EC account relationships with multiple integrator or installer accounts. 
This method will be removed no sooner than 06/30/2026. 
The following URL PATCH /tenantDelegations can be used for this content.

operationId: `assignMspEcToMultipleTechPartner`


**Request Body:** `MSP_Services_AssignMspEcToMultipleTechPartners`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `AssignDelegatedRequest` | `array` |  | List of tech partner details. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspIntegrators/{integratorId}`

**Retrieve Tenant Delegations**

Retrieve active relationships between designated accounts and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/tenantDelegations can be used for this content.

operationId: `getMspEcListToIntegrator`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `integratorId` | path | ✓ | `string` | MSP-EC Delegated Id |
| `delegationType` | query | ✓ | `string` |  |


**Responses:**

- `200` Ok → `MSP_Services_MspEcDelegationResponse`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/mspIntegrators/{integratorId}`

**Update Tenant Delegations**

Update active relationships between designated accounts and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/tenantDelegations can be used for this content.

operationId: `assignMspEcListToDelegated`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `integratorId` | path | ✓ | `string` | MSP-EC Delegated Id |


**Request Body:** `MSP_Services_AssignMspEcListRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `delegation_type` | `string` | ✓ | The type of MSP EC delegated tenant. |
| `isManageAllEcs` | `boolean` |  | Flag to admins to manage account. |
| `mspec_list` | `array` |  | List of MSP EC to be assigned. |
| `number_of_days` | `string` |  | Expiry days for MSP EC to delegated tenant. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/tenantDelegations`

**Add Designated Tenant Accounts**

Add or update MSP-EC account relationships with multiple integrator or installer accounts, enabling them to manage designated tenants.

operationId: `patchTenantDelegations`


**Request Body:** `MSP_Services_AssignMspEcToMultipleTechPartners`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `AssignDelegatedRequest` | `array` |  | List of tech partner details. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenants/{tenantId}/tenantDelegations`

**Retrieve Tenant Delegations**

Retrieve active relationships between designated accounts and their managed tenant, including delegation status and permissions.

operationId: `getTenantDelegations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |
| `delegationType` | query |  | `string` |  |


**Responses:**

- `200` Ok → `MSP_Services_MspEcDelegationResponse`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenants/{tenantId}/tenantDelegations`

**Update Tenant Delegations**

Update active relationships between designated accounts and their managed tenant, modifying access permissions and delegation settings.

operationId: `updateTenantDelegations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_AssignMspEcListRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `delegation_type` | `string` | ✓ | The type of MSP EC delegated tenant. |
| `isManageAllEcs` | `boolean` |  | Flag to admins to manage account. |
| `mspec_list` | `array` |  | List of MSP EC to be assigned. |
| `number_of_days` | `string` |  | Expiry days for MSP EC to delegated tenant. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---



## Administrator Access Control

*Manages administrator assignments and access control for MSP tenant accounts. Supports assigning or removing administrators, configuring role based permissions and privilege groups, and managing cross tenant administrator access.*


*15 endpoints*


### `PATCH` `/adminDelegations`

**Assign Administrators**

Add designated administrators to manage assigned tenants.

operationId: `patchAdminDelegations`


**Request Body:** `MSP_Services_MspAdminRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `associations` | `array` |  | Set of MSP administrator associations to create or modify for customer accounts. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/mspCustomers/mspAdmins/associations`

**Assign Administrators**

Add designated administrators to manage assigned tenants. 
This method will be removed no sooner than 06/30/2026. 
The following URL PATCH /adminDelegations can be used for this content.

operationId: `mspAdminAssociation`


**Request Body:** `MSP_Services_MspAdminRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `associations` | `array` |  | Set of MSP administrator associations to create or modify for customer accounts. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/admins`

**List Tenant Administrators**

Retrieve a list of all administrators assigned to the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/admins can be used for this content.

operationId: `getMspEcAdminList`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC administrator list to be retrieved. |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/mspCustomers/{customerId}/admins/{adminId}`

**Remove Administrator**

Remove an administrator's access from the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL DELETE /tenants/{tenantId}/admins/{adminId}  can be used for this content.

operationId: `deleteMspEcAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC administrator to be deleted. |
| `adminId` | path | ✓ | `string` | Admin Id of the MSP-EC administrator to be deleted. |


**Responses:**

- `204` No Content
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/admins/{adminId}`

**Get Administrator Details**

Retrieve detailed information for a specific administrator. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/admins/{adminId} can be used for this content.

operationId: `getMspEcAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC administrator to be retrieved. |
| `adminId` | path | ✓ | `string` | Admin Id of the MSP EC administrator to be retrieved. |


**Responses:**

- `200` Ok → `MSP_Services_MspEcAdminView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}/admins/{adminId}`

**Assign Administrator**

Assign an administrator to the tenant account with specified roles and permissions. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/admins/{adminId}  can be used for this content.

operationId: `updateMspEcAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant Id of the MSP EC administrator to be updated. |
| `adminId` | path | ✓ | `string` | Admin Id of the MSP EC administrator to be updated. |


**Request Body:** `MSP_Services_UpdateMspEcAdminRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `email` | `string` | ✓ | The email address of the MSP EC administrator. |
| `first_name` | `string` | ✓ | The first name of the MSP EC administrator. |
| `full_name` | `string` |  | The full name of the MSP EC administrator. |
| `last_name` | `string` |  | The last name of the MSP EC administrator. |
| `user_name` | `string` | ✓ | The user name of the MSP EC administrator. |


**Responses:**

- `204` No Content
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}/delegatorAdmins`

**Update Admin Delegations**

Update active relationships between designated administrators and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/adminDelegations can be used for this content.

operationId: `updateDelegatorAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP EC Tenant Id |


**Request Body:** `MSP_Services_AssignedMspAdminsRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `delegation_type` | `string` | ✓ | The type of MSP EC delegated tenant. |
| `mspec_list` | `array` |  | List of MSP EC admins to be assigned. |
| `privilege_group_ids` | `array` |  | Privilege groups to manage accounts. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/mspadmins`

**Retrieve Admin Delegations**

Retrieve active relationships between designated administrators and their assigned tenants. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/adminDelegations can be used for this content.

operationId: `getMspDelegatedAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant ID |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}/mspadmins`

**Update Admin Delegations**

Update active relationships between designated administrators and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/adminDelegations can be used for this content.

operationId: `updateMspDelegatedAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP EC Tenant Id |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenants/{tenantId}/adminDelegations`

**Retrieve Admin Delegations**

Retrieve active relationships between designated administrators and their assigned tenants.

operationId: `getDelegatedAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenants/{tenantId}/adminDelegations`

**Update Admin Delegations**

Update active relationships between designated administrators and their managed tenant.

operationId: `updateDelegatedAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_AssignedMspAdminsRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `delegation_type` | `string` | ✓ | The type of MSP EC delegated tenant. |
| `mspec_list` | `array` |  | List of MSP EC admins to be assigned. |
| `privilege_group_ids` | `array` |  | Privilege groups to manage accounts. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenants/{tenantId}/admins`

**List Tenant Administrators**

Retrieve a complete list of all administrators assigned to the tenant account, including their roles and permissions.

operationId: `getTenantAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/tenants/{tenantId}/admins/{adminId}`

**Remove Administrator**

Remove an administrator's access from the tenant account, revoking all their roles and permissions.

operationId: `deleteTenantAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |
| `adminId` | path | ✓ | `string` |  |


**Responses:**

- `204` No Content
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenants/{tenantId}/admins/{adminId}`

**Get Administrator Details**

Retrieve detailed information for a specific administrator, including their assigned roles, permissions, and contact information.

operationId: `getTenantAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |
| `adminId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok → `MSP_Services_MspEcAdminView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenants/{tenantId}/admins/{adminId}`

**Assign Administrator**

Assign an administrator to the tenant account with specified roles and permissions, enabling them to manage tenant resources.

operationId: `updateTenantAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |
| `adminId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_UpdateMspEcAdminRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `email` | `string` | ✓ | The email address of the MSP EC administrator. |
| `first_name` | `string` | ✓ | The first name of the MSP EC administrator. |
| `full_name` | `string` |  | The full name of the MSP EC administrator. |
| `last_name` | `string` |  | The last name of the MSP EC administrator. |
| `user_name` | `string` | ✓ | The user name of the MSP EC administrator. |


**Responses:**

- `204` No Content
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---



## Tenant Account Management

*Manages tenant accounts including creation, retrieval, updates, and deletion. Supports sending email invitations to tenant administrators and managing account configurations.*


*14 endpoints*


### `GET` `/mspCustomers`

**List Managed Tenants**

Retrieve a list of all managed tenant accounts. 
This method will be removed no sooner than 06/30/2026.
The following URL POST /tenants/query can be used for this content.

operationId: `getMspEcAccountList`


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers`

**Create Managed Tenant**

Create a new managed tenant account with specified configuration settings. 
This method will be removed no sooner than 06/30/2026. 
The following URL POST /tenants  can be used for this content.

operationId: `createMspEcAccountV3`


**Request Body:** `MSP_Services_AddMspEcRequestV1_3`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `account_id` | `string` |  |  |
| `admin_delegations` | `array` |  | Grant or revoke access to admins to manage the customer. |
| `admin_email` | `string` |  | The email address of the first MSP-EC administrator added to the account by the MSP. |
| `admin_firstname` | `string` |  | The first name of the first MSP-EC administrator added to the account by the MSP. |
| `admin_lastname` | `string` |  | The last name of the first MSP-EC administrator added to the account by the MSP. |
| `admin_role` | `string` |  | The admin role of the first MSP-EC administrator. |
| `city` | `string` |  | The MSP-EC mailing address' city. |
| `country` | `string` |  | The MSP-EC mailing address' country. |
| `delegations` | `array` |  | Grant or revoke access to tenants to manage the customer. |
| `fax_number` | `string` |  | The MSP-EC's fax number. |
| `licenses` | `MSP_Services_License` |  | License information for the account. |
| `mapping_url` | `string` |  | The map URL corresponding to the MSP-EC's mailing address. |
| `name` | `string` |  | The name of MSP-EC account. |
| `phone_number` | `string` |  | The MSP-EC's phone number. |
| `postal_code` | `string` |  | The MSP-EC mailing address' postal code. |
| `service_effective_date` | `string` |  | The date when the MSP-EC's service started. |
| `service_expiration_date` | `string` |  | The date when the MSP-EC's service terminates/terminated. |
| `state` | `string` |  | The MSP-EC mailing address' geographical state. |
| `street_address` | `string` |  | The MSP-EC mailing address' street name and number. |
| `tenant_type` | `string` |  | The tenant type of the MSP EC administrator. |
| `tier` | `string` |  | Service tier information for MSP-EC. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/mspCustomers/{customerId}`

**Remove Managed Tenant**

Delete a managed tenant account and all associated data. 
This method will be removed no sooner than 06/30/2026. 
The following URL DELETE /tenants/{tenantId}  can be used for this content.

operationId: `deleteMspEcAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC account to be deleted. |


**Responses:**

- `202` Ok → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}`

**Retrieve Managed Tenant**

Retrieve detailed information for a specific managed tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}  can be used for this content.

operationId: `getMspEcAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant Id of the MSP EC account to be retrieved. |


**Responses:**

- `200` Ok → `MSP_Services_MspEcAccountView`
- `401` Un Authorized → `MSP_Services_CustomErrorResponse`
- `403` Forbidden → `MSP_Services_CustomErrorResponse`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}`

**Update Managed Tenant**

Update configuration settings for an existing managed tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}  can be used for this content.

operationId: `updateMspEcAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC account to be updated. |


**Request Body:** `MSP_Services_UpdateMspEcRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `city` | `string` |  | The city of the MSP-EC account. |
| `country` | `string` |  | The country of the MSP-EC account. |
| `fax_number` | `string` |  | The fax number of the MSP-EC account. |
| `licenses` | `MSP_Services_License` |  | License information for the account. |
| `mapping_url` | `string` |  | The map URL of the MSP-EC account. |
| `name` | `string` | ✓ | The name of the MSP-EC account. |
| `phone_number` | `string` |  | The phone number of the MSP-EC account. |
| `postal_code` | `string` |  | The postal code of the MSP-EC account. |
| `privacyFeatures` | `array` |  | Privacy features for the account. |
| `service_effective_date` | `string` | ✓ | The effective date of the MSP-EC account. |
| `service_expiration_date` | `string` | ✓ | The expiration date of the MSP-EC account. |
| `state` | `string` |  | The state of the MSP-EC account. |
| `street_address` | `string` |  | The street address of the MSP-EC account. |
| `tags` | `array` |  | Tags for MSP EC. |
| `tier` | `string` |  | Service tier information for MSP-EC. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `403` Forbidden → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers/{customerId}/invitations`

**Send Administrator Invitation**

Send or resend an email invitation to an administrator to access the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/invitations can be used for this content.

operationId: `sendInvitationEmail_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant Id of the MSP EC account |


**Request Body:** `MSP_Services_EmailInvitation`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `admin_email` | `string` | ✓ | The email of the MSP-EC administrator. |
| `resend` | `boolean` |  | Indicate if this is to resend in case of email got lost. |


**Responses:**

- `200` OK
- `204` No Content
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/logoUrls`

**Retrieve Brand Logo URLs**

Retrieve download URLs for brand logo image files associated with the tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}  can be used for this content.

operationId: `getMspEcLogoURL`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP EC Tenant Id |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/tenants`

**Create Managed Tenant**

Create a new managed tenant account with specified configuration settings.

operationId: `createTenantV2`


**Request Body:** `MSP_Services_AddTenantRequestHolder`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `data` | `array` |  |  |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBOV2`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenants/files/apiSpecs`

**Get Consolidated API Download URL**

Get signed URL for downloading the consolidated API zip file.

operationId: `getConsolidatedApiUrl`


**Responses:**

- `200` Ok → `MSP_Services_ConsolidatedApiUrlResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/tenants/{tenantId}`

**Remove Managed Tenant**

Delete a managed tenant account and all associated data.

operationId: `deleteTenant`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `202` Ok → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/tenants/{tenantId}`

**Retrieve Managed Tenant**

Retrieve detailed information for a specific managed tenant account.

operationId: `getTenantAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok → `MSP_Services_MspEcAccountView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/tenants/{tenantId}`

**Patch Tenant Account**

Patch MSP-EC data.

operationId: `patchManagedTenant`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_PatchMspEcRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `tags` | `array` |  | Tags for MSP EC. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `403` Forbidden → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenants/{tenantId}`

**Update Managed Tenant**

Update configuration settings for an existing managed tenant account.

operationId: `updateManagedTenant`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_UpdateMspEcRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `city` | `string` |  | The city of the MSP-EC account. |
| `country` | `string` |  | The country of the MSP-EC account. |
| `fax_number` | `string` |  | The fax number of the MSP-EC account. |
| `licenses` | `MSP_Services_License` |  | License information for the account. |
| `mapping_url` | `string` |  | The map URL of the MSP-EC account. |
| `name` | `string` | ✓ | The name of the MSP-EC account. |
| `phone_number` | `string` |  | The phone number of the MSP-EC account. |
| `postal_code` | `string` |  | The postal code of the MSP-EC account. |
| `privacyFeatures` | `array` |  | Privacy features for the account. |
| `service_effective_date` | `string` | ✓ | The effective date of the MSP-EC account. |
| `service_expiration_date` | `string` | ✓ | The expiration date of the MSP-EC account. |
| `state` | `string` |  | The state of the MSP-EC account. |
| `street_address` | `string` |  | The street address of the MSP-EC account. |
| `tags` | `array` |  | Tags for MSP EC. |
| `tier` | `string` |  | Service tier information for MSP-EC. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `403` Forbidden → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/tenants/{tenantId}/invitations`

**Send Administrator Invitation**

Send or resend an email invitation to an administrator, granting them access credentials and login instructions for the tenant account.

operationId: `sendInvitationEmail`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tenantId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_EmailInvitation`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `admin_email` | `string` | ✓ | The email of the MSP-EC administrator. |
| `resend` | `boolean` |  | Indicate if this is to resend in case of email got lost. |


**Responses:**

- `204` No Content
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---



## Brand Customization

*Manages branding customization for managed service provider accounts. Supports uploading logo images, configuring contact information and portal settings such as custom domain names and support URLs.*


*10 endpoints*


### `GET` `/brandings`

**Retrieve Brand Details**

Retrieve MSP account branding, contact information, and portal settings.

operationId: `getBrandInfo`


**Responses:**

- `200` Ok → `MSP_Services_MspView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/brandings`

**Create Brand Details**

Create MSP account branding, contact information, and portal settings.

operationId: `addBrandInfo`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/brandings`

**Update Brand Details**

Update MSP account branding, contact information, and portal settings.

operationId: `updateBrandInfo`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/logoFiles`

**Upload Brand Logos**

Upload custom logo image files for branding customization, supports JPEG, PNG, and SVG formats.

operationId: `uploadBrandLogoFileUrl`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/logoFiles/{fileId}`

**Retrieve Brand Logo File**

Retrieve download URLs and metadata for uploaded brand logo image files by file identifier.

operationId: `getBrandLogoFileDownloadUrl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fileId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspLabels`

**Retrieve Brand Details**

Retrieve MSP account branding, contact information, and portal settings. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /brandings can be used for this content.

operationId: `getMspLabel`


**Responses:**

- `200` Ok → `MSP_Services_MspView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspLabels`

**Add Brand Details**

Create a new branding configuration.
This method will be removed no sooner than 06/30/2026. 
The following URL POST /brandings can be used for this content.

operationId: `addMspLabel`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspLabels`

**Update Brand Details**

Update existing branding configuration.
This method will be removed no sooner than 06/30/2026. 
The following URL put /brandings can be used for this content.

operationId: `updateMspLabel`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspLabels/baseUrls`

**Retrieve Brand Base URLs**

Retrieve base URLs for brand resources and assets.
This method will be removed no sooner than 06/30/2026.
The following URL GET /brandings can be used for this content.

operationId: `getMspBaseURL`


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspLabels/{mspLabel}`

**Check MSP Label**

Check whether a specific MSP label is already in use before brand configuration.This method will be removed no sooner than 06/30/2026.The following URL POST /brandings can be used for this content.

operationId: `checkMspLabel`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mspLabel` | path | ✓ | `string` | MSP Label |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---



## Batch Device Operations

*5 endpoints*


### `POST` `/batchOps/query`

**Query Batch Operations**

Retrieve batch operations for the MSP tenant, with pagination, filters, and sort options.

operationId: `queryBatchOperations`


**Request Body:** `MSP_Services_BatchOperationsQueryCtx`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `endDataTime` | `string` |  | When set, only batch operations created on or before this time are included. |
| `pageable` | `MSP_Services_PageableRequest` |  | Which page of results to return and how many entries per page. |
| `requestIds` | `array` |  | When set, only batch operations with these identifiers are included. |
| `sort` | `MSP_Services_SortSpec` |  | How results are ordered, using one or more field and direction pairs. |
| `startDateTime` | `string` |  | When set, only batch operations created on or after this time are included. |
| `useCases` | `array` |  | When set, only batch operations for these use cases are included. |


**Responses:**

- `200` Ok → `MSP_Services_BatchOperationsQueryResponse`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`
- `501` Not Implemented → `MSP_Services_BatchOperationsQueryResponse`


---

### `POST` `/batchOps/{batchOpId}/batchRequests/devicePairs/addAps/csv`

**Export Add-AP batch requests (CSV)**

Download add-AP (destination) request details as a CSV with AP import-style columns (name, serial, venue, etc.). Uses the same query body and filters as device pair CSV export.

operationId: `exportBatchRequestAddApsCsv`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `batchOpId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_BatchRequestDevicePairQueryCtx`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `addStatuses` | `array` |  | Optional filter: add-step API status (batch_requests.api_status for operation_order = 2) is one of these values (trimmed). Omit or empty for no filter. |
| `deleteStatuses` | `array` |  | Optional filter: delete-step API status (batch_requests.api_status for operation_order = 1) is one of these values (trimmed). Omit or empty for no filter. |
| `deviceIds` | `array` |  | Optional filter: paired rows whose device_id is in this list (exact match per id on delete-step batch_request.device_id, trimmed). Omit or empty for no filter. |
| `deviceType` | `string` |  | Optional filter: exact match on device_type (delete-step batch_request.device_type). |
| `exportMaxRows` | `integer` |  | Maximum number of rows to include in a CSV export. Ignored for the JSON list response. |
| `pageable` | `MSP_Services_PageableRequest` |  | Which page of results to return and how many entries per page. |
| `sort` | `MSP_Services_SortSpec` |  | How paired rows are ordered. Typical fields include device identifier, tenant, and status values for each side of the pair. |
| `triggerType` | `string` |  | Optional filter: exact match on add-step batch trigger_type (trimmed). Omit or blank for no filter. |


**Responses:**

- `200` Ok
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`
- `501` Not Implemented


---

### `POST` `/batchOps/{batchOpId}/batchRequests/devicePairs/csv`

**Export Batch Request Device Pairs**

Download paired device results as a CSV file for offline review or sharing. The export respects a maximum row limit. When no data is available, the file contains headers only.

operationId: `exportBatchRequestDevicePairsCsv`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `batchOpId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_BatchRequestDevicePairQueryCtx`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `addStatuses` | `array` |  | Optional filter: add-step API status (batch_requests.api_status for operation_order = 2) is one of these values (trimmed). Omit or empty for no filter. |
| `deleteStatuses` | `array` |  | Optional filter: delete-step API status (batch_requests.api_status for operation_order = 1) is one of these values (trimmed). Omit or empty for no filter. |
| `deviceIds` | `array` |  | Optional filter: paired rows whose device_id is in this list (exact match per id on delete-step batch_request.device_id, trimmed). Omit or empty for no filter. |
| `deviceType` | `string` |  | Optional filter: exact match on device_type (delete-step batch_request.device_type). |
| `exportMaxRows` | `integer` |  | Maximum number of rows to include in a CSV export. Ignored for the JSON list response. |
| `pageable` | `MSP_Services_PageableRequest` |  | Which page of results to return and how many entries per page. |
| `sort` | `MSP_Services_SortSpec` |  | How paired rows are ordered. Typical fields include device identifier, tenant, and status values for each side of the pair. |
| `triggerType` | `string` |  | Optional filter: exact match on add-step batch trigger_type (trimmed). Omit or blank for no filter. |


**Responses:**

- `200` Ok
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`
- `501` Not Implemented


---

### `POST` `/batchOps/{batchOpId}/batchRequests/devicePairs/query`

**Query Batch Request Device Pairs**

Retrieve paired device results for a completed or in-progress batch operation. Each entry combines the device with its source and destination details.

operationId: `queryBatchRequestDevicePairs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `batchOpId` | path | ✓ | `string` |  |


**Request Body:** `MSP_Services_BatchRequestDevicePairQueryCtx`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `addStatuses` | `array` |  | Optional filter: add-step API status (batch_requests.api_status for operation_order = 2) is one of these values (trimmed). Omit or empty for no filter. |
| `deleteStatuses` | `array` |  | Optional filter: delete-step API status (batch_requests.api_status for operation_order = 1) is one of these values (trimmed). Omit or empty for no filter. |
| `deviceIds` | `array` |  | Optional filter: paired rows whose device_id is in this list (exact match per id on delete-step batch_request.device_id, trimmed). Omit or empty for no filter. |
| `deviceType` | `string` |  | Optional filter: exact match on device_type (delete-step batch_request.device_type). |
| `exportMaxRows` | `integer` |  | Maximum number of rows to include in a CSV export. Ignored for the JSON list response. |
| `pageable` | `MSP_Services_PageableRequest` |  | Which page of results to return and how many entries per page. |
| `sort` | `MSP_Services_SortSpec` |  | How paired rows are ordered. Typical fields include device identifier, tenant, and status values for each side of the pair. |
| `triggerType` | `string` |  | Optional filter: exact match on add-step batch trigger_type (trimmed). Omit or blank for no filter. |


**Responses:**

- `200` Ok → `MSP_Services_BatchRequestDevicePairPageResponse`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`
- `501` Not Implemented → `MSP_Services_BatchRequestDevicePairPageResponse`


---

### `POST` `/tenants/venues/devices/batches`

**Submit Device Batch**

Submit a batch of device changes for customer venues, such as moving access points between accounts.

operationId: `batchOperation`


**Request Body:** `MSP_Services_BatchOps`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `operations` | `array` | ✓ | Ordered list of API calls that make up the batch. |
| `type` | `string` | ✓ | Bulk workflow to run, such as moving devices between customer accounts. |


**Responses:**

- `201` Created → `MSP_Services_ResponseBOV2`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`
- `501` Not Implemented → `MSP_Services_ResponseBOV2`


---



## Deprecated

*30 endpoints*


### `POST` `/delegations`

**Get Delegations**

Get the list of customer delegations. This method will be removed no sooner than 06/30/2026. The following URL POST /delegations/query can be used for this content.

operationId: `getDelegationsForViewLegacy`


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_DelegationData`
- `400` Bad request. → `MSP_Services_QueryResponseDelegationData`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseDelegationData`


---

### `GET` `/mspCustomers`

**List Managed Tenants**

Retrieve a list of all managed tenant accounts. 
This method will be removed no sooner than 06/30/2026.
The following URL POST /tenants/query can be used for this content.

operationId: `getMspEcAccountList`


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers`

**Create Managed Tenant**

Create a new managed tenant account with specified configuration settings. 
This method will be removed no sooner than 06/30/2026. 
The following URL POST /tenants  can be used for this content.

operationId: `createMspEcAccountV3`


**Request Body:** `MSP_Services_AddMspEcRequestV1_3`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `account_id` | `string` |  |  |
| `admin_delegations` | `array` |  | Grant or revoke access to admins to manage the customer. |
| `admin_email` | `string` |  | The email address of the first MSP-EC administrator added to the account by the MSP. |
| `admin_firstname` | `string` |  | The first name of the first MSP-EC administrator added to the account by the MSP. |
| `admin_lastname` | `string` |  | The last name of the first MSP-EC administrator added to the account by the MSP. |
| `admin_role` | `string` |  | The admin role of the first MSP-EC administrator. |
| `city` | `string` |  | The MSP-EC mailing address' city. |
| `country` | `string` |  | The MSP-EC mailing address' country. |
| `delegations` | `array` |  | Grant or revoke access to tenants to manage the customer. |
| `fax_number` | `string` |  | The MSP-EC's fax number. |
| `licenses` | `MSP_Services_License` |  | License information for the account. |
| `mapping_url` | `string` |  | The map URL corresponding to the MSP-EC's mailing address. |
| `name` | `string` |  | The name of MSP-EC account. |
| `phone_number` | `string` |  | The MSP-EC's phone number. |
| `postal_code` | `string` |  | The MSP-EC mailing address' postal code. |
| `service_effective_date` | `string` |  | The date when the MSP-EC's service started. |
| `service_expiration_date` | `string` |  | The date when the MSP-EC's service terminates/terminated. |
| `state` | `string` |  | The MSP-EC mailing address' geographical state. |
| `street_address` | `string` |  | The MSP-EC mailing address' street name and number. |
| `tenant_type` | `string` |  | The tenant type of the MSP EC administrator. |
| `tier` | `string` |  | Service tier information for MSP-EC. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/mspCustomers/delegations`

**Add Designated Tenant Accounts**

Add or update MSP-EC account relationships with multiple integrator or installer accounts. 
This method will be removed no sooner than 06/30/2026. 
The following URL PATCH /tenantDelegations can be used for this content.

operationId: `assignMspEcToMultipleTechPartner`


**Request Body:** `MSP_Services_AssignMspEcToMultipleTechPartners`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `AssignDelegatedRequest` | `array` |  | List of tech partner details. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/mspCustomers/mspAdmins/associations`

**Assign Administrators**

Add designated administrators to manage assigned tenants. 
This method will be removed no sooner than 06/30/2026. 
The following URL PATCH /adminDelegations can be used for this content.

operationId: `mspAdminAssociation`


**Request Body:** `MSP_Services_MspAdminRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `associations` | `array` |  | Set of MSP administrator associations to create or modify for customer accounts. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/mspCustomers/{customerId}`

**Remove Managed Tenant**

Delete a managed tenant account and all associated data. 
This method will be removed no sooner than 06/30/2026. 
The following URL DELETE /tenants/{tenantId}  can be used for this content.

operationId: `deleteMspEcAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC account to be deleted. |


**Responses:**

- `202` Ok → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}`

**Retrieve Managed Tenant**

Retrieve detailed information for a specific managed tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}  can be used for this content.

operationId: `getMspEcAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant Id of the MSP EC account to be retrieved. |


**Responses:**

- `200` Ok → `MSP_Services_MspEcAccountView`
- `401` Un Authorized → `MSP_Services_CustomErrorResponse`
- `403` Forbidden → `MSP_Services_CustomErrorResponse`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}`

**Update Managed Tenant**

Update configuration settings for an existing managed tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}  can be used for this content.

operationId: `updateMspEcAccount`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC account to be updated. |


**Request Body:** `MSP_Services_UpdateMspEcRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `city` | `string` |  | The city of the MSP-EC account. |
| `country` | `string` |  | The country of the MSP-EC account. |
| `fax_number` | `string` |  | The fax number of the MSP-EC account. |
| `licenses` | `MSP_Services_License` |  | License information for the account. |
| `mapping_url` | `string` |  | The map URL of the MSP-EC account. |
| `name` | `string` | ✓ | The name of the MSP-EC account. |
| `phone_number` | `string` |  | The phone number of the MSP-EC account. |
| `postal_code` | `string` |  | The postal code of the MSP-EC account. |
| `privacyFeatures` | `array` |  | Privacy features for the account. |
| `service_effective_date` | `string` | ✓ | The effective date of the MSP-EC account. |
| `service_expiration_date` | `string` | ✓ | The expiration date of the MSP-EC account. |
| `state` | `string` |  | The state of the MSP-EC account. |
| `street_address` | `string` |  | The street address of the MSP-EC account. |
| `tags` | `array` |  | Tags for MSP EC. |
| `tier` | `string` |  | Service tier information for MSP-EC. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `403` Forbidden → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/activationStatus`

**Get Tenant Activation Status**

Check whether a tenant account is currently activated or deactivated. 
This method will be removed no sooner than 06/30/2026.

operationId: `getMspEcActivationStatus`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the tenant to get MSP data. |


**Responses:**

- `200` Ok → `MSP_Services_MspEc`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/admins`

**List Tenant Administrators**

Retrieve a list of all administrators assigned to the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/admins can be used for this content.

operationId: `getMspEcAdminList`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC administrator list to be retrieved. |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/mspCustomers/{customerId}/admins/{adminId}`

**Remove Administrator**

Remove an administrator's access from the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL DELETE /tenants/{tenantId}/admins/{adminId}  can be used for this content.

operationId: `deleteMspEcAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC administrator to be deleted. |
| `adminId` | path | ✓ | `string` | Admin Id of the MSP-EC administrator to be deleted. |


**Responses:**

- `204` No Content
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/admins/{adminId}`

**Get Administrator Details**

Retrieve detailed information for a specific administrator. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/admins/{adminId} can be used for this content.

operationId: `getMspEcAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant ID of the MSP-EC administrator to be retrieved. |
| `adminId` | path | ✓ | `string` | Admin Id of the MSP EC administrator to be retrieved. |


**Responses:**

- `200` Ok → `MSP_Services_MspEcAdminView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}/admins/{adminId}`

**Assign Administrator**

Assign an administrator to the tenant account with specified roles and permissions. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/admins/{adminId}  can be used for this content.

operationId: `updateMspEcAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant Id of the MSP EC administrator to be updated. |
| `adminId` | path | ✓ | `string` | Admin Id of the MSP EC administrator to be updated. |


**Request Body:** `MSP_Services_UpdateMspEcAdminRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `email` | `string` | ✓ | The email address of the MSP EC administrator. |
| `first_name` | `string` | ✓ | The first name of the MSP EC administrator. |
| `full_name` | `string` |  | The full name of the MSP EC administrator. |
| `last_name` | `string` |  | The last name of the MSP EC administrator. |
| `user_name` | `string` | ✓ | The user name of the MSP EC administrator. |


**Responses:**

- `204` No Content
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `DELETE` `/mspCustomers/{customerId}/delegations`

**Disable Support Access**

Revoke support team access to the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL DELETE /tenantActivations/supportStatus/{tenantId} can be used for this content.

operationId: `disableRuckusSupport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant Id  |


**Responses:**

- `204` No Content → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/delegations`

**Get Support Access Status**

Check whether support team access is currently enabled or disabled for the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenantActivations/supportStatus/{tenantId} can be used for this content.

operationId: `getRuckusSupportStatus_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant Id  |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers/{customerId}/delegations`

**Enable Support Access**

Grant support team access to assist with tenant account issues. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenantActivations/supportStatus/{tenantId} can be used for this content.

operationId: `enableRuckusSupport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant Id  |


**Responses:**

- `201` Created → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}/delegatorAdmins`

**Update Admin Delegations**

Update active relationships between designated administrators and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/adminDelegations can be used for this content.

operationId: `updateDelegatorAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP EC Tenant Id |


**Request Body:** `MSP_Services_AssignedMspAdminsRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `delegation_type` | `string` | ✓ | The type of MSP EC delegated tenant. |
| `mspec_list` | `array` |  | List of MSP EC admins to be assigned. |
| `privilege_group_ids` | `array` |  | Privilege groups to manage accounts. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspCustomers/{customerId}/invitations`

**Send Administrator Invitation**

Send or resend an email invitation to an administrator to access the tenant account. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/invitations can be used for this content.

operationId: `sendInvitationEmail_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | Tenant Id of the MSP EC account |


**Request Body:** `MSP_Services_EmailInvitation`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `admin_email` | `string` | ✓ | The email of the MSP-EC administrator. |
| `resend` | `boolean` |  | Indicate if this is to resend in case of email got lost. |


**Responses:**

- `200` OK
- `204` No Content
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/logoUrls`

**Retrieve Brand Logo URLs**

Retrieve download URLs for brand logo image files associated with the tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}  can be used for this content.

operationId: `getMspEcLogoURL`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP EC Tenant Id |


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspCustomers/{customerId}/mspadmins`

**Retrieve Admin Delegations**

Retrieve active relationships between designated administrators and their assigned tenants. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/adminDelegations can be used for this content.

operationId: `getMspDelegatedAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP-EC Tenant ID |


**Responses:**

- `200` Ok
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspCustomers/{customerId}/mspadmins`

**Update Admin Delegations**

Update active relationships between designated administrators and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/adminDelegations can be used for this content.

operationId: `updateMspDelegatedAdmins`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `customerId` | path | ✓ | `string` | MSP EC Tenant Id |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspIntegrators/{integratorId}`

**Retrieve Tenant Delegations**

Retrieve active relationships between designated accounts and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /tenants/{tenantId}/tenantDelegations can be used for this content.

operationId: `getMspEcListToIntegrator`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `integratorId` | path | ✓ | `string` | MSP-EC Delegated Id |
| `delegationType` | query | ✓ | `string` |  |


**Responses:**

- `200` Ok → `MSP_Services_MspEcDelegationResponse`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PATCH` `/mspIntegrators/{integratorId}`

**Update Tenant Delegations**

Update active relationships between designated accounts and their managed tenant. 
This method will be removed no sooner than 06/30/2026. 
The following URL put /tenants/{tenantId}/tenantDelegations can be used for this content.

operationId: `assignMspEcListToDelegated`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `integratorId` | path | ✓ | `string` | MSP-EC Delegated Id |


**Request Body:** `MSP_Services_AssignMspEcListRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `delegation_type` | `string` | ✓ | The type of MSP EC delegated tenant. |
| `isManageAllEcs` | `boolean` |  | Flag to admins to manage account. |
| `mspec_list` | `array` |  | List of MSP EC to be assigned. |
| `number_of_days` | `string` |  | Expiry days for MSP EC to delegated tenant. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspLabels`

**Retrieve Brand Details**

Retrieve MSP account branding, contact information, and portal settings. 
This method will be removed no sooner than 06/30/2026. 
The following URL GET /brandings can be used for this content.

operationId: `getMspLabel`


**Responses:**

- `200` Ok → `MSP_Services_MspView`
- `404` Not Found → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspLabels`

**Add Brand Details**

Create a new branding configuration.
This method will be removed no sooner than 06/30/2026. 
The following URL POST /brandings can be used for this content.

operationId: `addMspLabel`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `PUT` `/mspLabels`

**Update Brand Details**

Update existing branding configuration.
This method will be removed no sooner than 06/30/2026. 
The following URL put /brandings can be used for this content.

operationId: `updateMspLabel`


**Request Body:** `MSP_Services_UpdateMspRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alarm_notification_logo_uuid` | `string` |  | The ID of alarm notification logo file. |
| `change_password_url` | `string` |  | The change password URL of MSP tenant. |
| `contact_support_behavior` | `string` |  | The contact support behavior of MSP tenant. |
| `contact_support_url` | `string` |  | The URL at which to obtain customer support from your MSP. |
| `default_logo_uuid` | `string` |  | The ID of default logo file. |
| `logo_uuid` | `string` |  | The ID of logo file. |
| `mlisa_logo_uuid` | `string` |  | The ID of RUCKUS one logo file. |
| `mspLogoFileDataList` | `array` |  | List of logo file metadata associated with the MSP account. |
| `msp_email` | `string` |  | Your MSP's customer support email address. |
| `msp_fqdn` | `string` |  | The FQDN of MSP portal. |
| `msp_label` | `string` | ✓ | Unique label identifying the MSP. |
| `msp_phone` | `string` |  | Your MSP's customer support phone number. |
| `msp_website` | `string` |  | Website URL for your MSP. |
| `my_open_case_behavior` | `string` |  | The my open case behavior of MSP tenant. |
| `my_open_case_url` | `string` |  | The URL to view your open customer support cases. |
| `open_case_behavior` | `string` |  | The open case behavior of MSP tenant. |
| `open_case_url` | `string` |  | The URL at which to open a customer support case with your MSP. |
| `ping_login_logo_uuid` | `string` |  | The ID of ping login logo file. |
| `ping_notification_logo_uuid` | `string` |  | The ID of ping notification logo file. |
| `preferredWisprProvider` | `MSP_Services_PreferredWisprProvider` |  | Preferred WISPr provider configuration for external captive portal authentication. |


**Responses:**

- `202` Accepted → `MSP_Services_ResponseBo`
- `400` Bad Request → `MSP_Services_CustomErrorResponse`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `GET` `/mspLabels/baseUrls`

**Retrieve Brand Base URLs**

Retrieve base URLs for brand resources and assets.
This method will be removed no sooner than 06/30/2026.
The following URL GET /brandings can be used for this content.

operationId: `getMspBaseURL`


**Responses:**

- `200` Ok → `MSP_Services_ResponseBo`
- `500` Server Error → `MSP_Services_CustomErrorResponse`


---

### `POST` `/mspecs/query`

**Query Customer Data for MSP-EC**

Retrieves customer details for managed service providers end customers. This method will be removed no sooner than 06/30/2026. The following URL POST /tenants/query can be used for this content.

operationId: `queryMSPECs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegation` | query |  | `string` |  |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspEcDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspEcDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspEcDto`


---

### `POST` `/msps/{mspTenantId}/ecInventories/query`

**Query Inventory for MSP**

View the list of networking devices installed in end customers venues. This method will be removed no sooner than 06/30/2026. The following URL POST /tenants/inventories/query can be used for this content.

operationId: `getDeviceInventory`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mspTenantId` | path | ✓ | `string` | Tenant Id of the MSP. |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspInventoryDeviceDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspInventoryDeviceDto`


---

### `POST` `/techpartners/mspecs/query`

**Query Technology Partners**

Retrieves the list of managed service providers end customers for technology partners based on the provided query parameters. This method will be removed no sooner than 06/30/2026. The following URL POST /tenants/query can be used for this content.

operationId: `getMSPECs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegation` | query |  | `string` |  |


**Request Body:** `MSP_Services_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `exists` | `string` |  | Field name to check for existence in documents. |
| `fields` | `array` |  | List of specific fields to include in the query results for projection. |
| `filters` | `object` |  | Additional custom filters to apply to the query for advanced filtering scenarios. |
| `groupBy` | `string` |  | Field name to group query results by for aggregation purposes. |
| `matchFields` | `array` |  | List of field filters to match documents where fields equal specific values. |
| `multiSortFields` | `array` |  | List of fields to sort by with their sort order for multiple field sorting. |
| `mustHaveFields` | `array` |  | List of fields that must exist in documents for them to be included in results. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist in documents for them to be included in results. |
| `mustNotMatchField` | `array` |  | List of field filters to exclude documents where fields equal specific values. |
| `page` | `integer` |  |  |
| `pageByDate` | `object` |  | Indicates whether pagination should be based on date fields instead of standard pagination. |
| `pageSize` | `integer` |  | Maximum number of results to return per page. |
| `rangeDateFilter` | `MSP_Services_RangeFilterDto` |  | Date range filter to match documents within a specific date or time range. |
| `rangeFilter` | `MSP_Services_RangeFilterDto` |  | Range filter to match documents where field values fall within specified numeric ranges. |
| `searchString` | `string` |  | Text string to search for across the specified target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when performing text based searches. |
| `search_after` | `array` |  | Pagination cursor for retrieving results after a specific point in the result set. |
| `sortField` | `string` |  | Primary field name to sort the query results by. |
| `sortOrder` | `string` |  | Sort order for the primary sort field (ASC for ascending, DESC for descending). |
| `termField` | `MSP_Services_TermFieldDto` |  | Field name for term based filtering to match specific term values. |
| `terms` | `object` |  | List of term values to match against the specified term field. |


**Responses:**

- `200` Successful operation. → `MSP_Services_QueryResponseMspEcDto`
- `400` Bad request. → `MSP_Services_QueryResponseMspEcDto`
- `404` Requested resource or related entity not found. → `MSP_Services_QueryResponseMspEcDto`


---


