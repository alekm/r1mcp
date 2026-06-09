# Venues

> RUCKUS One API Reference

---


## Venue Template

*Manage venue template instances and settings.*


*4 endpoints*


### `POST` `/templates/venues`

**Create Venue Template**

Create a new venue template.

operationId: `createVenueTemplate`


**Request Body:** `Venues_VenueTemplateView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `address` | `Venues_AddressView` | ✓ | Venue address and location information. |
| `description` | `string` |  | Venue description. |
| `id` | `string` |  | Venue identifier |
| `isEnforced` | `boolean` |  | Checked if its allowed to be updated. |
| `isTemplate` | `boolean` |  | Checked if its created as a template. |
| `name` | `string` | ✓ | Venue name. |
| `tags` | `array` |  | List of venue tags. |
| `templateContext` | `string` |  | Checked if its for MSP or MSP-EC. |
| `templateVersion` | `integer` |  | Version number of the venue template. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVenueView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueTemplateId}`

**Delete Venue Template by ID**

Delete venue template by ID.
Warning: note that all network devices under this venue Template will be removed as well.

operationId: `deleteVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVoid`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `GET` `/templates/venues/{venueTemplateId}`

**Get Venue Template by ID**

Get venue template by ID.

operationId: `getVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Venues_VenueTemplateView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}`

**Update Venue Template**

Update venue template by ID.

operationId: `updateVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` |  |


**Request Body:** `Venues_VenueTemplateView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `address` | `Venues_AddressView` | ✓ | Venue address and location information. |
| `description` | `string` |  | Venue description. |
| `id` | `string` |  | Venue identifier |
| `isEnforced` | `boolean` |  | Checked if its allowed to be updated. |
| `isTemplate` | `boolean` |  | Checked if its created as a template. |
| `name` | `string` | ✓ | Venue name. |
| `tags` | `array` |  | List of venue tags. |
| `templateContext` | `string` |  | Checked if its for MSP or MSP-EC. |
| `templateVersion` | `integer` |  | Version number of the venue template. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVenueView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---



## Venue

*Manage venue instances and settings.*


*7 endpoints*


### `DELETE` `/venues`

**Revoke Venues by IDs**

Delete venues by list.
Warning: note that all network devices under these venues will be removed as well.
This method will be removed no sooner than 06/30/2026.

operationId: `DeleteVenues`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Venues_OperationResponseVoid`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `GET` `/venues`

**Access Venues**

Get venue list.
This method will be removed no sooner than 06/30/2026.

operationId: `GetVenues`


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `POST` `/venues`

**Request Venue**

Create a new venue instance.

operationId: `CreateVenue`


**Request Body:** `Venues_VenueView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `address` | `Venues_AddressView` | ✓ | Venue address and location information. |
| `description` | `string` |  | Venue description. |
| `id` | `string` |  | Venue identifier |
| `isEnforced` | `boolean` |  | Checked if its allowed to be updated. |
| `isTemplate` | `boolean` |  | Checked if its created as a template. |
| `name` | `string` | ✓ | Venue name. |
| `tags` | `array` |  | List of venue tags. |
| `templateContext` | `string` |  | Checked if its for MSP or MSP-EC. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVenueView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `GET` `/venues/tags`

**Access Venue Tags**

Get list of venue tags.

operationId: `GetVenueTags`


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `DELETE` `/venues/{venueId}`

**Revoke Venue by ID**

Delete venues by ID.
Warning: note that all network devices under this venue will be removed as well.

operationId: `DeleteVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVoid`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `GET` `/venues/{venueId}`

**Access Venue by ID**

Get venue by ID.

operationId: `GetVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Venues_VenueView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `PUT` `/venues/{venueId}`

**Replace Venue**

Update venue by ID.

operationId: `UpdateVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Venues_VenueView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `address` | `Venues_AddressView` | ✓ | Venue address and location information. |
| `description` | `string` |  | Venue description. |
| `id` | `string` |  | Venue identifier |
| `isEnforced` | `boolean` |  | Checked if its allowed to be updated. |
| `isTemplate` | `boolean` |  | Checked if its created as a template. |
| `name` | `string` | ✓ | Venue name. |
| `tags` | `array` |  | List of venue tags. |
| `templateContext` | `string` |  | Checked if its for MSP or MSP-EC. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVenueView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---



## Floor Plan

*Manage venue floor plans.*


*9 endpoints*


### `GET` `/venues/{venueId}/floorplans`

**Access Floor Plans**

Get floor plans by a venue ID.

operationId: `GetVenueFloorPlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `POST` `/venues/{venueId}/floorplans`

**Request Floor Plan**

Create a new floor plan.

operationId: `createVenueFloorPlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Venues_FloorPlanView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `floorNumber` | `integer` | ✓ | Floor number of the plan. |
| `id` | `string` |  | Floor plan identifier. |
| `imageId` | `string` | ✓ | Identifier of the floor plan image. |
| `imageName` | `string` | ✓ | Display name of the image. |
| `name` | `string` | ✓ | Floor plan name. |
| `scales` | `array` |  | List of floor plan scale entries. |
| `venueId` | `string` |  | Identifier of the venue. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseFloorPlanView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `POST` `/venues/{venueId}/floorplans/query`

**Query Floor Plans**

Get floor plans by query criteria.

operationId: `QueryVenueFloorPlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Venues_FloorPlanQuery`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | Filter multiple target fields. |
| `page` | `integer` |  | Page number which start with 1. |
| `pageSize` | `integer` |  | How many items within a page. |
| `searchString` | `string` |  | Search string for query filter. |
| `searchTargetFields` | `array` |  | Fields to apply search against. |
| `sortField` | `string` |  | The field on which the response data should be sorted. |
| `sortOrder` | `string` |  | The sort order, this is either ascending or descending. |


**Responses:**

- `200` OK → `Venues_PageListFloorPlanView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/floorplans/{floorPlanId}`

**Revoke Floor Plan**

Delete floor plan by ID.

operationId: `DeleteVenueFloorPlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `floorPlanId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Venues_OperationResponseVoid`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `GET` `/venues/{venueId}/floorplans/{floorPlanId}`

**Access Floor Plan**

Get floor plan by ID.

operationId: `GetVenueFloorPlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `floorPlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Venues_FloorPlanView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `PUT` `/venues/{venueId}/floorplans/{floorPlanId}`

**Replace Floor Plan**

Update floor plan by ID.

operationId: `UpdateVenueFloorPlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `floorPlanId` | path | ✓ | `string` |  |


**Request Body:** `Venues_FloorPlanView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `floorNumber` | `integer` | ✓ | Floor number of the plan. |
| `id` | `string` |  | Floor plan identifier. |
| `imageId` | `string` | ✓ | Identifier of the floor plan image. |
| `imageName` | `string` | ✓ | Display name of the image. |
| `name` | `string` | ✓ | Floor plan name. |
| `scales` | `array` |  | List of floor plan scale entries. |
| `venueId` | `string` |  | Identifier of the venue. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseFloorPlanView`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `PUT` `/venues/{venueId}/floorplans/{floorPlanId}/scales`

**Replace Floor Plan Scale**

Update floor plan scales.

operationId: `setScale`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `floorPlanId` | path | ✓ | `string` |  |


**Request Body:** `Venues_FloorPlanScales`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `scales` | `array` |  | List of floor plan scale definitions. |


**Responses:**

- `202` Accepted → `Venues_OperationResponseFloorPlanScales`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `POST` `/venues/{venueId}/signurls/uploadurls`

**Access Image Upload URL**

Get a URL where to upload a floor plan image.

operationId: `GetFloorPlanImageUploadUrl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Venues_UploadUrlRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fileExtension` | `string` |  | File extension for the upload. |


**Responses:**

- `200` OK → `Venues_SignedUrlResponse`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---

### `GET` `/venues/{venueId}/signurls/{fileId}/urls`

**Access Image Download URL**

Get the URL where to download a floor plan image.

operationId: `GetFloorPlanImageDownloadUrl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `fileId` | path | ✓ | `string` |  |


**Responses:**

- `200` Returns with the signed url → `Venues_SignedUrlResponse`
- `400` Bad/malformed request → `Venues_ErrorResponse`
- `401` Not authorized → `Venues_ErrorResponse`
- `403` Forbidden → `Venues_ErrorResponse`
- `404` Requested resource or related entity not found → `Venues_ErrorResponse`
- `422` Validation error → `Venues_ErrorResponse`
- `500` Internal Server Error → `Venues_ErrorResponse`


---


