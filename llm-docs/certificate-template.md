# Certificate Template

> RUCKUS One API Reference

---


## Server and Client Certificate

*APIs for server and client certificate management.*


*19 endpoints*


### `POST` `/certificateAuthorities/{caId}/certificates`

**Create certificate**

Creates a new server or client certificate.

operationId: `createCert_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_CertificateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` | ✓ | SHA-256 - the SHA-2 hash using 256 bits. SHA-384 - the SHA-2 hash using 384 bits. SHA-512 - the SHA-2 hash using 512 bits. |
| `certificateAuthorityName` | `string` |  | The name of the certificate authority that issued this certificate. |
| `chain` | `string` |  | The chain of the certificate. |
| `commonName` | `string` |  | The common name of the certificate. |
| `country` | `string` |  | The country included in the certificate. |
| `createDate` | `string` |  | The date that creates the certificate. |
| `csrString` | `string` |  | The certificate signing request that should be signed by the CA. |
| `description` | `string` |  | The description of the certificate. |
| `details` | `string` |  | The details of the certificate. |
| `email` | `string` |  | The email of the certificate. |
| `extendedKeyUsages` | `array` |  | The extended key usage of the certificate. |
| `id` | `string` |  | The unique for this certificate. |
| `keyLength` | `integer` | ✓ | The length of the key. |
| `keyUsages` | `array` |  | The key usages of the certificate. |
| `locality` | `string` |  | The locality included in the certificate. |
| `name` | `string` | ✓ | The name of the certificate. |
| `notAfterDate` | `string` | ✓ | The expires date of the certificate. |
| `notBeforeDate` | `string` | ✓ | The start date of the certificate. |
| `organization` | `string` |  | The organization of the certificate. |
| `organizationUnit` | `string` |  | The organization unit of the certificate. |
| `privateKeyBase64` | `string` |  | The private key of the certificate. |
| `publicKeyBase64` | `string` |  | The public key of the certificate. |
| `revocationDate` | `string` |  | The date after which the certificate be revoked. |
| `revocationReason` | `string` |  | Reason for revocation of certificate. |
| `serialNumber` | `string` |  | The serial number of the certificate. |
| *… 4 more fields* | | | |


**Responses:**

- `202` Certificate created → `Certificate_Template_OperationResponse`
- `400` Invalid Certificate content → `Certificate_Template_ApiError`


---

### `POST` `/certificateAuthorities/{caId}/certificates/query`

**Search certificates by CA**

Searches for certificates issued by a specific certificate authority.

operationId: `getByCaId_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_CertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_CertFilters` |  | Filters to apply when querying server certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Server or Client Certificate → `Certificate_Template_CertQueryResponse`


---

### `POST` `/certificateAuthorities/{caId}/serverCertificates`

**Create certificate**

Creates a new server or client certificate.

operationId: `createCert`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_CertificateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` | ✓ | SHA-256 - the SHA-2 hash using 256 bits. SHA-384 - the SHA-2 hash using 384 bits. SHA-512 - the SHA-2 hash using 512 bits. |
| `certificateAuthorityName` | `string` |  | The name of the certificate authority that issued this certificate. |
| `chain` | `string` |  | The chain of the certificate. |
| `commonName` | `string` |  | The common name of the certificate. |
| `country` | `string` |  | The country included in the certificate. |
| `createDate` | `string` |  | The date that creates the certificate. |
| `csrString` | `string` |  | The certificate signing request that should be signed by the CA. |
| `description` | `string` |  | The description of the certificate. |
| `details` | `string` |  | The details of the certificate. |
| `email` | `string` |  | The email of the certificate. |
| `extendedKeyUsages` | `array` |  | The extended key usage of the certificate. |
| `id` | `string` |  | The unique for this certificate. |
| `keyLength` | `integer` | ✓ | The length of the key. |
| `keyUsages` | `array` |  | The key usages of the certificate. |
| `locality` | `string` |  | The locality included in the certificate. |
| `name` | `string` | ✓ | The name of the certificate. |
| `notAfterDate` | `string` | ✓ | The expires date of the certificate. |
| `notBeforeDate` | `string` | ✓ | The start date of the certificate. |
| `organization` | `string` |  | The organization of the certificate. |
| `organizationUnit` | `string` |  | The organization unit of the certificate. |
| `privateKeyBase64` | `string` |  | The private key of the certificate. |
| `publicKeyBase64` | `string` |  | The public key of the certificate. |
| `revocationDate` | `string` |  | The date after which the certificate be revoked. |
| `revocationReason` | `string` |  | Reason for revocation of certificate. |
| `serialNumber` | `string` |  | The serial number of the certificate. |
| *… 4 more fields* | | | |


**Responses:**

- `202` Certificate created → `Certificate_Template_OperationResponse`
- `400` Invalid Certificate content → `Certificate_Template_ApiError`


---

### `POST` `/certificateAuthorities/{caId}/serverCertificates/query`

**Search certificates by CA**

Searches for certificates issued by a specific certificate authority.

operationId: `getByCaId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_CertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_CertFilters` |  | Filters to apply when querying server certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Server or Client Certificate → `Certificate_Template_CertQueryResponse`


---

### `POST` `/certificates`

**Upload certificate**

Uploads a server or client certificate.

operationId: `uploadCert_1`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `certificateFile` | `string` | ✓ | The certificate in P12, DER or PEM format be uploaded. |
| `name` | `string` | ✓ | The name for the certificate. |
| `password` | `string` |  | If private key or key store is password-protected, specify the password. If not, leave the password blank. |
| `privateKeyFile` | `string` |  | The private key in PEM format be uploaded. |


**Responses:**

- `202` The upload request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/certificates/query`

**Search certificates**

Searches for server or client certificates matching the search criteria.

operationId: `queryCerts_1`


**Request Body:** `Certificate_Template_CertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_CertFilters` |  | Filters to apply when querying server certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificate → `Certificate_Template_CertQueryResponse`


---

### `DELETE` `/certificates/{certId}`

**Delete certificate**

Deletes a server or client certificate.

operationId: `deleteCert_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`
- `404` Certificate not found → `Certificate_Template_ApiError`
- `409` Certificate cannot be deleted because it is currently in use → `Certificate_Template_ApiError`


---

### `GET` `/certificates/{certId}`

**Get certificate by ID**

Retrieves a specific server or client certificate by ID.

operationId: `downloadCertPem_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `200` Certificate → `Certificate_Template_CertificateDto`
- `404` Certificate not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificates/{certId}`

**Update certificate**

Updates a server or client certificate.

operationId: `patchCert_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Request Body:** `Certificate_Template_UpdateServerCertificateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of this certificate. |
| `name` | `string` |  | The name for the certificate. |
| `notAfterDate` | `string` |  | The expiration date for the renewed certificate. The start date for the validity period will also be set to today. |
| `revocationReason` | `string` |  | The reason for revocation of passphrase. If not revoked, this field should be null. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/certificates/{certId}`

**Download certificate private key**

Downloads the private key of a certificate.

operationId: `downloadServerCertP12_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Request Body:** `Certificate_Template_CertDownloadRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `includeChain` | `boolean` |  | Whether to include the certificate chain in the download. |
| `password` | `string` |  | The password to use to encrypt the private key. If encryption is not required, please leave it blank. |


**Responses:**

- `200` Downloaded private key of CA


---

### `GET` `/certificates/{certId}/chains`

**Download certificate chain**

Downloads the certificate chain in PEM format.

operationId: `downloadServerCertChainInPkcs7`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `200` Downloaded certificate in chain.


---

### `GET` `/radiusProfiles/{radiusProfileId}/certificates`

**Get certificates by RADIUS**

Retrieves certificates associated with a RADIUS profile.

operationId: `getCertificatesByRadiusId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certType` | query | ✓ | `string` |  |
| `radiusProfileId` | path | ✓ | `string` | Radius id |
| `pageable` | query | ✓ | `Certificate_Template_Pageable` | parameters for paging |


**Responses:**

- `200` Certificate → `Certificate_Template_CertificateDto`


---

### `POST` `/serverCertificates`

**Upload certificate**

Uploads a server or client certificate.

operationId: `uploadCert`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `certificateFile` | `string` | ✓ | The certificate in P12, DER or PEM format be uploaded. |
| `name` | `string` | ✓ | The name for the certificate. |
| `password` | `string` |  | If private key or key store is password-protected, specify the password. If not, leave the password blank. |
| `privateKeyFile` | `string` |  | The private key in PEM format be uploaded. |


**Responses:**

- `202` The upload request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/serverCertificates/query`

**Search certificates**

Searches for server or client certificates matching the search criteria.

operationId: `queryCerts`


**Request Body:** `Certificate_Template_CertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_CertFilters` |  | Filters to apply when querying server certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificate → `Certificate_Template_CertQueryResponse`


---

### `DELETE` `/serverCertificates/{certId}`

**Delete certificate**

Deletes a server or client certificate.

operationId: `deleteCert`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`
- `404` Certificate not found → `Certificate_Template_ApiError`
- `409` Certificate cannot be deleted because it is currently in use → `Certificate_Template_ApiError`


---

### `GET` `/serverCertificates/{certId}`

**Get certificate by ID**

Retrieves a specific server or client certificate by ID.

operationId: `downloadCertPem`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `200` Certificate → `Certificate_Template_CertificateDto`
- `404` Certificate not found → `Certificate_Template_ApiError`


---

### `PATCH` `/serverCertificates/{certId}`

**Update certificate**

Updates a server or client certificate.

operationId: `patchCert`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Request Body:** `Certificate_Template_UpdateServerCertificateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of this certificate. |
| `name` | `string` |  | The name for the certificate. |
| `notAfterDate` | `string` |  | The expiration date for the renewed certificate. The start date for the validity period will also be set to today. |
| `revocationReason` | `string` |  | The reason for revocation of passphrase. If not revoked, this field should be null. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/serverCertificates/{certId}`

**Download certificate private key**

Downloads the private key of a certificate.

operationId: `downloadServerCertP12`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Request Body:** `Certificate_Template_CertDownloadRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `includeChain` | `boolean` |  | Whether to include the certificate chain in the download. |
| `password` | `string` |  | The password to use to encrypt the private key. If encryption is not required, please leave it blank. |


**Responses:**

- `200` Downloaded private key of CA


---

### `GET` `/serverCertificates/{certId}/chains`

**Download certificate chain**

Downloads the certificate chain in PEM format.

operationId: `downloadServerCertChainInPkcs7_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `200` Downloaded certificate in chain.


---



## Device Certificate

*APIs for device certificate management.*


*11 endpoints*


### `POST` `/certificateTemplates/certificates/query`

**Search certificates**

Searches for certificates matching the search criteria.

operationId: `queryAllCerts`


**Request Body:** `Certificate_Template_DeviceCertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_DeviceCertFilters` |  | Filters to apply when querying certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificates → `Certificate_Template_DeviceCertQueryResponse`


---

### `DELETE` `/certificateTemplates/{templateId}/certificates`

**Delete certificates**

Deletes multiple certificates in bulk.

operationId: `deleteCerts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate Template id |


**Request Body:** Yes


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`
- `400` Invalid request data → `Certificate_Template_ApiError`
- `404` Certificate Template not found → `Certificate_Template_ApiError`


---

### `POST` `/certificateTemplates/{templateId}/certificates`

**Generate Certificate**

Generates a new certificate.

operationId: `generateCert`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Certificate_Template_GenerateCertDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `csrString` | `string` |  | The certificate signing request that should be signed by the CA. |
| `description` | `string` |  | Description of the item for reference. |
| `userName` | `string` |  | The certificate template contains the variable. The value specified here will be used to replace the variable. |
| `variableValues` | `object` |  | The values in this map will be used to replace the variables in the generated certificate. |


**Responses:**

- `202` Certificate generated → `Certificate_Template_OperationResponse`
- `400` Invalid certificate data → `Certificate_Template_ApiError`


---

### `POST` `/certificateTemplates/{templateId}/certificates/query`

**Search certificates in template**

Searches for certificates in a specific template matching the search criteria.

operationId: `queryCerts_2`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Certificate_Template_DeviceCertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_DeviceCertFilters` |  | Filters to apply when querying certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificates → `Certificate_Template_DeviceCertQueryResponse`


---

### `GET` `/certificateTemplates/{templateId}/certificates/{certId}`

**Get certificate by ID**

Retrieves a specific certificate by ID.

operationId: `downloadCertDer`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |
| `templateId` | path | ✓ | `string` | Certificate template id |


**Responses:**

- `200` Certificate → `Certificate_Template_DeviceCertificateDto`
- `404` Certificate not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificateTemplates/{templateId}/certificates/{certId}`

**Update certificate**

Updates a device certificate with the provided changes.

operationId: `patchCert_2`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate Template id |
| `certId` | path | ✓ | `string` | Certificate id |


**Request Body:** `Certificate_Template_UpdateCertificateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `revocationReason` | `string` |  | The reason for revocation of certificate. If not revoked, this field should be null. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/certificateTemplates/{templateId}/certificates/{certId}`

**Download certificate private key**

Downloads the private key of an issued certificate.

operationId: `downloadCertP12`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |
| `templateId` | path | ✓ | `string` | Certificate template id |


**Request Body:** `Certificate_Template_CertDownloadRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `includeChain` | `boolean` |  | Whether to include the certificate chain in the download. |
| `password` | `string` |  | The password to use to encrypt the private key. If encryption is not required, please leave it blank. |


**Responses:**

- `200` Downloaded private key of issued certificate.


---

### `GET` `/certificateTemplates/{templateId}/certificates/{certId}/chains`

**Download certificate chain**

Downloads the certificate chain in PEM format.

operationId: `downloadCertChainInPkcs7`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `certId` | path | ✓ | `string` | Certificate id |
| `templateId` | path | ✓ | `string` | Certificate template id |


**Responses:**

- `200` Downloaded certificate in chain.


---

### `POST` `/certificateTemplates/{templateId}/identities/certificates`

**Generate certificates for identities**

Generates certificates for multiple identities.

operationId: `generateCertsForIdentities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Certificate_Template_BulkGenerateCertDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `csrString` | `string` |  | The certificate signing request that should be signed by the CA. |
| `description` | `string` |  | Description of the item for reference. |
| `identityIds` | `array` | ✓ | List of identity IDs for which certificates should be generated |
| `variableValues` | `object` |  | The values in this map will be used to replace the variables in the generated certificate. |


**Responses:**

- `202` Certificates generation request accepted → `Certificate_Template_OperationResponse`
- `400` Invalid certificate data or identities → `Certificate_Template_ApiError`


---

### `POST` `/certificateTemplates/{templateId}/identities/{identityId}/certificates`

**Generate certificate for identity**

Generates a certificate for a specific identity.

operationId: `generateCertToIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |
| `identityId` | path | ✓ | `string` |  |


**Request Body:** `Certificate_Template_GenerateCertDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `csrString` | `string` |  | The certificate signing request that should be signed by the CA. |
| `description` | `string` |  | Description of the item for reference. |
| `userName` | `string` |  | The certificate template contains the variable. The value specified here will be used to replace the variable. |
| `variableValues` | `object` |  | The values in this map will be used to replace the variables in the generated certificate. |


**Responses:**

- `202` Certificate generated → `Certificate_Template_OperationResponse`
- `400` Invalid certificate data → `Certificate_Template_ApiError`


---

### `POST` `/certificateTemplates/{templateId}/identities/{identityId}/certificates/query`

**Search certificates by identity**

Searches for certificates associated with a specific identity.

operationId: `getCertsByIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `identityId` | path | ✓ | `string` | Identity id |


**Request Body:** `Certificate_Template_DeviceCertQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_DeviceCertFilters` |  | Filters to apply when querying certificates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificates → `Certificate_Template_DeviceCertQueryResponse`


---



## Certificate Authority

*APIs for certificate authority management.*


*14 endpoints*


### `POST` `/certificateAuthorities`

**Create certificate authority**

Creates a new certificate authority.

operationId: `uploadCa`


**Request Body:** `Certificate_Template_CaDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` | ✓ | The algorithm with which to generate the certificate authority. |
| `chain` | `string` |  | The chain of the certificate. |
| `commonName` | `string` | ✓ | The common name of this authority. |
| `country` | `string` |  | The country where your organization is located. |
| `description` | `string` |  | The description of this authority. |
| `details` | `string` |  | The details of the certificate. |
| `email` | `string` |  | The email address for the party responsible for the certificate authority. |
| `expireDate` | `string` | ✓ | The expires date of the certificate authority. |
| `id` | `string` |  | The unique identifier for this authority. |
| `keyLength` | `integer` | ✓ | The key length for the certificate authority. |
| `keyUsages` | `array` |  | The key usage for the CA. |
| `locality` | `string` |  | The city where your organization is located. |
| `name` | `string` | ✓ | The name of this authority. |
| `ocspHash` | `string` |  | The hash of online certificate status protocol. |
| `ocspName` | `string` |  | The name hash of online certificate status protocol. |
| `organization` | `string` |  | The organization for the certificate authority. |
| `organizationUnit` | `string` |  | The division of your organization responsible for the certificate authority. |
| `privateKeyBase64` | `string` |  | Base64 string of the private key. |
| `publicKeyBase64` | `string` |  | Base64 string of the public key. |
| `publicKeyShaThumbprint` | `string` |  | Thumbprint of public key. |
| `serialNumber` | `string` |  | The serial number of public key of this authority. |
| `startDate` | `string` | ✓ | The expires date of the certificate authority. |
| `state` | `string` |  | The state or region where your organization is located. |
| `status` | `array` |  | The status of the certificate of the CA. |
| `templateCount` | `integer` |  | The count of template assign this CA. |
| *… 3 more fields* | | | |


**Responses:**

- `202` Certificate Authority created → `Certificate_Template_OperationResponse`
- `400` Invalid Certificate Authority content → `Certificate_Template_ApiError`


---

### `POST` `/certificateAuthorities/query`

**Search certificate authorities**

Searches for certificate authorities matching the search criteria.

operationId: `queryCas`


**Request Body:** `Certificate_Template_CaQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_CaFilters` |  | Filters to apply when querying certificate authorities. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificate Authorities → `Certificate_Template_CaQueryResponse`


---

### `DELETE` `/certificateAuthorities/{caId}`

**Delete certificate authority**

Deletes a certificate authority.

operationId: `deleteCa`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateAuthorities/{caId}`

**Get certificate authority by ID**

Retrieves a specific certificate authority by ID.

operationId: `downloadCaDer`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | CA id |


**Responses:**

- `200` Certificate Authority → `Certificate_Template_CaDto`
- `404` Certificate Authority not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificateAuthorities/{caId}`

**Update certificate authority**

Updates a certificate authority.

operationId: `patchCa`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_UpdateCaDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of this authority. |
| `name` | `string` |  | The name of this authority. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/certificateAuthorities/{caId}`

**Download CA private key**

Downloads the private key of certificate authority.

operationId: `downloadCaP12`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate id |


**Request Body:** `Certificate_Template_CertDownloadRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `includeChain` | `boolean` |  | Whether to include the certificate chain in the download. |
| `password` | `string` |  | The password to use to encrypt the private key. If encryption is not required, please leave it blank. |


**Responses:**

- `200` Downloaded private key of CA


---

### `GET` `/certificateAuthorities/{caId}/chains`

**Download CA certificate chain**

Downloads the certificate chain of a certificate authority in PEM format.

operationId: `downloadCaChainPKCS7`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate id |


**Responses:**

- `200` Downloaded chain


---

### `DELETE` `/certificateAuthorities/{caId}/privateKeys`

**Delete CA private key**

Deletes the private key for a certificate authority.

operationId: `deleteCaPrivateKey`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/certificateAuthorities/{caId}/privateKeys`

**Upload CA private key**

Uploads the private key for a certificate authority.

operationId: `uploadCaPrivateKey`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `password` | `string` |  | If upload private key is password-protected, specify the password. If not, leave the password blank. |
| `privateKey` | `string` | ✓ | Upload the private key of the certificate authority in PEM format. |


**Responses:**

- `202` The upload request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `POST` `/certificateAuthorities/{caId}/subCas`

**Create sub certificate authority**

Creates a new sub certificate authority.

operationId: `createSubCa`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Root Certificate Authority id |


**Request Body:** `Certificate_Template_CaDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` | ✓ | The algorithm with which to generate the certificate authority. |
| `chain` | `string` |  | The chain of the certificate. |
| `commonName` | `string` | ✓ | The common name of this authority. |
| `country` | `string` |  | The country where your organization is located. |
| `description` | `string` |  | The description of this authority. |
| `details` | `string` |  | The details of the certificate. |
| `email` | `string` |  | The email address for the party responsible for the certificate authority. |
| `expireDate` | `string` | ✓ | The expires date of the certificate authority. |
| `id` | `string` |  | The unique identifier for this authority. |
| `keyLength` | `integer` | ✓ | The key length for the certificate authority. |
| `keyUsages` | `array` |  | The key usage for the CA. |
| `locality` | `string` |  | The city where your organization is located. |
| `name` | `string` | ✓ | The name of this authority. |
| `ocspHash` | `string` |  | The hash of online certificate status protocol. |
| `ocspName` | `string` |  | The name hash of online certificate status protocol. |
| `organization` | `string` |  | The organization for the certificate authority. |
| `organizationUnit` | `string` |  | The division of your organization responsible for the certificate authority. |
| `privateKeyBase64` | `string` |  | Base64 string of the private key. |
| `publicKeyBase64` | `string` |  | Base64 string of the public key. |
| `publicKeyShaThumbprint` | `string` |  | Thumbprint of public key. |
| `serialNumber` | `string` |  | The serial number of public key of this authority. |
| `startDate` | `string` | ✓ | The expires date of the certificate authority. |
| `state` | `string` |  | The state or region where your organization is located. |
| `status` | `array` |  | The status of the certificate of the CA. |
| `templateCount` | `integer` |  | The count of template assign this CA. |
| *… 3 more fields* | | | |


**Responses:**

- `202` Certificate Authority created → `Certificate_Template_OperationResponse`
- `400` Invalid Certificate Authority content → `Certificate_Template_ApiError`


---

### `POST` `/certificateAuthorities/{caId}/subCas/query`

**Search sub certificate authorities**

Searches for sub certificate authorities matching the search criteria.

operationId: `querySubCas`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_CaQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_CaFilters` |  | Filters to apply when querying certificate authorities. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificate Authorities → `Certificate_Template_CaQueryResponse`


---

### `POST` `/certificateAuthorities/{caId}/templates`

**Create template for CA**

Creates a new certificate template for a specific certificate authority.

operationId: `createTemplateWithOnboardCa`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Onboard Certificate Authority id |


**Request Body:** `Certificate_Template_CertificateTemplateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` | ✓ | The algorithm to use for certificates generated using this template. |
| `caType` | `string` | ✓ | Which CA signs the certificates from the template. |
| `certificateCount` | `integer` |  | The count of certificate generated from this template. |
| `certificateNames` | `array` |  | The names of certificate generated from this template. |
| `chromebook` | `Certificate_Template_ChromebookDto` |  | The configuration of the Chromebook. |
| `defaultAccess` | `boolean` |  | Default RADIUS access response will either be accepted or rejected. |
| `description` | `string` |  | The description identifier for this template. |
| `id` | `string` |  | The unique identifier for this template. |
| `identityGroupId` | `string` | ✓ | The identity group id associated with the template. |
| `keyLength` | `integer` | ✓ | The key length for certificates generated using this template. |
| `name` | `string` | ✓ | The name for the certificate template. |
| `networkCount` | `integer` |  | The count of network assigned to this template. |
| `onboard` | `Certificate_Template_OnboardDto` |  | The configuration of the onboard CA. |
| `policySetId` | `string` |  | The policy set that is assigned to this template. |
| `variables` | `array` |  | The variables for replacing the variables in the generated certificate. |


**Responses:**

- `202` Certificate Template created → `Certificate_Template_OperationResponse`
- `400` Invalid Certificate Template content → `Certificate_Template_ApiError`


---

### `POST` `/certificateAuthorities/{caId}/templates/query`

**Search templates for CA**

Searches for templates belonging to a specific certificate authority.

operationId: `queryTemplatesByCa`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `caId` | path | ✓ | `string` | Certificate Authority id |


**Request Body:** `Certificate_Template_CertTemplateQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_TemplateFilters` |  | Filters to apply when querying certificate templates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificate Templates → `Certificate_Template_CertTemplateQueryResponse`


---

### `GET` `/radiusProfiles/{radiusProfileId}/certificateAuthorities`

**Get CAs by RADIUS**

Retrieves certificate authorities associated with a RADIUS profile.

operationId: `getCAsByRadiusId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusProfileId` | path | ✓ | `string` | Radius id |
| `pageable` | query | ✓ | `Certificate_Template_Pageable` | parameters for paging |


**Responses:**

- `200` Certificate Authority → `Certificate_Template_CaDto`


---



## Certificate Template

*APIs for certificate template management.*


*22 endpoints*


### `POST` `/certificateTemplates/query`

**Search certificate templates**

Searches for certificate templates matching the search criteria.

operationId: `queryTemplates`


**Request Body:** `Certificate_Template_CertTemplateQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in the response. |
| `filters` | `Certificate_Template_TemplateFilters` |  | Filters to apply when querying certificate templates. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of items per page for pagination. |
| `searchString` | `string` |  | Search string to filter results. |
| `searchTargetFields` | `array` |  | List of field names to search within. |
| `sortField` | `string` |  | Field name to sort the results by. |
| `sortOrder` | `string` |  | Sort order direction (ASC or DESC). |


**Responses:**

- `200` Certificate Templates → `Certificate_Template_CertTemplateQueryResponse`


---

### `DELETE` `/certificateTemplates/{templateId}`

**Delete certificate template**

Deletes a certificate template.

operationId: `deleteTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}`

**Get certificate template by ID**

Retrieves a specific certificate template by ID.

operationId: `getTemplateById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |


**Responses:**

- `200` Certificate Template → `Certificate_Template_CertificateTemplateDto`
- `404` Certificate Template not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificateTemplates/{templateId}`

**Update certificate template**

Updates a certificate template.

operationId: `patchTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |


**Request Body:** `Certificate_Template_UpdateCertificateTemplateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` |  | The algorithm to use for certificates generated using this template. |
| `chromebook` | `Certificate_Template_ChromebookDto` |  | The configuration of the Chromebook. |
| `defaultAccess` | `boolean` |  | Default RADIUS access response will either be accepted or rejected. |
| `description` | `string` |  | The description identifier for this template. |
| `keyLength` | `integer` |  | The key length for certificates generated using this template. |
| `name` | `string` |  | The name for the certificate template. |
| `onboard` | `Certificate_Template_OnboardDto` |  | The configuration of the onboard CA. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}/msiPackages`

**Get template msi packages**

Retrieves all MSI packages for a certificate template.

operationId: `getMsiPackages`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `pageable` | query | ✓ | `Certificate_Template_Pageable` | Parameters for paging |


**Responses:**

- `200` MSI Packages → `Certificate_Template_Page`


---

### `POST` `/certificateTemplates/{templateId}/msiPackages`

**Create msi package**

Creates a microsoft software installer package for a certificate template.

operationId: `createMsiPackage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Certificate_Template_MsiPackageDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowedSubnets` | `string` |  | If populated, only the IP addresses or subnets specified are allowed to use this package. |
| `blockedSubnets` | `string` |  | If populated, the IP addresses or subnets specified are blocked from using this package. Blocked subnets override the allowed subnets. |
| `description` | `string` |  | Description of the package. |
| `enabled` | `boolean` |  | Indicates whether this package should be used. |
| `expirationDate` | `string` | ✓ | The expire date for this package. |
| `id` | `string` |  | The unique identifier for this configuration. |
| `name` | `string` |  | The unique reference name of the package. |
| `passphrase` | `string` |  | The passphrase for the package. |
| `productId` | `string` |  | The product ID for the package. |
| `productName` | `string` | ✓ | The product name for the package. |
| `profileType` | `string` | ✓ | The profile type for the package. |
| `usernameVariableSource` | `string` | ✓ | Determines where the variable (usable in the certificate template) is derived from. |


**Responses:**

- `202` MSI Package created → `Certificate_Template_OperationResponse`
- `400` Invalid MSI Package content → `Certificate_Template_ApiError`


---

### `DELETE` `/certificateTemplates/{templateId}/msiPackages/{msiPackageId}`

**Delete msi package**

Deletes an MSI package from a certificate template.

operationId: `deleteMsiPackage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `msiPackageId` | path | ✓ | `string` | MSI package id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}/msiPackages/{msiPackageId}`

**Get msi package by ID**

Retrieves a specific MSI package by ID.

operationId: `getMsiPackageById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `msiPackageId` | path | ✓ | `string` | MSI package id |


**Responses:**

- `200` MSI Package → `Certificate_Template_MsiPackageDto`
- `404` MSI Package not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificateTemplates/{templateId}/msiPackages/{msiPackageId}`

**Update msi package**

Updates an MSI package for a certificate template.

operationId: `patchMsiPackage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `msiPackageId` | path | ✓ | `string` | MSI Package id |


**Request Body:** `Certificate_Template_MsiPackageDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowedSubnets` | `string` |  | If populated, only the IP addresses or subnets specified are allowed to use this package. |
| `blockedSubnets` | `string` |  | If populated, the IP addresses or subnets specified are blocked from using this package. Blocked subnets override the allowed subnets. |
| `description` | `string` |  | Description of the package. |
| `enabled` | `boolean` |  | Indicates whether this package should be used. |
| `expirationDate` | `string` | ✓ | The expire date for this package. |
| `id` | `string` |  | The unique identifier for this configuration. |
| `name` | `string` |  | The unique reference name of the package. |
| `passphrase` | `string` |  | The passphrase for the package. |
| `productId` | `string` |  | The product ID for the package. |
| `productName` | `string` | ✓ | The product name for the package. |
| `profileType` | `string` | ✓ | The profile type for the package. |
| `usernameVariableSource` | `string` | ✓ | Determines where the variable (usable in the certificate template) is derived from. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}/notifications`

**Get template notifications**

Retrieves all notifications for a certificate template.

operationId: `getNotifications`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `pageable` | query | ✓ | `Certificate_Template_Pageable` | Parameters for paging |


**Responses:**

- `200` Notifications → `Certificate_Template_Page`


---

### `POST` `/certificateTemplates/{templateId}/notifications`

**Create notification for template**

Creates a notification for a certificate template.

operationId: `createNotification`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Certificate_Template_NotificationDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dateValue` | `string` |  | The number of hours/days/months/etc to be offset from the event date when calculating when to send the notification. |
| `email` | `string` |  | Indicates whether this package should be used. |
| `emailSubject` | `string` |  | The subject of the email to be sent for this notification. |
| `emailTemplate` | `string` |  | The message of the email to be sent for this notification. |
| `id` | `string` |  | The unique if the notification. |
| `notificationEvent` | `string` |  | The event upon which to base the sending of the notification. |
| `notificationMethod` | `string` |  | The method(s) to use to notify the user. |
| `notificationMethodData` | `string` |  | The data of to use to notify the user. |
| `smsSubject` | `string` |  | The subject of the SMS to be sent for this notification. |
| `smsTemplate` | `string` |  | The message of the email to be sent for this notification. |
| `staticDerivedDateType` | `string` |  | The basis for calculating the date to send the notification. |


**Responses:**

- `202` Notification created → `Certificate_Template_OperationResponse`
- `400` Invalid Notification content → `Certificate_Template_ApiError`


---

### `DELETE` `/certificateTemplates/{templateId}/notifications/{notificationId}`

**Delete notification**

Deletes a notification from a certificate template.

operationId: `deleteNotification`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `notificationId` | path | ✓ | `string` | Notification id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}/notifications/{notificationId}`

**Get notification by ID**

Retrieves a specific notification by ID.

operationId: `getNotificationById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `notificationId` | path | ✓ | `string` | Notification id |


**Responses:**

- `200` Notification → `Certificate_Template_NotificationDto`
- `404` Notification not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificateTemplates/{templateId}/notifications/{notificationId}`

**Update template notification**

Updates a notification for a certificate template.

operationId: `patchNotification`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `notificationId` | path | ✓ | `string` | Notification id |


**Request Body:** `Certificate_Template_NotificationDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dateValue` | `string` |  | The number of hours/days/months/etc to be offset from the event date when calculating when to send the notification. |
| `email` | `string` |  | Indicates whether this package should be used. |
| `emailSubject` | `string` |  | The subject of the email to be sent for this notification. |
| `emailTemplate` | `string` |  | The message of the email to be sent for this notification. |
| `id` | `string` |  | The unique if the notification. |
| `notificationEvent` | `string` |  | The event upon which to base the sending of the notification. |
| `notificationMethod` | `string` |  | The method(s) to use to notify the user. |
| `notificationMethodData` | `string` |  | The data of to use to notify the user. |
| `smsSubject` | `string` |  | The subject of the SMS to be sent for this notification. |
| `smsTemplate` | `string` |  | The message of the email to be sent for this notification. |
| `staticDerivedDateType` | `string` |  | The basis for calculating the date to send the notification. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `DELETE` `/certificateTemplates/{templateId}/policySets/{policySetId}`

**Remove template policy set**

Removes the policy set from a certificate template.

operationId: `certTempRemovePolicySetId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Template id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` The update request has been accepted and is in progress → `Certificate_Template_OperationResponse`


---

### `PUT` `/certificateTemplates/{templateId}/policySets/{policySetId}`

**Update template policy set**

Updates the policy set for a certificate template.

operationId: `certTempUpdatePolicySetId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Template id |
| `policySetId` | path | ✓ | `string` | Policy set id |


**Responses:**

- `202` The update request has been accepted and is in progress → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}/scepKeys`

**Get template scep keys**

Retrieves all SCEP keys for a certificate template.

operationId: `getScepKeys`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `pageable` | query | ✓ | `Certificate_Template_Pageable` | Parameters for paging |


**Responses:**

- `200` SCEP Keys → `Certificate_Template_Page`


---

### `POST` `/certificateTemplates/{templateId}/scepKeys`

**Create scep key**

Creates a simple certificate enrollment protocol key for a certificate template.

operationId: `createScepKey`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |


**Request Body:** `Certificate_Template_ScepKeyDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowedSubnets` | `string` |  | If populated, only the IPs or subnets specified will be allowed to utilize the simple certificate enrollment protocol server using this key. |
| `azureApplicationId` | `string` |  | The azure application client ID from the azure configuration portal. |
| `azureApplicationKey` | `string` |  | The azure application key and client secret configured in the azure configuration portal. |
| `blockedSubnets` | `string` |  | If populated, the IPs or subnets specified will be blocked from utilizing the simple certificate enrollment protocol server using this key. |
| `challengePassword` | `string` |  | If checked, the client will need to provide this password during the exchange. |
| `challengePasswordType` | `string` | ✓ | Optionally specify a challenge password which must be provided by the client during the simple certificate enrollment protocol key exchange. |
| `cnValue1` | `string` | ✓ | The certificate signing requests created as part of the simple certificate enrollment protocol interaction will contain one or more common name values. The system will treat the first common name as the type of value specified. |
| `cnValue2` | `string` | ✓ | The certificate signing requests created as part of the simple certificate enrollment protocol interaction will contain one or more common name values. The system will treat the second common name as the type of value specified. |
| `cnValue3` | `string` | ✓ | The certificate signing requests created as part of the simple certificate enrollment protocol interaction will contain one or more common name values. The system will treat the third common name as the type of value specified. |
| `description` | `string` |  | Description of the item for reference. |
| `enabled` | `boolean` |  | Indicates whether this key should be used. |
| `enrollmentUrl` | `string` |  | The URL for device enrollment. |
| `expirationDate` | `string` | ✓ | The expire date for the key. |
| `id` | `string` |  | The unique for this simple certificate enrollment protocol key. |
| `intuneTenantId` | `string` |  | The azure tenant ID from the azure configuration portal. |
| `name` | `string` | ✓ | The reference name of the item. |
| `overrideDays` | `integer` |  | If greater than 0, this overrides the expiration date in the certificate template for certificates generated using this key. |
| `scepKey` | `string` |  | The shared secret used as the key within the URL. |


**Responses:**

- `202` SCEP Key created → `Certificate_Template_OperationResponse`
- `400` Invalid SCEP Key content → `Certificate_Template_ApiError`


---

### `DELETE` `/certificateTemplates/{templateId}/scepKeys/{scepKeyId}`

**Delete scep key**

Deletes a SCEP key from a certificate template.

operationId: `deleteScepKey`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `scepKeyId` | path | ✓ | `string` | SCEP key id |


**Responses:**

- `202` The delete request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/certificateTemplates/{templateId}/scepKeys/{scepKeyId}`

**Get scep key by ID**

Retrieves a specific SCEP key by ID.

operationId: `getScepKeyById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `scepKeyId` | path | ✓ | `string` | SCEP key id |


**Responses:**

- `200` SCEP Key → `Certificate_Template_ScepKeyDto`
- `404` SCEP Key not found → `Certificate_Template_ApiError`


---

### `PATCH` `/certificateTemplates/{templateId}/scepKeys/{scepKeyId}`

**Update scep key**

Updates a SCEP key for a certificate template.

operationId: `patchScepKey`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` | Certificate template id |
| `scepKeyId` | path | ✓ | `string` | ScepKey Id |


**Request Body:** `Certificate_Template_ScepKeyDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowedSubnets` | `string` |  | If populated, only the IPs or subnets specified will be allowed to utilize the simple certificate enrollment protocol server using this key. |
| `azureApplicationId` | `string` |  | The azure application client ID from the azure configuration portal. |
| `azureApplicationKey` | `string` |  | The azure application key and client secret configured in the azure configuration portal. |
| `blockedSubnets` | `string` |  | If populated, the IPs or subnets specified will be blocked from utilizing the simple certificate enrollment protocol server using this key. |
| `challengePassword` | `string` |  | If checked, the client will need to provide this password during the exchange. |
| `challengePasswordType` | `string` | ✓ | Optionally specify a challenge password which must be provided by the client during the simple certificate enrollment protocol key exchange. |
| `cnValue1` | `string` | ✓ | The certificate signing requests created as part of the simple certificate enrollment protocol interaction will contain one or more common name values. The system will treat the first common name as the type of value specified. |
| `cnValue2` | `string` | ✓ | The certificate signing requests created as part of the simple certificate enrollment protocol interaction will contain one or more common name values. The system will treat the second common name as the type of value specified. |
| `cnValue3` | `string` | ✓ | The certificate signing requests created as part of the simple certificate enrollment protocol interaction will contain one or more common name values. The system will treat the third common name as the type of value specified. |
| `description` | `string` |  | Description of the item for reference. |
| `enabled` | `boolean` |  | Indicates whether this key should be used. |
| `enrollmentUrl` | `string` |  | The URL for device enrollment. |
| `expirationDate` | `string` | ✓ | The expire date for the key. |
| `id` | `string` |  | The unique for this simple certificate enrollment protocol key. |
| `intuneTenantId` | `string` |  | The azure tenant ID from the azure configuration portal. |
| `name` | `string` | ✓ | The reference name of the item. |
| `overrideDays` | `integer` |  | If greater than 0, this overrides the expiration date in the certificate template for certificates generated using this key. |
| `scepKey` | `string` |  | The shared secret used as the key within the URL. |


**Responses:**

- `202` The update request has been accepted and is in progress. → `Certificate_Template_OperationResponse`


---

### `GET` `/wifiNetworks/{networkId}/certificateTemplates`

**Get templates by network**

Retrieves certificate templates associated with a network.

operationId: `getTemplateByNetworkId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | Wifi network id |
| `pageable` | query | ✓ | `Certificate_Template_Pageable` | parameters for paging |


**Responses:**

- `200` Certificate Template → `Certificate_Template_CertificateTemplateDto`
- `404` Certificate Template not found → `Certificate_Template_ApiError`


---



## system-controller

*2 endpoints*


### `GET` `/systems/certificateAuthorities`

operationId: `queryDefaultCa`


**Responses:**

- `200` OK


---

### `POST` `/systems/certificates`

operationId: `generateCertByDefaultCa`


**Request Body:** `Certificate_Template_CertificateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `algorithm` | `Certificate_Template_AlgorithmEnum` | ✓ | SHA-256 - the SHA-2 hash using 256 bits. SHA-384 - the SHA-2 hash using 384 bits. SHA-512 - the SHA-2 hash using 512 bits. |
| `certificateAuthorityName` | `string` |  | The name of the certificate authority that issued this certificate. |
| `chain` | `string` |  | The chain of the certificate. |
| `commonName` | `string` |  | The common name of the certificate. |
| `country` | `string` |  | The country included in the certificate. |
| `createDate` | `string` |  | The date that creates the certificate. |
| `csrString` | `string` |  | The certificate signing request that should be signed by the CA. |
| `description` | `string` |  | The description of the certificate. |
| `details` | `string` |  | The details of the certificate. |
| `email` | `string` |  | The email of the certificate. |
| `extendedKeyUsages` | `array` |  | The extended key usage of the certificate. |
| `id` | `string` |  | The unique for this certificate. |
| `keyLength` | `integer` | ✓ | The length of the key. |
| `keyUsages` | `array` |  | The key usages of the certificate. |
| `locality` | `string` |  | The locality included in the certificate. |
| `name` | `string` | ✓ | The name of the certificate. |
| `notAfterDate` | `string` | ✓ | The expires date of the certificate. |
| `notBeforeDate` | `string` | ✓ | The start date of the certificate. |
| `organization` | `string` |  | The organization of the certificate. |
| `organizationUnit` | `string` |  | The organization unit of the certificate. |
| `privateKeyBase64` | `string` |  | The private key of the certificate. |
| `publicKeyBase64` | `string` |  | The public key of the certificate. |
| `revocationDate` | `string` |  | The date after which the certificate be revoked. |
| `revocationReason` | `string` |  | Reason for revocation of certificate. |
| `serialNumber` | `string` |  | The serial number of the certificate. |
| *… 4 more fields* | | | |


**Responses:**

- `200` OK


---


