# Guest Service

> RUCKUS One API Reference

---


## Guest User

*Manage guest users and their access credentials.*


*12 endpoints*


### `DELETE` `/guestUsers`

**Delete Guest Users**

Delete one or more guest users per their IDs as defined in the payload. This method will be removed no sooner than 08/31/2026.

operationId: `DeleteGuestUsersByIds`


**Request Body:** Yes


**Responses:**

- `200` OK → `Guest_Service_OperationResponseVoid`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/guestUsers`

**Get Guest Users**

Get user details for the list of provisioned guest users. This method will be removed no sooner than 08/31/2026.

operationId: `GetGuestUsers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `page` | query |  | `integer` | Page index |
| `size` | query |  | `integer` | The size of the page to be returned |


**Responses:**

- `200` OK → `Guest_Service_PageResponseGuestUser`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `POST` `/guestUsers`

**Add Guest Users**

Provision one or more guest users as defined in the payload. This method will be removed no sooner than 08/31/2026.

operationId: `AddGuestUsers`


**Request Body:** Yes


**Responses:**

- `201` Created → `Guest_Service_OperationResponseListGuestUser`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `DELETE` `/guestUsers/{guestUserId}`

**Delete Guest User by ID**

Delete a guest user. This method will be removed no sooner than 08/31/2026.

operationId: `DeleteGuestUserById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `guestUserId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseVoid`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/guestUsers/{guestUserId}`

**Get Guest User by ID**

Get a guest user. This method will be removed no sooner than 08/31/2026.

operationId: `GetGuestUserById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `guestUserId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Guest_Service_GuestUser`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PATCH` `/guestUsers/{guestUserId}`

**Update Guest User**

Update guest user enable/disable status or create new password for the guest user. This method will be removed no sooner than 08/31/2026.

operationId: `UpdateByGuestUserId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `guestUserId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_GuestUserUpdateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` | ✓ | Action for updating guest user. |
| `deliveryMethods` | `array` |  | At least one delivery method. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseGuestUser`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `POST` `/networks/{networkId}/guestUsers`

**Import Guest Users**

Import one or more guest pass users from the payload's CSV file. This method will be removed no sooner than 08/31/2026.

operationId: `ImportGuestUsers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | Network ID of the guest network to which the guest user will connect. |
| `expiration.activationType` | query | ✓ | `string` | When activation type is set to creation, the guest pass is valid when it's created until the specified expiration duration, even if it's not being used; when set to login, the guest pass is valid star |
| `expiration.duration` | query | ✓ | `integer` |  |
| `expiration.unit` | query | ✓ | `string` |  |
| `maxDevices` | query | ✓ | `integer` | Maximum number of devices the guest user can simultaneously connect to the guest network. If set to -1, no limit is enforced. |
| `deliveryMethods` | query |  | `array` | At least one delivery method. |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `['string']` | ✓ |  |


**Responses:**

- `201` Created → `Guest_Service_OperationResponseGuestUserImport`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PATCH` `/wifiNetworks/{wifiNetworkId}/guestUsers`

**Guest User Action**

Guest user action for the guest user.

operationId: `ActionByGuestUserIdAndWifiNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_GuestUserAction`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` | ✓ | Action for guest user. |
| `password` | `string` |  | Manual password. The password must contain at least 6 characters (up to 16). The following characters are permitted: lowercase and uppercase letters, 0-9, and other special characters !@#$%^&*()\[]{}-_+=~`\|:;"'<>,./?. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `POST` `/wifiNetworks/{wifiNetworkId}/guestUsers`

**Add Guest User**

Create a new guest user.

operationId: `AddGuestUser_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | Network ID of the guest network to which the guest user will connect. |
| `expiration.activationType` | query | ✓ | `string` | When activation type is set to creation, the guest pass is valid when it's created until the specified expiration duration, even if it's not being used; when set to login, the guest pass is valid star |
| `expiration.duration` | query | ✓ | `integer` |  |
| `expiration.unit` | query | ✓ | `string` |  |
| `maxDevices` | query | ✓ | `integer` | Maximum number of devices the guest user can simultaneously connect to the guest network. If set to -1, no limit is enforced. |
| `deliveryMethods` | query |  | `array` | At least one delivery method. |


**Request Body:** `Guest_Service_GuestUserV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `createdDate` | `integer` |  | Timestamp when the guest user was created. |
| `deliveryMethods` | `array` | ✓ | At least one delivery method. |
| `disabled` | `boolean` |  | If true, this guest user will not be permitted to join the guest network. |
| `email` | `string` |  | Email address of the guest user. |
| `expiration` | `Guest_Service_GuestUserExpiration` | ✓ | Expiration configuration for the guest user account. |
| `expirationDate` | `integer` |  | Expiration date is calculated per the expiration configuration. |
| `guestUserType` | `string` |  | This field is not editable after creation. |
| `id` | `string` |  |  |
| `lastModified` | `integer` |  | Timestamp when the guest user was last modified. |
| `macAddresses` | `array` |  | MAC addresses of the guest user's connected devices. |
| `maxDevices` | `integer` | ✓ | Maximum number of devices the guest user can simultaneously connect to the guest network. If set to minus one, no limit is enforced. |
| `mobilePhoneNumber` | `string` | ✓ | The mobile phone number associated to the guest user. |
| `name` | `string` | ✓ | The name assigned to the guest user. |
| `notes` | `string` |  | Additional notes or comments about the guest user. |
| `password` | `string` |  | The password is generated automatically by the system. |
| `ssid` | `string` |  | SSID of the network to which the guest connected. |


**Responses:**

- `201` Created → `Guest_Service_OperationResponseGuestUserDtoV1`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/guestUsers/{guestUserId}`

**Remove Guest User by ID**

Remove a guest user.

operationId: `DeleteGuestUserByIdAndWifiNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` |  |
| `guestUserId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/wifiNetworks/{wifiNetworkId}/guestUsers/{guestUserId}`

**Retrieve Guest User by ID**

Retrieve a guest user.

operationId: `GetGuestUserByIdAndWifiNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` |  |
| `guestUserId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Guest_Service_GuestUserWithoutIdV1`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PATCH` `/wifiNetworks/{wifiNetworkId}/guestUsers/{guestUserId}`

**Update Guest User**

Update guest user enable/disable status or create new password for the guest user.

operationId: `UpdateByGuestUserIdAndWifiNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` |  |
| `guestUserId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_GuestUserUpdate`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` |  | Action for updating guest user. |
| `deliveryMethods` | `array` |  | At least one delivery method. |
| `disabled` | `boolean` |  | If true, this guest user will not be permitted to join the guest network. |
| `password` | `string` |  | Manual password. The password must contain at least 6 characters (up to 16). The following characters are permitted: lowercase and uppercase letters, 0-9, and other special characters !@#$%^&*()\[]{}-_+=~`\|:;"'<>,./?. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseGuestUserWithoutIdV1`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---



## Portal Service Profile

*Manage portal service profile.*


*12 endpoints*


### `DELETE` `/portalServiceProfiles`

**Remove Portal Service Profile**

Remove portal service profile by ids. This method will be removed no sooner than 08/31/2026.

operationId: `DeletePortalServiceProfiles`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Guest_Service_OperationResponseVoid`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/portalServiceProfiles`

**Get Portal Service Profiles**

Get portal service profile for the list. This method will be removed no sooner than 08/31/2026.

operationId: `GetPortalServiceProfiles`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serviceName` | query |  | `string` | Portal Service Profile Name |
| `networkId` | query |  | `string` | NetworkId |
| `tags` | query |  | `string` | Tags |
| `page` | query |  | `integer` | Indicates the page to return, will be 1 based, and default to page 1 |
| `pageSize` | query |  | `integer` | Default is 256, indicates the page size to return |
| `excludeContent` | query |  | `boolean` | Get the total count information from the query and NOT pull the data |


**Responses:**

- `200` OK → `Guest_Service_PagingResponsePortalServiceProfileDto`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `POST` `/portalServiceProfiles`

**Add Portal Service Profile**

Provision one portal service profile as defined in the payload.

operationId: `AddPortalServiceProfile_1_1`


**Request Body:** `Guest_Service_PortalServiceProfileDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `content` | `Guest_Service_PortalServiceProfileContentDto` |  | Content configuration for the portal profile. |
| `id` | `string` |  | Unique identifier for the portal service profile. |
| `serviceName` | `string` |  | Name of the portal service. |
| `tags` | `string` |  | Tags associated with the portal service profile for categorization. |


**Responses:**

- `201` Created → `Guest_Service_EntityIdOperationResponse`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/portalServiceProfiles/networks`

**Get Network Filter**

Get network filter for portal service profile lists. This method will be removed no sooner than 08/31/2026.

operationId: `GetPortalServiceProfilesOfNetworkFilter`


**Responses:**

- `200` OK
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/portalServiceProfiles/tags`

**Get Tags Filter**

Get tags filter for portal service profile lists. This method will be removed no sooner than 08/31/2026.

operationId: `GetPortalServiceProfilesOfTagsFilter`


**Responses:**

- `200` OK
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `DELETE` `/portalServiceProfiles/{portalServiceProfileId}`

**Remove Portal Service Profile**

Remove portal service profile by id.

operationId: `DeletePortalServiceProfileById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/portalServiceProfiles/{portalServiceProfileId}`

**Retrieve Portal Service Profile**

Retrieve a portal service profile.

operationId: `GetPortalServiceProfileById_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Guest_Service_PortalServiceProfileWithoutId`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/portalServiceProfiles/{portalServiceProfileId}`

**Update Portal Service Profile**

Update portal service profile by id.

operationId: `UpdatePortalServiceProfileById_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `content` | `Guest_Service_PortalServiceProfileContentDto` |  | Content configuration for the portal profile. |
| `id` | `string` |  | Unique identifier for the portal service profile. |
| `serviceName` | `string` |  | Name of the portal service. |
| `tags` | `string` |  | Tags associated with the portal service profile for categorization. |


**Responses:**

- `202` Accepted → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/portalServiceProfiles/{portalServiceProfileId}/backgroundImages`

**Update Portal Profile Background Image**

Update portal service profile background image by id.

operationId: `UpdatePortalServiceProfileBackgroundImage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/portalServiceProfiles/{portalServiceProfileId}/logos`

**Update Portal Profile Logo**

Update portal service profile logo by id.

operationId: `UpdatePortalServiceProfileLogo`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/portalServiceProfiles/{portalServiceProfileId}/photos`

**Update Portal Service Profile Photo**

Update portal service profile photo by id.

operationId: `UpdatePortalServiceProfilePhoto`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/portalServiceProfiles/{portalServiceProfileId}/poweredImages`

**Update Portal Profile Powered Image**

Update portal service profile powered image by id.

operationId: `UpdatePortalServiceProfilePoweredImage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---



## Portal Service Template

*Manage portal service profile template. Use /rec/templates for REC templates.*


*8 endpoints*


### `POST` `/templates/portalServiceProfiles`

**Add Portal Service Profile Template**

Add a portal service profile template.

operationId: `AddPortalServiceProfileTemplate`


**Request Body:** `Guest_Service_PortalServiceProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `content` | `Guest_Service_PortalServiceProfileContentDtoV1_1` |  | Content configuration for the portal profile. |
| `id` | `string` |  | Unique identifier for the portal service profile. |
| `name` | `string` |  | Name of the portal service. |


**Responses:**

- `201` Created → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `DELETE` `/templates/portalServiceProfiles/{portalServiceProfileId}`

**Remove Portal Service Profile Template**

Remove a portal service profile template by id.

operationId: `DeletePortalServiceProfileTemplateById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `GET` `/templates/portalServiceProfiles/{portalServiceProfileId}`

**Retrieve Portal Service Profile Template**

Retrieve a portal service profile template by id.

operationId: `GetPortalServiceProfileTemplateByIdV1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Guest_Service_PortalServiceProfileWithoutId`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/templates/portalServiceProfiles/{portalServiceProfileId}`

**Update Portal Service Profile Template**

Update portal service profile template by id.

operationId: `updatePortalServiceProfileTemplateV1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `content` | `Guest_Service_PortalServiceProfileContentDtoV1_1` |  | Content configuration for the portal profile. |
| `id` | `string` |  | Unique identifier for the portal service profile. |
| `name` | `string` |  | Name of the portal service. |


**Responses:**

- `202` Accepted → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/templates/portalServiceProfiles/{portalServiceProfileId}/backgroundImages`

**Update Portal Template Background**

Update portal service profile template background image by id.

operationId: `updatePortalServiceProfileBackgroundImageTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/templates/portalServiceProfiles/{portalServiceProfileId}/logos`

**Update Portal Template Logo**

Update portal service profile template logo by id.

operationId: `updatePortalServiceProfileLogoTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/templates/portalServiceProfiles/{portalServiceProfileId}/photos`

**Update Portal Template Photo**

Update portal service profile template photo by id.

operationId: `updatePortalServiceProfilePhotoTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---

### `PUT` `/templates/portalServiceProfiles/{portalServiceProfileId}/poweredImages`

**Update Portal Template Powered Image**

Update portal service profile template powered image by id.

operationId: `updatePortalServiceProfilePoweredImageTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalServiceProfileId` | path | ✓ | `string` |  |


**Request Body:** `Guest_Service_PortalServiceProfileImage`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `image` | `string` |  | A base 64 encoded string. Note that all images are saved as portable network graphics files. |


**Responses:**

- `200` OK → `Guest_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `Guest_Service_ErrorResponse`
- `401` The request is unauthorized. → `Guest_Service_ErrorResponse`
- `403` Forbidden. → `Guest_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `Guest_Service_ErrorResponse`
- `422` Validation error. → `Guest_Service_ErrorResponse`
- `423` Locked. → `Guest_Service_ErrorResponse`
- `500` Internal Server Error. → `Guest_Service_ErrorResponse`


---


