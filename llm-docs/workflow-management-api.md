# Workflow Management API

> RUCKUS One API Reference

---


## Workflow

*Manages the workflows, including create, update and delete.*


*8 endpoints*


### `POST` `/workflows`

**Create Workflow**

Creates a new workflow with the specified configuration and automatically initializes it with start and end steps. This operation accepts a workflow data object containing the workflow name, description, network restrictions (allowedIps/disAllowedIps), and publication details. The workflow is created in 'WORK_IN_PROGRESS' status by default, and start/end steps are automatically generated. The operation is asynchronous and returns a request ID for tracking the creation process. Required fields in

operationId: `createWorkflow`


**Request Body:** `Workflow_Management_API_Workflow_v1_0`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Workflow_Management_API_Links` |  |  |
| `allowedIps` | `array` |  | The list of IP addresses that are permitted to access this workflow. Only one allowed IP can be queried for using filter in the query data. |
| `description` | `string` |  | The description of a workflow. |
| `disAllowedIps` | `array` |  | The list of IP addresses that are not permitted to access this workflow. Only one not allowed IP can be queried for using filter in the query data. |
| `id` | `string` |  | The unique ID for this workflow. |
| `name` | `string` | ✓ | The name of the workflow. |
| `publishedChildren` | `boolean` |  | Indicates that there is a published workflow that is a child of this workflow. |
| `publishedDetails` | `Workflow_Management_API_PublishedDetails_v1_0` |  | This is the publication details for the workflow.  The only change here that will be recognized on a PATCH, is a request to change the publication state of this workflow. A status of 'validate' will validate the current workflow and return an error i |
| `startStepId` | `string` |  | The start step for this workflow. |
| `status` | `string` |  | The validation status of the workflow. |
| `statusReasons` | `array` |  | The set of reasons for an invalid status. This will be empty if the workflow is valid. |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request → `Workflow_Management_API_ErrorResource`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/query`

**Get Current Workflows**

Retrieves all of the work in progress workflows based on the query criteria.

operationId: `queryForWorkflows`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Workflow_Management_API_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` Success → `Workflow_Management_API_PagedResponseResourceWorkflow_v1_0`
- `400` Bad request, check query format. → `Workflow_Management_API_ErrorResource`


---

### `DELETE` `/workflows/{workflowId}`

**Delete Workflow**

Initiates a request that will delete the workflow requested. If the workflow id provided is for a workflow that is in a work in progress state then it will be deleted along with all dependent published and retired workflows.

operationId: `deleteWorkflow`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflows/{workflowId}`

**Get Workflow**

Retrieves the requested workflow by id.

operationId: `getWorkflowById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` | Workflow identifier. |


**Responses:**

- `200` Success → `Workflow_Management_API_Workflow_v1_0`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow not found. → `Workflow_Management_API_ErrorResource`


---

### `PATCH` `/workflows/{workflowId}`

**Update a Workflow**

Updates an existing workflow with new configuration values including name, description, network restrictions (allowedIps/disAllowedIps), and publication status. This operation supports partial updates where only provided fields are modified. The workflow can be updated in 'WORK_IN_PROGRESS' status, and publication status can be changed to 'VALIDATE' (for validation only) or 'PUBLISHED' (to publish the workflow). Once published, a workflow cannot be modified except for publication status changes.

operationId: `updateWorkflow`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |


**Request Body:** `Workflow_Management_API_Workflow_v1_0`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Workflow_Management_API_Links` |  |  |
| `allowedIps` | `array` |  | The list of IP addresses that are permitted to access this workflow. Only one allowed IP can be queried for using filter in the query data. |
| `description` | `string` |  | The description of a workflow. |
| `disAllowedIps` | `array` |  | The list of IP addresses that are not permitted to access this workflow. Only one not allowed IP can be queried for using filter in the query data. |
| `id` | `string` |  | The unique ID for this workflow. |
| `name` | `string` | ✓ | The name of the workflow. |
| `publishedChildren` | `boolean` |  | Indicates that there is a published workflow that is a child of this workflow. |
| `publishedDetails` | `Workflow_Management_API_PublishedDetails_v1_0` |  | This is the publication details for the workflow.  The only change here that will be recognized on a PATCH, is a request to change the publication state of this workflow. A status of 'validate' will validate the current workflow and return an error i |
| `startStepId` | `string` |  | The start step for this workflow. |
| `status` | `string` |  | The validation status of the workflow. |
| `statusReasons` | `array` |  | The set of reasons for an invalid status. This will be empty if the workflow is valid. |


**Responses:**

- `200` Ok - Returned if a validation request finds no errors. → `Workflow_Management_API_AsyncRequestResponse`
- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `404`  Workflow not found → `Workflow_Management_API_ErrorResource`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/steps/{stepId}/nextSteps/workflows/{referencedWorkflowId}`

**Clone Workflow Steps Into Workflow**

Imports an existing workflow as a nested workflow within the current workflow, creating a hierarchical workflow structure. This operation clones the referenced workflow and inserts all of that workflows' steps after the specified step in the current workflow. The imported workflow becomes a nested component that can be executed as part of the parent workflow's flow. This enables workflow composition and reuse, allowing complex workflows to be built from smaller, reusable workflow components. The

operationId: `nestedCloneWorkflow`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |
| `referencedWorkflowId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request → `Workflow_Management_API_ErrorResource`
- `404`  Workflow not found → `Workflow_Management_API_ErrorResource`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/versions/query`

**Get Versioned Workflows**

Retrieves all published versions of a specific workflow, including the original workflow and all its published iterations. This endpoint returns a paginated list of workflow versions that share the same parent workflow ID, allowing you to track the evolution of a workflow over time. Each version includes publication details such as version number, publication status, and publication date. Use the QueryData parameter to filter, sort, and paginate through the version history. The excludeContent pa

operationId: `queryForVersionedWorkflows`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Workflow_Management_API_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` Success → `Workflow_Management_API_PagedResponseResourceWorkflow_v1_0`
- `400` Bad request, check query format. → `Workflow_Management_API_ErrorResource`
- `404` Invalid id supplied. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/workflows`

**Clone Workflow**

Creates a complete copy of an existing workflow including all its steps, split options, and configuration. The cloned workflow will have a new unique ID and a name generated by appending 'Clone' to the original workflow name (with incremental numbering if duplicates exist). The cloned workflow is created in 'WORK_IN_PROGRESS' status regardless of the source workflow's status. This operation requires the source workflow to have more than just the default start/end steps. The operation is asynchro

operationId: `cloneWorkflow`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request → `Workflow_Management_API_ErrorResource`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---



## Steps

*Manages the steps for the workflow.*


*7 endpoints*


### `GET` `/workflows/{workflowId}/steps`

**Get All Steps**

Retrieves the complete list of steps for the workflow with paging.

operationId: `getAllStepsForWorkflow`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |
| `workflowId` | path | ✓ | `string` |  |


**Responses:**

- `200` The action definitions in a paged format. → `Workflow_Management_API_PagedResponseResourceAbstractBaseStepDto`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404` Not Found. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/steps/query`

**Search and Filter Workflow Steps**

Searches and retrieves workflow steps using advanced query criteria. This endpoint supports complex filtering by step properties (ID, action definition, step type, termination status), custom sorting by multiple fields, and pagination controls. The query accepts a QueryData object containing filter conditions, sort specifications, and pagination parameters. Use the excludeContent parameter to retrieve only the total count without step details for performance optimization.

operationId: `queryForStepsAssignedToThisWorkflow`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `excludeContent` | query |  | `boolean` |  |


**Request Body:** `Workflow_Management_API_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` Success → `Workflow_Management_API_PagedResponseResourceAbstractBaseStepDto`
- `400` Bad request, check query format. → `Workflow_Management_API_ErrorResource`
- `404` Not Found. → `Workflow_Management_API_ErrorResource`


---

### `DELETE` `/workflows/{workflowId}/steps/{stepId}`

**Delete Step And Disconnect**

Deletes the requested step and leaves the previous and next steps disconnected. If this is a split, all options except the first will be removed. The step under the first option will be moved to the current step flow. Start and end steps can never be deleted.

operationId: `deleteStepV2`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request. → `Workflow_Management_API_ErrorResource`
- `404` Workflow is not Found. → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflows/{workflowId}/steps/{stepId}`

**Retrieve Workflow Step by ID**

Retrieves detailed information about a specific workflow step by its unique identifier. Returns complete step data including step type, action definitions, navigation relationships (prior/next steps), split options, termination status, and enrollment actions. This operation requires both workflowId and stepId parameters to locate the step within the correct workflow context.

operationId: `getStepById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |


**Responses:**

- `200` Success → `Workflow_Management_API_AbstractBaseStepDto`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow not found. → `Workflow_Management_API_ErrorResource`


---

### `DELETE` `/workflows/{workflowId}/steps/{stepId}/descendantSteps`

**Delete Descendant Step**

Deletes all steps that are descendants of the specified step, effectively truncating the workflow at that point. This operation removes all steps that follow the specified step in the workflow sequence, making the specified step the final step in the workflow flow. The operation supports an optional parameter to also delete the selected step itself. This is useful for removing entire branches of a workflow or cleaning up workflow sections. The operation cannot be performed on end steps (as they

operationId: `deleteDescendantSteps`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |
| `deleteSelectedStep` | query |  | `boolean` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request. → `Workflow_Management_API_ErrorResource`
- `404` Workflow is not Found. → `Workflow_Management_API_ErrorResource`
- `409` Conflict. If the selected step is an end step, or a start step and the deleteSelectedStep parameter is true. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/steps/{stepId}/nextSteps`

**Create Step**

Creates a new step in the workflow that will be executed after the specified parent step. This operation allows you to add sequential steps to the workflow flow, including regular steps, split steps, or other step types. The new step requires a valid action definition that matches the step type being created, and will be automatically connected to the parent step in the workflow sequence. The operation validates that the parent step exists and is not an end step, and ensures the action type matc

operationId: `createChildStep`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |


**Request Body:** `Workflow_Management_API_AbstractActionStepDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Workflow_Management_API_Links` |  |  |
| `actionDefinitionId` | `string` |  | The action definition ID for this step. This is a read only attribute for steps, and will be determined by the provided enrollment action on the create. For split steps this will determine the type of options that can be added to the step. |
| `actionType` | `string` |  | The action type assigned to this step. |
| `enrollmentActionId` | `string` | ✓ | The ID of the enrollment action to be followed in this step. |
| `id` | `string` |  | The unique ID for this step. |
| `label` | `string` |  | The label for this step. This is an optional field. If provided, it must not be empty and cannot exceed 32 characters. |
| `priorStepId` | `string` |  | The prior step in the workflow. This is a read only attribute. |
| `splitOptionId` | `string` |  | If this step is referenced by an option, rather then the step, this is the ID. Either split option or  the prior step will be provided but not both. |
| `status` | `string` |  | The validation status of the step. |
| `statusReasons` | `array` |  | The set of reasons for an invalid status. This will be empty if the step is valid. |
| `type` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request. → `Workflow_Management_API_ErrorResource`
- `404` Not Found. → `Workflow_Management_API_ErrorResource`
- `409` Conflict. If the action requested cannot be found, or if the action type does not match the type of step created. → `Workflow_Management_API_ErrorResource`


---

### `PUT` `/workflows/{workflowId}/steps/{stepId}/nextSteps/{detachedStepId}`

**Attach Step**

Attach a detached step to an existing step in the workflow. This operation takes a step that is currently disconnected from the workflow flow and connects it as the next step after the specified parent step. The detached step must not already have a prior step, cannot be a start or end step, and cannot create circular dependencies. This operation is asynchronous and returns a request ID for tracking the attachment process.

operationId: `attachSteps`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` | Workflow ID |
| `stepId` | path | ✓ | `string` | The step ID under which the step will be attached. |
| `detachedStepId` | path | ✓ | `string` | The step ID that will be attached below the step. |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request. → `Workflow_Management_API_ErrorResource`
- `404` Not Found. → `Workflow_Management_API_ErrorResource`
- `409` Conflict. If either of the steps involved in attachment are of the wrong type or cannot be found. → `Workflow_Management_API_ErrorResource`


---



## Split Options

*Manages the split options for split steps in a workflow.*


*5 endpoints*


### `GET` `/workflows/{workflowId}/steps/{stepId}/splitOptions`

**Get All Split Options**

Retrieves all of the split options for the split step.

operationId: `getAllSplitStepOptionsForStep`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |


**Responses:**

- `200` Success → `Workflow_Management_API_PagedResponseResourceSplitStepOption_v1_0`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow, step, or split option is not found. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/steps/{stepId}/splitOptions`

**Creates Split Option**

Creates a new split option for a split step, defining a branching path in the workflow. A split option represents a conditional branch that users can take based on the evaluation of an enrollment action. The new option is automatically added to the end of the existing options list and will be processed in the order they were created. Each split option requires a unique name within the split step and must reference a valid enrollment action that matches the split step's action type. The operation

operationId: `createOption`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |


**Request Body:** `Workflow_Management_API_SplitStepOption_v1_0`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Workflow_Management_API_Links` |  |  |
| `actionDefinitionId` | `string` |  | The action definition ID for this step. This is a read only attribute, and will be determined by the provided enrollment action on the create. |
| `actionType` | `string` |  | The action type assigned to this step. |
| `enrollmentActionId` | `string` | ✓ | The ID of the enrollment action to be followed in this step. |
| `id` | `string` |  | The unique ID for this option on the workflow. |
| `nextStepId` | `string` |  | The next step for this option. This is a read only attribute. |
| `optionName` | `string` | ✓ | The name of the option for this step. |
| `status` | `string` |  | The validation status of the split option. |
| `statusReasons` | `array` |  | The set of reasons for an invalid status. This will be empty if the split option is valid. |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow, step, or split option is not found. → `Workflow_Management_API_ErrorResource`


---

### `DELETE` `/workflows/{workflowId}/steps/{stepId}/splitOptions/{optionId}`

**Delete Split Option**

Deletes the requested option and all of the steps under this option.

operationId: `deleteSplitOption`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |
| `optionId` | path | ✓ | `string` |  |
| `includeChildren` | query |  | `boolean` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow, step, or split option is not found. → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflows/{workflowId}/steps/{stepId}/splitOptions/{optionId}`

**Get Split Option**

Retrieves the split option by id.

operationId: `getSplitStepOptionById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |
| `optionId` | path | ✓ | `string` |  |


**Responses:**

- `200` Success → `Workflow_Management_API_SplitStepOption_v1_0`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow, step, or split option is not found. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/steps/{stepId}/splitOptions/{optionId}/nextSteps`

**Creates Step Under Split Option**

Creates a new step that will be executed when a specific split option is selected by the user. This operation allows you to define the workflow path that follows a particular split option. If no step is currently assigned to the option, the new step becomes the immediate next step for that option. If a step already exists for the option, the new step is inserted before the existing step, creating a sequential flow. The operation requires a valid action definition that matches the step type being

operationId: `createNextStepForOption`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `stepId` | path | ✓ | `string` |  |
| `optionId` | path | ✓ | `string` |  |


**Request Body:** `Workflow_Management_API_AbstractActionStepDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Workflow_Management_API_Links` |  |  |
| `actionDefinitionId` | `string` |  | The action definition ID for this step. This is a read only attribute for steps, and will be determined by the provided enrollment action on the create. For split steps this will determine the type of options that can be added to the step. |
| `actionType` | `string` |  | The action type assigned to this step. |
| `enrollmentActionId` | `string` | ✓ | The ID of the enrollment action to be followed in this step. |
| `id` | `string` |  | The unique ID for this step. |
| `label` | `string` |  | The label for this step. This is an optional field. If provided, it must not be empty and cannot exceed 32 characters. |
| `priorStepId` | `string` |  | The prior step in the workflow. This is a read only attribute. |
| `splitOptionId` | `string` |  | If this step is referenced by an option, rather then the step, this is the ID. Either split option or  the prior step will be provided but not both. |
| `status` | `string` |  | The validation status of the step. |
| `statusReasons` | `array` |  | The set of reasons for an invalid status. This will be empty if the step is valid. |
| `type` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow, step, or split option is not found. → `Workflow_Management_API_ErrorResource`
- `409` Conflict. When the action requested cannot be found, or the action type does not match the type of step created. → `Workflow_Management_API_ErrorResource`


---



## Enrollment UI Configuration

*Manages the enrollment configuration for the workflow.*


*4 endpoints*


### `DELETE` `/workflows/{workflowId}/uiConfigurations`

**Delete UI Configuration**

Deletes the custom settings on the UI configuration.

operationId: `resetUiConfig`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `404`  Workflow not found. → `Workflow_Management_API_ErrorResource`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflows/{workflowId}/uiConfigurations`

**Get Workflow's UI Configuration**

Retrieves the UI configuration for the specified workflow.

operationId: `getUiConfiguration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |


**Responses:**

- `200` Success → `Workflow_Management_API_UiConfiguration_v1_0`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow not found. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflows/{workflowId}/uiConfigurations`

**Update Workflows UI Configuration**

Initiates a request that will update the workflows UI configuration.

operationId: `createUiConfig`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `backgroundImage` | `string` |  |  |
| `iconImage` | `string` |  |  |
| `logoImage` | `string` |  |  |
| `uiConfiguration` | `Workflow_Management_API_UiConfiguration_v1_0` | ✓ |  |


**Responses:**

- `202` Accepted → `Workflow_Management_API_AsyncRequestResponse`
- `400` Bad request. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow not found. → `Workflow_Management_API_ErrorResource`
- `409` Conflict → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflows/{workflowId}/uiConfigurations/{imageType}`

**Get UI Configuration's Image**

Get UI configuration's image for the specified workflow and image type.

operationId: `getImageFile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `workflowId` | path | ✓ | `string` |  |
| `imageType` | path | ✓ | `string` |  |


**Responses:**

- `200` Success → `Workflow_Management_API_UiConfigImage_v1_0`
- `400` Bad request. → `Workflow_Management_API_ErrorResource`
- `404`  Workflow or images not found. → `Workflow_Management_API_ErrorResource`


---



## Action Definition

*Manages the action definitions that can be used in workflow steps.*


*4 endpoints*


### `GET` `/workflowActionDefinitions`

**Get All Action Definitions**

Retrieves the complete list of action definitions with paging.

operationId: `getAllActions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc). |


**Responses:**

- `200` The action definitions in a paged format. → `Workflow_Management_API_PagedResponseResourceActionDefinition_v1_0`
- `400` Invalid id supplied. → `Workflow_Management_API_ErrorResource`


---

### `POST` `/workflowActionDefinitions/query`

**Query Action Definitions**

Returns the list of action definitions using the specified query.

operationId: `queryForActionDefinitions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `excludeContent` | query |  | `boolean` | Excludes all of the content and just returns the counts for this query. |


**Request Body:** `Workflow_Management_API_QueryData`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | The list of filters to apply. |
| `page` | `integer` |  | The page number to return, paging starts with 0. |
| `pageSize` | `integer` |  | The number of items requested on the page. |
| `sortField` | `string` |  | The field to use to sort on. |
| `sortOrder` | `string` |  | The sort order of the applied query. |


**Responses:**

- `200` List of action definitions in a paged format. Can exclude content for just count information → `Workflow_Management_API_PagedResponseResourceActionDefinition_v1_0`
- `400` Bad request, check query format. → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflowActionDefinitions/{definitionId}`

**Get Action Definition**

Retrieves the requested action definition by id.

operationId: `getByDefinitionId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `definitionId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Workflow_Management_API_ActionDefinition_v1_0`
- `404`  Action definition not found. → `Workflow_Management_API_ErrorResource`


---

### `GET` `/workflowActionDefinitions/{definitionId}/requiredPriorDefinitions`

**Get Prior Required Actions**

Retrieves the list of required prior actions for this action.

operationId: `getRequiredPriorDefinitions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `definitionId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Workflow_Management_API_PagedResponseResourceActionDefinition_v1_0`
- `404`  Action definition not found. → `Workflow_Management_API_ErrorResource`


---


