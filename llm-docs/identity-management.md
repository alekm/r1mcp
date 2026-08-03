# Identity Management

> RUCKUS One API Reference

---


## Identity Group

*Operations for managing identity groups.*


*11 endpoints*


### `GET` `/identityGroups`

**Returns the Identity Groups**

Retrieve a paginated list of all identity groups for the tenant.

operationId: `getGroups`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |


**Responses:**

- `200` The Identity Groups → `Identity_Management_PageIdentityGroup`


---

### `POST` `/identityGroups`

**Create an Identity Group**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `createGroup`


**Request Body:** `Identity_Management_IdentityGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Identity_Management_Links` |  |  |
| `autoCleanupEnabled` | `boolean` |  | Whether auto cleanup is enabled for the group. |
| `certificateTemplateId` | `string` |  | The identifier of the certificate template associated with the group. |
| `createdAt` | `string` |  | The timestamp that the group get created. |
| `description` | `string` |  | The description for the group. |
| `dpskPoolId` | `string` |  | The identifier of the DPSK pool associated with the group. |
| `id` | `string` |  | The identifier for the group. |
| `identityCount` | `integer` |  | The number of identities belongs to the group. |
| `macRegistrationPoolId` | `string` |  | The identifier of the MAC registration pool associated with the group. |
| `name` | `string` | ✓ | The name for the group. |
| `networkCount` | `integer` |  | The number of the networks associated with the group. |
| `personalIdentityNetworkId` | `string` |  | The identifier of the personal identity network associated with the group. |
| `policySetId` | `string` |  | The identifier of the policy set associated with the group. |
| `propertyId` | `string` |  | Then identifier of the property associated with the group. |
| `templateVersion` | `integer` |  | The version of template. |
| `updatedAt` | `string` |  | The timestamp that the group get last update. |


**Responses:**

- `201` Group created → `Identity_Management_IdentityGroup`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid Group → `Identity_Management_ApiError`


---

### `POST` `/identityGroups/csvFile`

**Export Identity Groups Into File**

Export identity groups to a CSV file based on search criteria.

operationId: `exportGroupsCSV`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |
| `timezone` | query |  | `string` |  |
| `date-format` | query |  | `string` | Format will be applied for date values. Default value is "dd/MM/yyyy HH:mm" |


**Request Body:** `Identity_Management_IdentityGroupSearch`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `certificateTemplateId` | `string` |  | The filter to search by certificate template. |
| `dpskPoolId` | `string` |  | The filter to search by DPSK pool. |
| `groupIds` | `array` |  | The filter to search by identifiers. |
| `hasDpskService` | `boolean` |  | When true, only return identity groups with a DPSK service associated. When false, only return identity groups without a DPSK service. |
| `keyword` | `string` |  | The filter to search by keyword. |
| `macRegistrationPoolId` | `string` |  | The filter to search by MAC registration list. |
| `networkId` | `string` |  | The filter to search by network. |
| `personalIdentityNetworkId` | `string` |  | The filter to search by personal identity network. |
| `policySetId` | `string` |  | The filter to search by policy set. |
| `propertyId` | `string` |  | The filter to search by property. |


**Responses:**

- `200` The CSV returned


---

### `POST` `/identityGroups/query`

**Query the Identity Groups**

Search and filter identity groups based on specified criteria.

operationId: `searchGroups`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |


**Request Body:** `Identity_Management_IdentityGroupSearch`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `certificateTemplateId` | `string` |  | The filter to search by certificate template. |
| `dpskPoolId` | `string` |  | The filter to search by DPSK pool. |
| `groupIds` | `array` |  | The filter to search by identifiers. |
| `hasDpskService` | `boolean` |  | When true, only return identity groups with a DPSK service associated. When false, only return identity groups without a DPSK service. |
| `keyword` | `string` |  | The filter to search by keyword. |
| `macRegistrationPoolId` | `string` |  | The filter to search by MAC registration list. |
| `networkId` | `string` |  | The filter to search by network. |
| `personalIdentityNetworkId` | `string` |  | The filter to search by personal identity network. |
| `policySetId` | `string` |  | The filter to search by policy set. |
| `propertyId` | `string` |  | The filter to search by property. |


**Responses:**

- `200` The Identity Groups → `Identity_Management_PageIdentityGroup`


---

### `DELETE` `/identityGroups/{id}`

**Delete the Identity Group**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `deleteGroupById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |


**Responses:**

- `200` Group deleted → `Identity_Management_EmptyResponse`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id supplied → `Identity_Management_ApiError`
- `403` Operation forbidden → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`
- `405` Not allowed to delete → `Identity_Management_ApiError`


---

### `GET` `/identityGroups/{id}`

**Returns the Specific Identity Group**

Retrieve detailed information about a specific identity group by its ID.

operationId: `getGroupById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |


**Responses:**

- `200` Group found → `Identity_Management_IdentityGroup`
- `400` Invalid id supplied → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`


---

### `PATCH` `/identityGroups/{id}`

**Update the Identity Group**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `updateGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |


**Request Body:** `Identity_Management_IdentityGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Identity_Management_Links` |  |  |
| `autoCleanupEnabled` | `boolean` |  | Whether auto cleanup is enabled for the group. |
| `certificateTemplateId` | `string` |  | The identifier of the certificate template associated with the group. |
| `createdAt` | `string` |  | The timestamp that the group get created. |
| `description` | `string` |  | The description for the group. |
| `dpskPoolId` | `string` |  | The identifier of the DPSK pool associated with the group. |
| `id` | `string` |  | The identifier for the group. |
| `identityCount` | `integer` |  | The number of identities belongs to the group. |
| `macRegistrationPoolId` | `string` |  | The identifier of the MAC registration pool associated with the group. |
| `name` | `string` | ✓ | The name for the group. |
| `networkCount` | `integer` |  | The number of the networks associated with the group. |
| `personalIdentityNetworkId` | `string` |  | The identifier of the personal identity network associated with the group. |
| `policySetId` | `string` |  | The identifier of the policy set associated with the group. |
| `propertyId` | `string` |  | Then identifier of the property associated with the group. |
| `templateVersion` | `integer` |  | The version of template. |
| `updatedAt` | `string` |  | The timestamp that the group get last update. |


**Responses:**

- `200` Group updated → `Identity_Management_IdentityGroup`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id or change supplied → `Identity_Management_ApiError`
- `403` Not allowed to delete → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`


---

### `PUT` `/identityGroups/{id}/dpskPools/{dpskPoolId}`

**Update the DPSK Pool Association**

Associate a DPSK pool with an identity group.

operationId: `updateDpskPoolAssociation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |
| `dpskPoolId` | path | ✓ | `string` | DPSK pool id |


**Responses:**

- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id or change supplied → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`


---

### `PUT` `/identityGroups/{id}/macRegistrationPools/{poolId}`

**Update the MAC Registration Association**

Associate a MAC registration pool with an identity group.

operationId: `updateMacRegistrationAssociation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |
| `poolId` | path | ✓ | `string` | MAC registration pool id |


**Responses:**

- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id or change supplied → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`


---

### `DELETE` `/identityGroups/{id}/policySets/{policySetId}`

**Remove the Policy Set Association**

Remove the association between a policy set and an identity group.

operationId: `removePolicySetAssociation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id or change supplied → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`


---

### `PUT` `/identityGroups/{id}/policySets/{policySetId}`

**Update the Policy Set Association**

Associate a policy set with an identity group.

operationId: `updatePolicySetAssociation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Group id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id or change supplied → `Identity_Management_ApiError`
- `404` Group not found → `Identity_Management_ApiError`


---



## Identity

*Operations for managing identities.*


*15 endpoints*


### `GET` `/identities`

**Returns Identities in All Groups**

Retrieve a paginated list of all identities across all groups for the tenant.

operationId: `listIdentities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |


**Responses:**

- `200` Identities in all groups → `Identity_Management_PageIdentity`


---

### `POST` `/identities/csvFile`

**Export Identities Into File**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `exportIdentityToCSV`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |
| `timezone` | query |  | `string` |  |
| `date-format` | query |  | `string` | Format will be applied for date values. Default value is "dd/MM/yyyy HH:mm" |


**Request Body:** `Identity_Management_IdentitySearch`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dpskPoolId` | `string` |  | The filter to search by DPSK pool. |
| `ethernetPort` | `Identity_Management_EthernetPort` |  | The filter to search by ethernet port. |
| `filter` | `object` |  | The filter to search by additional fields. |
| `groupId` | `string` |  | The filter to search by group. |
| `ids` | `array` |  | The filter to search by identifiers. |
| `keyword` | `string` |  | The filter to search by keyword. |
| `propertyId` | `string` |  | The filter to search by property. |


**Responses:**

- `200` The identity csv


---

### `POST` `/identities/query`

**Query Identities**

Search and filter identities across all groups based on specified criteria.

operationId: `queryIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |


**Request Body:** `Identity_Management_IdentitySearch`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dpskPoolId` | `string` |  | The filter to search by DPSK pool. |
| `ethernetPort` | `Identity_Management_EthernetPort` |  | The filter to search by ethernet port. |
| `filter` | `object` |  | The filter to search by additional fields. |
| `groupId` | `string` |  | The filter to search by group. |
| `ids` | `array` |  | The filter to search by identifiers. |
| `keyword` | `string` |  | The filter to search by keyword. |
| `propertyId` | `string` |  | The filter to search by property. |


**Responses:**

- `200` Identities found → `Identity_Management_PageIdentity`


---

### `DELETE` `/identityGroups/{groupId}/identities`

**Delete the Identities in Group**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `bulkDeleteIdentities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |


**Request Body:** Yes


**Responses:**

- `200` Identities deleted → `Identity_Management_EmptyResponse`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid supplied id → `Identity_Management_ApiError`
- `403` Operation forbidden → `Identity_Management_ApiError`
- `404` Identities not found → `Identity_Management_ApiError`
- `405` Not allowed to delete the Identities → `Identity_Management_ApiError`


---

### `GET` `/identityGroups/{groupId}/identities`

**Returns Identities in the Group**

Retrieve a paginated list of all identities within a specific identity group.

operationId: `listIdentitiesByGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |


**Responses:**

- `200` Identities returned
- `400` Invalid group id supplied → `Identity_Management_ApiError`


---

### `POST` `/identityGroups/{groupId}/identities`

**Create Identity Into the Group**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `createIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `autoDpskPassphraseCreation` | query |  | `boolean` | Automatically create DPSK passphrase for the identity upon creation. Defaults to true. |


**Request Body:** `Identity_Management_Identity`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Identity_Management_Links` |  |  |
| `createdAt` | `string` |  | The timestamp that the identity get created. |
| `description` | `string` |  | The description for the identity. |
| `deviceCount` | `integer` |  | The count of devices belongs to the identity. |
| `devices` | `array` |  | The list of devices for the identity. |
| `displayName` | `string` |  | The display name for the identity. |
| `dpskGuid` | `string` |  | The identifier of the DPSK for the identity. |
| `dpskPassphrase` | `string` |  | The passphrase associated with the identity. If this field is set to null in an update request, the passphrase will be reset. Note: if a passphrase is provided but is shorter than the required minimum length, it will also be reset. |
| `email` | `string` |  | The email for the identity. |
| `ethernetPorts` | `array` |  | The list of ethernet port for the identity. |
| `expirationDate` | `string` |  | The expiration date for the metering profile of this identity. |
| `externalIdentityId` | `string` |  | The identifier of the external identity for the identity. |
| `groupId` | `string` |  | The identifier of the group for the identity. |
| `id` | `string` |  | The identifier for the identity. |
| `identityId` | `string` |  | The identifier of entity that associated with identity. |
| `lastLoginAt` | `string` |  | The latest timestamp that the identity login. |
| `meteringProfileId` | `string` |  | The identifier of the metering profile. |
| `name` | `string` | ✓ | The name for the identity. |
| `parentId` | `string` |  | The identifier of the parent identity. |
| `phoneNumber` | `string` |  | The phone number for the identity. |
| `primary` | `boolean` |  | The field to determine if identity is primary. |
| `revoked` | `boolean` |  | The field to determine if identity is revoked. |
| `switches` | `array` |  | The list of switch for the identity. |
| `updatedAt` | `string` |  | The timestamp that the identity get last update. |
| `vlan` | `integer` |  | The VLAN for the identity. |
| *… 1 more fields* | | | |


**Responses:**

- `201` Identity created → `Identity_Management_Identity`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid identity → `Identity_Management_ApiError`
- `403` Not allowed to create an Identity into the Group → `Identity_Management_ApiError`
- `404` Identity group not found → `Identity_Management_ApiError`
- `419` Resource limitation has already been reached → `Identity_Management_ApiError`


---

### `POST` `/identityGroups/{groupId}/identities/csvFile`

**Import Identities Into the Specified Identity Group**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `importIdentities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` |  |
| `autoDpskPassphraseCreation` | query |  | `boolean` | Automatically create DPSK passphrase for the identities upon import. Defaults to true. |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `201` The Identities get created
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid Identity → `Identity_Management_ApiError`
- `403` The tenant is not allowed to create an Identity into the group → `Identity_Management_ApiError`
- `404` Identity group not found → `Identity_Management_ApiError`
- `413` The file size is too large → `Identity_Management_ApiError`
- `419` The resource limitation has already been reached → `Identity_Management_ApiError`


---

### `DELETE` `/identityGroups/{groupId}/identities/{id}`

**Delete the Identity**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `deleteIdentityById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |


**Responses:**

- `200` Identity get deleted → `Identity_Management_EmptyResponse`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid supplied id → `Identity_Management_ApiError`
- `403` Operation forbidden → `Identity_Management_ApiError`
- `404` Identity not found → `Identity_Management_ApiError`
- `405` Not allowed to delete the Identity → `Identity_Management_ApiError`


---

### `GET` `/identityGroups/{groupId}/identities/{id}`

**Returns the Identity**

Retrieve detailed information about a specific identity by its ID.

operationId: `getIdentityById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |


**Responses:**

- `200` Identity found → `Identity_Management_Identity`
- `400` Invalid id supplied → `Identity_Management_ApiError`
- `404` Identity not found → `Identity_Management_ApiError`


---

### `PATCH` `/identityGroups/{groupId}/identities/{id}`

**Update the Identity**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `updateIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |


**Request Body:** `Identity_Management_Identity`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Identity_Management_Links` |  |  |
| `createdAt` | `string` |  | The timestamp that the identity get created. |
| `description` | `string` |  | The description for the identity. |
| `deviceCount` | `integer` |  | The count of devices belongs to the identity. |
| `devices` | `array` |  | The list of devices for the identity. |
| `displayName` | `string` |  | The display name for the identity. |
| `dpskGuid` | `string` |  | The identifier of the DPSK for the identity. |
| `dpskPassphrase` | `string` |  | The passphrase associated with the identity. If this field is set to null in an update request, the passphrase will be reset. Note: if a passphrase is provided but is shorter than the required minimum length, it will also be reset. |
| `email` | `string` |  | The email for the identity. |
| `ethernetPorts` | `array` |  | The list of ethernet port for the identity. |
| `expirationDate` | `string` |  | The expiration date for the metering profile of this identity. |
| `externalIdentityId` | `string` |  | The identifier of the external identity for the identity. |
| `groupId` | `string` |  | The identifier of the group for the identity. |
| `id` | `string` |  | The identifier for the identity. |
| `identityId` | `string` |  | The identifier of entity that associated with identity. |
| `lastLoginAt` | `string` |  | The latest timestamp that the identity login. |
| `meteringProfileId` | `string` |  | The identifier of the metering profile. |
| `name` | `string` | ✓ | The name for the identity. |
| `parentId` | `string` |  | The identifier of the parent identity. |
| `phoneNumber` | `string` |  | The phone number for the identity. |
| `primary` | `boolean` |  | The field to determine if identity is primary. |
| `revoked` | `boolean` |  | The field to determine if identity is revoked. |
| `switches` | `array` |  | The list of switch for the identity. |
| `updatedAt` | `string` |  | The timestamp that the identity get last update. |
| `vlan` | `integer` |  | The VLAN for the identity. |
| *… 1 more fields* | | | |


**Responses:**

- `200` Identity updated → `Identity_Management_Identity`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid change supplied → `Identity_Management_ApiError`
- `403` Operation forbidden → `Identity_Management_ApiError`
- `404` Identity not found → `Identity_Management_ApiError`


---

### `POST` `/identityGroups/{groupId}/identities/{id}/devices`

**Create Devices Into the Identity**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `createDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |


**Request Body:** Yes


**Responses:**

- `201` Devices created
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id or content supplied → `Identity_Management_ApiError`
- `403` Operation forbidden → `Identity_Management_ApiError`
- `404` Identity not found → `Identity_Management_ApiError`


---

### `DELETE` `/identityGroups/{groupId}/identities/{id}/devices/{macAddress}`

**Delete Device from Identity**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `deleteDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |
| `macAddress` | path | ✓ | `string` | Device's MAC |


**Responses:**

- `200` Device deleted → `Identity_Management_EmptyResponse`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id supplied → `Identity_Management_ApiError`
- `403` The tenant is not allowed to delete the device → `Identity_Management_ApiError`
- `404` Device not found → `Identity_Management_ApiError`


---

### `DELETE` `/identityGroups/{groupId}/identities/{id}/ethernetPorts/{macAddress}/{portIndex}`

**Delete Ethernet Port from Identity**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1+json which will be moved to application/vnd.ruckus.v1.1+json on 08/31/2026.

operationId: `deleteEthernetPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |
| `macAddress` | path | ✓ | `string` | Ethernet Port's MAC |
| `portIndex` | path | ✓ | `integer` | Ethernet Port's port index |


**Responses:**

- `200` Ethernet Port deleted → `Identity_Management_EmptyResponse`
- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid id supplied → `Identity_Management_ApiError`
- `403` Operation forbidden → `Identity_Management_ApiError`
- `404` Ethernet port not found → `Identity_Management_ApiError`


---

### `PUT` `/identityGroups/{groupId}/identities/{id}/venues/{venueId}/ethernetPorts`

**Update the Identity's Ethernet Ports**

Update the ethernet ports associated with an identity at a specific venue.

operationId: `updateIdentityEthernetPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `venueId` | path | ✓ | `string` | Venue id |
| `id` | path | ✓ | `string` | Identity id |


**Request Body:** Yes


**Responses:**

- `202` Request accepted → `Identity_Management_OperationResponse`
- `400` Invalid Identity → `Identity_Management_ApiError`
- `404` Identity not found → `Identity_Management_ApiError`


---

### `DELETE` `/identityGroups/{groupId}/identities/{id}/vnis`

**Retry VNI Allocation for Identity**

Retry the VNI allocation for a specific identity.

operationId: `allocateIdentityVni`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | Group id |
| `id` | path | ✓ | `string` | Identity id |


**Responses:**

- `200` The retry has been executed successfully → `Identity_Management_EmptyResponse`
- `400` The request is invalid → `Identity_Management_ApiError`
- `403` The tenant is not allowed to retry the vni for the Identity → `Identity_Management_ApiError`
- `404` Identity not found → `Identity_Management_ApiError`


---



## External Identity

*Operations for managing external identities.*


*1 endpoint*


### `POST` `/externalIdentities/query`

**Query External Identities**

Search and filter external identities based on specified criteria.

operationId: `queryExternalIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Identity_Management_Pageable` | Parameters for paging |


**Request Body:** `Identity_Management_ExternalIdentitySearch`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ids` | `array` |  | External identity identifiers filter. |


**Responses:**

- `200` External identities found → `Identity_Management_PageExternal Identity`


---


