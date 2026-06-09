# Radius Attribute Group

> RUCKUS One API Reference

---


## RADIUS Attribute Group Assignments

*Manages the external service assignments to the specified attribute group. Enables linking RADIUS attribute groups to external services and systems for distributed authentication and authorization across multiple platforms.*


*4 endpoints*


### `GET` `/radiusAttributeGroups/{groupId}/assignments`

**Get External Assignments**

Gets the external assignments for the specified RADIUS attribute group.

operationId: `getAllExternalAssignments`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `groupId` | path | ✓ | `string` | RADIUS Attribute Group id |


**Responses:**

- `200` RADIUS Attribute Group Assignments → `Radius_Attribute_Group_PageAttribute Group Assignment`
- `404`  RADIUS Attribute Group not found → `Radius_Attribute_Group_ErrorResource`


---

### `POST` `/radiusAttributeGroups/{groupId}/assignments`

**Create External Assignment**

Creates a new external service assignment linking the specified RADIUS attribute group to an external service. This enables the external service to reference and use the attribute group for authentication and authorization purposes.

operationId: `createExternalAssignment`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | RADIUS Attribute Group id |


**Request Body:** `Radius_Attribute_Group_Attribute Group Assignment`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Radius_Attribute_Group_Links` |  | Hypermedia links for HATEOAS navigation, including self reference and related resources. |
| `externalAssignmentIdentifier` | `string` | ✓ | The identifier for this external assignment and must be unique when combined with the service name. This identifier is used by the external service to reference the attribute group assignment. Format: alphanumeric string with optional hyphens and und |
| `id` | `string` |  | The unique identifier for this external assignment of an attribute group. |
| `serviceName` | `string` | ✓ | The name of the service that is using the attribute group. This identifies the target external system or application (e.g., 'wireless controller', 'VPN gateway', 'network access server', 'policy engine', 'authentication server'). Format: alphanumeric |


**Responses:**

- `201` Assignment created → `Radius_Attribute_Group_PageAttribute Group Assignment`
- `404`  RADIUS Attribute not found. → `Radius_Attribute_Group_ErrorResource`
- `409` Invalid assignment details provided. → `Radius_Attribute_Group_PageAttribute Group Assignment`


---

### `DELETE` `/radiusAttributeGroups/{groupId}/assignments/{assignmentId}`

**Delete External Assignment**

Delete the requested external assignment for this RADIUS attribute group.

operationId: `deleteExternalAssignment`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | RADIUS Attribute Group id |
| `assignmentId` | path | ✓ | `string` | RADIUS Attribute Group Assignment id |


**Responses:**

- `200` External Assignment to be deleted. → `Radius_Attribute_Group_EmptyResponse`
- `204` External Assignment to be deleted.
- `404`  Radius Attribute not found. → `Radius_Attribute_Group_ErrorResource`


---

### `GET` `/radiusAttributeGroups/{groupId}/assignments/{assignmentId}`

**Get External Assignment**

Gets the external assignment for the specified RADIUS attribute group.

operationId: `getExternalAssignmentByID`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | RADIUS Attribute Group id |
| `assignmentId` | path | ✓ | `string` | RADIUS Attribute Group Assignment id |


**Responses:**

- `200` RADIUS Attribute Group Assignment → `Radius_Attribute_Group_Attribute Group Assignment`
- `400` Invalid id supplied → `Radius_Attribute_Group_ErrorResource`
- `404`  RADIUS Attribute Group not found → `Radius_Attribute_Group_ErrorResource`


---



## RADIUS Attribute Group

*Comprehensive management of RADIUS attribute groups including creation, modification, deletion, and querying. Provides full read,create, update and delete operations for organizing RADIUS attributes into logical groups for network authentication and authorization.*


*6 endpoints*


### `GET` `/radiusAttributeGroups`

**Get RADIUS Attribute Groups**

Gets the complete list of RADIUS attribute group in a paged format.

operationId: `getAllRadiusAttributeGroups`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` Radius attribute groups paged. → `Radius_Attribute_Group_PageRADIUS Attribute Group`


---

### `POST` `/radiusAttributeGroups`

**Create RADIUS Attribute Group**

Creates a new RADIUS attribute group with the specified name, description, and attribute assignments. The group will be associated with the authenticated tenant and can be used for network authentication and authorization policies.

operationId: `createRadiusAttributeGroup`


**Request Body:** `Radius_Attribute_Group_RADIUS Attribute Group`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Radius_Attribute_Group_Links` |  | Hypermedia links for HATEOAS navigation, including self reference and related resources. |
| `attributeAssignments` | `array` | ✓ | The RADIUS attributes that are assigned to this group. |
| `attributeCount` | `integer` |  | The number of RADIUS attribute assignments within this attribute group. Allows sorting and filtering. |
| `description` | `string` |  | The description for this attribute group. |
| `externalAssignmentsCount` | `integer` |  | The total count of external service assignments for this attribute group across all services. Allows sorting and filtering. |
| `externalServiceAssignments` | `array` |  | The list of external service assignments grouped by service name, showing which services have assigned this attribute group and their associated external assignment identifiers. |
| `id` | `string` |  | The unique identifier for this attribute group. |
| `name` | `string` | ✓ | The name for this attribute group. |


**Responses:**

- `201` RADIUS attribute group created → `Radius_Attribute_Group_RADIUS Attribute Group Response`
- `409` Invalid RADIUS attribute group details provided. → `Radius_Attribute_Group_ErrorResource`


---

### `POST` `/radiusAttributeGroups/query`

**Get RADIUS Attribute Groups**

Gets the list of RADIUS attribute groups using the specified query.

operationId: `getAllRadiusAttributeGroupsByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Radius_Attribute_Group_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | A map of filter criteria to apply to the query results. Each key represents a field name to filter on, and the value is the filter condition. Supported filter formats depend on the resource type. Examples: {"name": "John Doe"} for exact match on attr |
| `page` | `integer` |  | The page number to return, indexed starting with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field name to use for sorting the results. Valid field names depend on the resource being queried. For RADIUS attributes, valid values include: id, name, vendorName, dataType, showOnDefault. For RADIUS attribute groups, valid values include: id,  |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` RADIUS attribute groups → `Radius_Attribute_Group_QueryResponseResource`
- `400` Invalid query data supplied. → `Radius_Attribute_Group_ErrorResource`


---

### `DELETE` `/radiusAttributeGroups/{groupId}`

**Delete RADIUS Attribute Group**

Deletes the requested RADIUS attribute group.

operationId: `deleteAttributeGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | RADIUS Attribute Group id |


**Responses:**

- `200` RADIUS attribute group deleted. → `Radius_Attribute_Group_EmptyResponse`
- `204` RADIUS attribute group deleted
- `404` RADIUS attribute group not found → `Radius_Attribute_Group_ErrorResource`
- `409` The requested RADIUS attribute group is still in use by another service. → `Radius_Attribute_Group_ErrorResource`


---

### `GET` `/radiusAttributeGroups/{groupId}`

**Get RADIUS Attribute Group**

Gets the requested RADIUS attribute group by the id.

operationId: `getAttributeGroupById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | RADIUS attribute group id |


**Responses:**

- `200` RADIUS attribute group → `Radius_Attribute_Group_RADIUS Attribute Group`
- `400` Invalid id supplied → `Radius_Attribute_Group_ErrorResource`
- `404`  RADIUS attribute group not found → `Radius_Attribute_Group_ErrorResource`


---

### `PATCH` `/radiusAttributeGroups/{groupId}`

**Update RADIUS Attribute Group**

Updates the properties of an existing RADIUS attribute group using PATCH semantics. Allows partial updates to the group name, description, and attribute assignments. All changes are validated before applying to ensure data integrity.

operationId: `updateRadiusAttribGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `groupId` | path | ✓ | `string` | RADIUS attribute group id |


**Request Body:** `Radius_Attribute_Group_RADIUS Attribute Group Update`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `attributeAssignments` | `array` |  | The RADIUS attributes that are assigned to this group. Must contain at least one attribute assignment. Maximum of 1000 assignments allowed. |
| `description` | `string` |  | The description for this attribute group. Maximum length is 1000 characters. |
| `name` | `string` |  | The name for this attribute group. Maximum length is 255 characters. |


**Responses:**

- `200` RADIUS attribute group → `Radius_Attribute_Group_RADIUS Attribute Group Response`
- `400` Invalid id or content supplied → `Radius_Attribute_Group_RADIUS Attribute Group Response`
- `404` RADIUS attribute group not found → `Radius_Attribute_Group_ErrorResource`


---



## RADIUS Attribute

*Browse and query the comprehensive catalog of supported RADIUS attributes. Provides read only access to standardized RADIUS parameters including vendor specific attributes, data types, and metadata for network authentication and authorization.*


*4 endpoints*


### `GET` `/radiusAttributes`

**Get RADIUS Attributes**

Gets the list of RADIUS attributes in a paged format.

operationId: `getAllRadiusAttribute`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` RADIUS Attributes in a paged format. → `Radius_Attribute_Group_PageRADIUS Attribute`


---

### `POST` `/radiusAttributes/query`

**Get RADIUS Attributes**

Gets the list of RADIUS attributes using the specified query. Paging is indexed starting at one.

operationId: `getAllRadiusAttributesByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Radius_Attribute_Group_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | A map of filter criteria to apply to the query results. Each key represents a field name to filter on, and the value is the filter condition. Supported filter formats depend on the resource type. Examples: {"name": "John Doe"} for exact match on attr |
| `page` | `integer` |  | The page number to return, indexed starting with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field name to use for sorting the results. Valid field names depend on the resource being queried. For RADIUS attributes, valid values include: id, name, vendorName, dataType, showOnDefault. For RADIUS attribute groups, valid values include: id,  |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List RADIUS attributes in a paged format. → `Radius_Attribute_Group_QueryResponseResource`
- `400` Invalid id supplied → `Radius_Attribute_Group_ErrorResource`


---

### `GET` `/radiusAttributes/vendors`

**Get RADIUS Attribute Vendors**

Gets the list of vendors that are supported in the RADIUS attributes.

operationId: `getAllRadiusAttributeVendors`


**Responses:**

- `200` RADIUS Attribute Vendors. → `Radius_Attribute_Group_RADIUS Attribute Vendors`


---

### `GET` `/radiusAttributes/{id}`

**Get RADIUS Attribute**

Gets the specific RADIUS attribute requested.

operationId: `getAttributeById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | path | ✓ | `integer` | Attribute unique identifier. |


**Responses:**

- `200` RADIUS Attribute → `Radius_Attribute_Group_RADIUS Attribute`
- `400` Invalid id supplied. → `Radius_Attribute_Group_ErrorResource`
- `404`  RADIUS Attribute not found. → `Radius_Attribute_Group_ErrorResource`


---


