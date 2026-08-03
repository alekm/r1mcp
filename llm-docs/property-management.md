# Property Management

> RUCKUS One API Reference

---


## Units Identity API

*Manages linked identities for a unit.*


*3 endpoints*


### `POST` `/venues/{venueId}/units/identities/query`

**Query Unit Identities**

Gets the list of identities using the specified query.

operationId: `queryIdentities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` | Indicates that the content should be excluded from the query and only count and size data returned. |
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Property_Management_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in results. |
| `filters` | `object` |  | Filter criteria specified as name and value pairs. |
| `keyword` | `string` |  | Search keyword for filtering results. |
| `page` | `integer` | ✓ | Page number to retrieve starting from one. |
| `pageSize` | `integer` | ✓ | Number of items to include per page. |
| `sortField` | `string` |  | Field name to use for sorting results. |
| `sortOrder` | `string` | ✓ | Sort direction: ASC for ascending or DESC for descending. |


**Responses:**

- `200` Identities for venue. → `Property_Management_PageEntityModelPersona`
- `400` Invalid query data supplied. → `Property_Management_ErrorResource`


---

### `DELETE` `/venues/{venueId}/units/{unitId}/identities/{identityId}`

**Delete Unit Identity **

Allows the user to delete associated identity of the unit.

operationId: `deleteIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `unitId` | path | ✓ | `string` | Unit Id |
| `identityId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `PUT` `/venues/{venueId}/units/{unitId}/identities/{identityId}`

**Associate Identity to Unit**

Allows the user to associate identities on the specified unit.

operationId: `associateIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `unitId` | path | ✓ | `string` |  |
| `identityId` | path | ✓ | `string` |  |


**Responses:**

- `200` Ok → `Property_Management_Persona`
- `400` Bad request → `Property_Management_Persona`
- `409` Conflict - The unit trying to add already exists → `Property_Management_Persona`
- `500` Internal server error → `Property_Management_Persona`


---



## Units API

*Manages units for a venue.*


*8 endpoints*


### `DELETE` `/venues/{venueId}/units`

**Delete Units for Venue**

Allows the user to delete units with the given ids. This method will be removed no sooner than 08/31/2026. The following URL DELETE /venues/{venueId}/units/{unitId} can be used for this content.

operationId: `deleteUnits`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |


**Request Body:** Yes


**Responses:**

- `200` Ok → `Property_Management_AcceptedResponse`
- `202` Accepted → `Property_Management_AcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `GET` `/venues/{venueId}/units`

**Gets Units for Venue**

Gets the list of units paged.

operationId: `getAllUnits`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `size` | query |  | `integer` | Page size |
| `page` | query |  | `integer` | The page to retrieve (starts at one). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` Units for venue. → `Property_Management_Page`
- `400` Invalid input supplied. → `Property_Management_ErrorResource`


---

### `POST` `/venues/{venueId}/units`

**Adds Unit to Venue**

Allows the user to add a unit on the specified venue.

operationId: `addUnit`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `bulk` | query | ✓ | `boolean` | Flag to indicate bulk operation |
| `venueId` | query |  | `string` | Venue Id |
| `category` | query |  | `string` | Category applied to every imported unit. |


**Request Body:** `Property_Management_Unit`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPoint` | `Property_Management_UnitAp` |  | Access point configuration for the unit. |
| `category` | `string` |  | Category of the unit. |
| `dpsks` | `array` |  | List of DPSK passphrase configurations. |
| `guestPersonaId` | `string` |  | Unique identifier of the guest persona. |
| `id` | `string` |  | Unique identifier of the unit. |
| `identityCount` | `integer` |  | Count of identities associated with the unit. |
| `name` | `string` | ✓ | Unit name. |
| `personaId` | `string` |  | Unique identifier of the unit persona. |
| `pmsUnitId` | `string` |  | Property management system unit identifier. |
| `resident` | `Property_Management_Resident` | ✓ | Contact details of the unit resident. |
| `status` | `string` |  | Unit status. |
| `trafficControl` | `Property_Management_TrafficControl` |  | Traffic control and QoS profile details. |
| `type` | `string` |  | Unit type. |


**Responses:**

- `200` OK → `Property_Management_BulkUnitsResponse`
- `202` Accepted → `Property_Management_EntityModelAcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `409` Conflict - The unit trying to add already exists. → `Property_Management_ErrorResource`
- `422` Unable to process the file → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `POST` `/venues/{venueId}/units/notifications`

**Gets Notifications for Units**

Allows the user to resend notifications for units with the given ids.

operationId: `resendNotifications`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |


**Request Body:** Yes


**Responses:**

- `200` Notifications sent successfully.
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `POST` `/venues/{venueId}/units/query`

**Query Units for Venue**

Gets the list of units using the specified query.

operationId: `queryUnits`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `excludeContent` | query |  | `boolean` | Indicates that the content should be excluded from the query and only count and size data returned. |


**Request Body:** `Property_Management_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in results. |
| `filters` | `object` |  | Filter criteria specified as name and value pairs. |
| `keyword` | `string` |  | Search keyword for filtering results. |
| `page` | `integer` | ✓ | Page number to retrieve starting from one. |
| `pageSize` | `integer` | ✓ | Number of items to include per page. |
| `sortField` | `string` |  | Field name to use for sorting results. |
| `sortOrder` | `string` | ✓ | Sort direction: ASC for ascending or DESC for descending. |


**Responses:**

- `200` Units for venue. → `Property_Management_PageEntityModelUnit`
- `400` Invalid query data supplied. → `Property_Management_ErrorResource`


---

### `DELETE` `/venues/{venueId}/units/{unitId}`

**Delete Unit for Venue**

Allows the user to delete a unit with the given id.

operationId: `deleteUnit`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `unitId` | path | ✓ | `string` | Unit Id |


**Responses:**

- `200` Ok → `Property_Management_AcceptedResponse`
- `202` Accepted → `Property_Management_AcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `GET` `/venues/{venueId}/units/{unitId}`

**Gets Unit for Venue**

Allows the user to get a unit with the given id.

operationId: `fetchUnit`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `unitId` | path | ✓ | `string` | Unit Id |


**Responses:**

- `200` Ok → `Property_Management_EntityModelUnit`
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `PATCH` `/venues/{venueId}/units/{unitId}`

**Selectively Updates Unit Configurations**

Allows the user to selectively update unit configurations on the specified venue.

operationId: `editUnit`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `unitId` | path | ✓ | `string` | Unit Id |


**Request Body:** `Property_Management_Unit`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPoint` | `Property_Management_UnitAp` |  | Access point configuration for the unit. |
| `category` | `string` |  | Category of the unit. |
| `dpsks` | `array` |  | List of DPSK passphrase configurations. |
| `guestPersonaId` | `string` |  | Unique identifier of the guest persona. |
| `id` | `string` |  | Unique identifier of the unit. |
| `identityCount` | `integer` |  | Count of identities associated with the unit. |
| `name` | `string` | ✓ | Unit name. |
| `personaId` | `string` |  | Unique identifier of the unit persona. |
| `pmsUnitId` | `string` |  | Property management system unit identifier. |
| `resident` | `Property_Management_Resident` | ✓ | Contact details of the unit resident. |
| `status` | `string` |  | Unit status. |
| `trafficControl` | `Property_Management_TrafficControl` |  | Traffic control and QoS profile details. |
| `type` | `string` |  | Unit type. |


**Responses:**

- `200` Unit configuration updated → `Property_Management_EntityModelAcceptedResponse`
- `202` Accepted → `Property_Management_EntityModelAcceptedResponse`
- `400` Missing or invalid request body → `Property_Management_ErrorResource`
- `404` Unit configuration not found for the given venue id → `Property_Management_ErrorResource`
- `500` Internal error → `Property_Management_ErrorResource`


---



## Property Configuration

*Manages property configuration for venue.*


*6 endpoints*


### `GET` `/venues/propertyConfigs`

**Gets Property Configurations**

Gets the list of property configurations paged. This method will be removed no sooner than 08/31/2026. The following URL POST /venues/propertyConfigs/query can be used for this content.

operationId: `getAllPropertyConfigs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `integer` | Page size |
| `page` | query |  | `integer` | The page to retrieve (starts at one). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` Property configurations. → `Property_Management_PageEntityModelPropertyDto`
- `400` Invalid input supplied. → `Property_Management_ErrorResource`


---

### `POST` `/venues/propertyConfigs/query`

**Query Property Configurations**

Gets the list of property configurations using the specified query.

operationId: `queryPropertyConfigs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` | Indicates that the content should be excluded from the query and only count and size data returned. |


**Request Body:** `Property_Management_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in results. |
| `filters` | `object` |  | Filter criteria specified as name and value pairs. |
| `keyword` | `string` |  | Search keyword for filtering results. |
| `page` | `integer` | ✓ | Page number to retrieve starting from one. |
| `pageSize` | `integer` | ✓ | Number of items to include per page. |
| `sortField` | `string` |  | Field name to use for sorting results. |
| `sortOrder` | `string` | ✓ | Sort direction: ASC for ascending or DESC for descending. |


**Responses:**

- `200` Collection of property configurations. → `Property_Management_Page`
- `400` Invalid query data supplied. → `Property_Management_ErrorResource`


---

### `GET` `/venues/{venueId}/propertyConfigs`

**Get Property Configuration**

Gets property configuration for the requested venue.

operationId: `getProperty`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |


**Responses:**

- `200` Ok → `Property_Management_EntityModelPropertyDto`
- `400` Bad request → `Property_Management_ErrorResource`
- `404` Not found → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `PATCH` `/venues/{venueId}/propertyConfigs`

**Selectively Update Property Configuration**

Allows the user to selectively update property management configuration on the specified venue.

operationId: `enablePropertySelectively`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |


**Request Body:** `Property_Management_PropertyDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `address` | `Property_Management_Address` |  | Physical address of the venue. |
| `communicationConfig` | `Property_Management_CommunicationConfigDto` |  | Configuration for communicating unit change events. |
| `description` | `string` |  |  |
| `personaGroupId` | `string` | ✓ | Identifier of the associated persona group. |
| `pmsId` | `string` |  | Property management system identifier. |
| `pmsPropertyId` | `string` |  | Identifier for the property in the associated property management system. |
| `residentPortalId` | `string` |  | Identifier of the assigned resident portal. |
| `status` | `string` | ✓ | Status of the property |
| `unitConfig` | `Property_Management_UnitConfigDto` |  | Basic configuration on property units. |
| `venue` | `object` | ✓ | Property venue details and address. |
| `venueId` | `string` |  | Unique identifier of the venue. |
| `venueName` | `string` | ✓ | Display name for the venue. |


**Responses:**

- `202` Accepted → `Property_Management_EntityModelAcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `404` Property configuration not found for the given venue id → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `PUT` `/venues/{venueId}/propertyConfigs`

**Update Property Configuration**

Allows the user to enable or disable property management configuration on the specified venue.

operationId: `enableProperty`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |


**Request Body:** `Property_Management_PropertyUpdateDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `address` | `Property_Management_Address` |  | Physical address of the venue. |
| `communicationConfig` | `Property_Management_CommunicationConfigDto` |  | Configuration for communicating unit change events. |
| `description` | `string` |  |  |
| `personaGroupId` | `string` | ✓ | Identifier of the associated persona group. |
| `pmsId` | `string` |  | Property management system identifier. |
| `pmsPropertyId` | `string` |  | Identifier for the property in the associated property management system. |
| `residentPortalId` | `string` |  | Identifier of the assigned resident portal. |
| `retainPmsUnits` | `boolean` |  | Whether to retain PMS units on changing or removing associated PMS. |
| `status` | `string` | ✓ | Status of the property |
| `unitConfig` | `Property_Management_UnitConfigDto` |  | Basic configuration on property units. |
| `venue` | `object` | ✓ | Property venue details and address. |
| `venueId` | `string` |  | Unique identifier of the venue. |
| `venueName` | `string` | ✓ | Display name for the venue. |


**Responses:**

- `202` Accepted → `Property_Management_EntityModelAcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `404` Property configuration not found for the given venue id → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `PUT` `/venues/{venueId}/propertyConfigs/residentPortalAssignments/{residentPortalId}`

**Update Resident Portal Assignment**

Allows the user to assign resident portal for the specified venue.

operationId: `assignResidentPortal`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue Id |
| `residentPortalId` | path | ✓ | `string` | Resident PortalId Id |


**Responses:**

- `200` Ok → `Property_Management_PropertyResidentPortalAssignment`
- `400` Bad request → `Property_Management_ErrorResource`
- `404` Property configuration not found for the given venue id → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---



## QoS Profile Assignment API

*Manages QoS profile assignments.*


*1 endpoint*


### `PUT` `/venues/{venueId}/units/qosProfileAssignments/{qosProfileId}`

**Update QoS Profile Assignment**

Allows the user to update QoS profile assignments.

operationId: `qosProfileAssignments`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `qosProfileId` | path | ✓ | `string` |  |


**Request Body:** `Property_Management_QoSProfileAssignment`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `profileExpiry` | `string` | ✓ | Expiration date and time for the metering profile. |
| `unitIds` | `array` | ✓ | List of unit identifiers to assign the QoS profile to. |


**Responses:**

- `202` Accepted → `Property_Management_AcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---



## Resident Portals

*Manages, creates and gets configuration of resident portals for a tenant.*


*9 endpoints*


### `DELETE` `/residentPortals`

**Delete Resident Portals**

Allows the user to delete resident portals with the given ids. This method will be removed no sooner than 08/31/2026. The following URL DELETE /residentPortals/{portalId} can be used for this content.

operationId: `deleteResidentPortals`


**Request Body:** Yes


**Responses:**

- `200` Ok
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `GET` `/residentPortals`

**Get Resident Portals**

Gets the list of resident portals paged. This method will be removed no sooner than 08/31/2026. The following URL POST /residentPortals/query can be used for this content.

operationId: `getAllPortals`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `integer` | Page size |
| `page` | query |  | `integer` | The page to retrieve (starts at one). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` Resident portal details. → `Property_Management_PageEntityModelResidentPortal`
- `400` Invalid input supplied. → `Property_Management_ErrorResource`


---

### `POST` `/residentPortals`

**Adds Resident Portal**

Allows the user to add a resident portal.

operationId: `addResidentPortal`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `favIcon` | `string` |  | Portal fav icon image |
| `logo` | `string` |  | Portal logo image |
| `portal` | `Property_Management_ResidentPortal` | ✓ |  |


**Responses:**

- `201` Created → `Property_Management_EntityModelAcceptedResponse`
- `400` Bad request → `Property_Management_ErrorResource`
- `409` Conflict - The resident portal trying to add already exists → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `POST` `/residentPortals/query`

**Query Resident Portals**

Gets the list of resident portals using the specified query.

operationId: `queryResidentPortals`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` | Indicates that the content should be excluded from the query and only count and size data returned. |


**Request Body:** `Property_Management_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | List of field names to include in results. |
| `filters` | `object` |  | Filter criteria specified as name and value pairs. |
| `keyword` | `string` |  | Search keyword for filtering results. |
| `page` | `integer` | ✓ | Page number to retrieve starting from one. |
| `pageSize` | `integer` | ✓ | Number of items to include per page. |
| `sortField` | `string` |  | Field name to use for sorting results. |
| `sortOrder` | `string` | ✓ | Sort direction: ASC for ascending or DESC for descending. |


**Responses:**

- `200` Resident portal details. → `Property_Management_PageEntityModelResidentPortal`
- `400` Invalid query data supplied. → `Property_Management_ErrorResource`


---

### `DELETE` `/residentPortals/{portalId}`

**Delete Resident Portal**

Allows the user to delete a resident portal with the given id.

operationId: `deleteResidentPortal`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalId` | path | ✓ | `string` | Resident Portal Id |


**Responses:**

- `200` Ok
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `GET` `/residentPortals/{portalId}`

**Gets Resident Portal**

Allows the user to get a resident portal with the given id.

operationId: `fetchResidentPortal`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalId` | path | ✓ | `string` | Resident Portal Id |


**Responses:**

- `200` Ok → `Property_Management_EntityModelResidentPortal`
- `400` Bad request → `Property_Management_ErrorResource`
- `404` Not found → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `PATCH` `/residentPortals/{portalId}`

**Updates Resident Portal Configurations**

Allows the user to selectively update resident portal configurations.

operationId: `editResidentPortal`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalId` | path | ✓ | `string` | Resident Portal Id |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `changes` | `Property_Management_ResidentPortal` |  | A map contains the keys and values to be updated for the resident portal resource. Minimum one and maximum twenty keys can be present in the map. |
| `favIcon` | `string` |  | Portal fav icon image |
| `logo` | `string` |  | Portal logo image |


**Responses:**

- `200` Resident portal configuration updated → `Property_Management_EntityModelResidentPortal`
- `400` Missing or invalid request body → `Property_Management_ErrorResource`
- `404` Resident portal configuration not found for the given id → `Property_Management_ErrorResource`
- `500` Internal error → `Property_Management_ErrorResource`


---

### `DELETE` `/residentPortals/{portalId}/files/{type}`

**Deletes Resident Portal File**

Allows the user to delete a resident portal file with the given id.

operationId: `deletePortalFile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalId` | path | ✓ | `string` | Resident Portal Id |
| `type` | path | ✓ | `string` | Resident Portal file type |


**Responses:**

- `200` Ok
- `400` Bad request → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---

### `GET` `/residentPortals/{portalId}/files/{type}`

**Gets Resident Portal File**

Allows the user to get a resident portal file with the given id.

operationId: `downloadPortalFile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `portalId` | path | ✓ | `string` | Resident Portal Id |
| `type` | path | ✓ | `string` | Resident Portal file type |


**Responses:**

- `200` Ok
- `400` Bad request → `Property_Management_ErrorResource`
- `404` Not found → `Property_Management_ErrorResource`
- `500` Internal server error → `Property_Management_ErrorResource`


---


