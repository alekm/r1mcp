# Message Templates

> RUCKUS One API Reference

---


## Variables

*Retrieve variables available to templates within the given template scope.*


*1 endpoint*


### `GET` `/templateScopes/{templateScopeId}/variables`

**Retrieve Template Scope Variables**

Retrieve variables within the given template scope.

operationId: `msgTemplate_getVariablesForTemplateScope`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | Sorting is not allowed for this endpoint. |
| `templateScopeId` | path | ✓ | `string` | Template scope id |


**Responses:**

- `200` The list of variables available to templates within this template scope. → `Message_Templates_Paged Variables Response`
- `404` Template scope not found. → `Message_Templates_Error`


---



## Template Registrations

*Retrieve template registrations.*


*1 endpoint*


### `GET` `/templateScopes/{templateScopeId}/templates/{templateId}/registrations`

**Retrieve a Template's Registrations**

Returns all registrations that reference the given template.

operationId: `msgTemplate_getAllTemplateRegistrations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort and the sort order  (asc or desc) comma separated. Sortable fields are: id, templateId, usageLocalizationKey, usageDescriptionFieldOne, usageDescriptionFieldTwo |
| `templateScopeId` | path | ✓ | `string` | Template Scope ID |
| `templateId` | path | ✓ | `string` | Template ID |


**Responses:**

- `200` The list of registrations referencing the given template. → `Message_Templates_Paged Registrations Response`
- `404` Template Scope not found → `Message_Templates_Error`


---



## Template Scope

*Retrieve information about the template scope.*


*2 endpoints*


### `GET` `/templateScopes`

**Retrieve All Template Scopes**

Returns all available template scopes.

operationId: `msgTemplate_getAllTemplateScopes`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc).  Sortable fields are: id, messageType, and nameLocalizationKey |


**Responses:**

- `200` The list of template scopes. → `Message_Templates_Paged Template Scope Response`


---

### `GET` `/templateScopes/{templateScopeId}`

**Get Template Scope**

Retrieves the template scope for the given id.

operationId: `msgTemplate_getTemplateScope`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateScopeId` | path | ✓ | `string` | Template scope id |
| `includes` | query |  | `array` | A comma separated list of child resources to include in the response in the format: includes={resource path},{resource path}. Where {resource path} must match the REST API path for that resource under |


**Responses:**

- `200` Template scope → `Message_Templates_Template Scope`
- `404` Template scope not found → `Message_Templates_Error`


---



## Registrations

*Manage template registrations.*


*2 endpoints*


### `GET` `/templateScopes/{templateScopeId}/registrations`

**Retrieve All Registrations**

Returns all registrations within the given template scope.

operationId: `msgTemplate_getAllRegistrations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort and the sort order  (asc or desc) comma separated. Sortable fields are: id, templateId, usageLocalizationKey, usageDescriptionFieldOne, usageDescriptionFieldTwo |
| `templateScopeId` | path | ✓ | `string` | Template Scope ID |


**Responses:**

- `200` The list of registrations within the template scope. → `Message_Templates_Paged Registrations Response`
- `404` Template Scope not found → `Message_Templates_Error`


---

### `GET` `/templateScopes/{templateScopeId}/registrations/{registrationId}`

**Retrieve Registration**

Returns the registration for the given ID.

operationId: `msgTemplate_getRegistration`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateScopeId` | path | ✓ | `string` | Template Scope ID |
| `registrationId` | path | ✓ | `string` | Registration ID |


**Responses:**

- `200` The registration. → `Message_Templates_Registration`
- `404` Template scope or registration not found. → `Message_Templates_Error`


---



## Manage Templates

*Manage Templates.*


*2 endpoints*


### `GET` `/templateScopes/{templateScopeId}/templates`

**Retrieve All Templates in Scope**

Returns all templates within the given template scope.

operationId: `msgTemplate_getTemplatesForScope`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `size` | query |  | `string` | Page size |
| `page` | query |  | `string` | The page to retrieve (starts at zero). |
| `sort` | query |  | `string` | The field name to sort, comma separated from the sort order (asc or desc).  Sortable fields are: id, nameLocalizationKey, userProvidedName, messageTemplate, and extraFieldOneTemplate |
| `templateScopeId` | path | ✓ | `string` | Template scope ID |


**Responses:**

- `200` The list of templates within the template scope. → `Message_Templates_Paged Templates Response`
- `404` Template Scope not found → `Message_Templates_Error`


---

### `GET` `/templateScopes/{templateScopeId}/templates/{genericTemplateId}`

**Retrieve Template**

Returns the template specified by the given id, which can be either a registration id or template id.

operationId: `msgTemplate_getTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateScopeId` | path | ✓ | `string` | Template Scope ID |
| `genericTemplateId` | path | ✓ | `string` | Template or Registration ID |


**Responses:**

- `200` The template → `Message_Templates_Template`
- `404` Template scope or template not found. → `Message_Templates_Error`


---


