# Adaptive Policy Management

> RUCKUS One API Reference

---


## Policy Conditions

*Manage the conditions that are applied on the specified policy.*


*5 endpoints*


### `GET` `/policyTemplates/{templateId}/policies/{policyId}/conditions`

**Get Conditions**

Retrieves the list of conditions for the policy.

operationId: `getAllConditionForPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `templateId` | path | ✓ | `integer` | Template identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |


**Responses:**

- `200` Success → `Adaptive_Policy_Management_PagedResponseResourcePolicy Condition`
- `404`  Not Found → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policyTemplates/{templateId}/policies/{policyId}/conditions`

**Create Condition**

Creates a condition and applies it to the policy.

operationId: `createPolicyCondition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` | Policy Template identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |


**Request Body:** `Adaptive_Policy_Management_Policy Condition`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Adaptive_Policy_Management_Links` |  |  |
| `evaluationRule` | `Adaptive_Policy_Management_Evaluation Criteria` |  | The evaluation criteria for this condition. Must match the attribute type selected. |
| `id` | `string` |  | The identifier for this policy condition. |
| `policyId` | `string` | ✓ | The identifier of the policy to assign this condition. |
| `templateAttribute` | `Adaptive_Policy_Management_Dynamic Policy Template Attribute` |  | The complete template attribute to associate with this condition. This is provided when getting the resource only, and will not be evaluated on POST or PATCH. |
| `templateAttributeId` | `integer` | ✓ | The identifier for the template attribute to associate with this condition. |


**Responses:**

- `201` Condition created → `Adaptive_Policy_Management_Policy Condition`
- `404` Not Found → `Adaptive_Policy_Management_ErrorResource`
- `409` Condition type is already mapped. → `Adaptive_Policy_Management_ErrorResource`


---

### `DELETE` `/policyTemplates/{templateId}/policies/{policyId}/conditions/{conditionId}`

**Delete Conditions**

Deletes the condition from the specified policy, but only if at least one condition still exists.

operationId: `deletePolicyConditions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` | Policy Template identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |
| `conditionId` | path | ✓ | `string` | Condition identifier. |


**Responses:**

- `200` Condition deleted successfully. → `Adaptive_Policy_Management_EmptyResponse`
- `204` Condition deleted, no content.
- `404` Policy or template not found → `Adaptive_Policy_Management_ErrorResource`
- `409` Policy will not have any conditions if this is deleted. → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policyTemplates/{templateId}/policies/{policyId}/conditions/{conditionId}`

**Get Condition**

Retrieves the requested condition for the policy.

operationId: `getConditionById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` | Template identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |
| `conditionId` | path | ✓ | `string` | Condition identifier. |


**Responses:**

- `200` Success → `Adaptive_Policy_Management_Policy Condition`
- `404`  Not Found. → `Adaptive_Policy_Management_ErrorResource`


---

### `PATCH` `/policyTemplates/{templateId}/policies/{policyId}/conditions/{conditionId}`

**Update Policy Condition**

Updates the policy condition from the requested values.

operationId: `updateCondition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `policyId` | path | ✓ | `string` |  |
| `conditionId` | path | ✓ | `string` |  |


**Request Body:** `Adaptive_Policy_Management_Policy Condition Update`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `evaluationRule` | `Adaptive_Policy_Management_Evaluation Criteria` |  | The evaluation criteria for this condition. Must match the attribute type selected. |
| `templateAttributeId` | `integer` |  | The complete template attribute to associate with this condition. |


**Responses:**

- `200` Policy condition updated → `Adaptive_Policy_Management_Policy Condition`
- `409` Invalid policy condition details provided. → `Adaptive_Policy_Management_Policy Condition`


---



## Policies

*Manages the creation and retrieval of policies assigned to a specific template.*


*6 endpoints*


### `GET` `/policyTemplates/{templateId}/policies`

**Get Policies for Template**

Gets the list of policies that are based off of this template.

operationId: `getAllPoliciesUnderTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve, paging starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `templateId` | path | ✓ | `integer` |  |
| `pageable` | query | ✓ | `Adaptive_Policy_Management_Pageable` |  |


**Responses:**

- `200` Policies in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePolicy`
- `400` Invalid id supplied. → `Adaptive_Policy_Management_ErrorResource`
- `404` Not Found → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policyTemplates/{templateId}/policies`

**Create Policy**

Creates a policy from the requested values, and based on the specified parent. If the content type of "application/ruckus.one.v1-synchronous+json" is provided, then the method will be synchronous, and will return only once it has correctly associated with the requested radius attribute group. Otherwise it is asynchronous, and must be looked up by id to be complete.

operationId: `createPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |


**Request Body:** `Adaptive_Policy_Management_Policy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Adaptive_Policy_Management_Links` |  |  |
| `conditionsCount` | `integer` |  | The number of conditions that are used when evaluating this policy. |
| `description` | `string` |  | The policy description. |
| `id` | `string` |  | The identifier for this dynamic policy. |
| `name` | `string` | ✓ | The name of the policy. |
| `onMatchResponse` | `string` |  | The response details if the policy is matched. For policy types which are RADIUS and DPSK, this is expected to be the identifier of a valid RADIUS attribute group. |
| `policySetCount` | `integer` |  | The number of policy sets that this policy is assigned to. |
| `policySetNames` | `array` |  | The names of the policy sets that this policy is currently assigned to. |
| `policyType` | `string` | ✓ | The data type for this attribute text. EX:  it identifies which type of value the test data will be. This cannot be changed, and will be matched with the policy template for this policy type. It cannot be changed. |


**Responses:**

- `201` Created → `Adaptive_Policy_Management_Policy`
- `202` Accepted → `Adaptive_Policy_Management_Policy`
- `409` Invalid policy details provided. → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policyTemplates/{templateId}/policies/query`

**Query Policies for Template**

Returns a paginated list of policies that are based on the specified template. This endpoint accepts query criteria in the request body to filter and search policies by various attributes such as name, description, policy type, and other defined fields. The query supports complex filtering, sorting, and pagination. An optional excludeContent parameter can be used to retrieve only the total count of matching policies without the full policy details.

operationId: `getAllPoliciesForTemplateByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Adaptive_Policy_Management_Query Data`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List Policy in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePolicy`
- `400` Invalid id supplied. → `Adaptive_Policy_Management_ErrorResource`
- `404` Not Found → `Adaptive_Policy_Management_ErrorResource`
- `422` Some of the provided query data is invalid. → `Adaptive_Policy_Management_ErrorResource`


---

### `DELETE` `/policyTemplates/{templateId}/policies/{policyId}`

**Delete Policy**

Deletes the policy and conditions, may not be assigned to a service.

operationId: `deletePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `policyId` | path | ✓ | `string` |  |


**Responses:**

- `200` Policy deleted → `Adaptive_Policy_Management_EmptyResponse`
- `204` Policy deleted, no content.
- `404` Policy not found → `Adaptive_Policy_Management_ErrorResource`
- `409` The requested policy is still in use in a policy set. → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policyTemplates/{templateId}/policies/{policyId}`

**Get Policy**

Retrieves the requested policy.

operationId: `getPolicyById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `policyId` | path | ✓ | `string` |  |


**Responses:**

- `200` Policy success → `Adaptive_Policy_Management_Policy`
- `400` Invalid id supplied. → `Adaptive_Policy_Management_ErrorResource`
- `404`  Policy Template not found. → `Adaptive_Policy_Management_ErrorResource`


---

### `PATCH` `/policyTemplates/{templateId}/policies/{policyId}`

**Update Policy**

Updates the policy from the requested values. The policy template assigned to this policy cannot be changed.

operationId: `updatePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `policyId` | path | ✓ | `string` |  |


**Request Body:** `Adaptive_Policy_Management_Policy Update`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The policy description. |
| `name` | `string` | ✓ | The name of the policy. Must be unique within the tenant. |
| `onMatchResponse` | `string` |  | The response details if the policy is matched. For policy types which are RADIUS and DPSK, this is expected to be the identifier of a valid RADIUS attribute group. |


**Responses:**

- `200` Policy updated → `Adaptive_Policy_Management_Policy`
- `409` Invalid policy details provided. → `Adaptive_Policy_Management_Policy`


---



## Policy Set Assignments

*Manage the assignments of policy sets to identities.*


*3 endpoints*


### `GET` `/policySets/{policySetId}/assignments`

**Get Policy Set Assignments**

Gets the list of assignments for the specified policy set.

operationId: `getAllPolicySetAssignments`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `policySetId` | path | ✓ | `string` | Policy set identifier. |


**Responses:**

- `200` Policy set assignments in a paged format. → `Adaptive_Policy_Management_Policy Set Assignment`
- `404` Policy set not found → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policySets/{policySetId}/assignments/query`

**Query Policy Set Assignments**

Returns the list of assignments for the specified policy set using the specified query.

operationId: `getAllPolicySetsAssignmentsByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |
| `excludeContent` | query |  | `boolean` | Indicates that the content should be excluded from the query and only count and size data returned. |


**Request Body:** `Adaptive_Policy_Management_Query Data`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List Policy Set Assignments in a paged format. → `Adaptive_Policy_Management_Policy Set Assignment`
- `404` Policy set not found → `Adaptive_Policy_Management_ErrorResource`
- `422` Some of the provided query data is invalid. → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policySets/{policySetId}/assignments/{assignmentId}`

**Get Policy Set Assignment**

Retrieves the requested policy set assignment.

operationId: `getAssignmentById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |
| `assignmentId` | path | ✓ | `string` | Assignment identifier. |


**Responses:**

- `200` Policy set assignment found → `Adaptive_Policy_Management_Policy Set Assignment`
- `404` Policy set or assignment not found → `Adaptive_Policy_Management_ErrorResource`


---



## Policy Templates

*View the list of policy templates.*


*8 endpoints*


### `GET` `/policyTemplates`

**Get Policy Templates**

Retrieves a paginated list of all policy templates in the system. Policy templates define the structure and rules for creating policies, including allowed return types such as RADIUS_ATTRIB_GROUP and rule types such as RADIUS or DPSK. This endpoint supports pagination with configurable page size and page number, and sorting by fields including id, name, description, returnType, and ruleType. This method will be removed no sooner than 08/31/2026. The URL /policyTemplates/query can be used for thi

operationId: `getAllPolicyTemplates`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `pageable` | query | ✓ | `Adaptive_Policy_Management_Pageable` |  |


**Responses:**

- `200` Policy templates in a paged format. → `Adaptive_Policy_Management_PagedResponseResourceDynamic Policy Template`


---

### `GET` `/policyTemplates/policies`

**Get Policies Across Templates**

Gets the list of policies across all templates. This method will be removed no sooner than 08/31/2026. The following URL /policyTemplates/policies/query can be used for this content.

operationId: `getAllPoliciesAcrossTemplates`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `pageable` | query | ✓ | `Adaptive_Policy_Management_Pageable` |  |


**Responses:**

- `200` Policies in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePolicy`


---

### `POST` `/policyTemplates/policies/query`

**Query Policies Across Templates**

Returns the list of policies across all templates using the specified query.

operationId: `getAllPoliciesAcrossTemplatesByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Adaptive_Policy_Management_Query Data`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List Policy in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePolicy`
- `422` Some of the provided query data is invalid. → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policyTemplates/query`

**Query Policy Templates**

Returns the list of policy templates using the specified query.

operationId: `getAllTemplatesByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Adaptive_Policy_Management_Query Data`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List Policy Template in a paged format. → `Adaptive_Policy_Management_PagedResponseResourceDynamic Policy Template`
- `422` Some of the provided query data is invalid. → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policyTemplates/{templateId}`

**Get Policy Template**

Retrieves the requested policy template.

operationId: `getPolicyTemplateById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |


**Responses:**

- `200` Policy template found → `Adaptive_Policy_Management_Dynamic Policy Template`
- `404` Policy template not found → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policyTemplates/{templateId}/attributes`

**Get Template Attributes**

Gets the list of attributes for the specified template.

operationId: `getAttributesForTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `templateId` | path | ✓ | `integer` |  |
| `pageable` | query | ✓ | `Adaptive_Policy_Management_Pageable` |  |


**Responses:**

- `200` Template attributes in a paged format. → `Adaptive_Policy_Management_PagedResponseResourceDynamic Policy Template Attribute`
- `404` Template not found → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policyTemplates/{templateId}/attributes/query`

**Query Template Attributes**

Returns the list of attributes for the specified template using the specified query.

operationId: `queryAttributeForTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Adaptive_Policy_Management_Query Data`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List Template Attributes in a paged format. → `Adaptive_Policy_Management_PagedResponseResourceDynamic Policy Template Attribute`
- `404` Template not found → `Adaptive_Policy_Management_ErrorResource`
- `422` Some of the provided query data is invalid. → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policyTemplates/{templateId}/attributes/{attributeId}`

**Get Template Attribute**

Retrieves the requested template attribute.

operationId: `getAttributesByIdForTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `integer` |  |
| `attributeId` | path | ✓ | `integer` |  |


**Responses:**

- `200` Template attribute found → `Adaptive_Policy_Management_Dynamic Policy Template Attribute`
- `404` Template or attribute not found → `Adaptive_Policy_Management_ErrorResource`


---



## Prioritized Policies

*Manage the prioritized policies within a policy set.*


*4 endpoints*


### `GET` `/policySets/{policySetId}/prioritizedPolicies`

**Get Prioritized Policies**

Gets the list of prioritized policies for the specified policy set.

operationId: `getAllPrioritizedPolicies`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |


**Responses:**

- `200` Prioritized policies in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePrioritized Policy`
- `404` Policy set not found → `Adaptive_Policy_Management_ErrorResource`


---

### `DELETE` `/policySets/{policySetId}/prioritizedPolicies/{policyId}`

**Remove Policy from Policy Set**

Removes a policy from a policy set.

operationId: `removeMappedPolicySet`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |


**Responses:**

- `200` Policy removed from policy set successfully. → `Adaptive_Policy_Management_EmptyResponse`
- `204` Policy removed from policy set, no content.
- `404` Policy set or policy not found → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policySets/{policySetId}/prioritizedPolicies/{policyId}`

**Get Prioritized Policy**

Retrieves the requested prioritized policy.

operationId: `getPrioritizedRuleById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |


**Responses:**

- `200` Prioritized policy found → `Adaptive_Policy_Management_Prioritized Policy`
- `404` Policy set or policy not found → `Adaptive_Policy_Management_ErrorResource`


---

### `PUT` `/policySets/{policySetId}/prioritizedPolicies/{policyId}`

**Assign Policy to Policy Set**

Assigns a policy to a policy set with a specific priority.

operationId: `assignPolicyToPolicySetWithPriority`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |
| `policyId` | path | ✓ | `string` | Policy identifier. |


**Request Body:** `Adaptive_Policy_Management_Prioritized Policy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Adaptive_Policy_Management_Links` |  |  |
| `policyId` | `string` |  | The identifier for the prioritized policy. Will be ignored on a put, as URL is the identifier. |
| `priority` | `integer` |  | The priority of this policy, 1 being the highest priority. |


**Responses:**

- `201` Policy assigned to policy set → `Adaptive_Policy_Management_Prioritized Policy`
- `409` Invalid assignment details provided. → `Adaptive_Policy_Management_ErrorResource`


---



## Policy Sets

*Manages the policy sets.*


*6 endpoints*


### `GET` `/policySets`

**Get Policy Sets**

Retrieves a paginated list of policy sets. A policy set is a collection of policies that can be assigned to external services for network access control. This endpoint returns policy sets with pagination support, allowing filtering by size, page number, and sorting by fields such as id, name, and description. This method will be removed no sooner than 08/31/2026. The following URL /policySets/query can be used for this content.

operationId: `getAllPolicySets`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` Policy sets in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePolicy Set`


---

### `POST` `/policySets`

**Create Policy Set**

Creates a new policy set from the provided values. A policy set is a collection of policies that can be assigned to external services for network access control. The request body must include the policy set name (required) and optionally a description. The response returns the created policy set with its unique identifier and HATEOAS links for further operations. Policy sets can be subsequently assigned to external services and used to evaluate network access policies.

operationId: `createPolicySet`


**Request Body:** `Adaptive_Policy_Management_Policy Set`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Adaptive_Policy_Management_Links` |  |  |
| `assignmentCount` | `integer` |  | The number of assignments to this policy set. |
| `description` | `string` | ✓ | The policy set description. |
| `externalAssignments` | `array` |  | The list of external assignments assigned to this policy set. |
| `id` | `string` |  | The identifier for this dynamic policy. |
| `mappedPolicyCount` | `integer` |  | The number of policies mapped to this policy set. |
| `name` | `string` | ✓ | The policy set name. |
| `policyNames` | `array` |  | The names of the policies mapped to this policy set. |
| `policyOverrideEnabled` | `boolean` |  | The policy override enabled flag. |


**Responses:**

- `201` Policy set created → `Adaptive_Policy_Management_Policy Set`
- `409` Invalid policy set details provided. → `Adaptive_Policy_Management_ErrorResource`


---

### `POST` `/policySets/query`

**Query Policy Sets**

Returns the list of policy sets using the specified query.

operationId: `getAllPolicySetsByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Adaptive_Policy_Management_Query Data`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List Policy Sets in a paged format. → `Adaptive_Policy_Management_PagedResponseResourcePolicy Set`
- `422` Some of the provided query data is invalid. → `Adaptive_Policy_Management_ErrorResource`


---

### `DELETE` `/policySets/{policySetId}`

**Delete Policy Set**

Deletes the policy set, may not be assigned to a service.

operationId: `deletePolicySet`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |


**Responses:**

- `200` Policy set deleted → `Adaptive_Policy_Management_EmptyResponse`
- `204` Policy set deleted, no content.
- `404` Policy set not found → `Adaptive_Policy_Management_ErrorResource`
- `409` The requested policy set is still in use. → `Adaptive_Policy_Management_ErrorResource`


---

### `GET` `/policySets/{policySetId}`

**Get Policy Set**

Retrieves the requested policy set.

operationId: `getPolicySetById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |


**Responses:**

- `200` Policy set found → `Adaptive_Policy_Management_Policy Set`
- `404` Policy set not found → `Adaptive_Policy_Management_ErrorResource`


---

### `PATCH` `/policySets/{policySetId}`

**Update Policy Set**

Updates the policy set from the requested values.

operationId: `updatePolicySet`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` | Policy set identifier. |


**Request Body:** `Adaptive_Policy_Management_Policy Set`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Adaptive_Policy_Management_Links` |  |  |
| `assignmentCount` | `integer` |  | The number of assignments to this policy set. |
| `description` | `string` | ✓ | The policy set description. |
| `externalAssignments` | `array` |  | The list of external assignments assigned to this policy set. |
| `id` | `string` |  | The identifier for this dynamic policy. |
| `mappedPolicyCount` | `integer` |  | The number of policies mapped to this policy set. |
| `name` | `string` | ✓ | The policy set name. |
| `policyNames` | `array` |  | The names of the policies mapped to this policy set. |
| `policyOverrideEnabled` | `boolean` |  | The policy override enabled flag. |


**Responses:**

- `200` Policy set updated → `Adaptive_Policy_Management_Policy Set`
- `409` Invalid policy set details provided. → `Adaptive_Policy_Management_ErrorResource`


---


