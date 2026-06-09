# MAC Registration

> RUCKUS One API Reference

---


## MAC Registration

*Operations for managing MAC address registrations within registration pools. MAC registrations allow devices to be authenticated and granted network access based on their MAC address.*


*8 endpoints*


### `DELETE` `/macRegistrationPools/{poolId}/registrations`

**Delete the Specific MAC Registrations**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `deleteRegistrations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | Registration pool id |


**Request Body:** Yes


**Responses:**

- `200` Registration deleted → `MAC_Registration_EmptyResponse`
- `202` The registration bulk delete request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid ids supplied → `MAC_Registration_ApiError`


---

### `GET` `/macRegistrationPools/{poolId}/registrations`

**List MAC Registrations in Pool**

List the MAC registrations in the registration pool.

operationId: `listAllRegistrations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `page` | query |  | `integer` | Page index starting from 0 (0..N) |
| `size` | query |  | `integer` | The size of the page to be returned |
| `sort` | query |  | `array` | Sorting criteria in the format: property,(asc\|desc). Default sort order is ascending. Multiple sort criteria are supported. |
| `poolId` | path | ✓ | `string` | Registration pool id |


**Responses:**

- `200` Registrations → `MAC_Registration_PageRegistration`


---

### `POST` `/macRegistrationPools/{poolId}/registrations`

**Create a MAC Registration in the Specified Registration Pool**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `createRegistration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | Registration pool id |


**Request Body:** `MAC_Registration_Registration`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `MAC_Registration_Links` |  |  |
| `createdDate` | `string` |  | The created date of this device. |
| `deviceName` | `string` |  | The name of the device. |
| `email` | `string` |  | The email to associate with this device. |
| `expirationDate` | `string` |  | Indicates when this registration expires. Will derive from the pool setting if not specified. |
| `id` | `string` |  | The unique identifier for this MAC registration. |
| `isReferenced` | `boolean` |  | This registration is referenced by an identity and cannot be deleted. |
| `location` | `string` |  | The location of this device. |
| `macAddress` | `string` | ✓ | The mac address for this registration. Must be provided on post, and may not be changed. |
| `revoked` | `boolean` |  | If this MAC registration is revoked or not. |
| `username` | `string` |  | A username for this device, it does not reflect an authenticated user that has gone through a real authentication process. |


**Responses:**

- `201` Registration created → `MAC_Registration_Registration`
- `202` The registration create request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid content supplied → `MAC_Registration_ApiError`
- `419` Exceed max registrations of the pool → `MAC_Registration_ApiError`


---

### `POST` `/macRegistrationPools/{poolId}/registrations/csvFile`

**Import MAC Registrations with the Specified Registration Pool**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `importRegistrations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `poolId` | path | ✓ | `string` | Registration pool id |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `201` Registration pools created
- `202` The registration import request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid content supplied → `MAC_Registration_ApiError`
- `413` Payload too large → `MAC_Registration_ApiError`
- `419` Exceed max registrations of the pool → `MAC_Registration_ApiError`


---

### `POST` `/macRegistrationPools/{poolId}/registrations/query`

**Search MAC Registrations by Criteria**

Search the MAC registrations by the criteria.

operationId: `searchRegistrations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `page` | query |  | `integer` | Page index starting from 0 (0..N) |
| `size` | query |  | `integer` | The size of the page to be returned |
| `sort` | query |  | `array` | Sorting criteria in the format: property,(asc\|desc). Default sort order is ascending. Multiple sort criteria are supported. |
| `poolId` | path | ✓ | `string` | Registration pool id |


**Request Body:** `MAC_Registration_SearchDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dataOption` | `string` |  | The data option for the search. |
| `searchCriteriaList` | `array` |  | The list of search criteria. |


**Responses:**

- `200` Registrations → `MAC_Registration_PageRegistration`


---

### `DELETE` `/macRegistrationPools/{poolId}/registrations/{id}`

**Delete the Specific MAC Registration**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `deleteRegistration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | MAC registration id |
| `poolId` | path | ✓ | `string` | Registration pool id |


**Responses:**

- `200` Registration deleted → `MAC_Registration_EmptyResponse`
- `202` The registration delete request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid id supplied → `MAC_Registration_ApiError`
- `404` MAC registration not found → `MAC_Registration_ApiError`
- `409` The Registration associated with other resources is not allowed to be deleted → `MAC_Registration_ApiError`


---

### `GET` `/macRegistrationPools/{poolId}/registrations/{id}`

**Returns the Specific MAC Registration**

Return the specific MAC registration.

operationId: `getRegistrationById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | MAC registration id |
| `poolId` | path | ✓ | `string` | Registration pool id |


**Responses:**

- `200` MAC registration → `MAC_Registration_Registration`
- `400` Invalid id supplied → `MAC_Registration_ApiError`
- `404` MAC registration not found → `MAC_Registration_ApiError`


---

### `PATCH` `/macRegistrationPools/{poolId}/registrations/{id}`

**Update Properties in the Specific MAC Registration**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `updateRegistration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | MAC registration id |
| `poolId` | path | ✓ | `string` | Registration pool id |


**Request Body:** `MAC_Registration_Registration`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `MAC_Registration_Links` |  |  |
| `createdDate` | `string` |  | The created date of this device. |
| `deviceName` | `string` |  | The name of the device. |
| `email` | `string` |  | The email to associate with this device. |
| `expirationDate` | `string` |  | Indicates when this registration expires. Will derive from the pool setting if not specified. |
| `id` | `string` |  | The unique identifier for this MAC registration. |
| `isReferenced` | `boolean` |  | This registration is referenced by an identity and cannot be deleted. |
| `location` | `string` |  | The location of this device. |
| `macAddress` | `string` | ✓ | The mac address for this registration. Must be provided on post, and may not be changed. |
| `revoked` | `boolean` |  | If this MAC registration is revoked or not. |
| `username` | `string` |  | A username for this device, it does not reflect an authenticated user that has gone through a real authentication process. |


**Responses:**

- `200` MAC registration updated → `MAC_Registration_Registration`
- `202` The registration update request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid id or content supplied → `MAC_Registration_ApiError`
- `404` MAC registration not found → `MAC_Registration_ApiError`


---



## Registration Pool

*Operations for managing registration pools. Registration pools are containers that hold MAC address registrations and define access policies for devices.*


*8 endpoints*


### `GET` `/macRegistrationPools`

**List Registration Pools**

List the registration pools.

operationId: `listAllPools`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `page` | query |  | `integer` | Page index starting from 0 (0..N) |
| `size` | query |  | `integer` | The size of the page to be returned |
| `sort` | query |  | `array` | Sorting criteria in the format: property,(asc\|desc). Default sort order is ascending. Multiple sort criteria are supported. |


**Responses:**

- `200` Registration pools → `MAC_Registration_PagePool`


---

### `POST` `/macRegistrationPools`

**Create a Registration Pool**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `createPool`


**Request Body:** `MAC_Registration_Pool`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `MAC_Registration_Links` |  |  |
| `autoCleanup` | `boolean` |  | A toggle determining whether MAC registrations that are 24 hours past the expiration time will be automatically removed from the pool. |
| `createdDate` | `string` |  | The created date of this pool. |
| `defaultAccess` | `string` |  | The type of default access. |
| `description` | `string` |  | A description of the pool. |
| `expirationDate` | `string` |  | If the expiration type is specified_date then this field is the related date. |
| `expirationEnabled` | `boolean` |  | If the expiration setting is enabled for new MAC registration. |
| `expirationOffset` | `integer` |  | If the expiration type is not specified_date then this field is the offset amount. |
| `expirationType` | `string` |  | Defines the rule for expiration date calculation. |
| `id` | `string` |  | The unique identifier for this pool. |
| `identityGroupId` | `string` |  | The identity group of this pool. |
| `identityId` | `string` |  | The single identity policy of this pool. |
| `isReferenced` | `boolean` |  | This pool is referenced by an identity group and cannot be deleted. |
| `name` | `string` | ✓ | The unique reference name of the pool. |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `policySetId` | `string` |  | The policy set of this pool. |
| `registrationCount` | `integer` |  | Number of registrations in the pool. |
| `ssidRegex` | `string` |  | A regex to determine which SSIDs this registration pool will allows access to. |


**Responses:**

- `201` Registration pool created → `MAC_Registration_Pool`
- `202` The registration pool create request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid pool content → `MAC_Registration_ApiError`
- `419` Exceed max pools per tenant → `MAC_Registration_ApiError`


---

### `POST` `/macRegistrationPools/query`

**Search Registration Pools by Criteria**

Search the registration pools by the criteria.

operationId: `searchPools`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `page` | query |  | `integer` | Page index starting from 0 (0..N) |
| `size` | query |  | `integer` | The size of the page to be returned |
| `sort` | query |  | `array` | Sorting criteria in the format: property,(asc\|desc). Default sort order is ascending. Multiple sort criteria are supported. |


**Request Body:** `MAC_Registration_SearchDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dataOption` | `string` |  | The data option for the search. |
| `searchCriteriaList` | `array` |  | The list of search criteria. |


**Responses:**

- `200` Registration pools → `MAC_Registration_PagePool`


---

### `DELETE` `/macRegistrationPools/{id}`

**Delete the Specific Registration Pool**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `deletePool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Registration pool id |


**Responses:**

- `200` Registration pool deleted → `MAC_Registration_EmptyResponse`
- `202` The registration pool delete request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid id supplied → `MAC_Registration_ApiError`
- `404` Registration pool not found → `MAC_Registration_ApiError`
- `409` The Registration pool associated with other resources is not allowed to be deleted → `MAC_Registration_ApiError`


---

### `GET` `/macRegistrationPools/{id}`

**Returns the Specific Registration Pool**

Return the specific registration pool.

operationId: `getPoolById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Registration pool id |


**Responses:**

- `200` Registration pool → `MAC_Registration_Pool`
- `400` Invalid id supplied → `MAC_Registration_ApiError`
- `404` Registration pool not found → `MAC_Registration_ApiError`


---

### `PATCH` `/macRegistrationPools/{id}`

**Update Properties in the Specific Registration Pool**

This method will be removed no sooner than 08/31/2026 and application/json is currently tied to application/vnd.ruckus.v1.1+json.

operationId: `updatePool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Registration pool id |


**Request Body:** `MAC_Registration_Pool`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `MAC_Registration_Links` |  |  |
| `autoCleanup` | `boolean` |  | A toggle determining whether MAC registrations that are 24 hours past the expiration time will be automatically removed from the pool. |
| `createdDate` | `string` |  | The created date of this pool. |
| `defaultAccess` | `string` |  | The type of default access. |
| `description` | `string` |  | A description of the pool. |
| `expirationDate` | `string` |  | If the expiration type is specified_date then this field is the related date. |
| `expirationEnabled` | `boolean` |  | If the expiration setting is enabled for new MAC registration. |
| `expirationOffset` | `integer` |  | If the expiration type is not specified_date then this field is the offset amount. |
| `expirationType` | `string` |  | Defines the rule for expiration date calculation. |
| `id` | `string` |  | The unique identifier for this pool. |
| `identityGroupId` | `string` |  | The identity group of this pool. |
| `identityId` | `string` |  | The single identity policy of this pool. |
| `isReferenced` | `boolean` |  | This pool is referenced by an identity group and cannot be deleted. |
| `name` | `string` | ✓ | The unique reference name of the pool. |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `policySetId` | `string` |  | The policy set of this pool. |
| `registrationCount` | `integer` |  | Number of registrations in the pool. |
| `ssidRegex` | `string` |  | A regex to determine which SSIDs this registration pool will allows access to. |


**Responses:**

- `200` Registration pool updated → `MAC_Registration_Pool`
- `202` The registration pool update request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid id supplied → `MAC_Registration_ApiError`
- `404` Registration pool not found → `MAC_Registration_ApiError`


---

### `DELETE` `/macRegistrationPools/{id}/policySets/{policySetId}`

**Remove Policy Set from Pool**

Remove the policy set id from the registration pool.

operationId: `macPoolRemovePolicySetId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Registration pool id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` The remove request has been accepted and is in progress → `MAC_Registration_OperationResponse`
- `404` Registration pool not found → `MAC_Registration_ApiError`


---

### `PUT` `/macRegistrationPools/{id}/policySets/{policySetId}`

**Change Policy Set for Pool**

Update the policy set id for the registration pool.

operationId: `macPoolUpdatePolicySetId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `string` | Registration pool id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` The update request has been accepted and is in progress → `MAC_Registration_OperationResponse`
- `404` Registration pool not found → `MAC_Registration_ApiError`


---



## Assign Registration Pool Identity Group

*Operations for associating registration pools with identity groups. Registration pools can be associated with identity groups to control which devices can access the pools.*


*1 endpoint*


### `POST` `/identityGroups/{identityGroupId}/macRegistrationPools`

**Create Pool with Identity Group**

Create a registration pool with the identity group.

operationId: `createPoolWithIdentityGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `identityGroupId` | path | ✓ | `string` | The identity group to create |


**Request Body:** `MAC_Registration_Pool`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `MAC_Registration_Links` |  |  |
| `autoCleanup` | `boolean` |  | A toggle determining whether MAC registrations that are 24 hours past the expiration time will be automatically removed from the pool. |
| `createdDate` | `string` |  | The created date of this pool. |
| `defaultAccess` | `string` |  | The type of default access. |
| `description` | `string` |  | A description of the pool. |
| `expirationDate` | `string` |  | If the expiration type is specified_date then this field is the related date. |
| `expirationEnabled` | `boolean` |  | If the expiration setting is enabled for new MAC registration. |
| `expirationOffset` | `integer` |  | If the expiration type is not specified_date then this field is the offset amount. |
| `expirationType` | `string` |  | Defines the rule for expiration date calculation. |
| `id` | `string` |  | The unique identifier for this pool. |
| `identityGroupId` | `string` |  | The identity group of this pool. |
| `identityId` | `string` |  | The single identity policy of this pool. |
| `isReferenced` | `boolean` |  | This pool is referenced by an identity group and cannot be deleted. |
| `name` | `string` | ✓ | The unique reference name of the pool. |
| `networkCount` | `integer` |  | Number of networks associated with this pool. |
| `policySetId` | `string` |  | The policy set of this pool. |
| `registrationCount` | `integer` |  | Number of registrations in the pool. |
| `ssidRegex` | `string` |  | A regex to determine which SSIDs this registration pool will allows access to. |


**Responses:**

- `202` The registration pool create request is in progress → `MAC_Registration_OperationResponse`
- `400` Invalid pool content → `MAC_Registration_ApiError`


---



## Wifi Network

*Operations for managing WiFi network associations with registration pools. Networks can be associated with pools to control which networks devices can access.*


*1 endpoint*


### `GET` `/wifiNetworks/{networkId}/macRegistrationPools`

**Get Pools by Network ID**

Get the registration pools by the network id.

operationId: `getPoolsByNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | Wifi network id |
| `page` | query |  | `integer` | Page index starting from 0 (0..N) |
| `size` | query |  | `integer` | The size of the page to be returned |
| `sort` | query |  | `array` | Sorting criteria in the format: property,(asc\|desc). Default sort order is ascending. Multiple sort criteria are supported. |


**Responses:**

- `200` Registration pools → `MAC_Registration_PagePool`


---


