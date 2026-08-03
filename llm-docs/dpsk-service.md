# DPSK Service

> RUCKUS One API Reference

---


## APIs for DPSK Service

*Operations for managing DPSK pools, including create, update, delete, and policy management.*


*13 endpoints*


### `GET` `/dpskServices`

**Get DPSK Pools**

This method will be removed no sooner than 08/31/2026. The following URL /dpskServices/query can be used for this content.

operationId: `listAllDpskPools`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `name` | query |  | `string` | Filter by dpsk service name |
| `networkId` | query |  | `string` | Filter by associated wifi network |
| `locked` | query |  | `boolean` | Filter by association status. true if locked by other service |
| `pageable` | query | ✓ | `DPSK_Service_Pageable` | parameters for paging |


**Responses:**

- `200` DPSK pools → `DPSK_Service_Page`


---

### `POST` `/dpskServices`

**Create New DPSK Pool**

This method will be removed no sooner than 08/31/2026.

operationId: `createDpskPool_1`


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` DPSK pool created → `DPSK_Service_OperationResponse`
- `400` Invalid pool content → `DPSK_Service_ApiError`


---

### `POST` `/dpskServices/query`

**Search for DPSK Pools**

Search for DPSK pools matching search string in paged result (response schema v1.2).

operationId: `queryDpskPoolsV1_2`


**Request Body:** `DPSK_Service_DpskPoolQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `DPSK_Service_DpskPoolFilters` |  | Filter criteria used to query DPSK pools. |
| `page` | `integer` |  | Page number, starting from index 0. |
| `pageSize` | `integer` |  | Number of items per page. |
| `searchString` | `string` |  | Search string to match against the specified searchTargetFields. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort by. |
| `sortOrder` | `string` |  | Sort order: ASC for ascending, DESC for descending. |


**Responses:**

- `200` DPSK pools → `DPSK_Service_DpskPoolQueryResponse`


---

### `DELETE` `/dpskServices/{poolId}`

**Delete the DPSK Pool**

Delete the specified DPSK pool.

operationId: `deleteDpskPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` |  |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `DPSK_Service_OperationResponse`


---

### `GET` `/dpskServices/{poolId}`

**Get Specific DPSK Pool**

Get specific DPSK pool by ID.

operationId: `getDpskPoolById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Responses:**

- `200` DPSK pool → `DPSK_Service_DpskPoolDto`
- `404` DPSK pool not found → `DPSK_Service_ApiError`


---

### `PATCH` `/dpskServices/{poolId}`

**Update the DPSK Pool**

Partially update the specified DPSK pool.

operationId: `patchDpskPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `DPSK_Service_OperationResponse`


---

### `PUT` `/dpskServices/{poolId}`

**Update the DPSK Pool**

Update the specified DPSK pool with the provided details.

operationId: `updateDpskPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `DPSK_Service_OperationResponse`


---

### `DELETE` `/dpskServices/{poolId}/identityGroups/{groupId}`

**Dissociate Identity Group from DPSK Pool**

Remove the association between an identity group and the specified DPSK pool. This operation will fail if there are passphrases belonging to this identity group.

operationId: `dissociateIdentityGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `groupId` | path | ✓ | `string` | Identity group id |


**Responses:**

- `202` The dissociation request has been accepted and is in progress → `DPSK_Service_OperationResponse`
- `400` Invalid request → `DPSK_Service_ApiError`
- `409` Cannot dissociate: passphrases exist for this identity group → `DPSK_Service_ApiError`


---

### `PUT` `/dpskServices/{poolId}/identityGroups/{groupId}`

**Associate Identity Group with DPSK Pool**

Associate an identity group with the specified DPSK pool. A pool can have up to 5 identity groups.

operationId: `associateIdentityGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `groupId` | path | ✓ | `string` | Identity group id |


**Responses:**

- `202` The association request has been accepted and is in progress → `DPSK_Service_OperationResponse`
- `400` Invalid request or maximum associations reached → `DPSK_Service_ApiError`


---

### `DELETE` `/dpskServices/{poolId}/policySets/{policySetId}`

**Remove DPSK Pool Policy Set**

Remove the policy set associated with the specified DPSK pool.

operationId: `removePolicySetId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK passphrase id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` The update request has been accepted and is in progress → `DPSK_Service_OperationResponse`


---

### `PUT` `/dpskServices/{poolId}/policySets/{policySetId}`

**Update DPSK Pool Policy Set**

Update the policy set associated with the DPSK pool.

operationId: `updatePolicySetId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK passphrase id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` The update request has been accepted and is in progress → `DPSK_Service_OperationResponse`


---

### `POST` `/identityGroups/{identityGroupId}/dpskServices`

**Create New DPSK Pool**

Create a new DPSK pool under the specified identity group.

operationId: `createDpskPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `identityGroupId` | path | ✓ | `string` | Identity group id |


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` DPSK pool created → `DPSK_Service_OperationResponse`
- `400` Invalid pool content → `DPSK_Service_ApiError`


---

### `GET` `/wifiNetworks/{networkId}/dpskServices`

**Get DPSK Pools by Network**

Get DPSK pools associated with the specified Wi-Fi network.

operationId: `getDpskPoolsByNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | Wifi network id |
| `pageable` | query | ✓ | `DPSK_Service_Pageable` | parameters for paging |


**Responses:**

- `200` DPSK pool → `DPSK_Service_DpskPoolQueryResponse`
- `404` DPSK pool not found → `DPSK_Service_ApiError`


---



## APIs for DPSK Passphrase

*Operations for managing DPSK passphrases, CSV import/export, and query support.*


*11 endpoints*


### `DELETE` `/dpskServices/{poolId}/passphrases`

**Delete Passphrase**

Delete DPSK passphrase(s) for the specified pool.

operationId: `deletePassphrases`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** Yes


**Responses:**

- `202` The passphrase(s) delete request is in progress → `DPSK_Service_OperationResponse`


---

### `GET` `/dpskServices/{poolId}/passphrases`

**Get Passphrase**

List passphrases for specific DPSK pool with pagination.

operationId: `listAllPassphrases`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `page` | query |  | `integer` | Page index starting from 0 (0..N) |
| `size` | query |  | `integer` | The size of the page to be returned |
| `sort` | query |  | `array` | Sorting criteria in the format: property,(asc\|desc). Default sort order is ascending. Multiple sort criteria are supported. |


**Responses:**

- `200` Passphrases → `DPSK_Service_Page`


---

### `PATCH` `/dpskServices/{poolId}/passphrases`

**Update Specific DPSK Passphrases**

Update entities partially with provided attributes. Only the attributes provided in the request body will be updated.

operationId: `updatePassphrases`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** `DPSK_Service_DpskPassphrasesPatchRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `changes` | `DPSK_Service_DpskPassphraseDto` | ✓ | Changes to be applied to the passphrases. |
| `ids` | `array` | ✓ | The passphrase IDs to be changed. |


**Responses:**

- `202` DPSK passphrases updated → `DPSK_Service_OperationResponse`


---

### `POST` `/dpskServices/{poolId}/passphrases`

**Create DPSK Passphrase**

Create DPSK passphrase(s) for the specified pool.

operationId: `createPassphrase`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** `DPSK_Service_DpskPassphraseCreateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `email` | `string` |  | The email for passphrase. |
| `expiration` | `string` |  | The expiration for passphrase. |
| `expirationDate` | `string` |  | The expiration for passphrase. |
| `format` | `string` |  | The format for passphrase. |
| `id` | `string` |  | Unique identifier for passphrase. |
| `identityId` | `string` |  | The identity ID for passphrase. |
| `length` | `integer` |  | Length of the passphrase. |
| `mac` | `string` |  | The mac for passphrase. |
| `numberOfDevices` | `integer` |  | Number of devices. Must be between 1 and 512. Inputs outside this range will be adjusted. |
| `numberOfDevicesType` | `string` |  | Number of devices type. |
| `numberOfPassphrases` | `integer` |  | The number of PSK to be generated if passphrase is not provided. |
| `passphrase` | `string` |  | The actual passphrase value to be created. |
| `phoneNumber` | `string` |  | The number for passphrase. |
| `username` | `string` |  | The username for passphrase. |
| `vlanId` | `integer` |  | The VLAN for passphrase. |
| `vxlanId` | `integer` |  | The VNI to associate with this PSK. |


**Responses:**

- `202` Create DPSK passphrase(s) accepted → `DPSK_Service_OperationResponse`
- `400` Invalid content supplied or multiple identity groups found → `DPSK_Service_ApiError`


---

### `POST` `/dpskServices/{poolId}/passphrases/csvFiles`

**Import Passphrase from CSV**

Import DPSK passphrases from a CSV file.

operationId: `importDpskPassphrasesFromCsv`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` |  |
| `usernamePrefix` | query |  | `string` | Prefix for generated user names when the Username column is empty. |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `200` Passphrases → `DPSK_Service_OperationResponse`


---

### `POST` `/dpskServices/{poolId}/passphrases/notifications`

**Send Passphrase Notifications**

Send email and/or SMS notifications to users for the specified DPSK passphrases.

operationId: `passphraseNotification`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** `DPSK_Service_DpskPassphraseNotificationDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ids` | `array` | ✓ | List of DPSK passphrase IDs for which notifications will be sent. |
| `shouldSendEmail` | `boolean` | ✓ | Whether to send email notifications. Defaults to true. |
| `shouldSendSms` | `boolean` | ✓ | Whether to send SMS notifications. Defaults to true. |


**Responses:**

- `202` The request to send notifications for the specified passphrase(s) has been accepted. → `DPSK_Service_OperationResponse`


---

### `POST` `/dpskServices/{poolId}/passphrases/query`

**Query Passphrases for Specified Pool**

Query passphrases for the specified DPSK pool.

operationId: `queryResponse`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` |  |


**Request Body:** `DPSK_Service_DpskPassphraseQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `DPSK_Service_DpskPassphraseFilters` |  | Filter criteria used to query DPSK passphrases. |
| `maxDevicesPerPassphrase` | `integer` |  | Maximum number of devices to return per passphrase, preventing excessive data retrieval for passphrases with large device counts. |
| `page` | `integer` |  | Page number, starting from index 0. |
| `pageSize` | `integer` |  | Number of items per page. |
| `searchString` | `string` |  | Search string to match against the specified searchTargetFields. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort by. |
| `sortOrder` | `string` |  | Sort order: ASC for ascending, DESC for descending. |


**Responses:**

- `200` Passphrases → `DPSK_Service_DpskPassphraseQueryResponse`


---

### `POST` `/dpskServices/{poolId}/passphrases/query/csvFiles`

**DPSK Passphrase to CSV**

Export DPSK passphrases to a CSV file.

operationId: `exportDpskPassphrase`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` |  |
| `timezone` | query |  | `string` | If specified, the timezone will be used for date values. Default value is UTC. |
| `date-format` | query |  | `string` | Format will be applied for date values. Default value is "day/month/year hour:minute" |


**Request Body:** `DPSK_Service_DpskPassphraseQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `DPSK_Service_DpskPassphraseFilters` |  | Filter criteria used to query DPSK passphrases. |
| `maxDevicesPerPassphrase` | `integer` |  | Maximum number of devices to return per passphrase, preventing excessive data retrieval for passphrases with large device counts. |
| `page` | `integer` |  | Page number, starting from index 0. |
| `pageSize` | `integer` |  | Number of items per page. |
| `searchString` | `string` |  | Search string to match against the specified searchTargetFields. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort by. |
| `sortOrder` | `string` |  | Sort order: ASC for ascending, DESC for descending. |


**Responses:**

- `200` Exported passphrases
- `400` Invalid timezone or date format supplied → `DPSK_Service_ApiError`


---

### `GET` `/dpskServices/{poolId}/passphrases/{id}`

**Get DPSK Passphrase**

Get the specified DPSK passphrase by ID.

operationId: `getPassphraseById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `id` | path | ✓ | `string` | DPSK passphrase id |


**Responses:**

- `200` DPSK passphrase → `DPSK_Service_DpskPassphraseDto`
- `404` DPSK passphrase not found → `DPSK_Service_ApiError`


---

### `PATCH` `/dpskServices/{poolId}/passphrases/{id}`

**Update Specific DPSK Passphrase**

Update an entity partially with provided attributes. Only the attributes provided in the request body will be updated.

operationId: `updatePassphrase_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `id` | path | ✓ | `string` | DPSK passphrase id |


**Request Body:** `DPSK_Service_DpskPassphraseDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `createdDate` | `string` |  | Passphrase creation date record. |
| `devices` | `array` |  | The devices configured or connected to the passphrase. |
| `email` | `string` |  | Email associated with passphrase. |
| `expiration` | `string` |  | Expiration type of passphrase. |
| `expirationDate` | `string` |  | Expiration date of passphrase. |
| `id` | `string` |  |  |
| `identityGroupId` | `string` |  | The identity group this passphrase belongs to. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `numberOfDevices` | `integer` |  | Number of devices. Must be between 1 and 512. Inputs outside this range will be adjusted. |
| `passphrase` | `string` |  | The actual passphrase value. |
| `phoneNumber` | `string` |  | Phone associated with passphrase. |
| `revocationDate` | `string` |  | The date time that the PSK was revoked. |
| `revocationReason` | `string` |  | Reason for revocation of passphrase. |
| `username` | `string` |  | Username for the passphrase. |
| `vlanId` | `integer` |  | VLAN associated with passphrase. |


**Responses:**

- `202` The passphrase update request is in progress → `DPSK_Service_OperationResponse`


---

### `PUT` `/dpskServices/{poolId}/passphrases/{id}`

**Update Specific DPSK Passphrase**

Update DPSK passphrase(s) for the specified pool.

operationId: `updatePassphrase`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `id` | path | ✓ | `string` | DPSK passphrase id |


**Request Body:** `DPSK_Service_DpskPassphraseDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `createdDate` | `string` |  | Passphrase creation date record. |
| `devices` | `array` |  | The devices configured or connected to the passphrase. |
| `email` | `string` |  | Email associated with passphrase. |
| `expiration` | `string` |  | Expiration type of passphrase. |
| `expirationDate` | `string` |  | Expiration date of passphrase. |
| `id` | `string` |  |  |
| `identityGroupId` | `string` |  | The identity group this passphrase belongs to. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `numberOfDevices` | `integer` |  | Number of devices. Must be between 1 and 512. Inputs outside this range will be adjusted. |
| `passphrase` | `string` |  | The actual passphrase value. |
| `phoneNumber` | `string` |  | Phone associated with passphrase. |
| `revocationDate` | `string` |  | The date time that the PSK was revoked. |
| `revocationReason` | `string` |  | Reason for revocation of passphrase. |
| `username` | `string` |  | Username for the passphrase. |
| `vlanId` | `integer` |  | VLAN associated with passphrase. |


**Responses:**

- `202` The passphrase update request is in progress → `DPSK_Service_OperationResponse`


---



## APIs for DPSK Passphrase Device

*Operations for managing devices linked to DPSK passphrases.*


*4 endpoints*


### `DELETE` `/dpskServices/{poolId}/passphrases/{passphraseId}/devices`

**Delete Devices Associated with Passphrase**

Delete devices associated with a specific passphrase.

operationId: `deletePassphraseDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `passphraseId` | path | ✓ | `string` | DPSK passphrase ID |
| `poolId` | path | ✓ | `string` | DPSK pool ID |


**Request Body:** Yes


**Responses:**

- `202` The request to delete devices associated with the specified passphrase has been accepted. → `DPSK_Service_OperationResponse`


---

### `GET` `/dpskServices/{poolId}/passphrases/{passphraseId}/devices`

**Get Passphrase Devices**

Get all devices associated with the specified DPSK passphrase.

operationId: `getPassphraseDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `passphraseId` | path | ✓ | `string` | DPSK passphrase id |
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Responses:**

- `200` Get passphrase devices → `DPSK_Service_DpskPassphraseDeviceDto`
- `404` DPSK passphrase not found → `DPSK_Service_ApiError`


---

### `POST` `/dpskServices/{poolId}/passphrases/{passphraseId}/devices`

**Create Devices for Passphrase**

Create devices for a specific passphrase.

operationId: `createPassphraseDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `passphraseId` | path | ✓ | `string` | DPSK passphrase ID |
| `poolId` | path | ✓ | `string` | DPSK pool ID |


**Request Body:** Yes


**Responses:**

- `202` The request to create devices for the specified passphrase has been accepted. → `DPSK_Service_OperationResponse`


---

### `POST` `/dpskServices/{poolId}/passphrases/{passphraseId}/devices/query`

**List Passphrase Devices**

List paginated devices for the specified DPSK passphrase.

operationId: `listAllPassphraseDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `passphraseId` | path | ✓ | `string` | DPSK passphrase id |
| `poolId` | path | ✓ | `string` | DPSK pool id |


**Request Body:** `DPSK_Service_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `page` | `integer` |  | Page number, starting from index 0. |
| `pageSize` | `integer` |  | Number of items per page. |
| `searchString` | `string` |  | Search string to match against the specified searchTargetFields. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort by. |
| `sortOrder` | `string` |  | Sort order: ASC for ascending, DESC for descending. |


**Responses:**

- `200` The request to list devices for the specified passphrase has succeeded. → `DPSK_Service_Page`


---



## APIs for DPSK Service Template

*Operations for managing DPSK templates, including creation, cloning, and network template association.*


*9 endpoints*


### `POST` `/templates/dpskServices`

**Create New DPSK Pool Template**

Create a new DPSK pool template with the provided content.

operationId: `createDpskPoolTemplate_1`


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` DPSK pool template created → `DPSK_Service_OperationResponse`
- `400` Invalid pool content → `DPSK_Service_ApiError`


---

### `POST` `/templates/dpskServices/query`

**Search DPSK Pool Templates**

Search for DPSK pool templates matching search string in paged result.

operationId: `queryDpskPoolTemplates`


**Request Body:** `DPSK_Service_DpskPoolQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `DPSK_Service_DpskPoolFilters` |  | Filter criteria used to query DPSK pools. |
| `page` | `integer` |  | Page number, starting from index 0. |
| `pageSize` | `integer` |  | Number of items per page. |
| `searchString` | `string` |  | Search string to match against the specified searchTargetFields. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort by. |
| `sortOrder` | `string` |  | Sort order: ASC for ascending, DESC for descending. |


**Responses:**

- `200` DPSK pool templates → `DPSK_Service_DpskPoolTemplateQueryResponse`


---

### `DELETE` `/templates/dpskServices/{poolTemplateId}`

**Delete the DPSK Pool Template**

Delete the specified DPSK pool template.

operationId: `deleteDpskPoolTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolTemplateId` | path | ✓ | `string` | DPSK pool template id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `DPSK_Service_OperationResponse`


---

### `GET` `/templates/dpskServices/{poolTemplateId}`

**Get Specific DPSK Pool Template**

Get the specified DPSK pool template by its ID.

operationId: `getDpskPoolTemplateById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolTemplateId` | path | ✓ | `string` | DPSK pool template id |


**Responses:**

- `200` DPSK pool template → `DPSK_Service_DpskPoolDto`
- `404` DPSK pool template not found → `DPSK_Service_ApiError`


---

### `PATCH` `/templates/dpskServices/{poolTemplateId}`

**Update the DPSK Pool Template**

Partially update the specified DPSK pool template.

operationId: `patchDpskPoolTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolTemplateId` | path | ✓ | `string` | DPSK pool template id |


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `DPSK_Service_OperationResponse`


---

### `PUT` `/templates/dpskServices/{poolTemplateId}`

**Update the DPSK Pool Template**

Update the specified DPSK pool template.

operationId: `updateDpskPoolTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolTemplateId` | path | ✓ | `string` | DPSK pool template id |


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `DPSK_Service_OperationResponse`


---

### `POST` `/templates/dpskServices/{poolTemplateId}/cloneSettings`

**Clone the DPSK Pool Template**

Clone the specified DPSK pool template.

operationId: `cloneDpskPoolTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolTemplateId` | path | ✓ | `string` | DPSK pool template id |


**Request Body:** `DPSK_Service_TemplateCloneSettingsRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `name` | `string` | ✓ |  |


**Responses:**

- `202` DPSK pool template cloned → `DPSK_Service_OperationResponse`
- `400` Invalid content → `DPSK_Service_ApiError`


---

### `POST` `/templates/identityGroups/{identityGroupId}/dpskServices`

**Create Template with Identity Group**

Create new DPSK pool template with identity group.

operationId: `createDpskPoolTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `identityGroupId` | path | ✓ | `string` | Identity group id |


**Request Body:** `DPSK_Service_DpskPoolDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `autoNotificationsEnabled` | `boolean` |  | Whether to automatically send email/SMS notifications for passphrase create, update, or delete operations. |
| `createdDate` | `string` |  | Creation date timestamp record. |
| `deviceCountLimit` | `integer` |  | Maximum number of devices allowed per passphrase. |
| `expirationDate` | `string` |  | Expiration date of pool. |
| `expirationOffset` | `integer` |  | Date of expiration offset. |
| `expirationType` | `string` |  | Expiration date rule of pool. |
| `id` | `string` |  | Unique identifier for pool. |
| `identityGroupId` | `string` |  | Linked identity group ID. Only editable for template. |
| `identityId` | `string` |  | Deprecated. Use identity group ID instead. |
| `isEnforced` | `boolean` |  | Whether enforcement is enabled for this template. |
| `isReferenced` | `boolean` |  | If this entity is referenced by an identity group and cannot be deleted. |
| `lastModifiedDate` | `string` |  | Last modification timestamp record. |
| `name` | `string` | ✓ |  |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `numericSuffixEnabled` | `boolean` |  | When true, append a numeric suffix to generated dictionary-word passphrases. |
| `passphraseFormat` | `string` | ✓ | Format type of the passphrase. |
| `passphraseLength` | `integer` | ✓ | Minimum allowed length for the passphrase. |
| `policyDefaultAccess` | `boolean` |  | Default access if no policy rule matches. |
| `wordCount` | `integer` |  | Number of dictionary words when passphrase format is DICTIONARY_WORDS; ignored for other formats. |


**Responses:**

- `202` DPSK pool created → `DPSK_Service_OperationResponse`
- `400` Invalid pool content → `DPSK_Service_ApiError`


---

### `GET` `/templates/wifiNetworks/{networkTemplateId}/dpskServices`

**Get Templates by Network Template**

Get DPSK pool templates by network template.

operationId: `getDpskPoolTemplatesByNetworkTemplateId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkTemplateId` | path | ✓ | `string` | Wifi network template id |
| `pageable` | query | ✓ | `DPSK_Service_Pageable` | parameters for paging |


**Responses:**

- `200` DPSK pool template → `DPSK_Service_DpskPoolDto`
- `404` DPSK pool not found → `DPSK_Service_ApiError`


---



## APIs for DPSK REC Template

*Operations for managing DPSK REC templates.*


*0 endpoints*




## APIs for DPSK Passphrase by Identity Group

*2 endpoints*


### `POST` `/dpskServices/{poolId}/identityGroups/{groupId}/passphrases`

**Create DPSK Passphrase for Identity Group**

Create DPSK passphrase(s) for the specified pool and identity group.

operationId: `createPassphrase_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | DPSK pool id |
| `groupId` | path | ✓ | `string` | Identity group id |


**Request Body:** `DPSK_Service_DpskPassphraseCreateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `email` | `string` |  | The email for passphrase. |
| `expiration` | `string` |  | The expiration for passphrase. |
| `expirationDate` | `string` |  | The expiration for passphrase. |
| `format` | `string` |  | The format for passphrase. |
| `id` | `string` |  | Unique identifier for passphrase. |
| `identityId` | `string` |  | The identity ID for passphrase. |
| `length` | `integer` |  | Length of the passphrase. |
| `mac` | `string` |  | The mac for passphrase. |
| `numberOfDevices` | `integer` |  | Number of devices. Must be between 1 and 512. Inputs outside this range will be adjusted. |
| `numberOfDevicesType` | `string` |  | Number of devices type. |
| `numberOfPassphrases` | `integer` |  | The number of PSK to be generated if passphrase is not provided. |
| `passphrase` | `string` |  | The actual passphrase value to be created. |
| `phoneNumber` | `string` |  | The number for passphrase. |
| `username` | `string` |  | The username for passphrase. |
| `vlanId` | `integer` |  | The VLAN for passphrase. |
| `vxlanId` | `integer` |  | The VNI to associate with this PSK. |


**Responses:**

- `202` Create DPSK passphrase(s) accepted → `DPSK_Service_OperationResponse`
- `400` Invalid content supplied or identity group not associated with pool → `DPSK_Service_ApiError`


---

### `POST` `/dpskServices/{poolId}/identityGroups/{groupId}/passphrases/csvFiles`

**Import Passphrase from CSV for Identity Group**

Import DPSK passphrases from a CSV file for the specified pool and identity group.

operationId: `importPassphrasesFromCsv`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` |  |
| `groupId` | path | ✓ | `string` |  |
| `usernamePrefix` | query |  | `string` | Prefix for generated user names when the Username column is empty. |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `202` Import accepted → `DPSK_Service_OperationResponse`
- `400` Invalid content or identity group not associated with pool → `DPSK_Service_ApiError`


---


