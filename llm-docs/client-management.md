# Client Management

> RUCKUS One API Reference

---


## Client Alias

*APIs for managing client aliases.*


*4 endpoints*


### `POST` `/clients/aliases/query`

**Query client aliases**

Query client aliases based on filter criteria such as alias name or MAC address, with support for pagination.

operationId: `queryAliases`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Client_Management_Pageable` | Parameters for paging |


**Request Body:** `Client_Management_ClientAliasQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alias` | `string` |  | A partial match filter for the alias. |
| `macAddresses` | `array` |  | A list of MAC addresses to filter the query. If omitted or empty, the query will not filter by MAC address. |


**Responses:**

- `200` Aliases found → `Client_Management_PageClientAlias`
- `400` Invalid request data → `Client_Management_PageClientAlias`


---

### `DELETE` `/clients/aliases/{macAddress}`

**Delete client alias**

Remove the alias associated with the specified client MAC address.

operationId: `DeleteClientAlias`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `macAddress` | path | ✓ | `string` | MAC address of the client |


**Responses:**

- `202` Request accepted → `Client_Management_OperationResponse`
- `400` Invalid request data → `Client_Management_ApiError`


---

### `GET` `/clients/aliases/{macAddress}`

**Get client alias**

Retrieve the alias information for the specified client MAC address.

operationId: `getAlias`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `macAddress` | path | ✓ | `string` | MAC address of the client |


**Responses:**

- `200` Alias found → `Client_Management_ClientAlias`
- `400` Invalid request data → `Client_Management_ApiError`
- `404` Alias not found → `Client_Management_ApiError`


---

### `PUT` `/clients/aliases/{macAddress}`

**Update or create client alias**

Update or create the alias for the specified client identified by MAC address.

operationId: `CreateUpdateClientAlias`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `macAddress` | path | ✓ | `string` | MAC address of the client |


**Request Body:** `Client_Management_ClientAlias`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `alias` | `string` | ✓ | The alias name of the client. |
| `deviceType` | `string` |  | The type of the device. |
| `id` | `string` |  | The identifier of the client alias. |
| `macAddress` | `string` |  | The MAC address of the client. |


**Responses:**

- `202` Request accepted → `Client_Management_OperationResponse`
- `400` Invalid request data → `Client_Management_ApiError`


---



## Identity Client

*APIs for querying identity client information.*


*2 endpoints*


### `POST` `/identities/clients/query`

**Query Identity Clients**

Query and retrieve a paginated list of clients associated with identities based on filter criteria such as identity IDs.

operationId: `queryIdentityClient`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `pageable` | query | ✓ | `Client_Management_Pageable` | Parameters for paging |


**Request Body:** `Client_Management_ClientQuery`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `aliasFilter` | `string` |  | Filter clients by alias presence. ALL returns all clients, ALIAS returns only clients with alias, NON_ALIAS returns only clients without alias. |
| `clientMacs` | `array` |  | A list of client MAC addresses used to filter specific clients. |
| `groupId` | `string` |  | A group identifier used to filter clients by their identity group. |
| `identityIds` | `array` |  | A list of identity identifiers used to filter and retrieve specific clients associated with those identities. |


**Responses:**

- `200` Clients found → `Client_Management_PageClient`


---

### `POST` `/identities/{identityId}/clients/associations`

**Associate Client to Identity**

Associate one or more clients to a target identity. This operation moves the specified clients from their current identity to the target identity.

operationId: `associateClientToIdentity`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `identityId` | path | ✓ | `string` |  |


**Request Body:** `Client_Management_ClientAssociationRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `clientIds` | `array` | ✓ | List of client IDs to be moved to the target identity. |
| `identityId` | `string` | ✓ | The ID of the destination identity where the specified clients will be moved. |


**Responses:**

- `202` Request accepted. The client association operation has been queued for processing. → `Client_Management_OperationResponse`
- `400` Invalid request data. The request contains validation errors or invalid parameters. → `Client_Management_ApiError`


---


