# RUCKUS Edge

> RUCKUS One API Reference

---


## Edge DNS Configuration

*Manage the DNS server for a Edge.*


*2 endpoints*


### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/dnsServers`

**Get DNS Configuration**

Get the DNS configuration.

operationId: `getEdgeDnsServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_DnsServersDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/dnsServers`

**Update DNS Configuration**

Patch the DNS configuration.

operationId: `patchEdgeDnsServers`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_DnsServersDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `primary` | `string` |  | The primary DNS server IP address. |
| `secondary` | `string` |  | The secondary DNS server IP address. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Cluster Configuration

*Manage the Edge cluster.*


*7 endpoints*


### `GET` `/venues/{venueId}/edgeClusters`

**Get Edge Clusters**

Get a list of Edge clusters.

operationId: `getEdgeClustersByPage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `page` | query |  | `integer` | Page index |
| `pageSize` | query |  | `integer` | The size of the page to be returned |


**Responses:**

- `200` OK → `RUCKUS_Edge_PageResponseClusterResponseDtoV1_1`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `POST` `/venues/{venueId}/edgeClusters`

**Create Edge Cluster**

Create a edge cluster.

operationId: `createEdgeCluster`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_CreateClusterDtoV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of the cluster. |
| `highAvailabilityMode` | `string` |  | The high availability mode. |
| `members` | `array` |  | A list of Edge devices to be in the cluster. |
| `name` | `string` |  | The name of the cluster. |
| `smartEdges` | `array` |  | A list of Edge devices to be in the cluster. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/venues/{venueId}/edgeClusters/{clusterId}`

**Delete a Edge Cluster**

Delete a Edge cluster.

operationId: `deleteSingleEdgeCluster`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/venues/{venueId}/edgeClusters/{clusterId}`

**Get Edge Cluster**

Get the Edge cluster by unique identifier.

operationId: `getEdgeCluster`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_ClusterResponseDtoV1_1`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}`

**Update Edge Cluster**

Update edge cluster configuration.

operationId: `updateEdgeCluster`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_PatchClusterDtoV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of the cluster. |
| `members` | `array` |  | A list of Edge devices to be in the cluster. |
| `name` | `string` |  | The name of the cluster. |
| `smartEdges` | `array` |  | A list of Edge devices to be in the cluster. |
| `virtualIpSettings` | `RUCKUS_Edge_VirtualIpSettingsDto` |  | The virtual IP settings of the cluster. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/networkSettings`

**Get Edge Cluster Network**

Get Edge cluster network settings.

operationId: `getEdgeClusterNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_ClusterNetworkSettingsResponseDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/networkSettings`

**Update Edge Cluster Network**

Update Edge cluster network settings.

operationId: `updateEdgeClusterNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_PatchClusterNetworkSettingsDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `highAvailabilitySettings` | `RUCKUS_Edge_HighAvailabilitySettingsDto` |  | High availability settings for active-active clusters. |
| `lagSettings` | `array` |  | List of cluster edges LAG settings. |
| `multiWanSettings` | `RUCKUS_Edge_ClusterNetworkMultiWanSettingsDto` |  | Multi WAN settings for the Edge cluster. |
| `portSettings` | `array` |  | List of cluster edges port settings. |
| `subInterfaceSettings` | `array` |  | List of cluster subinterface settings. |
| `virtualIpSettings` | `array` |  | List of cluster virtual IP settings for active-standby clusters. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge LAG Configuration

*Manage the link aggregation group for Edge devices.*


*5 endpoints*


### `POST` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags`

**Create Link Aggregation Group**

Create the link aggregation groups.

operationId: `createEdgeLinkAggregationGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_LinkAggregationGroupDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `description` | `string` |  | The description of the LAG. |
| `gateway` | `string` |  | The gateway address of the port. |
| `id` | `integer` | ✓ | The ID of the LAG, support from 0 to 3. |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The ip mode of the LAG. |
| `lacpMode` | `string` | ✓ | LACP operation mode (ACTIVE or PASSIVE) for link aggregation. |
| `lacpTimeout` | `string` | ✓ | LACP timeout interval (SHORT or LONG) for link failure detection. |
| `lagEnabled` | `boolean` | ✓ | Whether to enable the LAG. |
| `lagMembers` | `array` |  | List of port members in the LAG. |
| `lagType` | `string` |  | The type of the LAG only support the link aggregation control protocol. |
| `natEnabled` | `boolean` |  | Whether to enable the network address translation on the wan port. |
| `natPools` | `array` |  | List of NAT pools associated with the LAG. |
| `portType` | `string` | ✓ | The port type of the LAG. |
| `reportIp` | `string` |  | IP reported by edge device. |
| `reportSubnet` | `string` |  | Subnet mask reported by edge device. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}`

**Delete Link Aggregation Group**

Delete the link aggregation group by unique identifier.

operationId: `deleteEdgeLinkAggregationGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `integer` |  |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}`

**Get Link Aggregation Group**

Get the link aggregation group by unique identifier.

operationId: `getEdgeLinkAggregationGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `integer` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_LinkAggregationGroupDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}`

**Partial Update Link Aggregation Group**

Partial update of the link aggregation group by unique identifier.

operationId: `partialUpdateEdgeLinkAggregationGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `integer` |  |


**Request Body:** `RUCKUS_Edge_UpdateLinkAggregationGroupDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `description` | `string` |  | The description of the LAG. |
| `gateway` | `string` |  | The gateway address of the port. |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The ip mode of the LAG. |
| `lacpMode` | `string` | ✓ | LACP operation mode (ACTIVE or PASSIVE) for link aggregation. |
| `lacpTimeout` | `string` | ✓ | LACP timeout interval (SHORT or LONG) for link failure detection. |
| `lagEnabled` | `boolean` | ✓ | Whether to enable the LAG. |
| `lagMembers` | `array` |  | List of port members in the LAG. |
| `lagType` | `string` |  | The type of the LAG only support the link aggregation control protocol. |
| `natEnabled` | `boolean` |  | Whether to enable the network address translation on the wan port. |
| `natPools` | `array` |  | List of NAT pools associated with the LAG. |
| `portType` | `string` | ✓ | The port type of the LAG. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}`

**Update Link Aggregation Group**

Updates the link aggregation group by unique identifier.

operationId: `updateEdgeLinkAggregationGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |
| `lagId` | path | ✓ | `integer` |  |


**Request Body:** `RUCKUS_Edge_UpdateLinkAggregationGroupDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `description` | `string` |  | The description of the LAG. |
| `gateway` | `string` |  | The gateway address of the port. |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The ip mode of the LAG. |
| `lacpMode` | `string` | ✓ | LACP operation mode (ACTIVE or PASSIVE) for link aggregation. |
| `lacpTimeout` | `string` | ✓ | LACP timeout interval (SHORT or LONG) for link failure detection. |
| `lagEnabled` | `boolean` | ✓ | Whether to enable the LAG. |
| `lagMembers` | `array` |  | List of port members in the LAG. |
| `lagType` | `string` |  | The type of the LAG only support the link aggregation control protocol. |
| `natEnabled` | `boolean` |  | Whether to enable the network address translation on the wan port. |
| `natPools` | `array` |  | List of NAT pools associated with the LAG. |
| `portType` | `string` | ✓ | The port type of the LAG. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge LAG Subinterface

*Manage the subinterface of a LAG.*


*4 endpoints*


### `POST` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}/subInterfaces`

**Create Subinterface**

Create a subinterfaces of a LAG.

operationId: `createEdgeLagSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `lagId` | path | ✓ | `integer` | ID of the LAG |


**Request Body:** `RUCKUS_Edge_LagSubInterfaceDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `gateway` | `string` |  | The gateway address of the port. |
| `id` | `string` |  |  |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The IP mode for the subinterface. |
| `portType` | `string` | ✓ | The port type of the subinterface. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |
| `vlan` | `integer` | ✓ | The virtual LAN ID of the subinterface. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}/subInterfaces/{subInterfaceId}`

**Delete Subinterface**

Delete a subinterfaces of a LAG.

operationId: `deleteEdgeLagSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `lagId` | path | ✓ | `integer` | ID of the LAG |
| `subInterfaceId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}/subInterfaces/{subInterfaceId}`

**Get Subinterface**

Get the subinterface of a LAG.

operationId: `getEdgeLagSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `lagId` | path | ✓ | `integer` | ID of the LAG |
| `subInterfaceId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_LagSubInterfaceDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{edgeClusterId}/edges/{serialNumber}/lags/{lagId}/subInterfaces/{subInterfaceId}`

**Partial Update Subinterface**

Partial update a subinterface of a LAG.

operationId: `patchEdgeLagSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `lagId` | path | ✓ | `integer` | ID of the LAG |
| `subInterfaceId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_LagSubInterfaceDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `gateway` | `string` |  | The gateway address of the port. |
| `id` | `string` |  |  |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The IP mode for the subinterface. |
| `portType` | `string` | ✓ | The port type of the subinterface. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |
| `vlan` | `integer` | ✓ | The virtual LAN ID of the subinterface. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Tunnel Profile Configuration

*Manage the tunnel profile.*


*2 endpoints*


### `DELETE` `/venues/{venueId}/edgeClusters/{clusterId}/tunnelProfiles/{tunnelProfileId}`

**Deactivate Tunnel on Edge Cluster**

Deactivate tunnel profile on edge cluster.

operationId: `edgeClusterDeactivateTunnelProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `tunnelProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/venues/{venueId}/edgeClusters/{clusterId}/tunnelProfiles/{tunnelProfileId}`

**Activate Tunnel on Edge Cluster**

Activate tunnel profile on edge cluster.

operationId: `edgeClusterActivateTunnelProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `tunnelProfileId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Subinterface Configuration

*Manage the subinterface of a physical port.*


*4 endpoints*


### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/ports/{portId}/subInterfaces`

**Get Subinterfaces**

Get subinterfaces of a physical port.

operationId: `getEdgeSubInterfaces`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `portId` | path | ✓ | `string` | The ID of the physical port |
| `page` | query |  | `integer` |  |
| `pageSize` | query |  | `integer` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_GetSubInterfaceResponseDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `POST` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/ports/{portId}/subInterfaces`

**Create Subinterface**

Create a subinterfaces of a physical port.

operationId: `createEdgeSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `portId` | path | ✓ | `string` | The ID of the physical port |


**Request Body:** `RUCKUS_Edge_SubInterfaceDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `gateway` | `string` |  | The gateway address of the port. |
| `id` | `string` |  |  |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The IP mode for the subinterface. |
| `portType` | `string` |  | The port type of the subinterface. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |
| `vlan` | `integer` | ✓ | The virtual LAN ID of the subinterface. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/ports/{portId}/subInterfaces/{subInterfaceId}`

**Delete Subinterface**

Delete a subinterfaces of a physical port.

operationId: `deleteEdgeSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `portId` | path | ✓ | `string` | The ID of the physical port |
| `subInterfaceId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/ports/{portId}/subInterfaces/{subInterfaceId}`

**Update Subinterface**

Update a subinterface of a physical port.

operationId: `patchEdgeSubInterface`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |
| `portId` | path | ✓ | `string` | The ID of the physical port |
| `subInterfaceId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_SubInterfaceDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accessPortEnabled` | `boolean` |  | Whether to mark this port as a access port. |
| `corePortEnabled` | `boolean` |  | Whether to mark this port as a core port. |
| `gateway` | `string` |  | The gateway address of the port. |
| `id` | `string` |  |  |
| `ip` | `string` |  | The IP address to be assigned to the port. |
| `ipMode` | `string` |  | The IP mode for the subinterface. |
| `portType` | `string` |  | The port type of the subinterface. |
| `subnet` | `string` |  | The IP subnet mask to be assigned to the port. |
| `vlan` | `integer` | ✓ | The virtual LAN ID of the subinterface. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Static Route Configuration

*Manage the static routes for a Edge.*


*2 endpoints*


### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/staticRouteConfigs`

**Get Static Route Configuration**

Get static routes configuration.

operationId: `getEdgeStaticRouteConfig`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |


**Responses:**

- `200` OK → `RUCKUS_Edge_StaticRouteConfigDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/staticRouteConfigs`

**Update Static Route Configuration**

Patch static route configuration.

operationId: `patchEdgeStaticRouteConfig`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |


**Request Body:** `RUCKUS_Edge_StaticRouteConfigDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `routes` | `array` |  | List of static route configurations. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Multicast DNS Profile

*Manage the Multicast DNS Profile for Edge devices.*


*6 endpoints*


### `POST` `/edgeMulticastDnsProxyProfiles`

**Create Multicast DNS Profile**

Create multicast DNS profile.

operationId: `createMdnsProxyProfile`


**Request Body:** `RUCKUS_Edge_EdgeMdnsProxyProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `forwardingRules` | `array` |  | Up to 32 rules may be added. |
| `id` | `string` |  | The identifier of the multicast DNS proxy. |
| `name` | `string` | ✓ | The name of the multicast DNS proxy. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/edgeMulticastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Delete Multicast DNS Profile**

Delete multicast DNS profile.

operationId: `deleteMdnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The ID of Multicast DNS profile. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/edgeMulticastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Get Multicast DNS Profile**

Get multicast DNS profile.

operationId: `getMdnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The ID of Multicast DNS profile. |


**Responses:**

- `200` OK → `RUCKUS_Edge_EdgeMdnsProxyProfile`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/edgeMulticastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Update Multicast DNS Profile**

Update multicast DNS profile.

operationId: `updateMdnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The ID of Multicast DNS profile. |


**Request Body:** `RUCKUS_Edge_EdgeMdnsProxyProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `forwardingRules` | `array` |  | Up to 32 rules may be added. |
| `id` | `string` |  | The identifier of the multicast DNS proxy. |
| `name` | `string` | ✓ | The name of the multicast DNS proxy. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/edgeMulticastDnsProxyProfiles/{multicastDnsProxyProfileId}/venues/{venueId}/edgeClusters/{edgeClusterId}`

**Deactivate Multicast DNS**

Deactivate multicast DNS on edge cluster.

operationId: `DeactivateMdnsProxy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` |  |
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/edgeMulticastDnsProxyProfiles/{multicastDnsProxyProfileId}/venues/{venueId}/edgeClusters/{edgeClusterId}`

**Activate Multicast DNS**

Activate multicast DNS on edge cluster.

operationId: `ActivateMdnsProxy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` |  |
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Troubleshooting

*Manage troubleshooting operations for the devices.*


*1 endpoint*


### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/hostDetails`

**Trigger Edge Action**

Allows for the edge troubleshooting actions.

operationId: `TriggerEdgeAction`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The serial number of the EDGE. |


**Request Body:** `RUCKUS_Edge_TroubleshootingDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` | ✓ | The action to perform on the Edge device. |
| `targetHost` | `string` |  | The target host IP address or domain name for the troubleshooting action. |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge DHCP

*Manage the DHCP services for Edge devices.*


*8 endpoints*


### `POST` `/edgeDhcpServices`

**Create DHCP**

Create DHCP configuration for edge cluster.

operationId: `createDhcp`


**Request Body:** `RUCKUS_Edge_EdgeDhcpProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpOptions` | `array` |  | List of DHCP options. |
| `dhcpPools` | `array` |  | List of DHCP pools. |
| `dhcpRelay` | `boolean` |  | Whether DHCP relay is enabled. |
| `domainName` | `string` |  | The domain name for DHCP clients. |
| `externalDhcpServerFqdnIp` | `string` |  | The external DHCP server FQDN or IP address. |
| `hosts` | `array` |  | List of DHCP hosts with fixed IP addresses. |
| `id` | `string` |  | The identifier of the Edge DHCP profile. |
| `leaseTime` | `integer` |  | The lease time duration. |
| `leaseTimeUnit` | `string` |  | The unit of the lease time. |
| `primaryDnsIp` | `string` |  | The primary DNS server IP address. |
| `secondaryDnsIp` | `string` |  | The secondary DNS server IP address. |
| `serviceName` | `string` |  | The name of the DHCP service. |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `POST` `/edgeDhcpServices/edgeCompatibilities/query`

**Query DHCP Edge Compatibility Details**

Query the compatibility info of Edge by DHCP services.

operationId: `queryEdgeDhcpServiceCompatibilities`


**Request Body:** `RUCKUS_Edge_ServiceEdgeCompatibilityRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `RUCKUS_Edge_ServiceEdgeCompatibilityFilter` | ✓ | The filters for querying the services of the compatibility. |


**Responses:**

- `200` OK → `RUCKUS_Edge_ServiceEdgeCompatibilityResponseV1_1`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/edgeDhcpServices/{dhcpId}`

**Delete DHCP**

Delete DHCP configuration for edge cluster.

operationId: `deleteDhcpById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/edgeDhcpServices/{dhcpId}`

**Get DHCP**

Get DHCP configuration for edge cluster.

operationId: `getDhcpById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_EdgeDhcpProfile`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/edgeDhcpServices/{dhcpId}`

**Patch DHCP**

Partial update DHCP configuration for edge cluster.

operationId: `patchDhcp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_PatchEdgeDhcpProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` |  | The action to perform on the DHCP service. |
| `dhcpOptions` | `array` |  | List of DHCP options. |
| `dhcpPools` | `array` |  | List of DHCP pools. |
| `dhcpRelay` | `boolean` |  | Whether DHCP relay is enabled. |
| `domainName` | `string` |  | The domain name for DHCP clients. |
| `externalDhcpServerFqdnIp` | `string` |  | The external DHCP server FQDN or IP address. |
| `hosts` | `array` |  | List of DHCP hosts with fixed IP addresses. |
| `leaseTime` | `integer` |  | The lease time duration. |
| `leaseTimeUnit` | `string` |  | The unit of the lease time. |
| `primaryDnsIp` | `string` |  | The primary DNS server IP address. |
| `secondaryDnsIp` | `string` |  | The secondary DNS server IP address. |
| `serviceName` | `string` |  | The name of the DHCP service. |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/edgeDhcpServices/{dhcpId}`

**Update DHCP**

Update DHCP configuration for edge cluster.

operationId: `updateDhcp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_UpdateEdgeDhcpProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `string` |  | The action to perform on the DHCP service. |
| `dhcpOptions` | `array` |  | List of DHCP options. |
| `dhcpPools` | `array` |  | List of DHCP pools. |
| `dhcpRelay` | `boolean` |  | Whether DHCP relay is enabled. |
| `domainName` | `string` |  | The domain name for DHCP clients. |
| `externalDhcpServerFqdnIp` | `string` |  | The external DHCP server FQDN or IP address. |
| `hosts` | `array` |  | List of DHCP hosts with fixed IP addresses. |
| `leaseTime` | `integer` |  | The lease time duration. |
| `leaseTimeUnit` | `string` |  | The unit of the lease time. |
| `primaryDnsIp` | `string` |  | The primary DNS server IP address. |
| `secondaryDnsIp` | `string` |  | The secondary DNS server IP address. |
| `serviceName` | `string` |  | The name of the DHCP service. |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/edgeDhcpServices/{dhcpId}/venues/{venueId}/edgeClusters/{edgeClusterId}`

**Deactivate DHCP**

Deactivate DHCP service on edge cluster.

operationId: `DeactivateDhcp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpId` | path | ✓ | `string` |  |
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/edgeDhcpServices/{dhcpId}/venues/{venueId}/edgeClusters/{edgeClusterId}`

**Activate DHCP**

Activate DHCP service on Edge Cluster.

operationId: `ActivateDhcp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpId` | path | ✓ | `string` |  |
| `venueId` | path | ✓ | `string` |  |
| `edgeClusterId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Port Configuration

*Manage the port of a Edge.*


*2 endpoints*


### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/portConfigs`

**Get Physical Port Configuration**

Get the physical port configuration.

operationId: `getEdgePortConfig`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |


**Responses:**

- `200` OK → `RUCKUS_Edge_PortConfigDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}/portConfigs`

**Update Physical Port Configuration**

Patch the physical port configuration.

operationId: `patchEdgePortConfig`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` | The SN of the Edge device |


**Request Body:** `RUCKUS_Edge_PortConfigDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ports` | `array` |  | List of physical port configurations. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## ARP Termination Settings

*Configure ARP termination settings for a cluster.*


*2 endpoints*


### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/arpTerminationSettings`

**Get ARP Termination Settings**

Get ARP termination settings.

operationId: `getArpTerminationSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The ID of venue. |
| `clusterId` | path | ✓ | `string` | The ID of Edge cluster. |


**Responses:**

- `200` OK → `RUCKUS_Edge_EdgeArpTerminationSettings`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PUT` `/venues/{venueId}/edgeClusters/{clusterId}/arpTerminationSettings`

**Update ARP Termination Settings**

Update ARP termination settings.

operationId: `updateArpTerminationSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The ID of venue. |
| `clusterId` | path | ✓ | `string` | The ID of Edge cluster. |


**Request Body:** `RUCKUS_Edge_EdgeArpTerminationSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `agingTimeSec` | `integer` | ✓ | The aging time in seconds for the ARP termination cache. |
| `enabled` | `boolean` |  | Whether the ARP Termination is enabled. |


**Responses:**

- `202` Accepted → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Compatibility Checking

*Check the compatibility of Edge devices.*


*3 endpoints*


### `POST` `/edgeFeatureSets/query`

**Query Edge Features Requirement Information**

Query features' requirement info related to Edge.

operationId: `queryEdgeFeaturesRequirement`


**Request Body:** `RUCKUS_Edge_FeatureSetsRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `RUCKUS_Edge_FeatureSetsFilter` |  | The filters of the FeatureSets. |


**Responses:**

- `200` OK → `RUCKUS_Edge_FeatureSetsResponseV1_1`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `POST` `/venues/edgeAppCompatibilities/query`

**Query EdgeApp Compatibility Information**

Query the EdgeApp firmware compatibility for Edge devices in a venue.

operationId: `queryEdgeAppCompatibilities`


**Request Body:** `RUCKUS_Edge_VenueEdgeAppCompatibilityRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `RUCKUS_Edge_VenueEdgeAppCompatibilityFilter` | ✓ | Filters for querying EdgeApp compatibility. |


**Responses:**

- `200` OK → `RUCKUS_Edge_VenueEdgeAppCompatibilityResponse`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `POST` `/venues/edgeCompatibilities/query`

**Query Venue Edge Compatibility Information**

Query the compatibility info of Edge by venues or devices.

operationId: `queryVenueEdgeCompatibilities`


**Request Body:** `RUCKUS_Edge_VenueEdgeCompatibilityRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `featureNames` | `array` |  | The list of feature names to be queried. |
| `filters` | `RUCKUS_Edge_VenueEdgeCompatibilityFilter` | ✓ | The filters for querying the venues of the compatibility. |


**Responses:**

- `200` OK → `RUCKUS_Edge_VenueEdgeCompatibilityResponseV1_1`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---



## Edge Device Management

*Edge device management operations.*


*4 endpoints*


### `POST` `/venues/{venueId}/edgeClusters/{clusterId}/edges`

**Add Device**

Add a new device.

operationId: `createEdgeDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_CreateEdgeDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of the device. |
| `name` | `string` | ✓ | The name of the device. |
| `serialNumber` | `string` | ✓ | The serial number of the device. |


**Responses:**

- `201` Created → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `DELETE` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}`

**Delete Device**

Delete the device by the serial number.

operationId: `deleteEdgeDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `GET` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}`

**Get Device**

Get device by the serial number.

operationId: `getEdgeDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `RUCKUS_Edge_BaseEdgeDto`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---

### `PATCH` `/venues/{venueId}/edgeClusters/{clusterId}/edges/{serialNumber}`

**Update Device**

Patch the device configuration.

operationId: `patchEdgeDevice`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `clusterId` | path | ✓ | `string` |  |
| `serialNumber` | path | ✓ | `string` |  |


**Request Body:** `RUCKUS_Edge_PatchEdgeDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  | The description of the device. |
| `name` | `string` |  | The name of the device. |
| `otpState` | `string` |  | The OTP state for the Edge device. |


**Responses:**

- `200` OK → `RUCKUS_Edge_OperationResponseObject`
- `400` Bad/malformed request → `RUCKUS_Edge_GeneralErrorResponse`
- `401` Unauthorized → `RUCKUS_Edge_GeneralErrorResponse`
- `403` Forbidden → `RUCKUS_Edge_GeneralErrorResponse`
- `404` Requested resource or related entity not found → `RUCKUS_Edge_GeneralErrorResponse`
- `422` Validation error → `RUCKUS_Edge_GeneralErrorResponse`
- `500` Internal Server Error → `RUCKUS_Edge_GeneralErrorResponse`


---


