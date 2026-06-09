# Workflow Actions

> RUCKUS One API Reference

---


## Enrollment Action API

*Manages enrollment actions for workflow configuration.*


*6 endpoints*


### `GET` `/enrollmentActions`

**Get All Enrollment Actions**

Gets all enrollment actions across action types.

operationId: `getAllEnrollmentActions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `integer` | Number of records in a page. Will be defaulted to 20 if not specified or found invalid. |
| `page` | query |  | `integer` | The page to retrieve (starts at zero). Will be defaulted to 0 if not specified or found invalid |
| `sort` | query |  | `string` | The field names to sort with. Comma separated from the sort order (asc or desc). Allowed values are name, description, actionType and version. |


**Responses:**

- `200` Ok → `Workflow_Actions_Page`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `POST` `/enrollmentActions`

**Create Enrollment Action**

Allows user to create various enrollment actions across action types.

operationId: `createEnrollmentActions`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Workflow_Actions_AcceptedResponse`
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `POST` `/enrollmentActions/query`

**Query Enrollment Actions**

Gets the list of enrollment actions using the specified query.

operationId: `queryEnrollmentActions`


**Request Body:** `Workflow_Actions_ActionQueryCriteria`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `actionType` | `string` |  | Type of enrollment action to filter by. |
| `description` | `string` |  | Action description. |
| `id` | `string` |  | Action id. |
| `name` | `string` |  | Action name. |
| `page` | `integer` |  | Page number. If not specified the first page will be returned. |
| `pageSize` | `integer` |  | Number of records in a page.If not specified default page size of 20 will be applied. |
| `parentActionId` | `string` |  | ID of the parent action for filtering. |
| `sortDirection` | `string` |  | Direction to sort results in ascending or descending order. |
| `sortFields` | `array` |  | List of field names to sort results by. |
| `version` | `string` |  | Version. |


**Responses:**

- `200` ok → `Workflow_Actions_Page`
- `400` Invalid query data supplied. → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `DELETE` `/enrollmentActions/{actionId}`

**Delete Specific Enrollment Actions**

Allows the user to delete enrollment action with the given id.

operationId: `deleteEnrollmentActions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `actionId` | path | ✓ | `string` | Action Id |


**Responses:**

- `202` Accepted → `Workflow_Actions_AcceptedResponse`
- `204` No Content → `Workflow_Actions_AcceptedResponse`
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `GET` `/enrollmentActions/{actionId}`

**Get Enrollment Action by Identifier**

Gets enrollment action configuration for the requested action identifier.

operationId: `getEnrollmentAction`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `actionId` | path | ✓ | `string` | Action Id |


**Responses:**

- `200` Ok → `Workflow_Actions_EntityModel`
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `404` Not found
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `PATCH` `/enrollmentActions/{actionId}`

**Selectively Updates Enrollment Actions**

Allows the user to selectively update enrollment actions.

operationId: `editEnrollmentActions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `actionId` | path | ✓ | `string` | Action Id |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Workflow_Actions_EntityModel`
- `204` No Content → `Workflow_Actions_EntityModelAcceptedResponse`
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---



## Enrollment Action Files API

*Manages enrollment action files.*


*3 endpoints*


### `POST` `/enrollmentActions/files`

**Upload File**

Allows user to upload file.

operationId: `uploadFile`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fileDetails` | `Workflow_Actions_FileUploadDto` | ✓ |  |
| `fileToUpload` | `string` | ✓ | File to be uploaded |


**Responses:**

- `200` Uploaded → `Workflow_Actions_FileUploadResponseDto`
- `201` Created → `Workflow_Actions_FileUploadResponseDto`
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `DELETE` `/enrollmentActions/files/{fileId}`

**Delete File**

Deletes the specified enrollment action file.

operationId: `DeleteFile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `204` No Content
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `404` Not found → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---

### `GET` `/enrollmentActions/files/{fileId}`

**Get Signed URL for Download**

Get signed URL for download.

operationId: `getSignedUrlForDownload`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `fileId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok → `Workflow_Actions_FileResponseDto`
- `400` Bad request → `Workflow_Actions_ErrorResource`
- `404` Not found → `Workflow_Actions_ErrorResource`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---



## Enrollment Action Type API

*Manages enrollment actions for specific action types.*


*1 endpoint*


### `GET` `/enrollmentActions/actionTypes/{actionType}`

**Get Enrollment Actions by Type**

Gets all enrollment action configurations for a specific action type.

operationId: `getAllEnrollmentActionByType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `integer` | Number of records in a page. Will be defaulted to 20 if not specified or found invalid. |
| `page` | query |  | `integer` | The page to retrieve (starts at zero). Will be defaulted to 0 if not specified or found invalid |
| `sort` | query |  | `string` | The field names to sort with. Comma separated from the sort order (asc or desc). |
| `actionType` | path | ✓ | `string` | Action Type |


**Responses:**

- `200` Ok → `Workflow_Actions_Page`
- `500` Internal server error → `Workflow_Actions_ErrorResource`


---


