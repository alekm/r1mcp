# Files

> RUCKUS One API Reference

---


## File

*Manage upload or download files.*


*3 endpoints*


### `POST` `/files/uploadurls`

**Get Upload URL**

Get a URL with which to upload a file.


RUCKUS cloud won't provide file service API for general purpose.

All required file upload or download functions will be provided by respective RUCKUS cloud services.

This method will be removed no sooner than 06/30/2026.

operationId: `getUploadUrl`


**Request Body:** `Files_UploadUrlRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fileExtension` | `string` |  | The file extension identifier. |


**Responses:**

- `200` Returns with the signed url → `Files_SignedUrlResponse`
- `400` Invalid id supplied.
- `401` Unauthorized
- `403` Forbidden
- `404` Not Found
- `422` Some of the provided query data is invalid.
- `500` Internal Server Error


---

### `GET` `/files/{fileId}`

**Get Download URL**

Get the URL from which to download this file.


RUCKUS cloud won't provide file service API for general purpose.

All required file upload or download functions will be provided by respective RUCKUS cloud services.

This method will be removed no sooner than 06/30/2026.

operationId: `getDownloadUrl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fileId` | path | ✓ | `string` |  |


**Responses:**

- `302` Returns: Redirect (302) with the file signed url in 'Location' header
- `400` Invalid id supplied.
- `401` Unauthorized
- `403` Forbidden
- `404` Not Found
- `422` Some of the provided query data is invalid.
- `500` Internal Server Error


---

### `GET` `/files/{fileId}/urls`

**Get File Download URL**

Get the URL from which to download this file.


RUCKUS cloud won't provide file service API for general purpose.

All required file upload or download functions will be provided by respective RUCKUS cloud services.

This method will be removed no sooner than 06/30/2026.

operationId: `getFileDownloadUrl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fileId` | path | ✓ | `string` |  |


**Responses:**

- `200` Returns with the signed url → `Files_SignedUrlResponse`
- `400` Invalid id supplied.
- `401` Unauthorized
- `403` Forbidden
- `404` Not Found
- `422` Some of the provided query data is invalid.
- `500` Internal Server Error


---


