# Workflow Device Enrollments

> RUCKUS One API Reference

---


## Admin Enrollment Registration API

*Manages enrollment registration admin views.*


*2 endpoints*


### `POST` `/enrollments/registrations/query`

**Query Enrollment Registrations**

Gets the list of enrollment registrations using the specified query.

operationId: `queryEnrollmentRegistrations`


**Request Body:** `Workflow_Device_Enrollments_EnrollmentQueryCriteria`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | Description of the enrollment. |
| `enrollmentId` | `string` |  | Identifier of the enrollment. |
| `ipAddress` | `string` |  | Network address of the enrolled device. |
| `macAddress` | `string` |  | Mac address of the enrolled device. |
| `page` | `integer` |  | Page number. If not specified the first page will be returned. |
| `pageSize` | `integer` |  | Number of records in a page.If not specified default page size of 20 will be applied. |
| `sortDirection` | `string` |  | Sort direction for ordering query results in ascending or descending order. |
| `sortFields` | `array` |  | List of field names used to sort the enrollment query results. |
| `status` | `string` |  | Enrollment status. |
| `workflowId` | `string` |  | Identifier of the workflow. |


**Responses:**

- `200` ok → `Workflow_Device_Enrollments_PageEntityModelEnrollmentRegistrationDto`
- `400` Invalid query data supplied. → `Workflow_Device_Enrollments_ErrorResource`
- `500` Internal server error → `Workflow_Device_Enrollments_ErrorResource`


---

### `GET` `/enrollments/registrations/{enrollmentRegistrationId}`

**Get Registration Details**

Gets enrollment registration details for the requested enrollment registration identifier.

operationId: `getEnrollmentRegistration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `enrollmentRegistrationId` | path | ✓ | `string` | Enrollment Registration Id |


**Responses:**

- `200` Ok → `Workflow_Device_Enrollments_EntityModelEnrollmentRegistrationDto`
- `400` Bad request → `Workflow_Device_Enrollments_ErrorResource`
- `404` Not found
- `500` Internal server error → `Workflow_Device_Enrollments_ErrorResource`


---



## Admin Enrollment API

*Manages enrollment admin views.*


*2 endpoints*


### `POST` `/enrollments/query`

**Query Enrollments**

Gets the list of enrollments using the specified query.

operationId: `queryEnrollments`


**Request Body:** `Workflow_Device_Enrollments_EnrollmentQueryCriteria`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | Description of the enrollment. |
| `enrollmentId` | `string` |  | Identifier of the enrollment. |
| `ipAddress` | `string` |  | Network address of the enrolled device. |
| `macAddress` | `string` |  | Mac address of the enrolled device. |
| `page` | `integer` |  | Page number. If not specified the first page will be returned. |
| `pageSize` | `integer` |  | Number of records in a page.If not specified default page size of 20 will be applied. |
| `sortDirection` | `string` |  | Sort direction for ordering query results in ascending or descending order. |
| `sortFields` | `array` |  | List of field names used to sort the enrollment query results. |
| `status` | `string` |  | Enrollment status. |
| `workflowId` | `string` |  | Identifier of the workflow. |


**Responses:**

- `200` ok → `Workflow_Device_Enrollments_PageEntityModelEnrollmentDto`
- `400` Invalid query data supplied. → `Workflow_Device_Enrollments_ErrorResource`
- `500` Internal server error → `Workflow_Device_Enrollments_ErrorResource`


---

### `GET` `/enrollments/{enrollmentId}`

**Get Enrollment Details**

Gets enrollment details for the requested enrollment identifier.

operationId: `getEnrollment`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `enrollmentId` | path | ✓ | `string` | Enrollment Id |


**Responses:**

- `200` Ok → `Workflow_Device_Enrollments_EntityModelEnrollmentDetailsDto`
- `400` Bad request → `Workflow_Device_Enrollments_ErrorResource`
- `404` Not found
- `500` Internal server error → `Workflow_Device_Enrollments_ErrorResource`


---


