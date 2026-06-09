# Switch Services

> RUCKUS One API Reference

---


## AAA Server

*Manage AAA (authentication, authorization, and accounting) servers.*


*10 endpoints*


### `DELETE` `/venues/aaaServers`

**Delete AAA Servers**

Delete multiple authentication, authorization, and accounting servers. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aaaServers can be used for this content.

operationId: `DeleteAaaServers_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/aaaServers/query`

**Query AAA Servers**

List of venue's authentication, authorization, and accounting servers. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aaaServers/query can be used for this content.

operationId: `QueryAaaServers_1`


**Request Body:** `Switch_Services_AaaServerQueryRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `serverType` | `string` |  | The type of AAA server to filter by, with the default value set to LOCAL if not specified. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |
| `venueId` | `string` |  | The venue identifier to filter AAA servers by specific venue location. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/aaaServers/{aaaServerId}`

**Delete AAA Server**

Delete authentication, authorization, and accounting server by id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aaaServers/{aaaServerId} can be used for this content.

operationId: `DeleteAaaServer_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/aaaServers/{aaaServerId}`

**Get AAA Server Setting**

Get a switch's authentication, authorization, and accounting server setting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aaaServers/{aaaServerId} can be used for this content.

operationId: `GetAaaServer_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AAAServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aaaServers`

**Delete AAA Servers**

Delete multiple authentication, authorization, and accounting servers.

operationId: `DeleteAaaServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `204` No Content → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/aaaServers`

**Add AAA Server**

Add authentication, authorization, and accounting server. Use activity API with request id to get the status update.

operationId: `AddAaaServer_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaServerBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctPort` | `integer` |  | Accounting port number for RADIUS server (0-65535). |
| `authEnable` | `boolean` |  | Enable or disable authentication for RADIUS server. |
| `authPort` | `integer` |  | Authentication port number for RADIUS or TACACS+ server (0-65535). |
| `encryptedPassword` | `string` |  | Encrypted password for local user authentication. |
| `id` | `string` |  | Unique identifier for the AAA server |
| `ip` | `string` |  | IP address of the AAA server (supports both IPv4 and IPv6 formats). |
| `level` | `string` |  | Privilege level for local user. |
| `name` | `string` |  | Name of the AAA server (2-64 characters) |
| `password` | `string` |  | Password for local user authentication (8-64 characters, stored in plain text for internal use). |
| `purpose` | `string` |  | Purpose of TACACS+ server (e.g., authentication, authorization, accounting). |
| `secret` | `string` |  | Shared secret for RADIUS or TACACS+ server authentication (1-64 characters). |
| `serverType` | `string` |  | Type of AAA server (RADIUS, TACACS_PLUS, or LOCAL). |
| `username` | `string` |  | Username for local user authentication (2-48 characters). |


**Responses:**

- `200` OK → `Switch_Services_AAAServer_V1`
- `201` Created → `Switch_Services_AaaServerResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/aaaServers/query`

**Query AAA Servers**

List of venue's authentication, authorization, and accounting servers.

operationId: `QueryAaaServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaServerQueryRequest_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `serverType` | `string` |  | The type of AAA server to filter by, with the default value set to LOCAL if not specified. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aaaServers/{aaaServerId}`

**Delete AAA Server**

Delete authentication, authorization, and accounting server by id.

operationId: `DeleteAaaServer`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aaaServers/{aaaServerId}`

**Get AAA Server Setting**

Get a switch's authentication, authorization, and accounting server setting.

operationId: `GetAaaServer`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AaaServer_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aaaServers/{aaaServerId}`

**Update AAA Server**

Update authentication, authorization, and accounting server by id. Use activity API with request id to get the status update.

operationId: `PutAaaServer_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaServerId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaServerBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctPort` | `integer` |  | Accounting port number for RADIUS server (0-65535). |
| `authEnable` | `boolean` |  | Enable or disable authentication for RADIUS server. |
| `authPort` | `integer` |  | Authentication port number for RADIUS or TACACS+ server (0-65535). |
| `encryptedPassword` | `string` |  | Encrypted password for local user authentication. |
| `id` | `string` |  | Unique identifier for the AAA server |
| `ip` | `string` |  | IP address of the AAA server (supports both IPv4 and IPv6 formats). |
| `level` | `string` |  | Privilege level for local user. |
| `name` | `string` |  | Name of the AAA server (2-64 characters) |
| `password` | `string` |  | Password for local user authentication (8-64 characters, stored in plain text for internal use). |
| `purpose` | `string` |  | Purpose of TACACS+ server (e.g., authentication, authorization, accounting). |
| `secret` | `string` |  | Shared secret for RADIUS or TACACS+ server authentication (1-64 characters). |
| `serverType` | `string` |  | Type of AAA server (RADIUS, TACACS_PLUS, or LOCAL). |
| `username` | `string` |  | Username for local user authentication (2-48 characters). |


**Responses:**

- `200` OK → `Switch_Services_AAAServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## AAA Setting

*Manage AAA (authentication, authorization, and accounting) settings.*


*3 endpoints*


### `GET` `/venues/{venueId}/aaaSettings`

**Retrieve AAA Setting**

Retrieve venue's authentication, authorization, and accounting setting.

operationId: `GetAaaSettings_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AAASetting_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aaaSettings`

**Update AAA Setting**

Update authentication, authorization, and accounting setting by id. Use activity API with request id to get the status update.

operationId: `PutAaaSetting`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaSetting_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctCommonsFirstServer` | `string` |  | The first server to receive accounting records for common commands. |
| `acctCommonsLevel` | `string` |  | The accounting level for common commands, determining which commands are logged. |
| `acctCommonsSecondServer` | `string` |  | The second server to receive accounting records for common commands if the first server is unavailable. |
| `acctCommonsThirdServer` | `string` |  | The third server to receive accounting records for common commands if the first two servers are unavailable. |
| `acctEnabledCommand` | `boolean` |  | Indicates whether accounting is enabled for command execution, tracking user commands for auditing purposes. |
| `acctEnabledExec` | `boolean` |  | Indicates whether accounting is enabled for exec mode sessions, tracking user login sessions for auditing purposes. |
| `acctExecFirstServer` | `string` |  | The first server to receive accounting records for exec mode sessions. |
| `acctExecSecondServer` | `string` |  | The second server to receive accounting records for exec mode sessions if the first server is unavailable. |
| `acctExecThirdServer` | `string` |  | The third server to receive accounting records for exec mode sessions if the first two servers are unavailable. |
| `authnEnabledSsh` | `boolean` |  | Indicates whether AAA authentication is enabled for SSH access to the switch. |
| `authnFirstPref` | `string` |  | The first preference method for authentication, specifying the primary authentication mechanism to be used. |
| `authnFourthPref` | `string` |  | The fourth preference method for authentication, used as the final fallback option. |
| `authnSecondPref` | `string` |  | The second preference method for authentication, used as a fallback if the first method fails. |
| `authnThirdPref` | `string` |  | The third preference method for authentication, used as a fallback if the second method fails. |
| `authzCommonsFirstServer` | `string` |  | The first server to be consulted for common command authorization. |
| `authzCommonsLevel` | `string` |  | The authorization level for common commands, determining the privilege level required. |
| `authzCommonsSecondServer` | `string` |  | The second server to be consulted for common command authorization if the first server is unavailable. |
| `authzCommonsThirdServer` | `string` |  | The third server to be consulted for common command authorization if the first two servers are unavailable. |
| `authzEnabledCommand` | `boolean` |  | Indicates whether authorization is enabled for command execution on the switch. |
| `authzEnabledExec` | `boolean` |  | Indicates whether authorization is enabled for exec mode access on the switch. |
| `authzExecFirstServer` | `string` |  | The first server to be consulted for exec mode authorization. |
| `authzExecSecondServer` | `string` |  | The second server to be consulted for exec mode authorization if the first server is unavailable. |
| `authzExecThirdServer` | `string` |  | The third server to be consulted for exec mode authorization if the first two servers are unavailable. |
| `id` | `string` |  |  |


**Responses:**

- `200` OK → `Switch_Services_AaaSettingResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aaaSettings/{aaaSettingId}`

**Update AAA Setting**

Update authentication, authorization, and accounting setting by id. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aaaSettings can be used for this content.

operationId: `PutAaaSetting_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaSettingId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaSettingBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctCommonsFirstServer` | `string` |  | First preference for accounting command server. |
| `acctCommonsLevel` | `string` |  | Accounting command privilege level. |
| `acctCommonsSecondServer` | `string` |  | Second preference for accounting command server. |
| `acctCommonsThirdServer` | `string` |  | Third preference for accounting command server. |
| `acctEnabledCommand` | `boolean` |  | Enable or disable command accounting (default: false). |
| `acctEnabledExec` | `boolean` |  | Enable or disable exec accounting (default: false). |
| `acctExecFirstServer` | `string` |  | First preference for accounting exec server. |
| `acctExecSecondServer` | `string` |  | Second preference for accounting exec server. |
| `acctExecThirdServer` | `string` |  | Third preference for accounting exec server. |
| `authnEnabledSsh` | `boolean` |  | Enable or disable SSH authentication (default: true). |
| `authnFirstPref` | `string` |  | First preference for authentication server type. |
| `authnFourthPref` | `string` |  | Fourth preference for authentication server type. |
| `authnSecondPref` | `string` |  | Second preference for authentication server type. |
| `authnThirdPref` | `string` |  | Third preference for authentication server type. |
| `authzCommonsFirstServer` | `string` |  | First preference for authorization command server. |
| `authzCommonsLevel` | `string` |  | Authorization command privilege level. |
| `authzCommonsSecondServer` | `string` |  | Second preference for authorization command server. |
| `authzCommonsThirdServer` | `string` |  | Third preference for authorization command server. |
| `authzEnabledCommand` | `boolean` |  | Enable or disable command authorization (default: false). |
| `authzEnabledExec` | `boolean` |  | Enable or disable exec authorization (default: false). |
| `authzExecFirstServer` | `string` |  | First preference for authorization exec server. |
| `authzExecSecondServer` | `string` |  | Second preference for authorization exec server. |
| `authzExecThirdServer` | `string` |  | Third preference for authorization exec server. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Command Line Interface Template

*Manage command line interface templates.*


*10 endpoints*


### `DELETE` `/cliTemplates`

**Delete Command Line Interface Templates**

Delete command line interface templates.

operationId: `DeleteCliTemplates_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/cliTemplates`

**Get Command Line Interface Templates**

Get a list of command line interface templates. This method will be removed no sooner than 06/30/2026. The following URL /cliTemplates/{cliTemplateId} can be used for this content.

operationId: `GetCliTemplates`


**Responses:**

- `200` OK → `Switch_Services_AcxCliTemplate_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/cliTemplates`

**Add Command Line Interface Template**

Create a command line interface template for switches.

operationId: `AddCliTemplate_1_1`


**Request Body:** `Switch_Services_AcxCliTemplateBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `applyLater` | `boolean` |  | Flag indicating whether to apply the CLI template later rather than immediately (default: false). |
| `cli` | `string` |  | The CLI command template content with variable placeholders (e.g., {{variable_name}}). |
| `id` | `string` |  | Unique identifier for the CLI template. |
| `name` | `string` |  | Name of the CLI template. |
| `reload` | `boolean` |  | Flag indicating whether to reload the switch after applying the CLI commands (default: false). |
| `variables` | `array` |  | Set of template variables that can be customized for each switch when applying the CLI template. |
| `venueSwitches` | `array` |  | List of venue switches to which this CLI template will be applied. |


**Responses:**

- `200` OK → `Switch_Services_AcxCliTemplate_V1`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/cliTemplates/examples`

**Get Examples**

Get a list of command line interface template examples.

operationId: `GetCliTemplates_2_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `category` | query |  | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_CliTemplateSample_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/cliTemplates/query`

**Query Command Line Interface Templates**

Get a list of command line interface templates by query.

operationId: `QueryCliTemplates_1_1`


**Request Body:** `Switch_Services_SearchableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `searchString` | `string` |  | The search string for full text search across the specified target fields. |
| `searchTargetFields` | `array` |  | The list of field names to search within when applying the search string. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/cliTemplates/{cliTemplateId}`

**Delete Command Line Interface Template**

Delete a command line interface template by id.

operationId: `DeleteCliTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `cliTemplateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/cliTemplates/{cliTemplateId}`

**Get Command Line Interface Template**

Get a command line interface template by id.

operationId: `GetCliTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `cliTemplateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AcxCliTemplate_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/cliTemplates/{cliTemplateId}`

**Update Command Line Interface Template**

Update a command line interface template for switches by id.

operationId: `UpdateCliTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `cliTemplateId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AcxCliTemplateBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `applyLater` | `boolean` |  | Flag indicating whether to apply the CLI template later rather than immediately (default: false). |
| `cli` | `string` |  | The CLI command template content with variable placeholders (e.g., {{variable_name}}). |
| `id` | `string` |  | Unique identifier for the CLI template. |
| `name` | `string` |  | Name of the CLI template. |
| `reload` | `boolean` |  | Flag indicating whether to reload the switch after applying the CLI commands (default: false). |
| `variables` | `array` |  | Set of template variables that can be customized for each switch when applying the CLI template. |
| `venueSwitches` | `array` |  | List of venue switches to which this CLI template will be applied. |


**Responses:**

- `200` OK → `Switch_Services_AcxCliTemplate_V1`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/cliTemplates/{cliTemplateId}`

**Disassociate Command Line Interface Templates**

Disassociate command line interface templates to switches.

operationId: `DisassociateCliTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `cliTemplateId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/cliTemplates/{cliTemplateId}`

**Associate Command Line Interface Templates**

Associate command line interface templates to switches.

operationId: `AssociateCliTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `cliTemplateId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Configuration History

*Retrieve switch configuration history records.*


*6 endpoints*


### `POST` `/switches/{switchId}/configHistDetails/query`

**Get Configuration History**

Query for configuration history details on this switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configHistDetails/query can be used for this content.

operationId: `GetAllConfigurationHistDetailsBySwitch_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigurationHistoryDetailRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filterByConfigType` | `string` |  | The configuration type filter to limit results to specific types such as VLAN, ACL, or port configurations. |
| `filterByStatus` | `string` |  | The status filter to limit results to configuration deployments with specific status values such as success, failed, or in progress. |
| `filters` | `Switch_Services_ConfigurationHistoryFilter` |  | The comprehensive filter object containing multiple filter criteria in the new request format. |
| `limit` | `integer` |  | The maximum number of configuration history records to return per page, defaulting to 8. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The page size for pagination in the new request format, superseding the limit parameter when provided. |
| `sortField` | `string` |  | The sort column for ordering configuration history records in the new request format. |
| `sortInfo` | `Switch_Services_ConfigurationHistoryDetailSortInfo` |  | The sorting information specifying the sort column and direction for ordering configuration history records. |
| `sortOrder` | `string` |  | The sort order direction, either ascending or descending, for the new request format. |


**Responses:**

- `200` OK → `Switch_Services_ConfigurationHistory_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/transactions/{transactionId}/configHistDetails`

**Get Configuration History**

Get the configuration history details of this transaction on this switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/transactions/{transactionId}/configHistDetails can be used for this content.

operationId: `RetrieveSwitchConfigurationHistDetailByTransaction_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |
| `transactionId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ConfigurationHistory_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/configHistories/query`

**Get Configuration History**

Query for configuration history details for switches in this venue.

operationId: `GetConfigurationHistoryByVenue_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigurationHistoryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filterByConfigType` | `string` |  | Filter configuration history by configuration type. |
| `filters` | `Switch_Services_ConfigurationHistoryFilter` |  | Filter criteria for configuration history records. |
| `limit` | `integer` |  | Number of records per page (deprecated, use pageSize instead, default: 8). |
| `page` | `integer` |  | Page number for pagination. |
| `pageSize` | `integer` |  | Number of records per page for the new request format. |
| `sortField` | `string` |  | Field to sort by (currently only supports startTime). |
| `sortInfo` | `Switch_Services_SortInfo` |  | Sort information for ordering configuration history records (deprecated, use sortField and sortOrder instead). |
| `sortOrder` | `string` |  | Sort order (ASC or DESC). |


**Responses:**

- `200` OK → `Switch_Services_ConfigurationHistoryVenue_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/configHistDetails/query`

**Get Configuration History**

Query for configuration history details on this switch.

operationId: `GetAllConfigurationHistDetailsBySwitch`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigurationHistoryQueryRequest_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filterByConfigType` | `string` |  | The configuration type filter to limit results to specific types of configuration deployments. |
| `page` | `integer` |  | The page number for pagination, starting from 1. |
| `pageSize` | `integer` |  | The number of records to return per page. |
| `sortField` | `string` |  | The field name used to sort the configuration history records. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending. |


**Responses:**

- `200` OK → `Switch_Services_ConfigurationHistory_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/transactions/{transactionId}/configHistDetails`

**Get Configuration History**

Get the configuration history details of this transaction on this switch.

operationId: `RetrieveSwitchConfigurationHistDetailByTransaction`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `transactionId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ConfigurationHistory_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/transactions/{transactionId}/configHistDetails`

**Get Configuration History**

Get the configuration history details for this transaction relative to the switches in this venue.

operationId: `GetVenueConfigurationHistoryDetailByTransaction_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `transactionId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigurationHistoryDetailRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filterByConfigType` | `string` |  | The configuration type filter to limit results to specific types such as VLAN, ACL, or port configurations. |
| `filterByStatus` | `string` |  | The status filter to limit results to configuration deployments with specific status values such as success, failed, or in progress. |
| `filters` | `Switch_Services_ConfigurationHistoryFilter` |  | The comprehensive filter object containing multiple filter criteria in the new request format. |
| `limit` | `integer` |  | The maximum number of configuration history records to return per page, defaulting to 8. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The page size for pagination in the new request format, superseding the limit parameter when provided. |
| `sortField` | `string` |  | The sort column for ordering configuration history records in the new request format. |
| `sortInfo` | `Switch_Services_ConfigurationHistoryDetailSortInfo` |  | The sorting information specifying the sort column and direction for ordering configuration history records. |
| `sortOrder` | `string` |  | The sort order direction, either ascending or descending, for the new request format. |


**Responses:**

- `200` OK → `Switch_Services_ConfigurationHistory_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## DHCP Server

*Manage ICX DHCP servers.*


*15 endpoints*


### `POST` `/switches/dhcpServers/query`

**Query DHCP Servers**

List of venue's DHCP servers. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers/query can be used for this content.

operationId: `ListOfVenueDhcpServers`


**Request Body:** `Switch_Services_DhcpServerQueryRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |
| `venueId` | `string` |  | The venue identifier to filter DHCP server configurations by specific venue. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/dhcpServers/{dhcpServerId}`

**Get DHCP Server Setting**

Get switch's DHCP server setting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers/{dhcpServerId} can be used for this content.

operationId: `GetSwitchDhcpServerSetting_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_DHCPServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/dhcpServerStateSettings`

**Update DHCP Server**

Change switch's DHCP server state. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServerStates with PATCH method can be used for this content.

operationId: `ChangeSwitchDhcpServerState`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServerStateRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `state` | `boolean` |  | DHCP server state (true to enable, false to disable). |


**Responses:**

- `200` OK → `Switch_Services_DHCPServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/{switchId}/dhcpServers`

**Delete DHCP Servers**

Delete switch's DHCP servers. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers can be used for this content.

operationId: `DeleteSwitchDhcpServerSettings_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/dhcpServers`

**Add DHCP Server**

Add switch's DHCP server settings. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers can be used for this content.

operationId: `AddSwitchDhcpServerSettings_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServerBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultRouterIp` | `string` |  | Default gateway IP address to be assigned to DHCP clients. |
| `dhcpOptions` | `array` |  | List of additional DHCP options (e.g., DNS server, domain name). |
| `dhcpServerEnabled` | `boolean` |  | Flag indicating whether the DHCP server is enabled on the switch. |
| `excludedEnd` | `string` |  | End IP address of the excluded range (addresses not to be assigned). |
| `excludedStart` | `string` |  | Start IP address of the excluded range (addresses not to be assigned). |
| `id` | `string` |  | Unique identifier for the DHCP server configuration. |
| `leaseDays` | `integer` |  | Lease duration in days. |
| `leaseHrs` | `integer` |  | Lease duration in hours. |
| `leaseMins` | `integer` |  | Lease duration in minutes. |
| `network` | `string` |  | Network address in CIDR notation (e.g., 192.168.1.0/24). |
| `poolName` | `string` |  | Name of the DHCP address pool (must be unique). |
| `prefixLength` | `string` |  | Network prefix length (CIDR notation, e.g., 24 for /24). |
| `subnetAddress` | `string` |  | Subnet address extracted from the network configuration. |
| `subnetMask` | `string` |  | Subnet mask for the DHCP pool network (e.g., 255.255.255.0). |
| `switchId` | `string` |  | Switch identifier (serial number) where this DHCP server is configured. |


**Responses:**

- `200` OK → `Switch_Services_DHCPServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/{switchId}/dhcpServers`

**Update DHCP Server Setting**

Update switch's DHCP server setting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers/{dhcpServerId} can be used for this content.

operationId: `UpdateSwitchDhcpServerSettings_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServerBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultRouterIp` | `string` |  | Default gateway IP address to be assigned to DHCP clients. |
| `dhcpOptions` | `array` |  | List of additional DHCP options (e.g., DNS server, domain name). |
| `dhcpServerEnabled` | `boolean` |  | Flag indicating whether the DHCP server is enabled on the switch. |
| `excludedEnd` | `string` |  | End IP address of the excluded range (addresses not to be assigned). |
| `excludedStart` | `string` |  | Start IP address of the excluded range (addresses not to be assigned). |
| `id` | `string` |  | Unique identifier for the DHCP server configuration. |
| `leaseDays` | `integer` |  | Lease duration in days. |
| `leaseHrs` | `integer` |  | Lease duration in hours. |
| `leaseMins` | `integer` |  | Lease duration in minutes. |
| `network` | `string` |  | Network address in CIDR notation (e.g., 192.168.1.0/24). |
| `poolName` | `string` |  | Name of the DHCP address pool (must be unique). |
| `prefixLength` | `string` |  | Network prefix length (CIDR notation, e.g., 24 for /24). |
| `subnetAddress` | `string` |  | Subnet address extracted from the network configuration. |
| `subnetMask` | `string` |  | Subnet mask for the DHCP pool network (e.g., 255.255.255.0). |
| `switchId` | `string` |  | Switch identifier (serial number) where this DHCP server is configured. |


**Responses:**

- `200` OK → `Switch_Services_DHCPServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/dhcpServers/query`

**Query DHCP Servers**

List of ICX's DHCP servers. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers/query can be used for this content.

operationId: `ListOfIcxDhcpServers_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServerQueryRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |
| `venueId` | `string` |  | The venue identifier to filter DHCP server configurations by specific venue. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/{switchId}/dhcpServers/{dhcpServerId}`

**Delete DHCP Server Setting**

Delete switch's DHCP server setting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/dhcpServers/{dhcpServerId} can be used for this content.

operationId: `DeleteSwitchDhcpServerSetting_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |
| `dhcpServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/switches/{switchId}/dhcpServerStates`

**Change Switch DHCP Server State**

Change switch's DHCP server state. Use activity API with request id to get the status update.

operationId: `ChangeSwitchDhcpServerState_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServerState_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `state` | `boolean` |  | The operational state of the DHCP server, where true indicates enabled and false indicates disabled. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/dhcpServers`

**Delete DHCP Servers**

Delete switch's DHCP servers.

operationId: `DeleteSwitchDhcpServerSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `204` No Content → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/dhcpServers`

**Add DHCP Server**

Add switch's DHCP server settings. Use activity API with request id to get the status update.

operationId: `AddSwitchDhcpServerSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServer_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultRouterIp` | `string` |  | The default gateway IP address provided to DHCP clients. |
| `dhcpOptions` | `array` |  | The list of additional DHCP options to be provided to clients. |
| `excludedEnd` | `string` |  | The ending IP address of the excluded address range that will not be assigned to clients. |
| `excludedStart` | `string` |  | The starting IP address of the excluded address range that will not be assigned to clients. |
| `id` | `string` |  |  |
| `leaseDays` | `integer` |  | The number of days in the DHCP lease duration. |
| `leaseHrs` | `integer` |  | The number of hours in the DHCP lease duration. |
| `leaseMins` | `integer` |  | The number of minutes in the DHCP lease duration. |
| `poolName` | `string` |  | The name of the DHCP address pool. |
| `subnetAddress` | `string` |  | The subnet network address for the DHCP pool. |
| `subnetMask` | `string` |  | The subnet mask for the DHCP network. |


**Responses:**

- `201` Created → `Switch_Services_DhcpServerResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/dhcpServers/query`

**Query DHCP Servers**

List of ICX DHCP servers.

operationId: `ListOfIcxDhcpServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/dhcpServers/{dhcpServerId}`

**Delete DHCP Server Setting**

Delete switch's DHCP server setting.

operationId: `DeleteSwitchDhcpServerSetting`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `dhcpServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/dhcpServers/{dhcpServerId}`

**Get DHCP Server Setting**

Get switch's DHCP server setting.

operationId: `GetSwitchDhcpServerSetting`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `dhcpServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_DhcpServer_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/dhcpServers/{dhcpServerId}`

**Update DHCP Server Setting**

Update switch's DHCP server setting.

operationId: `UpdateSwitchDhcpServerSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `dhcpServerId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DhcpServer_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultRouterIp` | `string` |  | The default gateway IP address provided to DHCP clients. |
| `dhcpOptions` | `array` |  | The list of additional DHCP options to be provided to clients. |
| `excludedEnd` | `string` |  | The ending IP address of the excluded address range that will not be assigned to clients. |
| `excludedStart` | `string` |  | The starting IP address of the excluded address range that will not be assigned to clients. |
| `id` | `string` |  |  |
| `leaseDays` | `integer` |  | The number of days in the DHCP lease duration. |
| `leaseHrs` | `integer` |  | The number of hours in the DHCP lease duration. |
| `leaseMins` | `integer` |  | The number of minutes in the DHCP lease duration. |
| `poolName` | `string` |  | The name of the DHCP address pool. |
| `subnetAddress` | `string` |  | The subnet network address for the DHCP pool. |
| `subnetMask` | `string` |  | The subnet mask for the DHCP network. |


**Responses:**

- `200` OK → `Switch_Services_DhcpServerResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## ICX Switch

*Manage ICX switch settings.*


*20 endpoints*


### `DELETE` `/stacks/{stackSwitchSerialNumber}`

**Delete Stack Member**

Delete a specific stack member. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/stacks/{stackSwitchSerialNumber} can be used for this content.

operationId: `DeleteStackMember_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `stackSwitchSerialNumber` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches`

**Delete ICX Switches**

Delete multiple ICX switches. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches can be used for this content.

operationId: `DeleteMultipleSwitches_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches`

**Get ICX Switches**

List of tenant's ICX switches. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches can be used for this content.

operationId: `GetSwitchesOfTenant`


**Responses:**

- `200` OK → `Switch_Services_IcxSwitch_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches`

**Add ICX Switches**

Add multiple ICX switches. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches can be used for this content.

operationId: `AddMultipleSwitches_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/deviceRequests`

**Create Multiple Device Requests**

Execute sync venues admin password on multiple switch devices, switch id list should be provided on the request body. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/deviceRequests can be used for this content.

operationId: `SyncVenueAdminPasswordMultipleDeviceRequests_1`


**Request Body:** `Switch_Services_DeviceRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `deviceRequestAction` | `string` |  | Action to be performed on the specified devices (e.g., reboot, upgrade, delete). |
| `switchIdList` | `array` |  | List of switch identifiers (serial numbers or IDs) to perform the action on. |


**Responses:**

- `200` OK → `Switch_Services_SyncAdminPassword_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/{switchId}`

**Delete ICX Switch**

Delete ICX switch by id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId} can be used for this content.

operationId: `DeleteSwitchById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}`

**Get ICX Switch**

Get ICX switch by id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId} can be used for this content.

operationId: `GetSwitchById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_IcxSwitch_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/{switchId}`

**Update ICX Switch**

Update ICX switch. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId} can be used for this content.

operationId: `UpdateSwitchById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AddSwitchBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultGateway` | `string` |  | Default gateway IP address for the switch management interface. |
| `description` | `string` |  | Description or notes for the switch. |
| `dhcpClientEnabled` | `boolean` |  | Flag indicating whether DHCP client is enabled for obtaining IP address (default: true). |
| `dhcpServerEnabled` | `boolean` |  | Flag indicating whether DHCP server is enabled on the switch (default: false). |
| `displayOfStack` | `string` |  | Display string representing the stack configuration. |
| `enableStack` | `boolean` |  | Flag indicating whether stacking is enabled on this switch. |
| `firmwareVersion` | `string` |  | Current firmware version installed on the switch. |
| `id` | `string` |  | Unique identifier for the switch (typically the serial number). |
| `igmpSnooping` | `string` |  | IGMP snooping configuration status (e.g., enabled, disabled). |
| `initialVlanId` | `integer` |  | Initial VLAN ID for the switch management interface. |
| `ipAddress` | `string` |  | Static IP address assigned to the switch management interface. |
| `ipAddressInterface` | `string` |  | Interface name or number for the IP address assignment (e.g., ve1, ethernet1/1/1). |
| `ipAddressInterfaceType` | `string` |  | Type of interface for IP address assignment (e.g., VE, ETHERNET). |
| `ipAddressType` | `string` |  | IP address assignment type (static or dynamic). |
| `jumboMode` | `boolean` |  | Flag indicating whether jumbo frame mode is enabled (default: false). |
| `lastDataSyncTime` | `string` |  | Timestamp of the last successful data synchronization from the switch. |
| `lastDataSyncTriggerTime` | `string` |  | Timestamp when the last data synchronization was triggered. |
| `model` | `string` |  | Switch model (e.g., ICX7150, ICX7250, ICX7450). |
| `name` | `string` |  | Name or hostname for the switch. |
| `position` | `string` |  | Physical position or location description of the switch. |
| `previousMembers` | `array` |  | Set of serial numbers of previous stack members. |
| `rearModule` | `string` |  | Rear module configuration for the switch (e.g., 'none', 'stack-40g' for ICX7650). |
| `softDeletedDate` | `string` |  | Timestamp when the switch was soft deleted (marked for deletion). |
| `spanningTreePriority` | `integer` |  | STP (Spanning Tree Protocol) priority value for this switch (0-61440, in increments of 4096). |
| `specifiedType` | `string` |  | Specified firmware image type for the switch (e.g., ROUTER, SWITCH). |
| *… 10 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_IcxSwitch_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/deviceRequests`

**Sync or Reboot ICX Device**

Execute sync or reboot command on the specified switch device, no need to provide switch id list on the request body. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/deviceRequests can be used for this content.

operationId: `DeviceRequests_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DeviceRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `deviceRequestAction` | `string` |  | Action to be performed on the specified devices (e.g., reboot, upgrade, delete). |
| `switchIdList` | `array` |  | List of switch identifiers (serial numbers or IDs) to perform the action on. |


**Responses:**

- `200` OK → `Switch_Services_StringErrorCodeResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/deviceRequests`

**Create Multiple Device Requests**

Execute sync venues admin password on multiple switch devices, switch id list should be provided on the request body.

operationId: `SyncVenueAdminPasswordMultipleDeviceRequests`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DeviceRequest_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `deviceRequestAction` | `string` |  | The request action to the switches. |
| `switchIdList` | `array` |  | The list of switch id. |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/stacks/{stackSwitchSerialNumber}`

**Delete Stack Member**

Delete a specific stack member.

operationId: `DeleteStackMember`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `stackSwitchSerialNumber` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches`

**Delete ICX Switches**

Delete multiple ICX switches.

operationId: `DeleteMultipleSwitches`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches`

**Retrieve ICX Switches**

Retrieve list of venues' ICX switches.

operationId: `GetSwitchesByVenue_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_IcxSwitch_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches`

**Add ICX Switches**

Add multiple ICX switches. Use activity API with request id to get the status update.

operationId: `AddMultipleSwitches`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}`

**Delete ICX Switch**

Delete ICX switch by id.

operationId: `DeleteSwitchById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}`

**Get ICX Switch**

Get ICX switch by id.

operationId: `GetSwitchById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_IcxSwitch_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}`

**Add ICX Switch**

Add an ICX switch. Use activity API with request id to get the status update.

operationId: `AddSwitch`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_IcxSwitch_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `StackMembers_V1_1` | `array` |  | The list of member switches in a stack configuration, including their models and active status. |
| `configBackupNaming` | `Switch_Services_ConfigBackupNaming_V1_0` |  | Configuration backup file naming settings for this switch. |
| `defaultGateway` | `string` |  | The default gateway IP address for routing traffic from the switch management interface. |
| `description` | `string` |  | The descriptive text providing additional information about the switch configuration or purpose. |
| `dhcp6ServerEnabled` | `boolean` |  | The flag indicating whether the DHCPv6 server feature is enabled on the switch. |
| `dhcpClientEnabled` | `boolean` |  | The flag indicating whether the switch is configured as a DHCP client to obtain its management IP address. |
| `dhcpServerEnabled` | `boolean` |  | The flag indicating whether the DHCP server feature is enabled on the switch. |
| `enableStack` | `boolean` |  | The flag indicating whether switch stacking is enabled for combining multiple physical switches into a single logical unit. |
| `id` | `string` |  |  |
| `igmpSnooping` | `string` |  | The IGMP snooping mode for multicast traffic optimization: enabled, disabled, or default. |
| `initialVlanId` | `integer` |  | The VLAN ID used for initial switch configuration and management access. |
| `ipAddress` | `string` |  | The IPv4 address assigned to the switch management interface. |
| `ipAddressInterface` | `string` |  | The specific interface identifier for the management IP address configuration. |
| `ipAddressInterfaceType` | `string` |  | The interface type for the switch management IP address: VLAN interface or management port. |
| `ipAddressType` | `string` |  | The IP address assignment method: static or DHCP. |
| `jumboMode` | `boolean` |  | The flag indicating whether jumbo frame support is enabled, allowing frames larger than 1518 bytes. |
| `name` | `string` |  | The name assigned to the ICX switch for identification in the network. |
| `rearModule` | `string` |  | The model identifier of the rear expansion module installed on the switch, if applicable. |
| `spanningTreePriority` | `integer` |  | The STP (Spanning Tree Protocol) bridge priority value, used in root bridge election (lower values have higher priority). |
| `specifiedType` | `string` |  | The firmware image type specified for the switch: primary, secondary, or boot. |
| `subnetMask` | `string` |  | The subnet mask for the switch management IP address. |
| `vlanCustomize` | `boolean` |  | The flag indicating whether VLAN configurations have been customized from default settings. |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}`

**Update ICX Switch**

Update ICX switch. Use activity API with request id to get the status update.

operationId: `UpdateSwitchById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_IcxSwitch_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `StackMembers_V1_1` | `array` |  | The list of member switches in a stack configuration, including their models and active status. |
| `configBackupNaming` | `Switch_Services_ConfigBackupNaming_V1_0` |  | Configuration backup file naming settings for this switch. |
| `defaultGateway` | `string` |  | The default gateway IP address for routing traffic from the switch management interface. |
| `description` | `string` |  | The descriptive text providing additional information about the switch configuration or purpose. |
| `dhcp6ServerEnabled` | `boolean` |  | The flag indicating whether the DHCPv6 server feature is enabled on the switch. |
| `dhcpClientEnabled` | `boolean` |  | The flag indicating whether the switch is configured as a DHCP client to obtain its management IP address. |
| `dhcpServerEnabled` | `boolean` |  | The flag indicating whether the DHCP server feature is enabled on the switch. |
| `enableStack` | `boolean` |  | The flag indicating whether switch stacking is enabled for combining multiple physical switches into a single logical unit. |
| `id` | `string` |  |  |
| `igmpSnooping` | `string` |  | The IGMP snooping mode for multicast traffic optimization: enabled, disabled, or default. |
| `initialVlanId` | `integer` |  | The VLAN ID used for initial switch configuration and management access. |
| `ipAddress` | `string` |  | The IPv4 address assigned to the switch management interface. |
| `ipAddressInterface` | `string` |  | The specific interface identifier for the management IP address configuration. |
| `ipAddressInterfaceType` | `string` |  | The interface type for the switch management IP address: VLAN interface or management port. |
| `ipAddressType` | `string` |  | The IP address assignment method: static or DHCP. |
| `jumboMode` | `boolean` |  | The flag indicating whether jumbo frame support is enabled, allowing frames larger than 1518 bytes. |
| `name` | `string` |  | The name assigned to the ICX switch for identification in the network. |
| `rearModule` | `string` |  | The model identifier of the rear expansion module installed on the switch, if applicable. |
| `spanningTreePriority` | `integer` |  | The STP (Spanning Tree Protocol) bridge priority value, used in root bridge election (lower values have higher priority). |
| `specifiedType` | `string` |  | The firmware image type specified for the switch: primary, secondary, or boot. |
| `subnetMask` | `string` |  | The subnet mask for the switch management IP address. |
| `vlanCustomize` | `boolean` |  | The flag indicating whether VLAN configurations have been customized from default settings. |


**Responses:**

- `200` OK → `Switch_Services_IcxSwitchResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/deviceRequests`

**Sync or Reboot ICX Device**

Execute sync or reboot command on the specified switch device.

operationId: `DeviceRequests`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_DeviceRequest_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `deviceRequestAction` | `string` |  | The request action to the switches. |
| `switchIdList` | `array` |  | The list of switch id. |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/positions`

**Update Switch Position**

Update ICX switch position in the floor plan.

operationId: `UpdateSwitchPosition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_SwitchPosition_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `floorPlanId` | `string` |  | The unique identifier of the floor plan where the switch is located. |
| `xPercent` | `number` |  | The horizontal position of the switch on the floor plan as a percentage of the total width, ranging from 0.0 to 100.0. |
| `yPercent` | `number` |  | The vertical position of the switch on the floor plan as a percentage of the total height, ranging from 0.0 to 100.0. |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Import Switch

*Import and register new switches.*


*4 endpoints*


### `POST` `/venues/switches`

**Add Switches**

Add switches by CSV file. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/importRequests can be used for this content.

operationId: `ImportSwitches_1`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/switches/csvFile`

**Add Switches**

Add switches cross venues by CSV file. Use activity API with request id to get the status update.

operationId: `ImportSwitches_2`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/importRequests`

**Add Switches**

Add switches by CSV file. Use activity API with request id to get the status update.

operationId: `ImportSwitches`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/importResults`

**Get Download URL and Result**

Get download URL and import result.

operationId: `GetSwitchesImportResult`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `operationRequestId` | query | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ImportSwitchResult_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## LAG

*Manage LAGs (link aggregation groups).*


*12 endpoints*


### `DELETE` `/switches/lags`

**Delete LAGs**

Delete switch's multiple LAG settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/lags can be used for this content.

operationId: `DeleteLags_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/lags/{lagId}`

**Delete LAG**

Delete switch's LAG setting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/lags/{lagId} can be used for this content.

operationId: `DeleteLag_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `lagId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/lags/{lagId}`

**Get LAG**

Get LAG setting by id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/lags/{lagId} can be used for this content.

operationId: `GetLag_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `lagId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Lag_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/lags/{lagId}`

**Update LAG**

Update switch's LAG setting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/lags/{lagId} can be used for this content.

operationId: `UpdateLag_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `lagId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_LagBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `addPorts` | `array` |  | List of port identifiers to be added to this LAG. |
| `defaultVlanId` | `string` |  | Default VLAN ID of the switch (typically '1'). |
| `forceUpPort` | `string` |  | Port identifier that is forced to be in 'up' state to keep the LAG operational. |
| `id` | `string` |  | Unique identifier for the LAG. |
| `lagId` | `integer` |  | LAG identifier number (1-255, must be unique on the switch). |
| `lastName` | `string` |  | Previous name of the LAG before renaming. |
| `name` | `string` |  | Name of the LAG (1-64 characters, cannot contain quotes). |
| `originalUntaggedVlan` | `string` |  | Original untagged VLAN ID before any modifications. |
| `portAddVlans` | `array` |  | List of port VLAN configurations to be added for LAG member ports. |
| `portVlans` | `array` |  | List of port VLAN configurations for LAG member ports. |
| `ports` | `array` |  | Set of physical port identifiers that are members of this LAG (e.g., ['1/1/1', '1/1/2']). |
| `removePorts` | `array` |  | List of port identifiers to be removed from this LAG. |
| `switchId` | `string` |  | Switch identifier (serial number) where this LAG is configured. |
| `taggedVlans` | `array` |  | Set of tagged VLAN IDs assigned to this LAG interface. |
| `type` | `string` |  | IP address type for the LAG interface (static or dynamic). |
| `untaggedVlan` | `string` |  | Untagged VLAN ID (native VLAN) for this LAG interface. |


**Responses:**

- `200` OK → `Switch_Services_Lag_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/lags`

**Get LAGs**

List of switch's LAG settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/lags can be used for this content.

operationId: `GetLags_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Lag_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/lags`

**Add LAGs**

Add switch's multiple LAG settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/lags can be used for this content.

operationId: `AddLags_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_Lag_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/lags`

**Delete LAGs**

Delete switch's multiple LAG settings.

operationId: `DeleteLags`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/lags`

**Get LAGs**

List of switch's LAG settings.

operationId: `GetLags`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/lags`

**Add LAGs**

Add switch's multiple LAG settings.

operationId: `AddLags`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `201` Created → `Switch_Services_LagResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/lags/{lagId}`

**Delete LAG**

Delete switch's LAG setting.

operationId: `DeleteLag`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/lags/{lagId}`

**Get LAG**

Get LAG setting by id.

operationId: `GetLag`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Lag_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/lags/{lagId}`

**Update LAG**

Update switch's LAG setting.

operationId: `UpdateLag`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_LagDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `forceUpPort` | `string` |  | The port identifier to force into an up state within the LAG. |
| `name` | `string` |  | The name of the LAG interface. |
| `ports` | `array` |  | The set of physical port identifiers that are members of this LAG. |
| `taggedVlans` | `array` |  | The set of VLAN identifiers that are tagged on this LAG interface. |
| `type` | `string` |  | The type of LAG protocol, such as static or LACP (Link Aggregation Control Protocol). |
| `untaggedVlan` | `string` |  | The VLAN identifier for untagged traffic on this LAG interface. |


**Responses:**

- `200` OK → `Switch_Services_LagResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Profile

*Manage switch profiles and profile configurations.*


*10 endpoints*


### `DELETE` `/switchProfiles`

**Delete Switch Profiles**

Delete multiple regular switch profiles or command line interface profiles. This method will be removed no sooner than 06/30/2026. The following URL /switchProfiles/{switchProfileId} can be used for this content.

operationId: `DeleteProfiles`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles`

**Get Switch Profiles**

Get multiple regular switch profiles or command line interface profiles. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switchProfiles can be used for this content.

operationId: `GetProfiles`


**Responses:**

- `200` OK → `Switch_Services_Profile_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchProfiles`

**Add Switch Profile**

Add a regular switch profile or command line interface profile. Use activity API with request id to get the status update.

operationId: `AddProfile_1`


**Request Body:** `Switch_Services_ProfileBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acls` | `array` |  | Set of ACL (Access Control List) configurations included in this profile. |
| `applyOnboardOnly` | `boolean` |  | Flag indicating whether this profile should only be applied during switch onboarding. |
| `description` | `string` |  | Profile description providing additional details about the configuration purpose. |
| `id` | `string` |  | Unique identifier for the profile. |
| `isTemplate` | `boolean` |  | Flag indicating whether this profile is a template that can be used to create other profiles (default: false). |
| `name` | `string` |  | Profile name (1-64 characters). |
| `portProfileMappings` | `array` |  | Set of mappings between port profiles and this configuration profile. |
| `profileType` | `string` |  | Profile type (Regular, CLI). |
| `templateId` | `string` |  | Identifier of the template that this profile was created from (if applicable). |
| `templateVersion` | `integer` |  | Version number of the template being used. |
| `trustedPorts` | `array` |  | Set of trusted port configurations for QoS and security settings. |
| `venueCliTemplate` | `Switch_Services_AcxVenueCliTemplateBo_V1` |  | Venue level CLI template configuration to be executed on switches. |
| `venues` | `array` |  | List of venue identifiers where this profile is applied. |
| `vlans` | `array` |  | Set of VLAN configurations included in this profile. |
| `voiceVlanConfigs` | `array` |  | Set of voice VLAN configurations for IP phones and voice devices. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchProfiles/query`

**Query Switch Profiles**

List the regular switch profiles or command line interface profiles.

operationId: `QueryProfiles_1_1`


**Request Body:** `Switch_Services_SearchableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `searchString` | `string` |  | The search string for full text search across the specified target fields. |
| `searchTargetFields` | `array` |  | The list of field names to search within when applying the search string. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switchProfiles/{switchProfileId}`

**Delete Switch Profile**

Delete a regular switch profile or command line interface profile.

operationId: `DeleteProfileById_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles/{switchProfileId}`

**Get Switch Profile**

Get a regular switch profile or command line interface profile.

operationId: `GetProfileById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Profile_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switchProfiles/{switchProfileId}`

**Update Switch Profile**

Update a regular switch profile or command line interface profile. Use activity API with request id to get the status update.

operationId: `UpdateProfile_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ProfileBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acls` | `array` |  | Set of ACL (Access Control List) configurations included in this profile. |
| `applyOnboardOnly` | `boolean` |  | Flag indicating whether this profile should only be applied during switch onboarding. |
| `description` | `string` |  | Profile description providing additional details about the configuration purpose. |
| `id` | `string` |  | Unique identifier for the profile. |
| `isTemplate` | `boolean` |  | Flag indicating whether this profile is a template that can be used to create other profiles (default: false). |
| `name` | `string` |  | Profile name (1-64 characters). |
| `portProfileMappings` | `array` |  | Set of mappings between port profiles and this configuration profile. |
| `profileType` | `string` |  | Profile type (Regular, CLI). |
| `templateId` | `string` |  | Identifier of the template that this profile was created from (if applicable). |
| `templateVersion` | `integer` |  | Version number of the template being used. |
| `trustedPorts` | `array` |  | Set of trusted port configurations for QoS and security settings. |
| `venueCliTemplate` | `Switch_Services_AcxVenueCliTemplateBo_V1` |  | Venue level CLI template configuration to be executed on switches. |
| `venues` | `array` |  | List of venue identifiers where this profile is applied. |
| `vlans` | `array` |  | Set of VLAN configurations included in this profile. |
| `voiceVlanConfigs` | `array` |  | Set of voice VLAN configurations for IP phones and voice devices. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switchProfiles`

**Get Switch Profiles**

Get regular switch profiles or command line interface profiles of the venue.

operationId: `GetProfilesByVenueId_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Profile_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switchProfiles/{switchProfileId}`

**Disassociate Switch Profile to Venue**

Disassociate a switch profile to a venue.

operationId: `DisassociateProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switchProfiles/{switchProfileId}`

**Associate Switch Profile to Venue**

Associate a switch profile to a venue.

operationId: `AssociateProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Profile ACL

*Manage ACL (access control list) of switch profile.*


*7 endpoints*


### `DELETE` `/switchProfiles/{switchProfileId}/acls`

**Delete ACLs**

Delete multiple ACLs of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `DeleteProfileAcls`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles/{switchProfileId}/acls`

**Get ACLs**

Get multiple ACLs of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `GetAcls`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `page` | query |  | `integer` |  |
| `size` | query |  | `integer` |  |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchProfiles/{switchProfileId}/acls`

**Add ACL**

Add the ACL of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `AddProfileAcl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AclBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `aclRules` | `array` |  | Set of ACL rules defining the traffic filtering behavior. |
| `aclType` | `string` |  | Type of ACL (STANDARD, EXTENDED, IPV6). |
| `id` | `string` |  | Unique identifier for the ACL. |
| `name` | `string` |  | Name of the ACL (must be unique within the switch). |
| `switchId` | `string` |  | Switch identifier (MAC address) where this ACL is applied. |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switchProfiles/{switchProfileId}/acls/{aclId}`

**Delete ACL**

Delete ACL of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `DeleteProfileAcl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `aclId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles/{switchProfileId}/acls/{aclId}`

**Get ACL**

Get the ACL of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `GetAclById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `aclId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switchProfiles/{switchProfileId}/acls/{aclId}`

**Update ACL**

Update the ACL of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `UpdateProfileAcl`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `aclId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AclBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `aclRules` | `array` |  | Set of ACL rules defining the traffic filtering behavior. |
| `aclType` | `string` |  | Type of ACL (STANDARD, EXTENDED, IPV6). |
| `id` | `string` |  | Unique identifier for the ACL. |
| `name` | `string` |  | Name of the ACL (must be unique within the switch). |
| `switchId` | `string` |  | Switch identifier (MAC address) where this ACL is applied. |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switchProfiles/acls`

**Get ACLs**

Get all ACLs of switch profiles in the venue. This method will be removed no sooner than 06/30/2026.

operationId: `GetAclsByVenueId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Profile Template

*Manage switch profile templates.*


*10 endpoints*


### `DELETE` `/templates/switchProfiles`

**Delete Switch Profile Templates**

Delete multiple regular switch profile templates or command line interface profile templates. This method will be removed no sooner than 06/30/2026. The following URL /templates/switchProfiles/{switchProfileId} can be used for this content.

operationId: `DeleteProfileTemplates`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/templates/switchProfiles`

**Get Switch Profile Templates**

Get multiple regular switch profile templates or command line interface profile templates. This method will be removed no sooner than 06/30/2026. The following URL /templates/switchProfiles/{switchProfileId} can be used for this content.

operationId: `GetProfileTemplates`


**Responses:**

- `200` OK → `Switch_Services_Profile_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/templates/switchProfiles`

**Add Switch Profile Template**

Add a regular switch profile template or command line interface profile template. Use activity API with request id to get the status update.

operationId: `AddProfileTemplate_1_1`


**Request Body:** `Switch_Services_ProfileDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acls` | `array` |  | The set of Access Control List configurations to be applied as part of this profile. |
| `applyOnboardOnly` | `boolean` |  | The flag indicating whether this profile should only be applied during the initial switch onboarding process. |
| `description` | `string` |  | The descriptive text providing details about the purpose and usage of this profile. |
| `id` | `string` |  |  |
| `name` | `string` |  | The unique name identifier for this switch configuration profile. |
| `profileType` | `string` |  | The profile type indicating whether this is a port profile, switch profile, or other profile type. |
| `trustedPorts` | `array` |  | The set of trusted port configurations for DHCP snooping and ARP inspection security features. |
| `venueCliTemplate` | `Switch_Services_AcxVenueCliTemplate_V1_1` |  | The venue level CLI template configuration containing custom command line interface commands for this profile. |
| `vlans` | `array` |  | The set of VLAN configurations defining VLANs to be created or managed by this profile. |
| `voiceVlanConfigs` | `array` |  | The set of voice VLAN configurations for VoIP traffic prioritization on switches using this profile. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/templates/switchProfiles/query`

**Query Switch Profile Templates**

List the regular switch profile templates or command line interface profile templates.

operationId: `QueryProfileTemplates_1_1`


**Request Body:** `Switch_Services_SearchableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `searchString` | `string` |  | The search string for full text search across the specified target fields. |
| `searchTargetFields` | `array` |  | The list of field names to search within when applying the search string. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/templates/switchProfiles/{switchProfileId}`

**Delete Switch Profile Template**

Delete a regular switch profile template or command line interface profile template.

operationId: `DeleteProfileTemplateById_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/templates/switchProfiles/{switchProfileId}`

**Get Switch Profile Template**

Get a regular switch profile template or command line interface profile template.

operationId: `GetProfileTemplateById_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Profile_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/templates/switchProfiles/{switchProfileId}`

**Update Switch Profile Template**

Update a regular switch profile template or command line interface profile template. Use activity API with request id to get the status update.

operationId: `UpdateProfileTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ProfileDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acls` | `array` |  | The set of Access Control List configurations to be applied as part of this profile. |
| `applyOnboardOnly` | `boolean` |  | The flag indicating whether this profile should only be applied during the initial switch onboarding process. |
| `description` | `string` |  | The descriptive text providing details about the purpose and usage of this profile. |
| `id` | `string` |  |  |
| `name` | `string` |  | The unique name identifier for this switch configuration profile. |
| `profileType` | `string` |  | The profile type indicating whether this is a port profile, switch profile, or other profile type. |
| `trustedPorts` | `array` |  | The set of trusted port configurations for DHCP snooping and ARP inspection security features. |
| `venueCliTemplate` | `Switch_Services_AcxVenueCliTemplate_V1_1` |  | The venue level CLI template configuration containing custom command line interface commands for this profile. |
| `vlans` | `array` |  | The set of VLAN configurations defining VLANs to be created or managed by this profile. |
| `voiceVlanConfigs` | `array` |  | The set of voice VLAN configurations for VoIP traffic prioritization on switches using this profile. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/switchProfiles`

**Get Switch Profile Templates**

Get regular switch profile templates or command line interface profile templates of the venue.

operationId: `GetProfileTemplatesByVenueId_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueId}/switchProfiles/{switchProfileId}`

**Disassociate Switch Profile Template**

Disassociate a regular switch profile template or command line interface profile template to venue template.

operationId: `DisassociateProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/switchProfiles/{switchProfileId}`

**Associate Switch Profile Template**

Associate a regular switch profile template or command line interface profile template to venue template.

operationId: `AssociateProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Profile VLAN

*Manage VLANs (virtual local area networks) of switch profile.*


*12 endpoints*


### `DELETE` `/switchProfiles/{switchProfileId}/vlans`

**Delete Multiple VLANs**

Delete multiple VLANs of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `DeleteVlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles/{switchProfileId}/vlans`

**Get Multiple VLANs**

Get multiple VLANs of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `GetVlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `page` | query |  | `integer` |  |
| `size` | query |  | `integer` |  |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchProfiles/{switchProfileId}/vlans`

**Add VLAN**

Create a VLAN of the switch profile.

operationId: `AddVlan_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VlanBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `arpInspection` | `boolean` |  | Enable ARP inspection to prevent ARP spoofing attacks (default: false). |
| `arpInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for ARP inspection. |
| `arpInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for ARP inspection parsed from arpInspectionTrustPort. |
| `arpTrustPortsList` | `array` |  | List of ARP trusted ports for internal use. |
| `dhcpTrustPortsList` | `array` |  | List of DHCP trusted ports for internal use. |
| `enableAsDefaultVlan` | `boolean` | ✓ | Flag to enable this VLAN as the default VLAN for the switch (default: false). |
| `id` | `string` |  | Unique identifier for the VLAN configuration. |
| `igmpSnooping` | `string` |  | IGMP snooping mode for multicast traffic optimization. |
| `ipv4DhcpSnooping` | `boolean` |  | Enable IPv4 DHCP snooping to prevent rogue DHCP servers (default: false). |
| `ipv4DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for DHCP snooping. |
| `ipv4DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for DHCP snooping parsed from ipv4DhcpSnoopingTrustPort. |
| `ipv6DhcpSnooping` | `boolean` |  | Enable IPv6 DHCP snooping to prevent such attacks, DHCPv6 snooping helps to secure the IPv6 address configuration in the network (default: false). |
| `ipv6DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 DHCP snooping. |
| `ipv6DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 DHCP snooping parsed from ipv6DhcpSnoopingTrustPort. |
| `ipv6DhcpTrustPortsList` | `array` |  | List of IPv6 DHCP trusted ports for internal use. |
| `ipv6NdInspection` | `boolean` |  | Enable IPv6 ND (Neighbor Discovery) inspection to prevents IPv6 address spoofing at the switch level (default: false). |
| `ipv6NdInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection. |
| `ipv6NdInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection parsed from ipv6NdInspectionTrustPort. |
| `ipv6NdTrustPortsList` | `array` |  | List of IPv6 ND (Neighbor Discovery) trusted ports for internal use. |
| `managementVlan` | `boolean` |  | Flag indicating whether this is a management VLAN for switch management access (default: false). |
| `multicastVersion` | `integer` |  | IGMP multicast version (0-3). |
| `rootBridgeFamilyId` | `string` |  | Root bridge family ID for spanning tree protocol. |
| `spanningTreePriority` | `integer` |  | Spanning tree priority value for root bridge election (0-65535, default: 32768, lower values have higher priority). |
| `spanningTreeProtocol` | `string` |  | STP (Spanning Tree Protocol) mode for loop prevention. |
| `switchFamilyModels` | `array` |  | Set of switch family model configurations for this VLAN. |
| *… 4 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `201` Created → `Switch_Services_ProfileVlanResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switchProfiles/{switchProfileId}/vlans/{vlanId}`

**Delete Profile VLAN**

Delete the specified VLAN of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `DeleteVlanByUuid`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `vlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles/{switchProfileId}/vlans/{vlanId}`

**Get Profile VLAN**

Get the specified VLAN of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `GetVlanByUuid`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `vlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switchProfiles/{switchProfileId}/vlans/{vlanId}`

**Update VLAN**

Update the VLAN of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `UpdateVlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `vlanId` | path | ✓ | `integer` |  |


**Request Body:** `Switch_Services_VlanBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `arpInspection` | `boolean` |  | Enable ARP inspection to prevent ARP spoofing attacks (default: false). |
| `arpInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for ARP inspection. |
| `arpInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for ARP inspection parsed from arpInspectionTrustPort. |
| `arpTrustPortsList` | `array` |  | List of ARP trusted ports for internal use. |
| `dhcpTrustPortsList` | `array` |  | List of DHCP trusted ports for internal use. |
| `enableAsDefaultVlan` | `boolean` | ✓ | Flag to enable this VLAN as the default VLAN for the switch (default: false). |
| `id` | `string` |  | Unique identifier for the VLAN configuration. |
| `igmpSnooping` | `string` |  | IGMP snooping mode for multicast traffic optimization. |
| `ipv4DhcpSnooping` | `boolean` |  | Enable IPv4 DHCP snooping to prevent rogue DHCP servers (default: false). |
| `ipv4DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for DHCP snooping. |
| `ipv4DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for DHCP snooping parsed from ipv4DhcpSnoopingTrustPort. |
| `ipv6DhcpSnooping` | `boolean` |  | Enable IPv6 DHCP snooping to prevent such attacks, DHCPv6 snooping helps to secure the IPv6 address configuration in the network (default: false). |
| `ipv6DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 DHCP snooping. |
| `ipv6DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 DHCP snooping parsed from ipv6DhcpSnoopingTrustPort. |
| `ipv6DhcpTrustPortsList` | `array` |  | List of IPv6 DHCP trusted ports for internal use. |
| `ipv6NdInspection` | `boolean` |  | Enable IPv6 ND (Neighbor Discovery) inspection to prevents IPv6 address spoofing at the switch level (default: false). |
| `ipv6NdInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection. |
| `ipv6NdInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection parsed from ipv6NdInspectionTrustPort. |
| `ipv6NdTrustPortsList` | `array` |  | List of IPv6 ND (Neighbor Discovery) trusted ports for internal use. |
| `managementVlan` | `boolean` |  | Flag indicating whether this is a management VLAN for switch management access (default: false). |
| `multicastVersion` | `integer` |  | IGMP multicast version (0-3). |
| `rootBridgeFamilyId` | `string` |  | Root bridge family ID for spanning tree protocol. |
| `spanningTreePriority` | `integer` |  | Spanning tree priority value for root bridge election (0-65535, default: 32768, lower values have higher priority). |
| `spanningTreeProtocol` | `string` |  | STP (Spanning Tree Protocol) mode for loop prevention. |
| `switchFamilyModels` | `array` |  | Set of switch family model configurations for this VLAN. |
| *… 4 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/vlanUnions`

**Retrieve VLANs**

List all usable VLANs for multiple ports of the same switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlanUnions can be used for this content.

operationId: `GetVlanUnion_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VlanIntersectionResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switchProfiles/vlans`

**Get VLANs**

Get a list of VLANs in profiles with the specified venue.

operationId: `GetVlansByVenue_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/vlanUnions`

**Retrieve VLANs**

List all usable VLANs for multiple ports of the same switch.

operationId: `GetVlanUnion`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VlanIntersectionResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/taggedVlans/query`

**Retrieve Tagged VLANs**

List of venues switch profile VLANs with specific model and tagged port. This method will be removed no sooner than 06/30/2026.

operationId: `GetTaggedVlansByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VlanTaggingRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `model` | `string` |  | The switch model to determine the VLAN tagging capabilities and supported features. |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/untaggedVlans/query`

**Retrieve Untagged VLANs**

List of venues switch profile VLANs with specific model and untagged port. This method will be removed no sooner than 06/30/2026.

operationId: `GetUntaggedVlansByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VlanTaggingRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `model` | `string` |  | The switch model to determine the VLAN tagging capabilities and supported features. |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/vlans`

**Get VLANs**

List all of VLANs in profiles with the specified venue and the specific model. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switchProfiles/vlans can be used for this content.

operationId: `GetVlansByVenueAndModel`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `model` | query | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Vlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch Access Control List

*Manage ACLs (access control lists).*


*7 endpoints*


### `GET` `/switches/acls/{aclId}`

**Get ACL**

Get the ACL of the switch. This method will be removed no sooner than 06/30/2026.

operationId: `GetAclById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `aclId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/aclUnions`

**Get ACL Union**

List all usable ACLs for this switch (the union of venue and device levels). This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/aclUnions can be used for this content.

operationId: `GetAclUnion_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AclIntersectionResponse_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/acls`

**Get ACLs**

Get all ACLs of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/acls can be used for this content.

operationId: `GetAclsBySwitch_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Acl_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/acls/query`

**Retrieve ACLs**

Query the switch's switch level ACLs. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/acls/query can be used for this content.

operationId: `GetSwitchAclsByQuery_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/aclUnions`

**Get ACL Unions**

List all usable ACLs for this switch (the union of venue and device levels).

operationId: `GetAclUnion`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AclIntersection_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/acls`

**Get Switch ACLs**

Get all ACLs of the switch.

operationId: `GetAclsBySwitch`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/acls/query`

**Query Switch ACLs**

Get switch ACLs by query criteria.

operationId: `GetSwitchAclsByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch Configuration Backup

*Manage switch configuration backups and restore operations.*


*17 endpoints*


### `DELETE` `/switches/configBackups`

**Delete Switch Configuration Backups**

Delete switch's configuration backups. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups can be used for this content.

operationId: `DeleteSwitchConfigBackups_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/configBackups/comparisons`

**Compare Switch Configuration Backups**

Compare switch's configuration backups. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups/comparisons can be used for this content.

operationId: `CompareSwitchConfigBackups_1`


**Request Body:** `Switch_Services_CompareConfigBackupsRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `backupId1` | `string` |  | The first configuration backup id for comparison. |
| `backupId2` | `string` |  | The second configuration backup id for comparison. |


**Responses:**

- `200` OK → `Switch_Services_CompareConfigBackupsResponse_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/configBackups/{configBackupId}`

**Delete Switch Configuration Backup**

Delete switch's configuration backup by id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups/{configBackupId} can be used for this content.

operationId: `DeleteSwitchConfigBackupById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `configBackupId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/configBackups/{configBackupId}`

**Get Switch Configuration Backup**

Get a switch's configuration backup. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups/{configBackupId} can be used for this content.

operationId: `GetSwitchConfigBackupById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `configBackupId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ConfigBackup_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/configBackups/{configBackupId}`

**Restore Switch Configuration Backup**

Restore switch's configuration backup. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups/{configBackupId} with PATCH method can be used for this content.

operationId: `RestoreSwitchByConfigBackup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `configBackupId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/configBackups`

**Get Switch Configuration Backups**

List of switch's configuration backup. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups can be used for this content.

operationId: `GetConfigBackupsBySwitch_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ConfigBackup_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/configBackups`

**Add Switch Configuration Backup**

Create a switch's configuration backup. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups can be used for this content.

operationId: `AddSwitchConfigBackup_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AddConfigBackupRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `name` | `string` |  | The name of the configuration backup. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/configBackups/query`

**Retrieve Switch Configuration Backups**

Query the switch's configuration backups. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/configBackups/query can be used for this content.

operationId: `GetSwitchConfigBackupsByQuery_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/configBackups`

**Delete Switch Configuration Backups**

Delete switch's configuration backups.

operationId: `DeleteSwitchConfigBackups`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/configBackups`

**Get Switch Configuration Backups**

List of switch's configuration backup.

operationId: `GetConfigBackupsBySwitch`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/configBackups`

**Add Switch Configuration Backup**

Create a switch's configuration backup.

operationId: `AddSwitchConfigBackup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigBackupDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `name` | `string` |  | The name for this configuration backup. |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/configBackups/comparisons`

**Compare Switch Configuration Backups**

Compare switch's configuration backups.

operationId: `CompareSwitchConfigBackups`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigBackupComparisonDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `backupId1` | `string` |  | First configuration backup id for comparison. |
| `backupId2` | `string` |  | Second configuration backup id for comparison. |


**Responses:**

- `200` OK → `Switch_Services_ConfigBackupComparison_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/configBackups/query`

**Retrieve Switch Configuration Backups**

Query the switch's configuration backups.

operationId: `GetSwitchConfigBackupsByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/configBackups/{configBackupId}`

**Delete Switch Configuration Backup**

Delete switch's configuration backup by id.

operationId: `DeleteSwitchConfigBackupById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `configBackupId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/configBackups/{configBackupId}`

**Get Switch Configuration Backup**

Get a switch's configuration backup.

operationId: `GetSwitchConfigBackupById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `configBackupId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ConfigBackup_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/switches/{switchId}/configBackups/{configBackupId}`

**Restore Switch Configuration Backup**

Restore switch's configuration backup.

operationId: `RestoreSwitchByConfigBackup_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `configBackupId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ConfigBackupActionDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `configBackupAction` | `string` |  | The action to perform on the configuration backup, either restore to a switch or download for external storage. |


**Responses:**

- `202` Accepted → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/configBackups/{configBackupId}/formattedConfigs`

**Retrieve Formatted Configuration Backup**

Retrieve formatted string representation of switch's configuration backup for convert to template.

operationId: `GetFormattedConfigBackup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `configBackupId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_ConfigBackUpFormatted_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch Firmware Upgrade

*Manage switch firmware upgrade and scheduling operations.*


*14 endpoints*


### `GET` `/switchFirmwares/currentVersions`

**Get Current Versions**

Get current versions of the venues.

operationId: `GetCurrentVersionsByVenues_1_1`


**Responses:**

- `200` OK → `Switch_Services_VenueCurrentVersionView_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchFirmwares/schedules/query`

**Get Venues**

Get all venues by tenant id for upgrading.

operationId: `GetUpgradeVenues_1_1`


**Request Body:** `Switch_Services_UpgradeVenueQueryFilter_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `firmwareVersion` | `string` |  | Firmware version string to filter venues by switch firmware version. |
| `searchFilter` | `string` |  | Search filter string for filtering venues by name or other attributes. |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchFirmwares/schedules/switches/query`

**Get Switches**

Get all switches by tenant id for upgrading.

operationId: `GetUpgradeSwitches_1_1`


**Request Body:** `Switch_Services_UpgradeSwitchQueryFilter_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `searchFilter` | `string` |  | Search filter string for filtering switches by name, model, or other attributes. |
| `venueIdList` | `array` |  | List of venue identifiers to filter switches by venue. |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchFirmwares/versions/{versionType}`

**Get Versions**

Get different version type of firmware.

operationId: `GetVersions_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `versionType` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/switchFirmwares/currentVersions`

**Get Current Versions**

Get current versions of the venues. This method will be removed no sooner than 06/30/2026. The following URL /switchFirmwares/currentVersions can be used for this content.

operationId: `GetCurrentVersionsByVenues`


**Responses:**

- `200` OK → `Switch_Services_VenueCurrentVersion_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/switchFirmwares/schedules`

**Delete Upgrade Schedule**

Cancel the schedule for firmware upgrade. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switchFirmwares/schedules can be used for this content.

operationId: `SkipUpgradeSchedule_1`


**Request Body:** `Switch_Services_SkipScheduleUpgradeRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  | The identifier |
| `switchIds` | `array` |  | The list of switch identifiers for which the scheduled firmware upgrade should be skipped. |
| `venueIds` | `array` |  | The list of venue identifiers for which the scheduled firmware upgrade should be skipped. |


**Responses:**

- `200` OK → `Switch_Services_StringResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/switchFirmwares/schedules`

**Create Upgrade Schedule**

Schedule the firmware upgrade for venues. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switchFirmwares/schedules can be used for this content.

operationId: `UpdateSchedule`


**Request Body:** `Switch_Services_ChangeScheduleRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `date` | `string` |  | The new scheduled date for the firmware upgrade in string format. |
| `id` | `string` |  | The identifier |
| `preDownload` | `boolean` |  | The flag indicating whether firmware pre download should be enabled before the scheduled upgrade. |
| `switchIds` | `array` |  | The list of switch identifiers affected by this schedule change. |
| `switchVersion` | `string` |  | The target firmware version for switches with version numbers below 10.0.0. |
| `switchVersionAboveTen` | `string` |  | The target firmware version for switches with version numbers 10.0.0 and above. |
| `time` | `string` |  | The new scheduled time for the firmware upgrade in string format. |
| `venueIds` | `array` |  | The list of venue identifiers affected by this schedule change. |


**Responses:**

- `200` OK → `Switch_Services_StringResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/switchFirmwares/schedules/query`

**Get Venues**

Get all venues by tenant id for upgrading. This method will be removed no sooner than 06/30/2026. The following URL /switchFirmwares/schedules/query can be used for this content.

operationId: `GetUpgradeVenues`


**Request Body:** `Switch_Services_UpgradeVenueCriteria_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `firmwareType` | `string` |  | The firmware type to filter venues, such as primary or recovery firmware. |
| `firmwareVersion` | `string` |  | The firmware version to filter venues by their current or target firmware version. |
| `search` | `string` |  | The search term for filtering venues by name or identifier. |
| `updateAvailable` | `boolean` |  | The flag indicating whether to filter venues that have firmware updates available. |


**Responses:**

- `200` OK → `Switch_Services_UpgradeVenue_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/switchFirmwares/switches/schedules/query`

**Get Switches**

Get all switches by tenant id for upgrading. This method will be removed no sooner than 06/30/2026. The following URL /switchFirmwares/schedules/switches/query can be used for this content.

operationId: `GetUpgradeSwitches`


**Request Body:** `Switch_Services_UpgradeSwitchCriteria_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `search` | `string` |  | The search term for filtering switches by name, MAC address, or identifier. |
| `venueIdList` | `array` |  | The list of venue identifiers to filter switches by their associated venues. |


**Responses:**

- `200` OK → `Switch_Services_UpgradeSwitchView`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/switchFirmwares/upgradeStatusDetails/query`

**Get Venue Upgrade Statuses**

Get venue upgrade status by venue id for upgrading. This method will be removed no sooner than 06/30/2026.

operationId: `getUpgradeStatusDetails`


**Request Body:** `Switch_Services_UpgradeStatusDetailsCriteria_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `venueId` | `string` |  | The identifier of venue. |


**Responses:**

- `200` OK → `Switch_Services_UpgradeStatusDetailsView_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/switchFirmwares/versions/{versionType}`

**Get Versions**

Get different version type of firmware. This method will be removed no sooner than 06/30/2026. The following URL /switchFirmwares/versions/{versionType} can be used for this content.

operationId: `GetVersions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `versionType` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_SwitchVersionView`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switchFirmwares/schedules`

**Delete Upgrade Schedule**

Cancel the schedule for firmware upgrade.

operationId: `SkipUpgradeSchedule`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_SkipScheduleUpgradeDto_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `switchIds` | `array` |  | The list of switch identifiers for which the scheduled firmware upgrade should be skipped or postponed. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switchFirmwares/schedules`

**Create Upgrade Schedule**

Schedule the firmware upgrade for venues. Use activity API with request id to get the status update.

operationId: `UpdateSchedule_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `manualOverride` | query |  | `boolean` |  |


**Request Body:** `Switch_Services_ChangeScheduleDto_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `date` | `string` |  | The scheduled date for the firmware upgrade operation in string format. |
| `id` | `string` |  |  |
| `preDownload` | `boolean` |  | The flag indicating whether to pre download the firmware before the scheduled upgrade time. |
| `switchIds` | `array` |  | The list of switch identifiers to include in the scheduled firmware upgrade. |
| `switchVersion` | `string` |  | The target firmware version for switches with version 10 or below. |
| `switchVersionAboveTen` | `string` |  | The target firmware version for switches with version above 10. |
| `time` | `string` |  | The scheduled time for the firmware upgrade operation in string format. |


**Responses:**

- `201` Created → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switchFirmwares/schedules`

**Change Upgrade Schedule**

Schedule the firmware upgrade for venues. Use activity API with request id to get the status update.

operationId: `ChangeUpdateScheduleV1001`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_ChangeScheduleDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `date` | `string` |  | The scheduled date for the firmware upgrade operation in string format. |
| `id` | `string` |  |  |
| `preDownload` | `boolean` |  | The flag indicating whether to pre download the firmware before the scheduled upgrade time. |
| `switchIds` | `array` |  | The list of switch identifiers to include in the scheduled firmware upgrade. |
| `time` | `string` |  | The scheduled time for the firmware upgrade operation in string format. |
| `versions` | `array` |  | The set of model version pairs specifying target firmware versions for different switch models in this upgrade schedule. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch Ports

*Manage switch port configurations.*


*11 endpoints*


### `POST` `/switches/portSettings`

**Get Ports**

Get port settings of different switches. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/portSettings can be used for this content.

operationId: `GetPortsAmongSwitches_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_Port_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/portSettings`

**Update Ports**

Update ports of different switches. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/portSettings can be used for this content.

operationId: `UpdatePortsAmongSwitches_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_Port_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/portSettings`

**Get Ports**

Get switch's port settings by switch id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/portSettings can be used for this content.

operationId: `GetSwitchPortsBySwitchId_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Port_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/portSettings`

**Get Ports**

Get switch's port settings with port ids. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/portSettings can be used for this content.

operationId: `GetSwitchPortsByPortIds_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_Port_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/{switchId}/portSettings`

**Update Port**

Update switch's port setting. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/portSettings can be used for this content.

operationId: `UpdatePortSettings_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_UpdatePortBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminPtToPt` | `string` |  | The RSTP (Rapid Spanning Tree Protocol) point-to-point MAC mode. |
| `arpInspectionTrust` | `boolean` |  | The flag indicating whether this port is trusted for ARP inspection, bypassing ARP validation. |
| `authDefaultVlan` | `integer` |  | The VLAN ID to assign authenticated users when no specific VLAN is provided by the AAA server. |
| `authFailAction` | `string` |  | The action to take when authentication fails: restricted VLAN, drop, or block. |
| `authTimeoutAction` | `string` |  | The action to take when authentication times out: same as auth fail or critical VLAN. |
| `authenticationCustomize` | `boolean` |  | The flag indicating whether port specific authentication settings override the profile defaults. |
| `authenticationProfileId` | `string` |  | The identifier of the authentication profile applied to this port for access control. |
| `authenticationType` | `string` |  | The authentication method type configured for this port, such as 802.1X, MAC authentication, or Web authentication. |
| `changeAuthOrder` | `boolean` |  | The flag indicating whether the authentication method order has been modified from defaults. |
| `criticalVlan` | `integer` |  | The VLAN ID for critical users requiring network access during AAA server failure. |
| `dhcpSnoopingTrust` | `boolean` |  | The flag indicating whether this port is trusted for DHCP snooping, allowing DHCP server responses. |
| `dot1xPortControl` | `string` |  | The 802.1X port control mode determining authentication requirements: auto, force authorized, or force unauthorized. |
| `egressAcl` | `string` |  | The name of the Access Control List applied to egress (outgoing) traffic on this port. |
| `flexibleAuthenticationEnabled` | `boolean` |  | The flag indicating whether flexible authentication with multiple methods is enabled on this port. |
| `guestVlan` | `integer` |  | The VLAN ID for guest users who bypass authentication. |
| `id` | `string` |  |  |
| `ignoreFields` | `string` |  | The comma separated list of field names to ignore during update operations. |
| `ingressAcl` | `string` |  | The name of the Access Control List applied to ingress (incoming) traffic on this port. |
| `ipsg` | `boolean` |  | The flag indicating whether IP source guard is enabled for additional layer 2 security. |
| `ipv6DhcpSnoopingTrust` | `boolean` |  | The flag indicating whether this port is trusted for IPv6 DHCP snooping, bypassing DHCP validation. |
| `ipv6NdInspectionTrust` | `boolean` |  | The flag indicating whether this port is trusted for IPv6 ND (Neighbor Discovery) inspection, bypassing ND validation. |
| `lldpEnable` | `boolean` |  | The flag indicating whether LLDP (Link Layer Discovery Protocol) is enabled on this port. |
| `lldpQos` | `array` |  | The set of LLDP (Link Layer Discovery Protocol) QoS (Quality of Service) configurations for network priority advertising. |
| `name` | `string` |  | The descriptive name or label assigned to the port for identification purposes. |
| `poeBudget` | `integer` |  | The PoE power budget allocated to this port in watts. |
| *… 25 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_Port_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/portSettings`

**Get Ports**

Get port settings of different switches.

operationId: `GetPortsAmongSwitches`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/portSettings`

**Update Ports**

Update ports of different switches. Use activity API with request id to get the status update.

operationId: `UpdatePortsAmongSwitches`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_PortResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/powerCycleRequests`

**Power Cycle Port**

Power cycle switch's port. Use activity API with request id to get the status update.

operationId: `PowerCyclePort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/portSettings`

**Get Ports**

Get switch's port settings by switch id.

operationId: `GetSwitchPortsBySwitchId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/portSettings`

**Get Ports**

Get switch's port settings with port ids.

operationId: `GetSwitchPortsByPortIds`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/portSettings`

**Update Port**

Update switch's port setting. Use activity API with request id to get the status update.

operationId: `UpdatePortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_PortDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminPtToPt` | `string` |  | The RSTP (Rapid Spanning Tree Protocol) point-to-point MAC mode. |
| `arpInspectionTrust` | `boolean` |  | The flag indicating whether this port is trusted for ARP inspection, bypassing ARP validation. |
| `authDefaultVlan` | `integer` |  | The VLAN ID to assign authenticated users when no specific VLAN is provided by the AAA server. |
| `authFailAction` | `string` |  | The action to take when authentication fails: restricted VLAN, drop, or block. |
| `authTimeoutAction` | `string` |  | The action to take when authentication times out: same as auth fail or critical VLAN. |
| `authenticationCustomize` | `boolean` |  | The flag indicating whether port specific authentication settings override the profile defaults. |
| `authenticationProfileId` | `string` |  | The identifier of the authentication profile applied to this port for access control. |
| `authenticationType` | `string` |  | The authentication method type configured for this port, such as 802.1X, MAC authentication, or Web authentication. |
| `changeAuthOrder` | `boolean` |  | The flag indicating whether the authentication method order has been modified from defaults. |
| `criticalVlan` | `integer` |  | The VLAN ID for critical users requiring network access during AAA server failure. |
| `dhcpSnoopingTrust` | `boolean` |  | The flag indicating whether this port is trusted for DHCP snooping, allowing DHCP server responses. |
| `dot1xPortControl` | `string` |  | The 802.1X port control mode determining authentication requirements: auto, force authorized, or force unauthorized. |
| `egressAcl` | `string` |  | The name of the Access Control List applied to egress (outgoing) traffic on this port. |
| `flexibleAuthenticationEnabled` | `boolean` |  | The flag indicating whether flexible authentication with multiple methods is enabled on this port. |
| `guestVlan` | `integer` |  | The VLAN ID for guest users who bypass authentication. |
| `id` | `string` |  |  |
| `ignoreFields` | `string` |  | The comma separated list of field names to ignore during update operations. |
| `ingressAcl` | `string` |  | The name of the Access Control List applied to ingress (incoming) traffic on this port. |
| `ipsg` | `boolean` |  | The flag indicating whether IP source guard is enabled for additional layer 2 security. |
| `lldpEnable` | `boolean` |  | The flag indicating whether LLDP (Link Layer Discovery Protocol) is enabled on this port. |
| `lldpQos` | `array` |  | The set of LLDP (Link Layer Discovery Protocol) QoS (Quality of Service) configurations for network priority advertising. |
| `name` | `string` |  | The descriptive name or label assigned to the port for identification purposes. |
| `poeBudget` | `number` |  | The PoE power budget allocated to this port in watts. |
| `poeCapability` | `boolean` |  | The flag indicating whether this port has PoE (Power over Ethernet) hardware capability. |
| `poeClass` | `string` |  | The PoE (Power over Ethernet) class indicating the maximum power level supported by the connected device. |
| *… 20 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_PortResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch Static Routes

*Manage static route configurations.*


*12 endpoints*


### `DELETE` `/switches/staticRoutes`

**Delete Static Routes**

Delete multiple static routes. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/staticRoutes can be used for this content.

operationId: `DeleteStaticRoutes_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/staticRoutes/{staticRouteId}`

**Delete Static Route**

Delete the specified static route. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/staticRoutes/{staticRouteId} can be used for this content.

operationId: `DeleteStaticRoute_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `staticRouteId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/staticRoutes/{staticRouteId}`

**Get Static Route**

Get the specified static route. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/staticRoutes/{staticRouteId} can be used for this content.

operationId: `GetStaticRouteById_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `staticRouteId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_StaticRoute_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/staticRoutes/{staticRouteId}`

**Update Static Route**

Update the specified static route. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/staticRoutes/{staticRouteId} can be used for this content.

operationId: `UpdateStaticRoute_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `staticRouteId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_StaticRouteBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminDistance` | `integer` |  | Administrative distance for route priority (1-255, lower values have higher priority). |
| `destinationIp` | `string` | ✓ | Destination IP address in CIDR notation. For IPv4: '192.168.10.0/24', For IPv6: '2001:db8::/32'. |
| `id` | `string` |  | Unique identifier for the static route. |
| `nextHop` | `string` | ✓ | Next hop IP address where packets matching the destination will be forwarded. For IPv4: '192.168.1.1', For IPv6: '2001:db8::1'. |


**Responses:**

- `200` OK → `Switch_Services_StaticRoute_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/staticRoutes`

**Get Static Routes**

Get multiple static routes of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/staticRoutes can be used for this content.

operationId: `GetStaticRoutesBySwitchId_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_StaticRoute_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/staticRoutes`

**Add Static Route**

Add multiple static routes of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/staticRoutes can be used for this content.

operationId: `AddStaticRoutes_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_StaticRoute_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/staticRoutes`

**Delete Static Routes**

Delete multiple static routes.

operationId: `DeleteStaticRoutes`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/staticRoutes`

**Get Static Routes**

Get multiple static routes of the switch.

operationId: `GetStaticRoutesBySwitchId`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/staticRoutes`

**Add Static Route**

Add multiple static routes of the switch.

operationId: `AddStaticRoutes`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `201` Created → `Switch_Services_StaticRouteResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/staticRoutes/{staticRouteId}`

**Delete Static Route**

Delete the specified static route.

operationId: `DeleteStaticRoute`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `staticRouteId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/staticRoutes/{staticRouteId}`

**Get Static Route**

Get the specified static route.

operationId: `GetStaticRouteById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `staticRouteId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_StaticRoute_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/staticRoutes/{staticRouteId}`

**Update Static Route**

Update the specified static route.

operationId: `UpdateStaticRoute`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `staticRouteId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_StaticRoute_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminDistance` | `integer` |  | The administrative distance value for route preference, with lower values having higher priority. |
| `destinationIp` | `string` | ✓ | The destination IP address in CIDR notation. For IPv4: '192.168.10.0/24', For IPv6: '2001:db8::/32'. |
| `id` | `string` |  |  |
| `nextHop` | `string` | ✓ | The IP address of the next hop gateway to route traffic. For IPv4: '192.168.1.1', For IPv6: '2001:db8::1'. |


**Responses:**

- `200` OK → `Switch_Services_StaticRouteResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch VLAN

*Manage VLANs (virtual local area networks).*


*19 endpoints*


### `DELETE` `/switches/vlans`

**Delete Switch VLANs**

Delete multiple VLANs of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans can be used for this content.

operationId: `DeleteSwitchVlans_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/vlans`

**Add Switch VLANs**

Create multiple VLANs under the specified switches. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/vlans can be used for this content.

operationId: `AddSwitchVlans_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/vlans/query`

**Retrieve Switch VLANs**

Retrieve all usable VLANs under the specified switches. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/vlans/query can be used for this content.

operationId: `GetSwitchVlanBySwitchIds_1`


**Request Body:** `Switch_Services_SwitchVlanRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `isDefault` | `boolean` |  | Flag indicating whether this is a default VLAN operation (default: false). |
| `switchIds` | `array` |  | List of switch identifiers (serial numbers) to perform the VLAN operation on. |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlanResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/vlans/{vlanId}`

**Delete Switch VLAN**

Delete a VLAN of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans/{vlanId} can be used for this content.

operationId: `DeleteSwitchVlan_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/vlans/{vlanId}`

**Get Switch VLAN**

Get the specified switch level VLAN by id. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans/{vlanId} can be used for this content.

operationId: `GetSwitchVlan_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/vlans/{vlanId}`

**Update Switch VLAN**

Update a VLAN of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans/{vlanId} can be used for this content.

operationId: `UpdateSwitchVlan_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VlanBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `arpInspection` | `boolean` |  | Enable ARP inspection to prevent ARP spoofing attacks (default: false). |
| `arpInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for ARP inspection. |
| `arpInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for ARP inspection parsed from arpInspectionTrustPort. |
| `arpTrustPortsList` | `array` |  | List of ARP trusted ports for internal use. |
| `dhcpTrustPortsList` | `array` |  | List of DHCP trusted ports for internal use. |
| `enableAsDefaultVlan` | `boolean` | ✓ | Flag to enable this VLAN as the default VLAN for the switch (default: false). |
| `id` | `string` |  | Unique identifier for the VLAN configuration. |
| `igmpSnooping` | `string` |  | IGMP snooping mode for multicast traffic optimization. |
| `ipv4DhcpSnooping` | `boolean` |  | Enable IPv4 DHCP snooping to prevent rogue DHCP servers (default: false). |
| `ipv4DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for DHCP snooping. |
| `ipv4DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for DHCP snooping parsed from ipv4DhcpSnoopingTrustPort. |
| `ipv6DhcpSnooping` | `boolean` |  | Enable IPv6 DHCP snooping to prevent such attacks, DHCPv6 snooping helps to secure the IPv6 address configuration in the network (default: false). |
| `ipv6DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 DHCP snooping. |
| `ipv6DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 DHCP snooping parsed from ipv6DhcpSnoopingTrustPort. |
| `ipv6DhcpTrustPortsList` | `array` |  | List of IPv6 DHCP trusted ports for internal use. |
| `ipv6NdInspection` | `boolean` |  | Enable IPv6 ND (Neighbor Discovery) inspection to prevents IPv6 address spoofing at the switch level (default: false). |
| `ipv6NdInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection. |
| `ipv6NdInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection parsed from ipv6NdInspectionTrustPort. |
| `ipv6NdTrustPortsList` | `array` |  | List of IPv6 ND (Neighbor Discovery) trusted ports for internal use. |
| `managementVlan` | `boolean` |  | Flag indicating whether this is a management VLAN for switch management access (default: false). |
| `multicastVersion` | `integer` |  | IGMP multicast version (0-3). |
| `rootBridgeFamilyId` | `string` |  | Root bridge family ID for spanning tree protocol. |
| `spanningTreePriority` | `integer` |  | Spanning tree priority value for root bridge election (0-65535, default: 32768, lower values have higher priority). |
| `spanningTreeProtocol` | `string` |  | STP (Spanning Tree Protocol) mode for loop prevention. |
| `switchFamilyModels` | `array` |  | Set of switch family model configurations for this VLAN. |
| *… 4 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/vlans`

**Get Switch VLANs**

Get switch level VLANs by switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans can be used for this content.

operationId: `GetSwitchVlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/vlans`

**Add Switch VLAN**

Create a VLAN of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans can be used for this content.

operationId: `AddSwitchVlan_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VlanBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `arpInspection` | `boolean` |  | Enable ARP inspection to prevent ARP spoofing attacks (default: false). |
| `arpInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for ARP inspection. |
| `arpInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for ARP inspection parsed from arpInspectionTrustPort. |
| `arpTrustPortsList` | `array` |  | List of ARP trusted ports for internal use. |
| `dhcpTrustPortsList` | `array` |  | List of DHCP trusted ports for internal use. |
| `enableAsDefaultVlan` | `boolean` | ✓ | Flag to enable this VLAN as the default VLAN for the switch (default: false). |
| `id` | `string` |  | Unique identifier for the VLAN configuration. |
| `igmpSnooping` | `string` |  | IGMP snooping mode for multicast traffic optimization. |
| `ipv4DhcpSnooping` | `boolean` |  | Enable IPv4 DHCP snooping to prevent rogue DHCP servers (default: false). |
| `ipv4DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for DHCP snooping. |
| `ipv4DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for DHCP snooping parsed from ipv4DhcpSnoopingTrustPort. |
| `ipv6DhcpSnooping` | `boolean` |  | Enable IPv6 DHCP snooping to prevent such attacks, DHCPv6 snooping helps to secure the IPv6 address configuration in the network (default: false). |
| `ipv6DhcpSnoopingTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 DHCP snooping. |
| `ipv6DhcpSnoopingTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 DHCP snooping parsed from ipv6DhcpSnoopingTrustPort. |
| `ipv6DhcpTrustPortsList` | `array` |  | List of IPv6 DHCP trusted ports for internal use. |
| `ipv6NdInspection` | `boolean` |  | Enable IPv6 ND (Neighbor Discovery) inspection to prevents IPv6 address spoofing at the switch level (default: false). |
| `ipv6NdInspectionTrustPort` | `string` |  | Comma separated list of trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection. |
| `ipv6NdInspectionTrustPortList` | `array` |  | List of individual trusted port identifiers for IPv6 ND (Neighbor Discovery) inspection parsed from ipv6NdInspectionTrustPort. |
| `ipv6NdTrustPortsList` | `array` |  | List of IPv6 ND (Neighbor Discovery) trusted ports for internal use. |
| `managementVlan` | `boolean` |  | Flag indicating whether this is a management VLAN for switch management access (default: false). |
| `multicastVersion` | `integer` |  | IGMP multicast version (0-3). |
| `rootBridgeFamilyId` | `string` |  | Root bridge family ID for spanning tree protocol. |
| `spanningTreePriority` | `integer` |  | Spanning tree priority value for root bridge election (0-65535, default: 32768, lower values have higher priority). |
| `spanningTreeProtocol` | `string` |  | STP (Spanning Tree Protocol) mode for loop prevention. |
| `switchFamilyModels` | `array` |  | Set of switch family model configurations for this VLAN. |
| *… 4 more fields* | | | |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlan_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/vlans/query`

**Query Switch VLANs**

Query the switch's switch level VLANs. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vlans/query can be used for this content.

operationId: `QuerySwitchVlans_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_SearchableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `searchString` | `string` |  | The search string for full text search across the specified target fields. |
| `searchTargetFields` | `array` |  | The list of field names to search within when applying the search string. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/vlans`

**Delete Switch VLANs**

Delete multiple VLANs of the switch.

operationId: `DeleteSwitchVlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/vlans`

**Get VLAN VE Ports**

List all usable VLANs that are available for the VE setting.

operationId: `GetVlanByVenueWithVePortsInfoBySwitchId_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VlanVePort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/vlans`

**Add Switch VLAN**

Create a VLAN of the switch.

operationId: `AddSwitchVlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_SwitchVlanDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `arpInspection` | `boolean` |  | The flag indicating whether ARP inspection is enabled for this VLAN to prevent ARP spoofing attacks. |
| `enableAsDefaultVlan` | `boolean` |  | The flag indicating whether this VLAN should be configured as the default VLAN for the switch. |
| `id` | `string` |  |  |
| `igmpSnooping` | `string` |  | The IGMP snooping mode for this VLAN to optimize multicast traffic delivery. |
| `ipv4DhcpSnooping` | `boolean` |  | The flag indicating whether IPv4 DHCP snooping is enabled for this VLAN to prevent rogue DHCP servers. |
| `multicastVersion` | `integer` |  | The IGMP version number used for multicast group management in this VLAN. |
| `spanningTreeProtocol` | `string` |  | STP (Spanning Tree Protocol) variant enabled for this VLAN. |
| `switchVlanPortModels` | `array` |  | The set of port model configurations specific to this VLAN on different switch models in a stack. |
| `vlanId` | `integer` |  | The VLAN identifier, ranging from 1 to 4095, uniquely identifying this VLAN on the switch. |
| `vlanName` | `string` |  | The descriptive name assigned to this VLAN, limited to 32 characters. |


**Responses:**

- `201` Created → `Switch_Services_SwitchVlanResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/vlans/query`

**Query Switch VLANs**

Query the switch's switch level VLANs.

operationId: `QuerySwitchVlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_SearchableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `searchString` | `string` |  | The search string for full text search across the specified target fields. |
| `searchTargetFields` | `array` |  | The list of field names to search within when applying the search string. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/vlans/{vlanId}`

**Delete Switch VLAN**

Delete a VLAN of the switch.

operationId: `DeleteSwitchVlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `vlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/vlans/{vlanId}`

**Get Switch VLAN**

Get the specified switch level VLAN by id.

operationId: `GetSwitchVlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `vlanId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlanView_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/vlans/{vlanId}`

**Update Switch VLAN**

Update a VLAN of the switch.

operationId: `UpdateSwitchVlan`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `vlanId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_SwitchVlanDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `arpInspection` | `boolean` |  | The flag indicating whether ARP inspection is enabled for this VLAN to prevent ARP spoofing attacks. |
| `enableAsDefaultVlan` | `boolean` |  | The flag indicating whether this VLAN should be configured as the default VLAN for the switch. |
| `id` | `string` |  |  |
| `igmpSnooping` | `string` |  | The IGMP snooping mode for this VLAN to optimize multicast traffic delivery. |
| `ipv4DhcpSnooping` | `boolean` |  | The flag indicating whether IPv4 DHCP snooping is enabled for this VLAN to prevent rogue DHCP servers. |
| `multicastVersion` | `integer` |  | The IGMP version number used for multicast group management in this VLAN. |
| `spanningTreeProtocol` | `string` |  | STP (Spanning Tree Protocol) variant enabled for this VLAN. |
| `switchVlanPortModels` | `array` |  | The set of port model configurations specific to this VLAN on different switch models in a stack. |
| `vlanId` | `integer` |  | The VLAN identifier, ranging from 1 to 4095, uniquely identifying this VLAN on the switch. |
| `vlanName` | `string` |  | The descriptive name assigned to this VLAN, limited to 32 characters. |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlanResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/vlanUnions`

**Get VLANs**

List all usable VLANs under this venue.

operationId: `GetVlanUnionByVenue_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_SwitchVlanConcise`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/vlans`

**Add Switch VLANs**

Create multiple VLANs under the specified switches.

operationId: `AddSwitchVlans`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `201` Created → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/vlans/query`

**Retrieve Switch VLANs**

Retrieve all usable VLANs under the specified switches.

operationId: `GetSwitchVlanBySwitchIds`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Switch Virtual Ethernet

*Manage VE (virtual ethernet) port settings.*


*15 endpoints*


### `DELETE` `/switches/vePorts`

**Delete Virtual Ethernet Settings**

Delete multiple virtual ethernet ports. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts can be used for this content.

operationId: `DeleteVePorts_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switches/vePorts/{vePortId}`

**Delete Virtual Ethernet Setting**

Delete virtual ethernet port. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts/{vePortId} can be used for this content.

operationId: `DeleteVePort_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vePortId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/vePorts/{vePortId}`

**Get Virtual Ethernet Setting**

Get a specified virtual ethernet port. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts/{vePortId} can be used for this content.

operationId: `GetVePort_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vePortId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VePortBo`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switches/vePorts/{vePortId}`

**Update Virtual Ethernet Setting**

Update virtual ethernet port. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts/{vePortId} can be used for this content.

operationId: `UpdateVePort_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vePortId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VePortBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultVlan` | `boolean` |  | Flag indicating whether this VE port is associated with the default VLAN (default: false). |
| `dhcpRelayAgent` | `string` |  | DHCP relay agent IP address for forwarding DHCP requests. |
| `egressAcl` | `string` |  | Egress ACL name or ID applied to outgoing traffic on this VE port. |
| `id` | `string` |  | Unique identifier for the VE port. |
| `ingressAcl` | `string` |  | Ingress ACL name or ID applied to incoming traffic on this VE port. |
| `ipAddress` | `string` |  | IPv4 address assigned to the VE interface (e.g., '192.168.1.1'). |
| `ipAddressType` | `string` |  | IP address type for the VE interface (static or dynamic). |
| `ipRouterId` | `string` |  | The router ID for the switch. |
| `ipSubnetMask` | `string` |  | IP subnet mask for the VE interface (e.g., '255.255.255.0'). |
| `ipv6Address` | `string` |  | IPv6 address assigned to the VE interface (e.g., '2001:b030:2516:101:1:1:1:242'). |
| `ipv6AddressType` | `string` |  | IPv6 address type for the VE interface (static or dynamic). |
| `ipv6DhcpRelayAgent` | `string` |  | Enable the DHCPv6 relay agent function and specify the relay destination (the DHCP server) address on a VE interface. |
| `ipv6OspfArea` | `string` |  | Enables OSPFv3 on a VE interface. |
| `ipv6Prefix` | `string` |  | IPv6 address prefix to the VE interface (e.g., '64'). |
| `name` | `string` |  | Name of the VE port for identification. |
| `ospfArea` | `string` |  | OSPF area ID for routing configuration (e.g., '0.0.0.0' for backbone area). |
| `switchId` | `string` |  | Switch identifier where this VE port is configured. |
| `veId` | `integer` |  | VE port identifier number (1-4096). |
| `vlanId` | `integer` |  | VLAN ID associated with this VE port (1-4095). |
| `vsixEgressAcl` | `string` |  | IPv6 Egress ACL name or ID applied to outgoing traffic on this VE port. |
| `vsixIngressAcl` | `string` |  | IPv6 Ingress ACL name or ID applied to incoming traffic on this VE port. |


**Responses:**

- `200` OK → `Switch_Services_VePort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switches/{switchId}/vePorts`

**Retrieve Virtual Ethernet Settings**

Retrieve virtual ethernet ports of the specified switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts can be used for this content.

operationId: `GetVePortsBySwitch_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VePort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/vePorts`

**Add Virtual Ethernet Settings**

Add virtual ethernet ports of the switch. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts can be used for this content.

operationId: `AddVePorts_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_VePort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switches/{switchId}/vePorts/query`

**Retrieve Virtual Ethernet Settings**

Retrieve virtual ethernet ports of switch by query. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/switches/{switchId}/vePorts/query can be used for this content.

operationId: `GetVePortsByQuery_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_FilterableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/vePorts`

**Delete Virtual Ethernet Settings**

Delete multiple virtual ethernet ports.

operationId: `DeleteVePorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/vePorts`

**Retrieve Virtual Ethernet Settings**

Retrieve virtual ethernet ports of the specified switch.

operationId: `GetVePortsBySwitch`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/vePorts`

**Add Virtual Ethernet Settings**

Add virtual ethernet ports of the switch.

operationId: `AddVePorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `201` Created → `Switch_Services_VePortResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/switches/{switchId}/vePorts/query`

**Retrieve Virtual Ethernet Settings**

Retrieve virtual ethernet ports of switch by query.

operationId: `GetVePortsByQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_FilterableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/switches/{switchId}/vePorts/{vePortId}`

**Delete Virtual Ethernet Setting**

Delete virtual ethernet port.

operationId: `DeleteVePort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `vePortId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switches/{switchId}/vePorts/{vePortId}`

**Get Virtual Ethernet Setting**

Get a specified virtual ethernet port.

operationId: `GetVePort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `vePortId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VePort_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switches/{switchId}/vePorts/{vePortId}`

**Update Virtual Ethernet Setting**

Update virtual ethernet port.

operationId: `UpdateVePort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `switchId` | path | ✓ | `string` |  |
| `vePortId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VePortDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpRelayAgent` | `string` |  | The IP address of the DHCP relay agent for forwarding DHCP requests across subnets. |
| `egressAcl` | `string` |  | The name of the Access Control List applied to egress traffic on this VE interface. |
| `ingressAcl` | `string` |  | The name of the Access Control List applied to ingress traffic on this VE interface. |
| `ipAddress` | `string` |  | The IPv4 address assigned to this virtual ethernet interface. |
| `ipAddressType` | `string` |  | The IP address assignment method for this VE interface: static or dynamic. |
| `ipSubnetMask` | `string` |  | The subnet mask for the IP address of this virtual ethernet interface. |
| `name` | `string` |  | The descriptive name assigned to the virtual ethernet interface. |
| `ospfArea` | `string` |  | The OSPF area identifier for routing protocol configuration on this VE interface. |
| `veId` | `integer` |  | The virtual ethernet interface identifier, used as the VE interface number. |
| `vlanId` | `integer` |  | The VLAN ID associated with this virtual ethernet interface for layer 3 routing. |


**Responses:**

- `200` OK → `Switch_Services_VePortResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/vePorts/query`

**Retrieve Virtual Ethernet Settings**

Retrieve virtual ethernet ports of venue by query.

operationId: `GetVePortsByVenueQuery_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_FilterableQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `filterType` | `string` |  | The dynamic filter type (deprecated, use filters instead). |
| `filters` | `object` |  | The dynamic filter map where keys are field names and values are lists of filter criteria to apply for each field. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Trusted Port

*Manage a port's trust settings.*


*6 endpoints*


### `DELETE` `/switchProfiles/{switchProfileId}/trustedPorts`

**Delete Trusted Ports**

Delete multiple trusted ports of the specified switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `DeleteTrustedPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_OperationResponseBaseViewObject`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/switchProfiles/{switchProfileId}/trustedPorts`

**Add Trusted Port**

Add the trusted port of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `AddTrustedPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_TrustedPortBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `familyId` | `string` |  | ICX switch familyId type (e.g., ICX7150, ICX7250, ICX7450). |
| `id` | `string` |  | Unique identifier for the trusted port configuration. |
| `model` | `string` |  | ICX switch model type (e.g., ICX7150, ICX7250, ICX7450). |
| `slots` | `array` |  | Set of slot configurations for modular switches with expansion slots. |
| `tenantId` | `string` |  | The unique identifier of the tenant. |
| `trustPorts` | `array` |  | List of port identifiers configured as trusted ports for QoS priority marking. |
| `trustedPortType` | `string` |  | Trusted port type indicating what traffic priority marking to trust (DOT1P for 802.1p, DSCP for IP DSCP). |
| `vlanDemand` | `boolean` |  | Flag indicating whether VLAN demand is required (default: false). |


**Responses:**

- `200` OK → `Switch_Services_TrustedPort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/switchProfiles/{switchProfileId}/trustedPorts/{trustedPortId}`

**Delete Trusted Port**

Delete the specified trusted port of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `DeleteTrustedPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `trustedPortId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/switchProfiles/{switchProfileId}/trustedPorts/{trustedPortId}`

**Get Trusted Port**

Get the specified trusted port of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `GetTrustedPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `trustedPortId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_TrustedPort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/switchProfiles/{switchProfileId}/trustedPorts/{trustedPortId}`

**Update Trusted Port**

Update the trusted port of the switch profile. This method will be removed no sooner than 06/30/2026.

operationId: `UpdateTrustedPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `switchProfileId` | path | ✓ | `string` |  |
| `trustedPortId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_TrustedPortBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `familyId` | `string` |  | ICX switch familyId type (e.g., ICX7150, ICX7250, ICX7450). |
| `id` | `string` |  | Unique identifier for the trusted port configuration. |
| `model` | `string` |  | ICX switch model type (e.g., ICX7150, ICX7250, ICX7450). |
| `slots` | `array` |  | Set of slot configurations for modular switches with expansion slots. |
| `tenantId` | `string` |  | The unique identifier of the tenant. |
| `trustPorts` | `array` |  | List of port identifiers configured as trusted ports for QoS priority marking. |
| `trustedPortType` | `string` |  | Trusted port type indicating what traffic priority marking to trust (DOT1P for 802.1p, DSCP for IP DSCP). |
| `vlanDemand` | `boolean` |  | Flag indicating whether VLAN demand is required (default: false). |


**Responses:**

- `200` OK → `Switch_Services_TrustedPort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/trustedPorts`

**Get Trusted Ports**

Retrieve trusted ports with the specified venue. This method will be removed no sooner than 06/30/2026.

operationId: `GetTrustedPortsByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_TrustedPort_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Venue Switch Setting

*Manage a switch's venue level settings.*


*3 endpoints*


### `DELETE` `/venues/{venueId}/switchSettings`

**Delete Venue Switch Settings**

Delete switch settings of the venue. This method will be removed no sooner than 06/30/2026.The following URL /venues/{venueId}/switchSettings with PUT method can be used for this content.

operationId: `DeleteVenueSwitchSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_OperationResponseBaseViewObject`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/switchSettings`

**Get Venue Switch Setting**

Get the switch settings of the venue.

operationId: `GetVenueSetting_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_Venue_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/switchSettings`

**Update Venue Switch Setting**

Update the switch settings of the venue. Use activity API with request id to get the status update.

operationId: `UpdateVenueSetting_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_UpdateVenueSettingBo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dns` | `array` |  | List of DNS server IP addresses for switches in this venue. |
| `id` | `string` |  | Unique identifier for the venue. |
| `profileId` | `array` |  | List of profile identifiers to be associated with this venue. |
| `syslogEnabled` | `boolean` |  | Enable syslog for centralized logging (default: false). |
| `syslogPrimaryServer` | `string` |  | Primary syslog server IP address or hostname. |
| `syslogSecondaryServer` | `string` |  | Secondary syslog server IP address or hostname for redundancy. |


**Responses:**

- `200` OK → `Switch_Services_Venue_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Venue Template AAA Server

*Manage venue template AAA (authentication, authorization, and accounting) servers.*


*10 endpoints*


### `DELETE` `/templates/venues/aaaServers`

**Delete Venue Template AAA Servers**

Delete venue template's multiple authentication, authorization, and accounting servers. This method will be removed no sooner than 06/30/2026. The following URL /templates/venues/{venueId}/aaaServers can be used for this content.

operationId: `DeleteVenueTemplateAaaServers_1`


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/templates/venues/aaaServers/query`

**Query Venue Template AAA Servers**

List of venue template's authentication, authorization, and accounting servers. This method will be removed no sooner than 06/30/2026. The following URL /templates/venues/{venueId}/aaaServers/query can be used for this content.

operationId: `QueryVenueTemplateAaaServers_1`


**Request Body:** `Switch_Services_AaaServerQueryRequest_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `serverType` | `string` |  | The type of AAA server to filter by, with the default value set to LOCAL if not specified. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |
| `venueId` | `string` |  | The venue identifier to filter AAA servers by specific venue location. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/aaaServers/{aaaServerId}`

**Delete Venue Template AAA Server**

Delete venue template's authentication, authorization, and accounting server by id. This method will be removed no sooner than 06/30/2026. The following URL /templates/venues/{venueId}/aaaServers/{aaaServerId} can be used for this content.

operationId: `DeleteVenueTemplateAaaServer_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/templates/venues/aaaServers/{aaaServerId}`

**Get Venue Template AAA Server**

Get venue template's authentication, authorization, and accounting server. This method will be removed no sooner than 06/30/2026. The following URL /templates/venues/{venueId}/aaaServers/{aaaServerId} can be used for this content.

operationId: `GetVenueTemplateAaaServer_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AAAServer_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueId}/aaaServers`

**Delete Venue Template AAA Servers**

Delete venue template's multiple authentication, authorization, and accounting servers. Add prefix '/rec' for REC templates.

operationId: `DeleteVenueTemplateAaaServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** Yes


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/templates/venues/{venueId}/aaaServers`

**Add Venue Template AAA Server**

Add venue template's authentication, authorization, and accounting server. Use activity API with request id to get the status update.

operationId: `AddVenueTemplateAaaServer_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaServerDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctPort` | `integer` |  | The port number for accounting services, ranging from 0 to 65535. |
| `authPort` | `integer` |  | The port number for authentication services, ranging from 0 to 65535. |
| `ip` | `string` |  | The IP address of the AAA server, supporting both IPv4 and IPv6 formats. |
| `level` | `string` |  | The authorization level to be assigned to users authenticated through this server. |
| `name` | `string` |  | The unique name identifier for this AAA server, with a length between 2 and 64 characters. |
| `password` | `string` |  | The password credential for server authentication, with a length between 8 and 64 characters. |
| `purpose` | `string` |  | The purpose of this AAA server, specifying whether it handles authentication, authorization, or accounting. |
| `secret` | `string` |  | The shared secret key for secure communication with the AAA server, with a length between 1 and 64 characters. |
| `serverType` | `string` |  | The AAA server protocol type, such as RADIUS or TACACS+. |
| `username` | `string` |  | The username credential for server authentication, with a length between 2 and 48 characters. |


**Responses:**

- `200` OK → `Switch_Services_AAAServer_V1`
- `201` Created → `Switch_Services_VenueTemplateAaaServerResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/templates/venues/{venueId}/aaaServers/query`

**Query Venue Template AAA Servers**

List of venue template's authentication, authorization, and accounting servers. Add prefix '/rec' for REC templates.

operationId: `QueryVenueTemplateAaaServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaServerQueryRequest_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `serverType` | `string` |  | The type of AAA server to filter by, with the default value set to LOCAL if not specified. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueId}/aaaServers/{aaaServerId}`

**Delete Venue Template AAA Server**

Delete venue template's authentication, authorization, and accounting server by id. Add prefix '/rec' for REC templates.

operationId: `DeleteVenueTemplateAaaServer`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/aaaServers/{aaaServerId}`

**Get Venue Template AAA Server**

Get venue template's authentication, authorization, and accounting server. Add prefix '/rec' for REC templates.

operationId: `GetVenueTemplateAaaServer`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaServerId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VenueTemplateAaaServer_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/aaaServers/{aaaServerId}`

**Update Venue Template AAA Server**

Update venue template's authentication, authorization, and accounting server by id. Use activity API with request id to get the status update.

operationId: `UpdateVenueTemplateAaaServer_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaServerId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaServerDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctPort` | `integer` |  | The port number for accounting services, ranging from 0 to 65535. |
| `authPort` | `integer` |  | The port number for authentication services, ranging from 0 to 65535. |
| `ip` | `string` |  | The IP address of the AAA server, supporting both IPv4 and IPv6 formats. |
| `level` | `string` |  | The authorization level to be assigned to users authenticated through this server. |
| `name` | `string` |  | The unique name identifier for this AAA server, with a length between 2 and 64 characters. |
| `password` | `string` |  | The password credential for server authentication, with a length between 8 and 64 characters. |
| `purpose` | `string` |  | The purpose of this AAA server, specifying whether it handles authentication, authorization, or accounting. |
| `secret` | `string` |  | The shared secret key for secure communication with the AAA server, with a length between 1 and 64 characters. |
| `serverType` | `string` |  | The AAA server protocol type, such as RADIUS or TACACS+. |
| `username` | `string` |  | The username credential for server authentication, with a length between 2 and 48 characters. |


**Responses:**

- `200` OK → `Switch_Services_VenueTemplateAaaServerResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Venue Template AAA Setting

*Manage venue template AAA (authentication, authorization, and accounting) settings.*


*3 endpoints*


### `GET` `/templates/venues/{venueId}/aaaSettings`

**Retrieve Venue Template AAA Setting**

Retrieve venue template's authentication, authorization, and accounting setting.

operationId: `GetVenueTemplateAaaSettings_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_AaaSetting_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/aaaSettings`

**Update Venue Template AAA Setting**

Update venue template's authentication, authorization, and accounting setting by id. Use activity API with request id to get the status update. Add prefix '/rec' for REC templates.

operationId: `UpdateVenueTemplateAaaSetting`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaSetting_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctCommonsFirstServer` | `string` |  | The first server to receive accounting records for common commands. |
| `acctCommonsLevel` | `string` |  | The accounting level for common commands, determining which commands are logged. |
| `acctCommonsSecondServer` | `string` |  | The second server to receive accounting records for common commands if the first server is unavailable. |
| `acctCommonsThirdServer` | `string` |  | The third server to receive accounting records for common commands if the first two servers are unavailable. |
| `acctEnabledCommand` | `boolean` |  | Indicates whether accounting is enabled for command execution, tracking user commands for auditing purposes. |
| `acctEnabledExec` | `boolean` |  | Indicates whether accounting is enabled for exec mode sessions, tracking user login sessions for auditing purposes. |
| `acctExecFirstServer` | `string` |  | The first server to receive accounting records for exec mode sessions. |
| `acctExecSecondServer` | `string` |  | The second server to receive accounting records for exec mode sessions if the first server is unavailable. |
| `acctExecThirdServer` | `string` |  | The third server to receive accounting records for exec mode sessions if the first two servers are unavailable. |
| `authnEnabledSsh` | `boolean` |  | Indicates whether AAA authentication is enabled for SSH access to the switch. |
| `authnFirstPref` | `string` |  | The first preference method for authentication, specifying the primary authentication mechanism to be used. |
| `authnFourthPref` | `string` |  | The fourth preference method for authentication, used as the final fallback option. |
| `authnSecondPref` | `string` |  | The second preference method for authentication, used as a fallback if the first method fails. |
| `authnThirdPref` | `string` |  | The third preference method for authentication, used as a fallback if the second method fails. |
| `authzCommonsFirstServer` | `string` |  | The first server to be consulted for common command authorization. |
| `authzCommonsLevel` | `string` |  | The authorization level for common commands, determining the privilege level required. |
| `authzCommonsSecondServer` | `string` |  | The second server to be consulted for common command authorization if the first server is unavailable. |
| `authzCommonsThirdServer` | `string` |  | The third server to be consulted for common command authorization if the first two servers are unavailable. |
| `authzEnabledCommand` | `boolean` |  | Indicates whether authorization is enabled for command execution on the switch. |
| `authzEnabledExec` | `boolean` |  | Indicates whether authorization is enabled for exec mode access on the switch. |
| `authzExecFirstServer` | `string` |  | The first server to be consulted for exec mode authorization. |
| `authzExecSecondServer` | `string` |  | The second server to be consulted for exec mode authorization if the first server is unavailable. |
| `authzExecThirdServer` | `string` |  | The third server to be consulted for exec mode authorization if the first two servers are unavailable. |
| `id` | `string` |  |  |


**Responses:**

- `200` OK → `Switch_Services_AaaSettingResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/aaaSettings/{aaaSettingId}`

**Update Venue Template AAA Setting**

Update venue template's authentication, authorization, and accounting setting by id. Use activity API with request id to get the status update. This method will be removed no sooner than 06/30/2026. The following URL /templates/venues/{venueId}/aaaSettings can be used for this content.

operationId: `UpdateVenueTemplateAaaSetting_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `aaaSettingId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_AaaSettingBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `acctCommonsFirstServer` | `string` |  | First preference for accounting command server. |
| `acctCommonsLevel` | `string` |  | Accounting command privilege level. |
| `acctCommonsSecondServer` | `string` |  | Second preference for accounting command server. |
| `acctCommonsThirdServer` | `string` |  | Third preference for accounting command server. |
| `acctEnabledCommand` | `boolean` |  | Enable or disable command accounting (default: false). |
| `acctEnabledExec` | `boolean` |  | Enable or disable exec accounting (default: false). |
| `acctExecFirstServer` | `string` |  | First preference for accounting exec server. |
| `acctExecSecondServer` | `string` |  | Second preference for accounting exec server. |
| `acctExecThirdServer` | `string` |  | Third preference for accounting exec server. |
| `authnEnabledSsh` | `boolean` |  | Enable or disable SSH authentication (default: true). |
| `authnFirstPref` | `string` |  | First preference for authentication server type. |
| `authnFourthPref` | `string` |  | Fourth preference for authentication server type. |
| `authnSecondPref` | `string` |  | Second preference for authentication server type. |
| `authnThirdPref` | `string` |  | Third preference for authentication server type. |
| `authzCommonsFirstServer` | `string` |  | First preference for authorization command server. |
| `authzCommonsLevel` | `string` |  | Authorization command privilege level. |
| `authzCommonsSecondServer` | `string` |  | Second preference for authorization command server. |
| `authzCommonsThirdServer` | `string` |  | Third preference for authorization command server. |
| `authzEnabledCommand` | `boolean` |  | Enable or disable command authorization (default: false). |
| `authzEnabledExec` | `boolean` |  | Enable or disable exec authorization (default: false). |
| `authzExecFirstServer` | `string` |  | First preference for authorization exec server. |
| `authzExecSecondServer` | `string` |  | Second preference for authorization exec server. |
| `authzExecThirdServer` | `string` |  | Third preference for authorization exec server. |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Venue Template Switch Setting

*Manage switch settings of venue template.*


*2 endpoints*


### `GET` `/templates/venues/{venueId}/switchSettings`

**Get Venue Template Switch Setting**

Get the switch settings of the venue template.

operationId: `GetVenueTemplateSetting_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_VenueTemplate_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/switchSettings`

**Update Venue Template Switch Setting**

Update the switch settings of the venue template. Use activity API with request id to get the status update.

operationId: `UpdateVenueTemplateSetting_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_VenueTemplateDto_V1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dns` | `array` |  | List of DNS server IP addresses for switches in venues using this template. |
| `id` | `string` |  |  |
| `profileId` | `array` |  | Set of profile identifiers associated with this venue template. |
| `syslogEnabled` | `boolean` |  | Enable syslog for centralized logging of switches in venues using this template (default: false). |
| `syslogPrimaryServer` | `string` |  | Primary syslog server IP address or hostname for the template. |
| `syslogSecondaryServer` | `string` |  | Secondary syslog server IP address or hostname for redundancy in the template. |


**Responses:**

- `200` OK → `Switch_Services_VenueResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---



## Web Authentication Page Template

*Manage web authentication page template.*


*6 endpoints*


### `POST` `/webAuthPageTemplates`

**Add Web Authentication Template**

Add web authentication page template.

operationId: `AddWebAuthPageTemplate_1_1`


**Request Body:** `Switch_Services_WebAuthPageTemplateBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  | Unique identifier for the web auth page template (maximum 37 characters). |
| `name` | `string` | ✓ | Template name for identification (maximum 32 characters, required). |
| `tag` | `string` |  | Tag for categorizing or grouping templates (maximum 255 characters). |
| `tenantId` | `string` |  | The unique identifier of the tenant. |
| `webAuthCustomBottom` | `string` |  | Custom text displayed at the bottom section of the login page (maximum 255 characters). |
| `webAuthCustomLoginButton` | `string` |  | Custom text for the login button (maximum 32 characters). |
| `webAuthCustomTitle` | `string` |  | Custom title text displayed at the top of the login page (maximum 128 characters). |
| `webAuthCustomTop` | `string` |  | Custom text displayed at the top section of the login page (maximum 255 characters). |
| `webAuthPasswordLabel` | `string` |  | Custom label text for the password input field (maximum 32 characters). |


**Responses:**

- `200` OK → `Switch_Services_WebAuthPageTemplate_V1`
- `201` Created → `Switch_Services_WebAuthPageTemplateResponse_V1_1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `POST` `/webAuthPageTemplates/query`

**Query Web Authentication Templates**

List of tenant's web authentication page templates.

operationId: `QueryWebAuthPageTemplates_1_1`


**Request Body:** `Switch_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  | The list of field names to include in the query response, allowing clients to request only specific fields. |
| `page` | `integer` |  | The page number for pagination, starting from 1, defaulting to 1. |
| `pageSize` | `integer` |  | The number of records to return per page, defaulting to 25. |
| `sortField` | `string` |  | The field name to use for sorting the query results. |
| `sortOrder` | `string` |  | The sort order direction for the query results, either ascending or descending, defaulting to ascending. |


**Responses:**

- `200` OK → `Switch_Services_QueryResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `DELETE` `/webAuthPageTemplates/{templateId}`

**Delete Web Authentication Template**

Delete web authentication page template by id.

operationId: `DeleteWebAuthPageTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_EmptyResponse`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/webAuthPageTemplates/{templateId}`

**Get Web Authentication Template**

Get a web authentication page template by id.

operationId: `GetWebAuthPageTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_WebAuthPageTemplate_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `PUT` `/webAuthPageTemplates/{templateId}`

**Update Web Authentication Template**

Update web authentication page template by id.

operationId: `PutWebAuthPageTemplate_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Request Body:** `Switch_Services_WebAuthPageTemplateBo_V1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  | Unique identifier for the web auth page template (maximum 37 characters). |
| `name` | `string` | ✓ | Template name for identification (maximum 32 characters, required). |
| `tag` | `string` |  | Tag for categorizing or grouping templates (maximum 255 characters). |
| `tenantId` | `string` |  | The unique identifier of the tenant. |
| `webAuthCustomBottom` | `string` |  | Custom text displayed at the bottom section of the login page (maximum 255 characters). |
| `webAuthCustomLoginButton` | `string` |  | Custom text for the login button (maximum 32 characters). |
| `webAuthCustomTitle` | `string` |  | Custom title text displayed at the top of the login page (maximum 128 characters). |
| `webAuthCustomTop` | `string` |  | Custom text displayed at the top section of the login page (maximum 255 characters). |
| `webAuthPasswordLabel` | `string` |  | Custom label text for the password input field (maximum 32 characters). |


**Responses:**

- `200` OK → `Switch_Services_WebAuthPageTemplate_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---

### `GET` `/webAuthPageTemplates/{templateId}/switches`

**Get Template Switch Info**

Get a web authentication page template's switch info by id.

operationId: `GetWebAuthPageTemplateSwitchInfo_1_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `templateId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Switch_Services_WebAuthPageTemplate_V1`
- `400` Bad/malformed request → `Switch_Services_ErrorResponse`
- `401` Unauthorized → `Switch_Services_ErrorResponse`
- `403` Forbidden → `Switch_Services_ErrorResponse`
- `404` Requested resource or related entity not found → `Switch_Services_ErrorResponse`
- `422` Validation error → `Switch_Services_ErrorResponse`
- `500` Internal Server Error → `Switch_Services_ErrorResponse`


---


