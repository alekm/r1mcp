# External Authentication Service

> RUCKUS One API Reference

---


## Directory Profile

*Manage directory server profiles for LDAP and active directory integration enabling enterprise user authentication and authorization.*


*4 endpoints*


### `POST` `/directoryServerProfiles`

**Create Directory Server Profile**

Create a new directory server profile for LDAP or active directory integration enabling enterprise user authentication.

operationId: `addDirectoryServerProfile`


**Request Body:** `External_Authentication_Service_DirectoryServerProfileDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminDomainName` | `string` | ✓ | The administrative domain name (admin DN) for directory server authentication. Used for binding to the directory server. |
| `adminPassword` | `string` | ✓ | The administrative password for directory server authentication. This password is encrypted and masked in logs. |
| `attributeMappings` | `array` |  | List of attribute mappings that map directory server attributes to local attribute names. This field is hidden and used for internal configuration purposes. |
| `domainName` | `string` | ✓ | The domain name for directory server authentication. This is the base DN for LDAP or domain name for active directory. |
| `host` | `string` | ✓ | The hostname, IPv4 address, or IPv6 address of the directory server. Must be a valid hostname or IP address. |
| `keyAttribute` | `string` |  | The key attribute name used for user identification in directory searches. Optional field, must start with a letter if specified. |
| `name` | `string` | ✓ | The unique name of the directory server profile. Must be 2-32 characters. |
| `port` | `integer` | ✓ | The port number for connecting to the directory server. Typically 389 for LDAP or 636 for LDAPs. |
| `searchFilter` | `string` |  | The LDAP search filter for finding users in the directory. Optional field, must follow LDAP filter syntax if specified. |
| `tlsEnabled` | `boolean` |  | Indicates whether TLS encryption is enabled for directory server connections. When enabled, connections are secured with TLS/SSL. |
| `type` | `string` | ✓ | The type of directory server, either AD (Active Directory) or LDAP. |


**Responses:**

- `200` OK → `External_Authentication_Service_EntityIdOperationResponse`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `DELETE` `/directoryServerProfiles/{directoryServerProfileId}`

**Delete **

Delete an existing directory server profile removing LDAP or active directory integration configuration from the system.

operationId: `deleteDirectoryServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `directoryServerProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `GET` `/directoryServerProfiles/{directoryServerProfileId}`

**Get Directory Server Profile**

Retrieve detailed configuration information for a specific directory server profile using the unique profile identifier.

operationId: `getDirectoryServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `directoryServerProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_DirectoryServerProfileDto`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `PUT` `/directoryServerProfiles/{directoryServerProfileId}`

**Update Directory Server Profile**

Update the configuration settings of an existing directory server profile for LDAP or active directory integration.

operationId: `updateDirectoryServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `directoryServerProfileId` | path | ✓ | `string` |  |


**Request Body:** `External_Authentication_Service_DirectoryServerProfileDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminDomainName` | `string` | ✓ | The administrative domain name (admin DN) for directory server authentication. Used for binding to the directory server. |
| `adminPassword` | `string` | ✓ | The administrative password for directory server authentication. This password is encrypted and masked in logs. |
| `attributeMappings` | `array` |  | List of attribute mappings that map directory server attributes to local attribute names. This field is hidden and used for internal configuration purposes. |
| `domainName` | `string` | ✓ | The domain name for directory server authentication. This is the base DN for LDAP or domain name for active directory. |
| `host` | `string` | ✓ | The hostname, IPv4 address, or IPv6 address of the directory server. Must be a valid hostname or IP address. |
| `keyAttribute` | `string` |  | The key attribute name used for user identification in directory searches. Optional field, must start with a letter if specified. |
| `name` | `string` | ✓ | The unique name of the directory server profile. Must be 2-32 characters. |
| `port` | `integer` | ✓ | The port number for connecting to the directory server. Typically 389 for LDAP or 636 for LDAPs. |
| `searchFilter` | `string` |  | The LDAP search filter for finding users in the directory. Optional field, must follow LDAP filter syntax if specified. |
| `tlsEnabled` | `boolean` |  | Indicates whether TLS encryption is enabled for directory server connections. When enabled, connections are secured with TLS/SSL. |
| `type` | `string` | ✓ | The type of directory server, either AD (Active Directory) or LDAP. |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---



## SAML Identity Provider

*Manage SAML identity providers.*


*9 endpoints*


### `POST` `/samlIdpProfiles`

**Create SAML Identity Provider Profile**

Create a SAML identity provider profile.

operationId: `createSamlIdpProfile`


**Request Body:** `External_Authentication_Service_SamlIdpProfileRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `attributeMappings` | `array` |  | List of mappings from SAML provider attributes to R1 user attributes. |
| `metadata` | `string` |  | Base64-encoded content, max 512KB when decoded. |
| `metadataUrl` | `string` |  | URL to fetch SAML identity provider metadata from. |
| `name` | `string` | ✓ |  |
| `updatedDate` | `string` |  | Timestamp when the profile was last updated. |


**Responses:**

- `200` OK → `External_Authentication_Service_EntityIdOperationResponse`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `DELETE` `/samlIdpProfiles/{samlIdpProfileId}`

**Delete SAML Identity Provider Profile**

Delete the specified SAML identity provider profile.

operationId: `deleteSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `GET` `/samlIdpProfiles/{samlIdpProfileId}`

**Get SAML Identity Provider Profile**

Retrieve the specified SAML identity provider profile.

operationId: `getSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_SamlIdpProfileRequest`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `PATCH` `/samlIdpProfiles/{samlIdpProfileId}`

**Update Partial SAML Profile**

Update the specified partial SAML identity provider profile.

operationId: `samlIdpProfileAction`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |


**Request Body:** `External_Authentication_Service_SamlIdpProfileAction`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` |  | The action type to execute on the profile. |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `PUT` `/samlIdpProfiles/{samlIdpProfileId}`

**Update Entire SAML Profile**

Update the specified entire SAML identity provider profile.

operationId: `updateSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |


**Request Body:** `External_Authentication_Service_SamlIdpProfileRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `attributeMappings` | `array` |  | List of mappings from SAML provider attributes to R1 user attributes. |
| `metadata` | `string` |  | Base64-encoded content, max 512KB when decoded. |
| `metadataUrl` | `string` |  | URL to fetch SAML identity provider metadata from. |
| `name` | `string` | ✓ |  |
| `updatedDate` | `string` |  | Timestamp when the profile was last updated. |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `DELETE` `/samlIdpProfiles/{samlIdpProfileId}/encryptionCertificates/{certificateId}`

**Deactivate Encryption Certificate**

Deactivates the specified encryption certificate for the SAML identity provider profile.

operationId: `deactivateEncryptionCertificateOnSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |
| `certificateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `PUT` `/samlIdpProfiles/{samlIdpProfileId}/encryptionCertificates/{certificateId}`

**Activate Encryption Certificate**

Activates the specified encryption certificate for the SAML identity provider profile.

operationId: `activateEncryptionCertificateOnSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |
| `certificateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `DELETE` `/samlIdpProfiles/{samlIdpProfileId}/signingCertificates/{certificateId}`

**Deactivate Signing Certificate**

Deactivates the specified signing certificate for the SAML identity provider profile.

operationId: `deactivateSigningCertificateOnSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |
| `certificateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---

### `PUT` `/samlIdpProfiles/{samlIdpProfileId}/signingCertificates/{certificateId}`

**Activate Signing Certificate**

Activates the specified signing certificate for the SAML identity provider profile.

operationId: `activateSigningCertificateOnSamlIdpProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `samlIdpProfileId` | path | ✓ | `string` |  |
| `certificateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `External_Authentication_Service_OperationResponseRequestIdOnly`
- `400` Bad/malformed request. → `External_Authentication_Service_ErrorResponse`
- `401` The request is unauthorized. → `External_Authentication_Service_ErrorResponse`
- `403` Forbidden. → `External_Authentication_Service_ErrorResponse`
- `404` Requested resource or related entity not found. → `External_Authentication_Service_ErrorResponse`
- `422` Validation error. → `External_Authentication_Service_ErrorResponse`
- `423` Locked. → `External_Authentication_Service_ErrorResponse`
- `500` Internal Server Error. → `External_Authentication_Service_ErrorResponse`


---


