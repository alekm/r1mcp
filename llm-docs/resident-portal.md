# Resident Portal

> RUCKUS One API Reference

---


## Resident Portal Login API

*Manages resident portal access.*


*1 endpoint*


### `POST` `/residents/properties/{propertyId}/units/logins`

**Access Resident Portal**

Enables user authentication and authorization.

operationId: `residentLogin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Request Body:** `Resident_Portal_LoginResource`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `hashedSecret` | `string` |  | Hashed secret used for login authentication. |


**Responses:**

- `200` Ok → `Resident_Portal_PortalTokenResource`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `401` Unauthorized → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---



## Resident Portal UI Configuration

*Provides resident portal UI configuration.*


*3 endpoints*


### `GET` `/residents/properties/{propertyId}/access`

**Gets Portal Access Details**

Fetches resident portal access details.

operationId: `getTenantPortalAccess`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Responses:**

- `200` Ok → `Resident_Portal_ResidentPortalAccessDto`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/files/favicons`

**Gets Resident Portal Icon File**

Enables the user to get a resident portal icon file for the property.

operationId: `downloadFavicons`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Responses:**

- `200` Ok
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/styles`

**Gets Resident Portal Styles**

Gets resident portal page details.

operationId: `getPropertyStyles`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Responses:**

- `200` Ok
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---



## Resident Portal Configuration

*Manages resident portal configuration.*


*3 endpoints*


### `GET` `/residents/properties/{propertyId}`

**Gets Property Details**

Gets details of the property.

operationId: `residentFetchProperty`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Responses:**

- `200` Ok → `Resident_Portal_EntityModelPropertyDto`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Property requested is not found → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/files/{type}`

**Gets Resident Portal File**

Allows the user to download resident portal file with the given type.

operationId: `residentDownloadPortalFile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |
| `type` | path | ✓ | `string` | Resident Portal file type. |


**Responses:**

- `200` Ok
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/uiConfigurations`

**Gets User Interface Configurations**

Gets user interface configurations for the portal.

operationId: `residentFetchUiConfiguration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Responses:**

- `200` Ok → `Resident_Portal_EntityModelPortalUiConfiguration`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---



## Resident Portal Unit API

*Manages units associated to the resident portal.*


*4 endpoints*


### `GET` `/residents/properties/{propertyId}/units`

**Gets Unit Details**

Gets unit details for the authenticated unit.

operationId: `residentFetchUnit`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Responses:**

- `200` Ok → `Resident_Portal_EntityModelUnitDto`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `PUT` `/residents/properties/{propertyId}/units`

**Selectively Updates Unit Configurations**

Allows the user to selectively update unit configurations such as passphrase, contact details.

operationId: `residentEditUnit`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |


**Request Body:** `Resident_Portal_UnitDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `contact` | `Resident_Portal_UnitContactDto` |  | Contact details for the resident. |
| `description` | `string` |  |  |
| `guestSecret` | `string` |  | Passphrase for the unit guest. |
| `guid` | `string` |  | Unique identifier for the unit. |
| `number` | `string` | ✓ | Name or number of the unit. |
| `secret` | `string` |  | Passphrase for the unit owner. |
| `status` | `string` |  | Current status of the unit. |


**Responses:**

- `200` Unit configuration updated → `Resident_Portal_EntityModelUnitDto`
- `202` Accepted → `Resident_Portal_EntityModelUnitDto`
- `400` Missing or invalid request body → `Resident_Portal_ErrorResource`
- `404` Unit configuration not found for the given unit id → `Resident_Portal_ErrorResource`
- `500` Internal error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/units/devices`

**Gets Unit Devices**

Allows the user to get all unit and guest devices with the given unit id.

operationId: `residentFetchUnitDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |
| `type` | query | ✓ | `string` | Type of device.UNIT and GUEST are the possible values |


**Responses:**

- `200` Ok → `Resident_Portal_EntityModelDevicesListResource`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `DELETE` `/residents/properties/{propertyId}/units/devices/{deviceId}`

**Delete Device**

Allows the user to selectively remove unit device on the specified unit and device MAC address.

operationId: `residentRemoveDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |
| `deviceId` | path | ✓ | `string` | Device Identification |


**Responses:**

- `200` Unit device removed
- `400` Missing or invalid request body → `Resident_Portal_ErrorResource`
- `404` Unit device not found for the given unit → `Resident_Portal_ErrorResource`
- `500` Internal error → `Resident_Portal_ErrorResource`


---



## Resident Portal Unit Users API

*Manages users of unit associated to the resident portal.*


*5 endpoints*


### `POST` `/residents/properties/{propertyId}/units/users/query`

**Query Unit Users**

Gets the list of unit users using the specified query.

operationId: `queryUnitUsers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property Id |


**Request Body:** `Resident_Portal_UnitUsersQueryCriteria`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `page` | `integer` |  | Page number. If not specified the first page will be returned. |
| `pageSize` | `integer` |  | Number of records in a page.If not specified default page size of 20 will be applied. |
| `sortDirection` | `string` |  | Direction for sorting results (ASC/DESC). |
| `sortFields` | `array` |  | Fields to sort results by. |
| `userId` | `string` |  | Unique identifier for the unit user. |


**Responses:**

- `200` ok → `Resident_Portal_PageEntityModelUnitUserDto`
- `400` Invalid query data supplied. → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/units/users/{userId}`

**Get unit user details**

Gets unit user details for the requested user.

operationId: `getUnitUser`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `userId` | path | ✓ | `string` | User Id |
| `propertyId` | path | ✓ | `string` | Property Id |


**Responses:**

- `200` Ok → `Resident_Portal_EntityModelUnitUserDto`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `PUT` `/residents/properties/{propertyId}/units/users/{userId}`

**Updates Unit User**

Enables update of unit user.

operationId: `updateUnitUser`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property Id |
| `userId` | path | ✓ | `string` | User Id |


**Request Body:** `Resident_Portal_UnitUserDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `email` | `string` |  | Email address of the unit user. |
| `passphrase` | `string` |  | Unit user passphrase.  For resetting passphrase please provide empty string in request. |
| `phoneNumber` | `string` |  | Unit user phone number. |
| `status` | `string` |  | Unit user status. |
| `type` | `string` |  | Unit user type. |
| `userId` | `string` |  | Unique identifier for the unit user. |
| `userName` | `string` |  | Display name of the unit user. |


**Responses:**

- `200` ok → `Resident_Portal_MultiRequestResponse`
- `202` Accepted → `Resident_Portal_MultiRequestResponse`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `GET` `/residents/properties/{propertyId}/units/users/{userId}/devices`

**Get unit user devices**

Gets unit user devices for the requested user.

operationId: `getUnitUserDevices`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `userId` | path | ✓ | `string` | User Id |
| `propertyId` | path | ✓ | `string` | Property Id |


**Responses:**

- `200` Ok → `Resident_Portal_EntityModelDevicesListResource`
- `400` Bad request → `Resident_Portal_ErrorResource`
- `404` Not found
- `500` Internal server error → `Resident_Portal_ErrorResource`


---

### `DELETE` `/residents/properties/{propertyId}/units/users/{userId}/devices/{deviceId}`

**Delete Unit User Device**

Allows the user to selectively remove a device.

operationId: `removeUnitUserDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `propertyId` | path | ✓ | `string` | Property identifier. |
| `deviceId` | path | ✓ | `string` | Device Identification |
| `userId` | path | ✓ | `string` | User Id |


**Responses:**

- `200` Device removed
- `400` Missing or invalid request body → `Resident_Portal_ErrorResource`
- `404` Device not found for the given unit → `Resident_Portal_ErrorResource`
- `500` Internal error → `Resident_Portal_ErrorResource`


---


