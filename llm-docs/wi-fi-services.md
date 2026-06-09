# Wi-Fi Services

> RUCKUS One API Reference

---


## Hotspot 2.0 Identity Provider

*Manage Hotspot 2.0 identity providers including creation, updates, and assignments.*


*6 endpoints*


### `POST` `/hotspot20IdentityProviders`

**Add Hotspot 2.0 Identity Provider**

Create a Hotspot 2.0 identity provider to define authentication realms and EAP methods for Wi-Fi Passpoint networks.

operationId: `addHotspot20IdentityProvider`


**Request Body:** `Wi-Fi_Services_Hotspot20IdentityProvider`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accountingRadiusEnabled` | `boolean` |  |  |
| `id` | `string` |  |  |
| `naiRealms` | `array` | ✓ |  |
| `name` | `string` | ✓ |  |
| `plmns` | `array` |  |  |
| `roamConsortiumOIs` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/hotspot20IdentityProviders/{hotspot20IdentityProviderId}`

**Delete Hotspot 2.0 Identity Provider**

Delete a Hotspot 2.0 identity provider by its unique identifier, permanently deleting the provider and its configurations.

operationId: `deleteHotspot20IdentityProvider`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/hotspot20IdentityProviders/{hotspot20IdentityProviderId}`

**Get Hotspot 2.0 Identity Provider**

Retrieve detailed information about a Hotspot 2.0 identity provider by its unique identifier including NAI realms, EAP authentication methods, and RADIUS accounting settings.

operationId: `getHotspot20IdentityProvider`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Hotspot20IdentityProvider`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/hotspot20IdentityProviders/{hotspot20IdentityProviderId}`

**Update Hotspot 2.0 Identity Provider**

Update an existing Hotspot 2.0 identity provider by its unique identifier, updating NAI realms, EAP authentication methods, and RADIUS accounting settings.

operationId: `updateHotspot20IdentityProvider`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider to be modified. |


**Request Body:** `Wi-Fi_Services_Hotspot20IdentityProvider`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accountingRadiusEnabled` | `boolean` |  |  |
| `id` | `string` |  |  |
| `naiRealms` | `array` | ✓ |  |
| `name` | `string` | ✓ |  |
| `plmns` | `array` |  |  |
| `roamConsortiumOIs` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/hotspot20IdentityProviders/{hotspot20IdentityProviderId}`

**Deactivate Hotspot 2.0 Identity Provider On Wi-Fi Network**

Remove the association between a Hotspot 2.0 identity provider and a Wi-Fi network without deleting the provider.

operationId: `deactivateHotspot20IdentityProviderOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the Hotspot 2.0 identity provider will be deactivated. |
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/hotspot20IdentityProviders/{hotspot20IdentityProviderId}`

**Activate Hotspot 2.0 Identity Provider On Wi-Fi Network**

Associate a Hotspot 2.0 identity provider with a Wi-Fi network to enable Passpoint authentication using configured realms and EAP methods.

operationId: `activateHotspot20IdentityProviderOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the Hotspot 2.0 identity provider will be activated. |
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Syslog Server Profile Template

*Manage Syslog server profile templates.*


*6 endpoints*


### `POST` `/templates/syslogServerProfiles`

**Create Syslog Server Profile Template**

Create a new syslog server profile MSP template with syslog servers, facility, priority, and flow level settings.

operationId: `createSyslogServerProfileTemplate`


**Request Body:** `Wi-Fi_Services_SyslogServerProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `facility` | `string` |  |  |
| `flowLevel` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `primary` | `Wi-Fi_Services_SyslogServer` | ✓ |  |
| `priority` | `string` |  |  |
| `secondary` | `Wi-Fi_Services_SyslogServer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/syslogServerProfiles/{syslogServerProfileTemplateId}`

**Delete Syslog Server Profile Template**

Remove a syslog server profile MSP template and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteSyslogServerProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `syslogServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the syslog server profile MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/syslogServerProfiles/{syslogServerProfileTemplateId}`

**Get Syslog Server Profile Template**

Retrieve detailed information about a syslog server profile MSP template including syslog servers, facility, priority, and flow level.

operationId: `getSyslogServerProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `syslogServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the syslog server profile MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_SyslogServerProfileV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/syslogServerProfiles/{syslogServerProfileTemplateId}`

**Update Syslog Server Profile Template**

Update an existing syslog server profile MSP template including syslog servers, facility, priority, and flow level settings.

operationId: `updateSyslogServerProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `syslogServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the syslog server profile MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_SyslogServerProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `facility` | `string` |  |  |
| `flowLevel` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `primary` | `Wi-Fi_Services_SyslogServer` | ✓ |  |
| `priority` | `string` |  |  |
| `secondary` | `Wi-Fi_Services_SyslogServer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueTemplateId}/syslogServerProfiles/{syslogServerProfileTemplateId}`

**Deactivate Syslog Server Profile Template On Venue Template**

Remove the association between a syslog server profile MSP template and a venue MSP template.

operationId: `deactivateSyslogServerProfileTemplateOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template from which the syslog server profile MSP template will be deactivated. |
| `syslogServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the syslog server profile MSP template to be disassociated from the venue MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/syslogServerProfiles/{syslogServerProfileTemplateId}`

**Activate Syslog Server Profile Template On Venue Template**

Associate a syslog server profile MSP template with a venue MSP template to enable syslog forwarding from access points.

operationId: `activateSyslogServerProfileTemplateOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template where the syslog server profile MSP template will be activated. |
| `syslogServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the syslog server profile MSP template to be associated with the venue MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Application Library

*Manage the current tenant's application library settings including signature packages for application visibility and control policies.*


*4 endpoints*


### `GET` `/applicationLibraries/{applicationLibraryId}/categories`

**Get Application Library Categories**

Retrieve a list of all application categories available in the specified application library version. The response includes category identifiers and names used for organizing applications.

operationId: `getApplicationLibraryCategories`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationLibraryId` | path | ✓ | `string` | The unique identifier (version) of the application library whose categories are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApplicationLibraryCategories`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/applicationLibraries/{applicationLibraryId}/categories/{categoryId}/applications`

**Get Application Library Applications**

Retrieve a list of all applications available in the specified category of the application library version. The response includes application identifiers and names that can be used in application policies.

operationId: `getApplicationLibraryApplications`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationLibraryId` | path | ✓ | `string` | The unique identifier (version) of the application library whose applications are to be retrieved. |
| `categoryId` | path | ✓ | `integer` | The unique identifier of the application category whose applications are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApplicationLibraryApplications`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/applicationLibrarySettings`

**Get Application Library Settings**

Retrieve the current application library settings for the tenant. The response includes library version information, release dates, and optionally changed application details when requested.

operationId: `getApplicationLibrarySettingsCsv`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `type` | query |  | `string` | Specify which type of changed application would be included in the response |
| `changesIncluded` | query |  | `boolean` | Include changed application information in response. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApplicationLibrarySettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/applicationLibrarySettings`

**Patch Application Library Settings**

Update application library settings for the tenant. This operation allows you to modify library configuration and trigger library update operations asynchronously.

operationId: `patchApplicationLibrarySettings`


**Request Body:** `Wi-Fi_Services_ApplicationLibrarySettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `changedApplications` | `array` |  |  |
| `latestReleasedDate` | `string` |  |  |
| `latestVersion` | `string` |  |  |
| `releasedDate` | `string` |  |  |
| `updatedDate` | `string` |  |  |
| `version` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Network Template

*Query Wi-Fi network template configuration settings on venue templates for standardized network deployment and management across locations.*


*10 endpoints*


### `POST` `/templates/venues/wifiNetworks/query`

**Query Wi-Fi Network Template Settings On Venue Templates**

Query Wi-Fi network template configuration settings on venue templates for standardized network deployment management.

operationId: `queryWifiNetworkTemplateSettingsOnVenueTemplates`


**Request Body:** `Wi-Fi_Services_VenueWifiNetworkSettingsQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkIds` | `array` |  |  |
| `venueIds` | `array` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueWifiNetworkSettingsQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}`

**Deactivate Wi-Fi Network Template On Venue Template**

Remove the association between a Wi-Fi network template and a venue template.

operationId: `deactivateWifiNetworkTemplateOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template from which the Wi-Fi network template will be deactivated. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template to be disassociated from the venue template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}`

**Activate Wi-Fi Network Template On Venue Template**

Associate a Wi-Fi network template with a venue template to enforce network configurations.

operationId: `activateWifiNetworkTemplateOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template where the Wi-Fi network template will be activated. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template to be associated with the venue template. |


**Request Body:** `Wi-Fi_Services_VenueWifiNetwork`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `isAllApGroups` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}/settings`

**Get Venue Wi-Fi Network Template Settings**

Retrieve Wi-Fi network template settings for a venue template including AP group configurations, VLAN settings, and scheduling rules.

operationId: `getVenueWifiNetworkTemplateSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template for which to retrieve Wi-Fi network template settings. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template for which to retrieve settings. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueWifiNetworkSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}/settings`

**Update Venue Wi-Fi Network Template Settings**

Update Wi-Fi network template settings for a venue template including AP group configurations, VLAN settings, and scheduling rules.

operationId: `updateVenueWifiNetworkTemplateSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template for which to update Wi-Fi network template settings. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template whose settings will be updated. |


**Request Body:** `Wi-Fi_Services_VenueWifiNetworkSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allApGroupsRadioTypes` | `array` |  |  |
| `allApGroupsVlanId` | `integer` |  |  |
| `isAllApGroups` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `scheduler` | `Wi-Fi_Services_NetworkVenueScheduler` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/wifiNetworks`

**Create Wi-Fi Network Template**

Create a new Wi-Fi network template with WLAN settings, security policies, and advanced customization options for managing network configurations.

operationId: `createWifiNetworkTemplate`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/wifiNetworks/{wifiNetworkTemplateId}`

**Delete Wi-Fi Network Template**

Remove a Wi-Fi network template and its associated configurations by its unique identifier, permanently deleting all related settings.

operationId: `deleteWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/wifiNetworks/{wifiNetworkTemplateId}`

**Get Wi-Fi Network Template**

Retrieve detailed information about a specific Wi-Fi network template including configuration settings, WLAN settings, security policies, and customization options.

operationId: `getWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiNetwork`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}`

**Update Wi-Fi Network Template**

Update an existing Wi-Fi network template configuration including WLAN settings, security policies, and advanced customization options.

operationId: `updateWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template to be updated. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/wifiNetworks/{wifiNetworkTemplateId}/cloneSettings`

**Clone Wi-Fi Network Template**

Create a copy of an existing Wi-Fi network template including all configuration settings, WLAN settings, and security policies.

operationId: `cloneWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template to be cloned. |


**Request Body:** `Wi-Fi_Services_CloneSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Portal Service Profile

*Portal service profile.*


*1 endpoint*


### `PUT` `/wifiNetworks/{wifiNetworkId}/portalServiceProfiles/{portalServiceProfileId}`

**Activate Portal Service Profile On Wi-Fi Network**

Associate a portal service profile with a Wi-Fi network to enable captive portal functionality.

operationId: `activatePortalServiceProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the portal service profile will be activated. |
| `portalServiceProfileId` | path | ✓ | `string` | The unique identifier of the portal service profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## SAML Identity Provider Profile

*Manage SAML identity provider profiles.*


*1 endpoint*


### `PUT` `/wifiNetworks/{wifiNetworkId}/samlIdpProfiles/{samlIdpProfileId}`

**Activate SAML Identity Provider Profile On Wi-Fi Network**

Associate a SAML identity provider profile with a Wi-Fi network to enable SAML based authentication.

operationId: `activateSamlIdpProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the SAML identity provider profile will be activated. |
| `samlIdpProfileId` | path | ✓ | `string` | The unique identifier of the SAML identity provider profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Layer 3 ACL Policy

*Manage layer 3 ACL policy profiles.*


*10 endpoints*


### `DELETE` `/accessControlProfiles/{accessControlProfileId}/l3AclPolicies/{l3AclPolicyId}`

**Deactivate Layer 3 ACL Policy On Access Control Profile**

Remove the association between a layer 3 ACL policy and an access control profile without deleting the policy.

operationId: `deactivateL3AclPolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile from which the layer 3 ACL policy will be deactivated. |
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be disassociated from the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/accessControlProfiles/{accessControlProfileId}/l3AclPolicies/{l3AclPolicyId}`

**Activate Layer 3 ACL Policy On Access Control Profile**

Associate a layer 3 ACL policy with an access control profile to enforce IP based access control.

operationId: `activateL3AclPolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile where the layer 3 ACL policy will be activated. |
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be associated with the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/l3AclPolicies`

**Delete Layer 3 ACL Policies.**

Perform a batch deletion of multiple layer 3 ACL policies by providing a list of their unique identifiers. This operation permanently removes all specified policies and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /l3AclPolicies/{l3AclPolicyId} can be used for this content.

operationId: `deleteBulkL3AclPolicies`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/l3AclPolicies`

**Get Layer 3 ACL Policies.**

Retrieve a complete list of all layer 3 ACL policies in the system including name, description, rules, and default access actions. This method will be removed no sooner than 06/30/2026. The following URL /l3AclPolicies/query can be used for this content.

operationId: `getAllL3AclPolicies`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/l3AclPolicies`

**Add Layer 3 ACL**

Create a layer 3 ACL policy to control network access based on IP addresses, ports, and protocols for access control profiles or Wi-Fi networks. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `addL3AclPolicy`


**Request Body:** `Wi-Fi_Services_L3AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `l3Rules` | `array` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_L3AclPolicyOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/l3AclPolicies/{l3AclPolicyId}`

**Delete Layer 3 ACL**

Delete a layer 3 ACL policy by its unique identifier, permanently deleting the policy and its configurations.

operationId: `deleteL3AclPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/l3AclPolicies/{l3AclPolicyId}`

**Get Layer 3 ACL**

Retrieve detailed information about a specific layer 3 ACL policy by its unique identifier. The response includes all configured rules, default access actions, and other policy settings.

operationId: `getL3AclPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_L3AclPolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/l3AclPolicies/{l3AclPolicyId}`

**Update Layer 3 ACL**

Update an existing layer 3 ACL policy by its unique identifier, updating rules, default access actions, and other policy settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateL3AclPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be modified. |


**Request Body:** `Wi-Fi_Services_L3AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `l3Rules` | `array` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/l3AclPolicies/{l3AclPolicyId}`

**Deactivate Layer 3 ACL Policy On Wi-Fi Network**

Remove the association between a layer 3 ACL policy and a Wi-Fi network without deleting the policy.

operationId: `deactivateL3AclPolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the layer 3 ACL policy will be deactivated. |
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/l3AclPolicies/{l3AclPolicyId}`

**Activate Layer 3 ACL Policy On Wi-Fi Network**

Associate a layer 3 ACL policy with a Wi-Fi network to enforce IP based access control on the network.

operationId: `activateL3AclPolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the layer 3 ACL policy will be activated. |
| `l3AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Access Control Profile Template

*Manage access control profile templates that define reusable network access policies for Wi-Fi networks and clients.*


*6 endpoints*


### `POST` `/templates/accessControlProfiles`

**Add Access Control Profile Template**

Create an access control profile MSP template with rules and policies for Wi-Fi network MSP templates.

operationId: `addAccessControlProfileTemplate`


**Request Body:** `Wi-Fi_Services_AccessControlProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rateLimiting` | `Wi-Fi_Services_RateLimiting` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/accessControlProfiles/{accessControlProfileTemplateId}`

**Delete Access Control Profile Template**

Delete an access control profile MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteAccessControlProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/accessControlProfiles/{accessControlProfileTemplateId}`

**Get Access Control Profile Template**

Retrieve detailed information about a specific access control profile MSP template by its unique identifier. The response includes all configuration settings, rules, and policies associated with the template.

operationId: `getAccessControlProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_AccessControlProfileV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/accessControlProfiles/{accessControlProfileTemplateId}`

**Update Access Control Profile Template**

Update an existing access control profile MSP template by its unique identifier, updating rules, policies, and settings while preserving associations with Wi-Fi network MSP templates.

operationId: `updateAccessControlProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_AccessControlProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rateLimiting` | `Wi-Fi_Services_RateLimiting` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/wifiNetworks/{wifiNetworkTemplateId}/accessControlProfiles/{accessControlProfileTemplateId}`

**Deactivate Access Control Profile Template On Wi-Fi Network Template**

Remove the association between an access control profile MSP template and a Wi-Fi network MSP template.

operationId: `deactivateAccessControlProfileTemplateOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template from which the access control profile MSP template will be deactivated. |
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template to be disassociated from the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/accessControlProfiles/{accessControlProfileTemplateId}`

**Activate Access Control Profile Template On Wi-Fi Network Template**

Associate an access control profile MSP template with a Wi-Fi network MSP template to enforce access policies.

operationId: `activateAccessControlProfileTemplateOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template where the access control profile MSP template will be activated. |
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template to be associated with the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## DPSK Service

*Manage DPSK (Dynamic Pre-Shared Key) services including creation, updates, and associations with Wi-Fi networks for per-user authentication.*


*1 endpoint*


### `PUT` `/wifiNetworks/{wifiNetworkId}/dpskServices/{dpskServiceId}`

**Activate DPSK Service On Wi-Fi Network**

Associate a DPSK service with a Wi-Fi network to enable per user or per device authentication.

operationId: `activateDpskServiceOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the DPSK service will be activated. |
| `dpskServiceId` | path | ✓ | `string` | The unique identifier of the DPSK service to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP Group Template

*Manage AP Group templates.*


*9 endpoints*


### `POST` `/templates/venues/{venueId}/apGroups`

**Create AP Group Template**

Create an AP group MSP template to organize and manage APs within a venue template with specific settings.

operationId: `addVenueApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template where the AP group template will be created. |


**Request Body:** `Wi-Fi_Services_VenueApGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSerialNumbers` | `array` |  | List of AP serial numbers which are associated with the AP group. |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  | Indicates whether this is the default AP group for the associated venue. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  | The name of the AP group. Is required during creation and modification but not for the default AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueId}/apGroups/{apGroupId}`

**Delete AP Group Template**

Delete an AP group MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteVenueApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the AP group template. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apGroups/{apGroupId}`

**Get AP Group Template**

Retrieve detailed information about a specific AP group MSP template by its unique identifier. The response includes all configuration settings, associated AP serial numbers, and policies associated with the template.

operationId: `getVenueApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the AP group template. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroup`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apGroups/{apGroupId}`

**Update AP Group Template**

Update an existing AP group MSP template by its unique identifier, updating AP associations, settings, and policies.

operationId: `updateVenueApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the AP group template. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSerialNumbers` | `array` |  | List of AP serial numbers which are associated with the AP group. |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  | Indicates whether this is the default AP group for the associated venue. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  | The name of the AP group. Is required during creation and modification but not for the default AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/venues/{venueId}/apGroups/{apGroupId}/cloneSettings`

**Clone AP Group Template**

Create a copy of an existing AP group MSP template with a new name, duplicating all configuration settings.

operationId: `cloneVenueApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the AP group template to be cloned. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template to be cloned. |


**Request Body:** `Wi-Fi_Services_CloneSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}`

**Deactivate AP Group Template On Wi-Fi Network Template**

Remove the association between an AP group MSP template and a Wi-Fi network template without deleting the template.

operationId: `deactivateApGroupTemplateOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the Wi-Fi network template. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template where the AP group template will be disassociated. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template to be disassociated from the Wi-Fi network template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}`

**Activate AP Group Template On Wi-Fi Network Template**

Associate an AP group MSP template with a Wi-Fi network template to enforce AP group configurations.

operationId: `activateApGroupTemplateOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the Wi-Fi network template. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template where the AP group template will be activated. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template to be associated with the Wi-Fi network template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}/settings`

**Get AP Group Settings Template On Wi-Fi Network Template**

Retrieve the AP group template settings for a Wi-Fi network template including VLAN and radio type configurations.

operationId: `getApGroupTemplateSettingsOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the Wi-Fi network template. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template where the AP group template settings are configured. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template whose settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueWifiNetworkApGroupSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}/settings`

**Update AP Group Settings Template On Wi-Fi Network Template**

Update the AP group template settings for a Wi-Fi network template including VLAN and radio type configurations.

operationId: `updateApGroupTemplateSettingsOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue template containing the Wi-Fi network template. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template where the AP group template settings will be updated. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group template whose settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueWifiNetworkApGroupSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `radioTypes` | `array` |  |  |
| `vlanId` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Portal Service Profile Template

*Portal service profile template.*


*1 endpoint*


### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/portalServiceProfiles/{portalServiceProfileTemplateId}`

**Activate Portal Service Profile Template On Wi-Fi Network Template**

Associate a portal service profile MSP template with a Wi-Fi network MSP template to enable captive portal functionality.

operationId: `activatePortalServiceProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template where the portal service profile MSP template will be activated. |
| `portalServiceProfileTemplateId` | path | ✓ | `string` | The unique identifier of the portal service profile MSP template to be associated with the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## RADIUS Profile

*Manage RADIUS server profiles.*


*12 endpoints*


### `DELETE` `/hotspot20IdentityProviders/{hotspot20IdentityProviderId}/radiusServerProfiles/{radiusId}`

**Deactivate RADIUS Server Profile On Hotspot 2.0 Identity Provider**

Remove the association between a RADIUS server profile and a Hotspot 2.0 identity provider.

operationId: `deactivateRadiusServerProfileOnHotspot20IdentityProvider`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider from which the RADIUS server profile will be deactivated. |
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be disassociated from the Hotspot 2.0 identity provider. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/hotspot20IdentityProviders/{hotspot20IdentityProviderId}/radiusServerProfiles/{radiusId}`

**Activate RADIUS Server Profile On Hotspot 2.0 Identity Provider**

Associate a RADIUS server profile with a Hotspot 2.0 identity provider to enable RADIUS authentication and accounting.

operationId: `activateRadiusServerProfileOnHotspot20IdentityProvider`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20IdentityProviderId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 identity provider where the RADIUS server profile will be activated. |
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be associated with the Hotspot 2.0 identity provider. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/radiusServerProfiles`

**Delete RADIUS Profiles**

Perform a batch deletion of multiple RADIUS server profiles by providing a list of their unique identifiers. This operation permanently removes all specified profiles and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /radiusServerProfiles/{radiusId} can be used for this content.

operationId: `deleteRadiuses`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/radiusServerProfiles`

**List RADIUS Profiles**

Retrieve a complete list of all RADIUS server profiles configured in the system. This method will be removed no sooner than 06/30/2026. The following URL /radiusServerProfiles/query can be used for this content.

operationId: `getRadiuses`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/radiusServerProfiles`

**Add RADIUS Server Profile**

Create a new RADIUS server profile with primary and secondary servers, server types, shared secrets, and auto-fallback settings.

operationId: `addRadius`


**Request Body:** `Wi-Fi_Services_RadiusServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `primary` | `Wi-Fi_Services_RadiusServerV1_1` | ✓ |  |
| `radSecOptions` | `Wi-Fi_Services_RadSecOptions` |  |  |
| `secondary` | `Wi-Fi_Services_RadiusServerV1_1` |  |  |
| `type` | `['string', 'null']` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/radiusServerProfiles/{radiusId}`

**Delete RADIUS Profile**

Remove a RADIUS server profile by its unique identifier, permanently deleting all associated configurations.

operationId: `deleteRadius`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/radiusServerProfiles/{radiusId}`

**Get RADIUS Profile**

Retrieve detailed information about a RADIUS server profile including primary and secondary servers, server types, and shared secrets. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026.

operationId: `getRadius`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Radius`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/radiusServerProfiles/{radiusId}`

**Update RADIUS Server Profile**

Update an existing RADIUS server profile including primary and secondary servers, server types, shared secrets, and auto-fallback settings.

operationId: `updateRadius`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be modified. |


**Request Body:** `Wi-Fi_Services_RadiusServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `primary` | `Wi-Fi_Services_RadiusServerV1_1` | ✓ |  |
| `radSecOptions` | `Wi-Fi_Services_RadSecOptions` |  |  |
| `secondary` | `Wi-Fi_Services_RadiusServerV1_1` |  |  |
| `type` | `['string', 'null']` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/{wifiNetworkId}/radiusServerProfileSettings`

**Get RADIUS Server Profile Settings On Wi-Fi Network**

Retrieve RADIUS server profile settings configured for a specific Wi-Fi network. The response includes authentication proxy settings, accounting proxy settings, and MAC authentication MAC format configurations.

operationId: `getWifiNetworkRadiusServerProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network for which RADIUS server profile settings will be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiNetworkRadiusServerProfileSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/radiusServerProfileSettings`

**Update RADIUS Server Profile Settings On Wi-Fi Network**

Update RADIUS server profile settings including authentication proxy settings, accounting proxy settings, and MAC authentication format configurations.

operationId: `updateWifiNetworkRadiusServerProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network for which RADIUS server profile settings will be updated. |


**Request Body:** `Wi-Fi_Services_WifiNetworkRadiusServerProfileSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enableAccountingProxy` | `boolean` |  |  |
| `enableAuthProxy` | `boolean` |  |  |
| `macAuthMacFormat` | `['string', 'null']` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/radiusServerProfiles/{radiusId}`

**Deactivate RADIUS Server Profile On Wi-Fi Network**

Remove the association between a RADIUS server profile and a Wi-Fi network.

operationId: `deactivateRadiusServerProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the RADIUS server profile will be deactivated. |
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/radiusServerProfiles/{radiusId}`

**Activate RADIUS Server Profile On Wi-Fi Network**

Associate a RADIUS server profile with a Wi-Fi network to enable RADIUS authentication and accounting.

operationId: `activateRadiusServerProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the RADIUS server profile will be activated. |
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Device Policy Template

*Manage device policy templates.*


*6 endpoints*


### `DELETE` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/devicePolicies/{devicePolicyTemplateId}`

**Deactivate Device Policy Template On Access Control Profile Template**

Remove the association between a device policy MSP template and an access control profile MSP template.

operationId: `deactivateDevicePolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template from which the device policy MSP template will be deactivated. |
| `devicePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the device policy MSP template to be disassociated from the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/devicePolicies/{devicePolicyTemplateId}`

**Activate Device Policy Template On Access Control Profile Template**

Associate a device policy MSP template with an access control profile MSP template to enforce device access control.

operationId: `activateDevicePolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template where the device policy MSP template will be activated. |
| `devicePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the device policy MSP template to be associated with the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/devicePolicies`

**Create Device Policy Template**

Create a new device policy template.

operationId: `addDevicePolicyTemplate`


**Request Body:** `Wi-Fi_Services_DevicePolicyV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/devicePolicies/{devicePolicyTemplateId}`

**Delete Device Policy Template**

Delete a device policy MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteDevicePolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `devicePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the device policy MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/devicePolicies/{devicePolicyTemplateId}`

**Get Device Policy Template**

Retrieve detailed information about a specific device policy MSP template by its unique identifier. The response includes all configuration settings, rules, and policies associated with the template.

operationId: `getDevicePolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `devicePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the device policy MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_DevicePolicyV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/devicePolicies/{devicePolicyTemplateId}`

**Update Device Policy Template**

Update an existing device policy MSP template by its unique identifier, updating rules, policies, and settings.

operationId: `updateDevicePolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `devicePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the device policy MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_DevicePolicyV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Application Policy Template

*Manage application policy template profile template.*


*6 endpoints*


### `DELETE` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/applicationPolicies/{applicationPolicyTemplateId}`

**Deactivate Application Policy Template On Access Control Profile Template**

Remove the association between an application policy MSP template and an access control profile MSP template.

operationId: `deactivateApplicationPolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template from which the application policy MSP template will be deactivated. |
| `applicationPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the application policy MSP template to be disassociated from the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/applicationPolicies/{applicationPolicyTemplateId}`

**Activate Application Policy Template On Access Control Profile Template**

Associate an application policy MSP template with an access control profile MSP template to enforce traffic control policies.

operationId: `activateApplicationPolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template where the application policy MSP template will be activated. |
| `applicationPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the application policy MSP template to be associated with the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/applicationPolicies`

**Add Application Policy Template**

Create an application policy MSP template with traffic control and QoS rules for access control profile templates.

operationId: `addApplicationPolicyTemplate`


**Request Body:** `Wi-Fi_Services_ApplicationPolicyV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/applicationPolicies/{applicationPolicyTemplateId}`

**Delete Application Policy Template**

Delete an application policy MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteApplicationPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the application policy MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/applicationPolicies/{applicationPolicyTemplateId}`

**Get Application Policy Template**

Retrieve detailed information about a specific application policy MSP template by its unique identifier. The response includes all configuration settings, rules, and policies associated with the template.

operationId: `getApplicationPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the application policy MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApplicationPolicyV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/applicationPolicies/{applicationPolicyTemplateId}`

**Update Application Policy Template**

Update an existing application policy MSP template by its unique identifier, updating rules, policies, and settings.

operationId: `updateApplicationPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the application policy MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_ApplicationPolicyV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Location Based Service Server Profile

*Manage location based service server profiles.*


*6 endpoints*


### `POST` `/lbsServerProfiles`

**Create Location Based Service Server Profile**

Create a location based service server profile to manage location based services with server address, port, and authentication settings.

operationId: `createLbsServerProfile`


**Request Body:** `Wi-Fi_Services_LbsServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `lbsServerVenueName` | `string` | ✓ |  |
| `name` | `string` | ✓ |  |
| `password` | `string` | ✓ |  |
| `serverAddress` | `string` | ✓ |  |
| `serverPort` | `integer` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/lbsServerProfiles/{lbsServerProfileId}`

**Delete Location Based Service Server Profile**

Delete a location based service server profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteLbsServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `lbsServerProfileId` | path | ✓ | `string` | The unique identifier of the location based service server profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/lbsServerProfiles/{lbsServerProfileId}`

**Get Location Based Service Server Profile**

Retrieve detailed information about a specific location based service server profile by its unique identifier. The response includes all configuration settings, rules, and policies associated with the profile.

operationId: `getLbsServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `lbsServerProfileId` | path | ✓ | `string` | The unique identifier of the location based service server profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_LbsServerProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/lbsServerProfiles/{lbsServerProfileId}`

**Update Location Based Service Server Profile**

Update an existing location based service server profile by its unique identifier, updating server address, port, and authentication settings.

operationId: `updateLbsServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `lbsServerProfileId` | path | ✓ | `string` | The unique identifier of the location based service server profile to be updated. |


**Request Body:** `Wi-Fi_Services_LbsServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `lbsServerVenueName` | `string` | ✓ |  |
| `name` | `string` | ✓ |  |
| `password` | `string` | ✓ |  |
| `serverAddress` | `string` | ✓ |  |
| `serverPort` | `integer` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/lbsServerProfiles/{lbsServerProfileId}`

**Deactivate Location Based Service Server Profile On Venue**

Remove the association between a location based service server profile and a venue without deleting the profile.

operationId: `deactivateLbsServerProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the location based service server profile will be deactivated. |
| `lbsServerProfileId` | path | ✓ | `string` | The unique identifier of the location based service server profile to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/lbsServerProfiles/{lbsServerProfileId}`

**Activate Location Based Service Server Profile On Venue**

Associate a location based service server profile with a venue to enable location based services and location tracking.

operationId: `activateLbsServerProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the location based service server profile will be activated. |
| `lbsServerProfileId` | path | ✓ | `string` | The unique identifier of the location based service server profile to be associated with the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Layer 2 ACL Policy Template

*Manage layer 2 ACL policy profile templates.*


*6 endpoints*


### `DELETE` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/l2AclPolicies/{l2AclPolicyTemplateId}`

**Deactivate On Access Control Profile Template**

Remove the association between a layer 2 ACL policy MSP template and an access control profile MSP template without deleting the template.

operationId: `deactivateL2AclPolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template from which the layer 2 ACL policy MSP template will be deactivated. |
| `l2AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy MSP template to be disassociated from the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/l2AclPolicies/{l2AclPolicyTemplateId}`

**Activate On Access Control Profile Template**

Associate a layer 2 ACL policy MSP template with an access control profile MSP template to enforce MAC based access control.

operationId: `activateL2AclPolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template where the layer 2 ACL policy MSP template will be activated. |
| `l2AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy MSP template to be associated with the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/l2AclPolicies`

**Add Layer 2 ACL Policy Template**

Create a layer 2 ACL policy MSP template to control network access based on MAC addresses for access control profile MSP templates.

operationId: `addL2AclPolicyTemplate`


**Request Body:** `Wi-Fi_Services_L2AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `access` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `macAddresses` | `array` | ✓ |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/l2AclPolicies/{l2AclPolicyTemplateId}`

**Delete Layer 2 ACL Policy Template**

Delete a layer 2 ACL policy MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteL2AclPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l2AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/l2AclPolicies/{l2AclPolicyTemplateId}`

**Get Layer 2 ACL Template**

Retrieve detailed information about a specific layer 2 ACL policy MSP template by its unique identifier. The response includes all configured MAC addresses, access actions, and other template settings.

operationId: `getL2AclPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l2AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_L2AclPolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/l2AclPolicies/{l2AclPolicyTemplateId}`

**Update Layer 2 ACL Policy Template**

Update an existing layer 2 ACL policy MSP template by its unique identifier, updating MAC addresses and access actions.

operationId: `updateL2AclPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l2AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_L2AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `access` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `macAddresses` | `array` | ✓ |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Network Activation

*Manage Wi-Fi network venue activation relationships.*


*7 endpoints*


### `DELETE` `/networkActivations`

**Delete Network Activation**

Perform a batch deletion of multiple network venue activations by providing a list of activation identifiers. This operation permanently removes all specified activations and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `deleteNetworkVenuesBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/networkActivations`

**Create Network Activation**

Create a network venue activation to associate a Wi-Fi network with a venue, configuring AP groups, VLAN settings, and scheduling rules. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `createNetworkVenue`


**Request Body:** `Wi-Fi_Services_NetworkVenue`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allApGroupsRadio` | `string` |  |  |
| `allApGroupsRadioTypes` | `array` |  |  |
| `allApGroupsVlanId` | `integer` |  |  |
| `apGroups` | `array` |  |  |
| `clientIsolationAllowlistId` | `string` |  |  |
| `dual5gEnabled` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isAllApGroups` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `networkId` | `string` |  |  |
| `scheduler` | `Wi-Fi_Services_NetworkVenueScheduler` |  |  |
| `tripleBandEnabled` | `boolean` |  |  |
| `venueId` | `string` |  |  |
| `vlanPoolId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_NetworkVenueOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/networkActivations/mappings`

**Create Network Activation Mappings**

Create multiple network venue activations in a single operation to associate Wi-Fi networks with venues with AP groups and VLAN settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `createNetworkVenueMappings`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/networkActivations/query`

**Get Network Activations by Query Filter**

Retrieve a filtered list of network venue activations based on query criteria including configuration settings, AP groups, VLAN settings, and scheduling rules. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026.

operationId: `getNetworkActivationsByQuery`


**Request Body:** `Wi-Fi_Services_NetworkActivationsQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkId` | `string` |  |  |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `venueId` | `string` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_NetworkActivationsQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/networkActivations/{networkVenueId}`

**Delete Network Activation**

Remove a network venue activation by its unique identifier. This operation permanently deletes the activation and its associated configurations. Ensure the activation is not actively in use before deletion. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `deleteNetworkVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkVenueId` | path | ✓ | `string` | The unique identifier of the network venue activation to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/networkActivations/{networkVenueId}`

**Get Network Activation**

Retrieve detailed information about a specific network venue activation by its unique identifier. The response includes all configuration settings, AP groups, VLAN settings, and scheduling rules associated with the activation. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiNetworks/{wifiNetworkId}/settings can be used for this content.

operationId: `getNetworkVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkVenueId` | path | ✓ | `string` | The unique identifier of the network venue activation to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_NetworkVenue`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/networkActivations/{networkVenueId}`

**Update Network Activation**

Update an existing network venue activation by its unique identifier, updating AP groups, VLAN settings, and scheduling rules. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiNetworks/{wifiNetworkId}/settings can be used for this content.

operationId: `updateNetworkVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkVenueId` | path | ✓ | `string` | The unique identifier of the network venue activation to be updated. |


**Request Body:** `Wi-Fi_Services_NetworkVenue`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allApGroupsRadio` | `string` |  |  |
| `allApGroupsRadioTypes` | `array` |  |  |
| `allApGroupsVlanId` | `integer` |  |  |
| `apGroups` | `array` |  |  |
| `clientIsolationAllowlistId` | `string` |  |  |
| `dual5gEnabled` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isAllApGroups` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `networkId` | `string` |  |  |
| `scheduler` | `Wi-Fi_Services_NetworkVenueScheduler` |  |  |
| `tripleBandEnabled` | `boolean` |  |  |
| `venueId` | `string` |  |  |
| `vlanPoolId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## VLAN Pool Profile Template

*Manage VLAN pool profile templates.*


*8 endpoints*


### `DELETE` `/templates/venues/{venueTemplateId}/wifiNetworks/{wifiNetworkTemplateId}/apGroups/{apGroupTemplateId}/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Deactivate VLAN Pool Profile Template On AP Group Template**

Remove the association between a VLAN pool profile template and an AP group template.

operationId: `deactivateVlanPoolProfileTemplateOnVenueWifiNetworkApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template containing the Wi-Fi network template and AP group template. |
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template containing the AP group template. |
| `apGroupTemplateId` | path | ✓ | `string` | The unique identifier of the AP group template where the VLAN pool profile template will be deactivated. |
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be disassociated from the AP group template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/wifiNetworks/{wifiNetworkTemplateId}/apGroups/{apGroupTemplateId}/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Activate VLAN Pool Profile Template On AP Group Template**

Associate a VLAN pool profile template with an AP group template to enable VLAN pool assignment.

operationId: `activateVlanPoolProfileTemplateOnVenueWifiNetworkApGroupTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template containing the Wi-Fi network template and AP group template. |
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template containing the AP group template. |
| `apGroupTemplateId` | path | ✓ | `string` | The unique identifier of the AP group template where the VLAN pool profile template will be activated. |
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be associated with the AP group template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/vlanPoolProfiles`

**Add VLAN Pool Profile Template**

Create a new VLAN pool profile template with VLAN members and settings for managing VLAN pool configurations.

operationId: `addVlanPoolProfileTemplate`


**Request Body:** `Wi-Fi_Services_VlanPoolProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `vlanMembers` | `array` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Delete VLAN Pool Profile Template**

Remove a VLAN pool profile template and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteVlanPoolProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Get VLAN Pool Profile Template**

Retrieve detailed information about a specific VLAN pool profile template by its unique identifier. The response includes all configuration settings, VLAN members, and policies associated with the template.

operationId: `getVlanPoolProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VlanPoolProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Update VLAN Pool Profile Template**

Update an existing VLAN pool profile template configuration including VLAN members, description, and settings.

operationId: `updateVlanPoolProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be updated. |


**Request Body:** `Wi-Fi_Services_VlanPoolProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `vlanMembers` | `array` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/wifiNetworks/{wifiNetworkTemplateId}/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Deactivate VLAN Pool Profile Template On Wi-Fi Network Template**

Remove the association between a VLAN pool profile template and a Wi-Fi network template.

operationId: `deactivateVlanPoolProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template where the VLAN pool profile template will be deactivated. |
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be disassociated from the Wi-Fi network template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/vlanPoolProfiles/{vlanPoolProfileTemplateId}`

**Activate VLAN Pool Profile Template On Wi-Fi Network Template**

Associate a VLAN pool profile template with a Wi-Fi network template to enable VLAN pool assignment.

operationId: `activateVlanPoolProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network template where the VLAN pool profile template will be activated. |
| `vlanPoolProfileTemplateId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile template to be associated with the Wi-Fi network template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP SNMP Agent Profile

*Manage AP SNMP policy profiles.*


*7 endpoints*


### `DELETE` `/apSnmpAgentProfiles`

**Delete AP SNMP Agent Profiles**

Perform a batch deletion of multiple AP SNMP agent profiles by providing a list of profile identifiers. This operation permanently removes all specified profiles and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/{snmpAgentProfileId} can be used for this content.

operationId: `deleteApSnmpAgentProfilesBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/apSnmpAgentProfiles`

**Get AP SNMP Agent Profiles**

Retrieve a complete list of all AP SNMP agent profiles configured in the system. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/query can be used for this content.

operationId: `getApSnmpAgentProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/apSnmpAgentProfiles`

**Create AP SNMP Agent Profile**

Create an AP SNMP agent profile with SNMPv2 or SNMPv3 settings that can be applied to APs for SNMP monitoring. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles can be used for this content.

operationId: `createApSnmpAgentProfile`


**Request Body:** `Wi-Fi_Services_ApSnmpAgentProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `policyName` | `string` | ✓ |  |
| `snmpV2Agents` | `array` |  |  |
| `snmpV3Agents` | `array` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_ApSnmpAgentProfileOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/apSnmpAgentProfiles/{apSnmpProfileId}`

**Delete AP SNMP Agent Profile**

Delete an AP SNMP agent profile by its unique identifier, permanently deleting the profile and its configurations. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/{snmpAgentProfileId} can be used for this content.

operationId: `deleteApSnmpAgentProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apSnmpProfileId` | path | ✓ | `string` | The unique identifier of the AP SNMP agent profile to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/apSnmpAgentProfiles/{apSnmpProfileId}`

**Get AP SNMP Profile**

Retrieve detailed information about a specific AP SNMP agent profile by its unique identifier including SNMPv2 and SNMPv3 configurations. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/{snmpAgentProfileId} can be used for this content.

operationId: `getApSnmpAgentProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apSnmpProfileId` | path | ✓ | `string` | The unique identifier of the AP SNMP agent profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApSnmpAgentProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/apSnmpAgentProfiles/{apSnmpProfileId}`

**Update AP SNMP Agent Profile**

Update an existing AP SNMP agent profile by its unique identifier, updating SNMPv2 and SNMPv3 agent settings. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/{snmpAgentProfileId} can be used for this content.

operationId: `updateApSnmpAgentProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apSnmpProfileId` | path | ✓ | `string` | The unique identifier of the AP SNMP agent profile to be modified. |


**Request Body:** `Wi-Fi_Services_ApSnmpAgentProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `policyName` | `string` | ✓ |  |
| `snmpV2Agents` | `array` |  |  |
| `snmpV3Agents` | `array` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/apSnmpAgentProfiles/{apSnmpProfileId}/aps/query`

**Get AP SNMP Agent Profile AP Usage**

Query access points that are associated with a specific AP SNMP agent profile. The response includes a paginated list of APs using the profile, along with their venue information. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/query can be used for this content.

operationId: `getApSnmpAgentProfileApUsage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apSnmpProfileId` | path | ✓ | `string` | The unique identifier of the AP SNMP agent profile to query for associated access points. |


**Request Body:** `Wi-Fi_Services_ApSnmpAgentProfileApQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `searchString` | `string` |  | The search string used to filter access points by name, serial number, or other identifying attributes. |
| `sortField` | `string` |  | The field name used to sort the query results in ascending or descending order. |
| `sortOrder` | `['string', 'null']` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApSnmpAgentProfileApQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Hotspot 2.0 Operator

*Manage Hotspot 2.0 operators including creation, updates, assignments, and network associations.*


*6 endpoints*


### `POST` `/hotspot20Operators`

**Create Hotspot 2.0 Operator**

Create a Hotspot 2.0 operator to define operator information for Wi-Fi Passpoint networks with domain names and friendly names.

operationId: `createHotspot20Operator`


**Request Body:** `Wi-Fi_Services_Hotspot20Operator`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `domainNames` | `array` | ✓ |  |
| `friendlyNames` | `array` |  |  |
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/hotspot20Operators/{hotspot20OperatorId}`

**Delete Hotspot 2.0 Operator**

Delete a Hotspot 2.0 operator by its unique identifier, permanently deleting the operator and its configurations.

operationId: `deleteHotspot20Operator`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20OperatorId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 operator to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/hotspot20Operators/{hotspot20OperatorId}`

**Get Hotspot 2.0 Operator**

Retrieve detailed information about a specific Hotspot 2.0 operator by its unique identifier. The response includes all configured domain names, friendly names in multiple languages, and other operator specific settings.

operationId: `getHotspot20Operator`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20OperatorId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 operator to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Hotspot20Operator`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/hotspot20Operators/{hotspot20OperatorId}`

**Update Hotspot 2.0 Operator**

Update an existing Hotspot 2.0 operator by its unique identifier, updating domain names, friendly names, and other operator settings.

operationId: `updateHotspot20Operator`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `hotspot20OperatorId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 operator to be modified. |


**Request Body:** `Wi-Fi_Services_Hotspot20Operator`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `domainNames` | `array` | ✓ |  |
| `friendlyNames` | `array` |  |  |
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/hotspot20Operators/{hotspot20OperatorId}`

**Deactivate Hotspot 2.0 Operator On Wi-Fi Network**

Remove the association between a Hotspot 2.0 operator and a Wi-Fi network without deleting the operator.

operationId: `deactivateHotspot20OperatorOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the Hotspot 2.0 operator will be deactivated. |
| `hotspot20OperatorId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 operator to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/hotspot20Operators/{hotspot20OperatorId}`

**Activate Hotspot 2.0 Operator On Wi-Fi Network**

Associate a Hotspot 2.0 operator with a Wi-Fi network to identify the network operator for Passpoint clients.

operationId: `activateHotspot20OperatorOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the Hotspot 2.0 operator will be activated. |
| `hotspot20OperatorId` | path | ✓ | `string` | The unique identifier of the Hotspot 2.0 operator to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Radius Service Certificate Authority Assignments

*Manage certificate authorities bindings for entities.*


*2 endpoints*


### `DELETE` `/radiusServerProfiles/{radiusId}/certificateAuthorities/{certificateAuthorityId}`

**Deactivate Certificate Authority On RADIUS Server Profile**

Remove the association between a certificate authority and a RADIUS server profile without deleting the certificate authority.

operationId: `deactivateCertificateAuthorityOnRadiusServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile. |
| `certificateAuthorityId` | path | ✓ | `string` | The unique identifier of the certificate authority. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/radiusServerProfiles/{radiusId}/certificateAuthorities/{certificateAuthorityId}`

**Activate Certificate Authority On RADIUS Server Profile**

Associate a certificate authority with a RADIUS server profile to enable certificate validation for RADIUS authentication.

operationId: `activateCertificateAuthorityOnRadiusServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile. |
| `certificateAuthorityId` | path | ✓ | `string` | The unique identifier of the certificate authority. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP Compatibility

*Query AP feature compatibility report, including incompatible feature of AP model and firmware version.*


*4 endpoints*


### `POST` `/venues/apCompatibilities/query`

**Venue Compatibility Query**

Query AP compatibility information for specified venues. The response includes detailed feature requirements, supported AP firmware versions and models, as well as the count of compatible and incompatible APs based on the targeted venues.

operationId: `venueCompatibilitiesQuery`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `preCheck` | query |  | `boolean` |  |


**Request Body:** `Wi-Fi_Services_CompatibilityVenueNetworkRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Wi-Fi_Services_CompatibilityVenueNetworkFilter` |  | Filter criteria for venue and network compatibility queries including features, venues, and network identifiers. |
| `page` | `integer` |  | Page number for paginated results in the venue and network compatibility query response. |
| `pageSize` | `integer` |  | Number of items per page for paginated venue and network compatibility query results. |


**Responses:**

- `200` Request processed successfully and returns the requested compatibility information data. → `Wi-Fi_Services_ApCompatibilitiesV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/aps/apCompatibilities/query`

**AP Compatibility Query**

Query AP compatibility information for specified access points. The response includes detailed feature requirements, supported AP firmware versions and models based on the targeted APs.

operationId: `apCompatibilitiesQuery`


**Request Body:** `Wi-Fi_Services_CompatibilityApRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Wi-Fi_Services_CompatibilityApFilter` |  | Filter criteria for querying AP compatibility information based on features, networks, and specific access points. |
| `page` | `integer` |  | Page number for paginated results in the compatibility query response. |
| `pageSize` | `integer` |  | Number of items per page for paginated compatibility query results. |


**Responses:**

- `200` Request processed successfully and returns the requested compatibility information data. → `Wi-Fi_Services_ApCompatibilitiesV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/wifiFeatureSets/query`

**Wi-Fi Feature Sets Query**

Retrieve a list of available Wi-Fi feature sets that can be used for compatibility checking. The response includes all feature sets configured in the system for querying AP compatibility information.

operationId: `wifiFeatureSetsQuery`


**Request Body:** `Wi-Fi_Services_CompatibilityFeatureSetRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Wi-Fi_Services_CompatibilityFeatureSetFilter` |  | Filter criteria for querying feature set compatibility information by feature names and requirement levels. |
| `page` | `integer` |  | Page number for paginated results in the feature set compatibility query response. |
| `pageSize` | `integer` |  | Number of items per page for paginated feature set compatibility query results. |


**Responses:**

- `200` Request processed successfully and returns the requested compatibility information data. → `Wi-Fi_Services_WifiFeatureSets`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/wifiNetworks/apCompatibilities/query`

**Wi-Fi Network Compatibility Query**

Query AP compatibility information for specified Wi-Fi networks. The response includes detailed feature requirements, supported AP firmware versions and models, as well as the count of compatible and incompatible APs based on the targeted Wi-Fi networks.

operationId: `networkCompatibilitiesQuery`


**Request Body:** `Wi-Fi_Services_CompatibilityVenueNetworkRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `Wi-Fi_Services_CompatibilityVenueNetworkFilter` |  | Filter criteria for venue and network compatibility queries including features, venues, and network identifiers. |
| `page` | `integer` |  | Page number for paginated results in the venue and network compatibility query response. |
| `pageSize` | `integer` |  | Number of items per page for paginated venue and network compatibility query results. |


**Responses:**

- `200` Request processed successfully and returns the requested compatibility information data. → `Wi-Fi_Services_ApCompatibilitiesV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## SNMP Agent Profile

*Manage SNMP agent profiles.*


*10 endpoints*


### `POST` `/snmpAgentProfiles`

**Create SNMP Agent Profile**

Create a new SNMP agent profile with SNMPv2 or SNMPv3 agent settings for monitoring and management. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `createSnmpAgentProfile`


**Request Body:** `Wi-Fi_Services_SnmpAgentProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |
| `snmpV2Agents` | `array` |  |  |
| `snmpV3Agents` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/snmpAgentProfiles/{snmpAgentProfileId}`

**Delete SNMP Agent Profile**

Remove a SNMP agent profile and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteSnmpAgentProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `snmpAgentProfileId` | path | ✓ | `string` | The unique identifier of the SNMP agent profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/snmpAgentProfiles/{snmpAgentProfileId}`

**Get SNMP Agent Profile**

Retrieve detailed information about a specific SNMP agent profile by its unique identifier. The response includes all configuration settings, SNMP version settings, and agent configurations associated with the profile. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `getSnmpAgentProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `snmpAgentProfileId` | path | ✓ | `string` | SNMP Agent Profile ID. |


**Responses:**

- `200` OK → `Wi-Fi_Services_SnmpAgentProfileV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/snmpAgentProfiles/{snmpAgentProfileId}`

**Update SNMP Agent Profile**

Update an existing SNMP agent profile including SNMP version settings and agent configurations. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `updateSnmpAgentProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `snmpAgentProfileId` | path | ✓ | `string` | SNMP Agent Profile ID. |


**Request Body:** `Wi-Fi_Services_SnmpAgentProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |
| `snmpV2Agents` | `array` |  |  |
| `snmpV3Agents` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/snmpAgentProfileSettings`

**Get SNMP Agent Profile Settings On AP**

Retrieve SNMP agent profile settings for an AP including whether it uses venue level or AP specific settings.

operationId: `getVenueApSnmpAgentProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP for which to retrieve SNMP agent profile settings. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApSnmpAgentProfileSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/snmpAgentProfileSettings`

**Update SNMP Agent Profile Settings On AP**

Update SNMP agent profile settings for an AP including whether it uses venue level or AP specific settings.

operationId: `updateVenueApSnmpAgentProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP for which to update SNMP agent profile settings. |


**Request Body:** `Wi-Fi_Services_VenueApSnmpAgentProfileSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/snmpAgentProfiles/{snmpAgentProfileId}`

**Deactivate SNMP Agent Profile On AP**

Remove the association between a SNMP agent profile and an AP.

operationId: `deactivateSnmpAgentProfileOnAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP where the SNMP agent profile will be deactivated. |
| `snmpAgentProfileId` | path | ✓ | `string` | The unique identifier of the SNMP agent profile to be disassociated from the AP. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/snmpAgentProfiles/{snmpAgentProfileId}`

**Activate SNMP Agent Profile On AP**

Associate a SNMP agent profile with an AP to enable SNMP monitoring and management.

operationId: `activateSnmpAgentProfileOnAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP where the SNMP agent profile will be activated. |
| `snmpAgentProfileId` | path | ✓ | `string` | The unique identifier of the SNMP agent profile to be associated with the AP. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/snmpAgentProfiles/{snmpAgentProfileId}`

**Deactivate SNMP Agent Profile On Venue**

Remove the association between a SNMP agent profile and a venue.

operationId: `deactivateSnmpAgentProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the SNMP agent profile will be deactivated. |
| `snmpAgentProfileId` | path | ✓ | `string` | The unique identifier of the SNMP agent profile to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/snmpAgentProfiles/{snmpAgentProfileId}`

**Activate SNMP Agent Profile On Venue**

Associate a SNMP agent profile with a venue to enable SNMP monitoring and management.

operationId: `activateSnmpAgentProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the SNMP agent profile will be activated. |
| `snmpAgentProfileId` | path | ✓ | `string` | The unique identifier of the SNMP agent profile to be associated with the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## RADIUS Server Profile Template

*Manage RADIUS server profile templates.*


*10 endpoints*


### `POST` `/templates/radiusServerProfiles`

**Add RADIUS Server Profile Template**

Create a new RADIUS server profile MSP template with primary and secondary servers, server types, shared secrets, and auto-fallback settings.

operationId: `addRadiusServerProfileTemplateV1`


**Request Body:** `Wi-Fi_Services_RadiusServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `primary` | `Wi-Fi_Services_RadiusServerV1_1` | ✓ |  |
| `radSecOptions` | `Wi-Fi_Services_RadSecOptions` |  |  |
| `secondary` | `Wi-Fi_Services_RadiusServerV1_1` |  |  |
| `type` | `['string', 'null']` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Delete RADIUS Server Profile Template**

Remove a RADIUS server profile MSP template by its unique identifier, permanently deleting all associated configurations.

operationId: `deleteRadiusServerProfileTemplateV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Get RADIUS Server Profile Template**

Retrieve detailed information about a RADIUS server profile MSP template including primary and secondary servers, server types, and auto-fallback settings.

operationId: `getRadiusServerProfileTemplateV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_RadiusServerProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Update RADIUS Server Profile Template**

Update an existing RADIUS server profile MSP template including primary and secondary servers, server types, shared secrets, and auto-fallback settings.

operationId: `updateRadiusServerProfileTemplateV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_RadiusServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `primary` | `Wi-Fi_Services_RadiusServerV1_1` | ✓ |  |
| `radSecOptions` | `Wi-Fi_Services_RadSecOptions` |  |  |
| `secondary` | `Wi-Fi_Services_RadiusServerV1_1` |  |  |
| `type` | `['string', 'null']` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueTemplateId}/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Deactivate RADIUS Server Profile On Venue**

Remove the association between a RADIUS server profile MSP template and a venue MSP template.

operationId: `deactivateRadiusServerProfileTemplateOnVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template from which the RADIUS server profile MSP template will be deactivated. |
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be disassociated from the venue MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Activate RADIUS Server Profile Template On Venue Template**

Associate a RADIUS server profile MSP template with a venue MSP template to enable RADIUS authentication and accounting.

operationId: `activateRadiusServerProfileTemplateOnVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template where the RADIUS server profile MSP template will be activated. |
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be associated with the venue MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/wifiNetworks/{wifiNetworkTemplateId}/radiusServerProfileSettings`

**Get RADIUS Server Profile Template Settings On Wi-Fi Network Template**

Retrieve RADIUS server profile MSP template settings configured for a specific Wi-Fi network MSP template. The response includes authentication proxy settings, accounting proxy settings, and MAC authentication MAC format configurations.

operationId: `getWifiNetworkTemplateRadiusServerProfileTemplateSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template for which RADIUS server profile MSP template settings will be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiNetworkRadiusServerProfileSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/radiusServerProfileSettings`

**Update RADIUS Server Profile Template Settings On Wi-Fi Network Template**

Update RADIUS server profile MSP template settings including authentication proxy settings, accounting proxy settings, and MAC authentication format configurations.

operationId: `updateWifiNetworkTemplateRadiusServerProfileTemplateSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template for which RADIUS server profile MSP template settings will be updated. |


**Request Body:** `Wi-Fi_Services_WifiNetworkRadiusServerProfileSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enableAccountingProxy` | `boolean` |  |  |
| `enableAuthProxy` | `boolean` |  |  |
| `macAuthMacFormat` | `['string', 'null']` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/wifiNetworks/{wifiNetworkTemplateId}/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Deactivate RADIUS Server Profile Template On Wi-Fi Network Template**

Remove the association between a RADIUS server profile MSP template and a Wi-Fi network MSP template.

operationId: `deactivateRadiusServerProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template from which the RADIUS server profile MSP template will be deactivated. |
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be disassociated from the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/radiusServerProfiles/{radiusServerProfileTemplateId}`

**Activate RADIUS Server Profile Template On Wi-Fi Network Template**

Associate a RADIUS server profile MSP template with a Wi-Fi network MSP template to enable RADIUS authentication and accounting.

operationId: `activateRadiusServerProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template where the RADIUS server profile MSP template will be activated. |
| `radiusServerProfileTemplateId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile MSP template to be associated with the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Layer 3 ACL Policy Template

*Manage layer 3 ACL policy profile templates for creation and lifecycle operations.*


*6 endpoints*


### `DELETE` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/l3AclPolicies/{l3AclPolicyTemplateId}`

**Deactivate On Access Control Profile Template**

Remove the association between a layer 3 ACL policy MSP template and an access control profile MSP template without deleting the template.

operationId: `deactivateL3AclPolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template from which the layer 3 ACL policy MSP template will be deactivated. |
| `l3AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy MSP template to be disassociated from the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/accessControlProfiles/{accessControlProfileTemplateId}/l3AclPolicies/{l3AclPolicyTemplateId}`

**Activate On Access Control Profile Template**

Associate a layer 3 ACL policy MSP template with an access control profile MSP template to enforce IP based access control.

operationId: `activateL3AclPolicyTemplateOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileTemplateId` | path | ✓ | `string` | The unique identifier of the access control profile MSP template where the layer 3 ACL policy MSP template will be activated. |
| `l3AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy MSP template to be associated with the access control profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/l3AclPolicies`

**Add Layer 3 ACL Policy Template**

Create a layer 3 ACL policy MSP template to control network access based on IP addresses, ports, and protocols for access control profile MSP templates.

operationId: `addL3AclPolicyTemplate`


**Request Body:** `Wi-Fi_Services_L3AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `l3Rules` | `array` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/l3AclPolicies/{l3AclPolicyTemplateId}`

**Delete Layer 3 ACL Policy Template**

Delete a layer 3 ACL policy MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteL3AclPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l3AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/l3AclPolicies/{l3AclPolicyTemplateId}`

**Get Layer 3 ACL Template**

Retrieve detailed information about a specific layer 3 ACL policy MSP template by its unique identifier. The response includes all configured rules, default access actions, and other template settings.

operationId: `getL3AclPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l3AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_L3AclPolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/l3AclPolicies/{l3AclPolicyTemplateId}`

**Update Layer 3 ACL Policy Template**

Update an existing layer 3 ACL policy MSP template by its unique identifier, updating rules, default access actions, and other template settings.

operationId: `updateL3AclPolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l3AclPolicyTemplateId` | path | ✓ | `string` | The unique identifier of the layer 3 ACL policy MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_L3AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `l3Rules` | `array` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP Group

*Manage AP groups and their configurations including creation, retrieval, update, and deletion.*


*26 endpoints*


### `DELETE` `/venues/apGroups`

**Delete AP Groups**

Perform a batch deletion of multiple AP groups by providing a list of group identifiers. This operation permanently removes all specified groups and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId} can be used for this content.

operationId: `deleteAPGroupsBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/apGroups`

**Get AP Groups**

Retrieve a complete list of all AP groups configured in the system. The response includes general AP group information, configuration settings, and associated AP serial numbers for each group. This method will be removed no sooner than 06/30/2026. The following URL /venues/apGroups/query can be used for this content.

operationId: `getApGroups`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/apGroups/{apGroupId}`

**Delete AP Group**

Delete an AP group by its unique identifier, permanently deleting the group and its configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId} can be used for this content.

operationId: `deleteAPGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/apGroups/{apGroupId}`

**Get AP Group**

Retrieve detailed information about a specific AP group by its unique identifier. The response includes all configuration settings, associated AP serial numbers, and policies associated with the group. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId} can be used for this content.

operationId: `getAPGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApGroupDeep`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/apGroups/{apGroupId}`

**Update AP Group**

Update an existing AP group by its unique identifier, updating AP associations, settings, and policies. APs can be moved between venues using the update AP endpoint. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId} can be used for this content.

operationId: `updateAPGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be modified. |


**Request Body:** `Wi-Fi_Services_ApGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSerialNumbers` | `array` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `venueId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups`

**Get AP Groups by Venue**

Retrieve a list of AP groups for a specific venue including configuration settings and associated AP serial numbers. This method will be removed no sooner than 06/30/2026. The following URL /venues/apGroups/query can be used for this content.

operationId: `getAPGroupsByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP groups are to be retrieved. |
| `defaultOnly` | query |  | `boolean` | Only get the details of default AP Group in this venue. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/apGroups`

**Create AP Group**

Create an AP group to organize and manage APs within a venue with specific settings for Wi-Fi networks.

operationId: `createAPGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP group will be created. |


**Request Body:** `Wi-Fi_Services_VenueApGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSerialNumbers` | `array` |  | List of AP serial numbers which are associated with the AP group. |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  | Indicates whether this is the default AP group for the associated venue. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  | The name of the AP group. Is required during creation and modification but not for the default AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/apGroups/{apGroupId}`

**Delete AP Group**

Delete an AP group by its unique identifier, permanently deleting the group and its configurations.

operationId: `deleteVenueApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP group. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}`

**Get AP Group**

Retrieve detailed information about a specific AP group by its unique identifier. The response includes all configuration settings, associated AP serial numbers, and policies associated with the group.

operationId: `getVenueApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP group. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroup`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}`

**Update AP Group**

Update an existing AP group by its unique identifier, updating AP associations, settings, and policies.

operationId: `updateVenueApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP group. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApGroup`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSerialNumbers` | `array` |  | List of AP serial numbers which are associated with the AP group. |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  | Indicates whether this is the default AP group for the associated venue. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  | The name of the AP group. Is required during creation and modification but not for the default AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/apClientAdmissionControlSettings`

**Get Ap Group Client Admission Control Settings**

Get client admission control settings for this AP group.

operationId: `getVenueApGroupApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroupApClientAdmissionControlSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}/apClientAdmissionControlSettings`

**Update Ap Group Client Admission Control Settings**

Update Ap group client admission control settings of this Ap group.

operationId: `updateVenueApGroupApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Request Body:** `Wi-Fi_Services_VenueApGroupApClientAdmissionControlSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `maxRadioLoad24G` | `integer` |  |  |
| `maxRadioLoad50G` | `integer` |  |  |
| `minClientCount24G` | `integer` |  |  |
| `minClientCount50G` | `integer` |  |  |
| `minClientThroughput24G` | `integer` |  |  |
| `minClientThroughput50G` | `integer` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/apModelAntennaTypeSettings`

**Get AP Group Antenna Type**

Get AP group antenna type settings. The settings are defined per AP model.

operationId: `getVenueApGroupAntennaType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroupApModelAntennaTypeSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}/apModelAntennaTypeSettings`

**Update AP Group Antenna Type**

Update AP group antenna type settings. The settings are defined per AP model.

operationId: `updateVenueApGroupAntennaType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Request Body:** `Wi-Fi_Services_VenueApGroupApModelAntennaTypeSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `antennaTypeSettings` | `array` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/apModelBandModeSettings`

**Get AP Group Band Mode**

Get AP group band mode settings. The settings are defined per AP model.

operationId: `getVenueApGroupBandMode`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroupApModelBandModeSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}/apModelBandModeSettings`

**Update AP Group Band Mode**

Update AP group band mode settings. The settings are defined per AP model.

operationId: `updateVenueApGroupBandMode`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Request Body:** `Wi-Fi_Services_VenueApGroupApModelBandModeSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apModelBandModeSettings` | `array` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/apModelCapabilities`

**Get AP Group AP model Capabilities**

Get AP model capabilities of the AP group.

operationId: `getVenueApGroupApModelCapabilities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroupApModelCapabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/apModelExternalAntennaSettings`

**Get Ap Group Ap Model External Antenna Settings**

Get Ap model external antenna settings for this AP group.

operationId: `getVenueApGroupApModelExternalAntennaSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApGroupApModelExternalAntennaSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}/apModelExternalAntennaSettings`

**Update AP Group AP Model External Antenna Settings**

Update AP group external antenna settings. The settings are defined per AP model.

operationId: `updateVenueApGroupApModelExternalAntennaSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Request Body:** `Wi-Fi_Services_VenueApGroupApModelExternalAntennaSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `externalAntennaSettings` | `array` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/radioSettings`

**Get AP Group Radio**

Get AP group radio details.

operationId: `getApGroupRadioSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApGroupRadioSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}/radioSettings`

**Update AP Group Radio**

Update AP group radio settings.

operationId: `updateApGroupRadioSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Request Body:** `Wi-Fi_Services_ApGroupRadioSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `radioParams24G` | `Wi-Fi_Services_ApGroupRadio24GHzSettings` |  |  |
| `radioParams5G` | `Wi-Fi_Services_ApGroupRadio5GHzSettings` |  |  |
| `radioParams6G` | `Wi-Fi_Services_ApGroupRadio6GHzSettings` |  |  |
| `radioParamsDual5G` | `Wi-Fi_Services_ApGroupRadioDual5GHzSettings` |  |  |
| `tripleBandEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apGroups/{apGroupId}/wifiAvailableChannels`

**Get Ap Group Available Channels**

Get AP group available channels.

operationId: `getWifiAvailableChannelsOfApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiAvailableChannelsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}`

**Deactivate AP Group On Wi-Fi Network**

Remove the association between an AP group and a Wi-Fi network without deleting the group.

operationId: `deactivateApGroupOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the AP group will be disassociated. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}`

**Activate AP Group On Wi-Fi Network**

Associate an AP group with a Wi-Fi network within a venue to apply the group settings to the network.

operationId: `activateApGroupOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the AP group will be activated. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}/settings`

**Get AP Group Settings On Wi-Fi Network**

Retrieve the AP group settings configured for a Wi-Fi network including VLAN and radio type assignments.

operationId: `getApGroupSettingsOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the AP group settings are configured. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group whose settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueWifiNetworkApGroupSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}/settings`

**Update AP Group Settings On Wi-Fi Network**

Update the AP group settings for a Wi-Fi network including VLAN assignments and radio type selections.

operationId: `updateApGroupSettingsOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the AP group settings will be updated. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group whose settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueWifiNetworkApGroupSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `radioTypes` | `array` |  |  |
| `vlanId` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Access Control Profile

*Manage access control profiles.*


*8 endpoints*


### `DELETE` `/accessControlProfiles`

**Delete Multiple Access Control Profiles**

Perform a batch deletion of multiple access control profiles by providing a list of profile identifiers. This operation permanently removes all specified profiles and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /accessControlProfiles/{accessControlProfileId} can be used for this content.

operationId: `deleteBulkAccessControlProfiles`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/accessControlProfiles`

**Get All Access Control Profiles**

Retrieve a complete list of all access control profiles configured in the system. This method will be removed no sooner than 06/30/2026. The following URL /accessControlProfiles/query can be used for this content.

operationId: `getAllAccessControlProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/accessControlProfiles`

**Add Access Control Profile**

Create an access control profile to manage network access permissions with rules and policies that can be applied to Wi-Fi networks. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `addAccessControlProfile`


**Request Body:** `Wi-Fi_Services_AccessControlProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `applicationPolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `description` | `string` |  |  |
| `devicePolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `l2AclPolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `l3AclPolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `name` | `string` | ✓ |  |
| `rateLimiting` | `Wi-Fi_Services_RateLimiting` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_AccessControlProfileOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/accessControlProfiles/{accessControlProfileId}`

**Delete Access Control Profile**

Delete an access control profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/accessControlProfiles/{accessControlProfileId}`

**Get Access Control Profile**

Retrieve detailed information about a specific access control profile by its unique identifier. The response includes all configuration settings, rules, and policies associated with the profile. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_AccessControlProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/accessControlProfiles/{accessControlProfileId}`

**Update Access Control Profile**

Update an existing access control profile by its unique identifier, updating rules, policies, and settings while maintaining network associations. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile to be modified. |


**Request Body:** `Wi-Fi_Services_AccessControlProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `applicationPolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `description` | `string` |  |  |
| `devicePolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `l2AclPolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `l3AclPolicy` | `Wi-Fi_Services_IdAndEnabled` |  |  |
| `name` | `string` | ✓ |  |
| `rateLimiting` | `Wi-Fi_Services_RateLimiting` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/accessControlProfiles/{accessControlProfileId}`

**Deactivate Access Control Profile On Wi-Fi Network**

Remove the association between an access control profile and a Wi-Fi network without deleting the profile.

operationId: `deactivateAccessControlProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the access control profile will be disassociated. |
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/accessControlProfiles/{accessControlProfileId}`

**Activate Access Control Profile On Wi-Fi Network**

Associate an access control profile with a Wi-Fi network to enforce access policies and control client access.

operationId: `activateAccessControlProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the access control profile will be activated. |
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Ethernet Port Profile

*Manage ethernet port profiles for configuring LAN ports on APs.*


*18 endpoints*


### `POST` `/ethernetPortProfiles`

**Create Ethernet Port Profile**

Create an ethernet port profile to configure LAN port settings for access points with port types, authentication methods, and VLAN settings.

operationId: `createEthernetPortProfile`


**Request Body:** `Wi-Fi_Services_EthernetPortProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authType` | `string` |  |  |
| `bypassMacAddressAuthentication` | `boolean` |  |  |
| `dynamicVlanEnabled` | `boolean` |  |  |
| `enableAccountingProxy` | `boolean` |  |  |
| `enableAuthProxy` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `supplicantAuthenticationOptions` | `Wi-Fi_Services_SupplicantAuthenticationOptions` |  |  |
| `type` | `['string', 'null']` | ✓ |  |
| `unauthenticatedGuestVlan` | `integer` |  |  |
| `untagId` | `integer` |  |  |
| `vlanMembers` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/ethernetPortProfiles/{ethernetPortProfileId}`

**Delete Ethernet Port Profile**

Delete an ethernet port profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteEthernetPortProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/ethernetPortProfiles/{ethernetPortProfileId}`

**Get Ethernet Port Profile**

Retrieve detailed information about a specific ethernet port profile by its unique identifier. The response includes all configuration settings, authentication types, VLAN settings, and RADIUS server associations.

operationId: `getEthernetPortProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_EthernetPortProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/ethernetPortProfiles/{ethernetPortProfileId}`

**Update Ethernet Port Profile**

Update an existing ethernet port profile by its unique identifier, updating port types, authentication methods, VLAN settings, and other configurations.

operationId: `updateEthernetPortProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be modified. |


**Request Body:** `Wi-Fi_Services_EthernetPortProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authType` | `string` |  |  |
| `bypassMacAddressAuthentication` | `boolean` |  |  |
| `dynamicVlanEnabled` | `boolean` |  |  |
| `enableAccountingProxy` | `boolean` |  |  |
| `enableAuthProxy` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `supplicantAuthenticationOptions` | `Wi-Fi_Services_SupplicantAuthenticationOptions` |  |  |
| `type` | `['string', 'null']` | ✓ |  |
| `unauthenticatedGuestVlan` | `integer` |  |  |
| `untagId` | `integer` |  |  |
| `vlanMembers` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/ethernetPortProfiles/{ethernetPortProfileId}/radiusServerProfiles/{radiusServerProfileId}`

**Deactivate RADIUS Server Profile On Ethernet Port Profile**

Remove the association between a RADIUS server profile and an ethernet port profile without deleting either profile.

operationId: `deactivateRadiusToEthernetPortProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile from which the RADIUS server profile will be deactivated. |
| `radiusServerProfileId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be disassociated from the ethernet port profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/ethernetPortProfiles/{ethernetPortProfileId}/radiusServerProfiles/{radiusServerProfileId}`

**Activate RADIUS Server Profile On Ethernet Port Profile**

Associate a RADIUS server profile with an ethernet port profile to enable 802.1X authentication for clients connecting through the port.

operationId: `activateRadiusToEthernetPortProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile where the RADIUS server profile will be activated. |
| `radiusServerProfileId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile to be associated with the ethernet port profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModels/{apModel}/lanPortSpecificSettings`

**Get Venue AP Model LAN Port Specific Settings**

Retrieve AP model specific LAN port settings for all APs of a model within a venue including PoE mode and PoE output settings.

operationId: `getVenueApModelLanPortSpecificSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP model LAN port specific settings are to be retrieved. |
| `apModel` | path | ✓ | `string` | The AP model name whose LAN port specific settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelLanPortSpecificSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModels/{apModel}/lanPortSpecificSettings`

**Update Venue AP Model LAN Port Specific Settings**

Update AP model specific LAN port settings for all APs of a model within a venue including PoE mode and PoE output settings.

operationId: `updateVenueApModelLanPortSpecificSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP model LAN port specific settings are to be modified. |
| `apModel` | path | ✓ | `string` | The AP model name whose LAN port specific settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApModelLanPortSpecificSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `poeMode` | `['string', 'null']` |  |  |
| `poeOut` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId}`

**Deactivate Ethernet Port Profile On Venue AP Model LAN Port**

Remove the association between an ethernet port profile and a LAN port on an AP model within a venue without deleting the profile.

operationId: `deactivateEthernetPortProfileToVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue from which the ethernet port profile will be deactivated. |
| `apModel` | path | ✓ | `string` | The AP model name from which the ethernet port profile will be removed from the specified LAN port. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP model from which the ethernet port profile will be deactivated. |
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be disassociated from the AP model LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId}`

**Activate Ethernet Port Profile On Venue AP Model LAN Port**

Associate an ethernet port profile with a LAN port on an AP model within a venue, applying profile configurations to all APs of the model.

operationId: `activateEthernetPortProfileToVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the ethernet port profile will be activated. |
| `apModel` | path | ✓ | `string` | The AP model name for which the ethernet port profile will be applied to the specified LAN port. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP model where the ethernet port profile will be activated. |
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be associated with the AP model LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/settings`

**Get Venue AP Model LAN Port Settings**

Retrieve LAN port settings for a port on an AP model within a venue including port enablement, client isolation, and DHCP option 82.

operationId: `getVenueApModelLanPortOverwriteSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP model LAN port settings are to be retrieved. |
| `apModel` | path | ✓ | `string` | The AP model name whose LAN port settings are to be retrieved. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP model whose settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelLanPortSettingsV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/settings`

**Update Venue AP Model LAN Port Settings**

Update LAN port settings for a port on an AP model within a venue including port enablement, client isolation, and DHCP option 82.

operationId: `updateVenueApModelLanPortOverwriteSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP model LAN port settings are to be modified. |
| `apModel` | path | ✓ | `string` | The AP model name whose LAN port settings are to be modified. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP model whose settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApModelLanPortSettingsV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `clientIsolationEnabled` | `boolean` |  |  |
| `clientIsolationSettings` | `Wi-Fi_Services_LanPortClientIsolationSettings` |  |  |
| `dhcpOption82Enabled` | `boolean` |  |  |
| `dhcpOption82Settings` | `Wi-Fi_Services_DhcpOption82Settings` |  |  |
| `enabled` | `boolean` |  |  |
| `softGreEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/lanPortSpecificSettings`

**Get AP LAN Port Specific Settings**

Retrieve LAN port specific settings for all LAN ports on a specific AP within a venue including PoE mode and PoE output settings.

operationId: `getApLanPortSpecificSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port specific settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLanPortSpecificSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/lanPortSpecificSettings`

**Update AP LAN Port Specific Settings**

Update LAN port specific settings for all LAN ports on a specific AP within a venue including PoE mode and PoE output settings.

operationId: `updateApLanPortSpecificSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port specific settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApLanPortSpecificSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `poeMode` | `['string', 'null']` |  |  |
| `poeOut` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId}`

**Deactivate Ethernet Port Profile On AP LAN Port**

Remove the association between an ethernet port profile and a LAN port on an AP within a venue without deleting the profile.

operationId: `deactivateEthernetPortProfileToApLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port will have the ethernet port profile deactivated. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP from which the ethernet port profile will be deactivated. |
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be disassociated from the AP LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId}`

**Activate Ethernet Port Profile On AP LAN Port**

Associate an ethernet port profile with a LAN port on an AP within a venue, applying authentication, VLAN assignment, and traffic control settings.

operationId: `activateEthernetPortProfileToApLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port will have the ethernet port profile activated. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP where the ethernet port profile will be activated. |
| `ethernetPortProfileId` | path | ✓ | `string` | The unique identifier of the ethernet port profile to be associated with the AP LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/settings`

**Get AP LAN Port Settings**

Retrieve LAN port settings for a port on an AP within a venue including port enablement, client isolation, DHCP option 82, and VLAN overwrite settings.

operationId: `getApLanPortOverwriteSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be retrieved. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP whose settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLanPortSettingsV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/settings`

**Update AP LAN Port Settings**

Update LAN port settings for a port on an AP within a venue including port enablement, client isolation, DHCP option 82, and VLAN overwrite settings.

operationId: `updateApLanPortOverwriteSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be modified. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port on the AP whose settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApLanPortSettingsV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `clientIsolationEnabled` | `boolean` |  |  |
| `clientIsolationSettings` | `Wi-Fi_Services_LanPortClientIsolationSettings` |  |  |
| `dhcpOption82Enabled` | `boolean` |  |  |
| `dhcpOption82Settings` | `Wi-Fi_Services_DhcpOption82Settings` |  |  |
| `enabled` | `boolean` |  |  |
| `overwriteUntagId` | `integer` |  |  |
| `overwriteVlanMembers` | `string` |  |  |
| `softGreEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Recovery

*Retrieve and set the recovery PSK.*


*5 endpoints*


### `GET` `/applicationPolicies/capabilities/applications`

**Get Application Policies Applications**

List supported application signatures for AVC policies. This method will be removed no sooner than 06/30/2026. The following URL /applicationLibraries/{applicationLibraryId}/categories/{categoryId}/applications can be used for this content.

operationId: `getAvcApplications`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/applicationPolicies/capabilities/categories`

**Get Application Policies Categories**

List supported application categories for AVC policies. This method will be removed no sooner than 06/30/2026. The following URL /applicationLibraries/{applicationLibraryId}/categories can be used for this content.

operationId: `getAvcCategories`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/recoveryPskSettings`

**Get Recovery PSK**

Retrieve the pre-shared key (PSK) configured for the recovery network. The recovery network provides a fallback Wi-Fi network for administrative access when the primary network is unavailable. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/recoveryPassphraseSettings can be used for this content.

operationId: `getRecoveryPsk`


**Responses:**

- `200` OK → `Wi-Fi_Services_RecoveryPsk`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/recoveryPskSettings`

**Update Recovery PSK**

Update the PSK for the recovery network used for administrative access. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/recoveryPassphraseSettings can be used for this content.

operationId: `updateRecoveryPsk`


**Request Body:** `Wi-Fi_Services_RecoveryPsk`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `obsolete` | `boolean` |  |  |
| `psk` | `string` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/capabilities`

**Get Capabilities**

List access point capability metadata supported by the system. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/capabilities can be used for this content.

operationId: `getCapabilities`


**Responses:**

- `200` OK → `Wi-Fi_Services_Capabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP

*Manage AP devices including pinging, traceroute, resetting, rebooting, floor plan positioning, and LAN port settings.*


*110 endpoints*


### `GET` `/venues/apGroups/{apGroupId}/aps`

**Get APs by AP Group**

Retrieve a list of access points associated with a specific AP group. The response includes general AP information, configuration settings, and operational status for each access point in the group. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/query can be used for this content.

operationId: `getApsByAPGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group whose access points are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps`

**Delete APs**

Perform a batch deletion of multiple access points by providing a list of serial numbers. This operation permanently removes all specified APs and their associated configurations from the system. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber} can be used for this content.

operationId: `deleteApsBulk`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `resetFirmware` | query |  | `boolean` | Reset AP firmware to Standalone image. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps`

**Get APs**

Retrieve a complete list of all access points configured in the system. The response includes general AP information, configuration settings, and operational status for each access point. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/query can be used for this content.

operationId: `getAps`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `operational` | query |  | `boolean` | Include operational data in response. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/aps`

**Import APs**

Create one or more access points in the system, registering and associating them with venues for management and configuration. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps can be used for this content.

operationId: `addAps`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/aps/csvFile`

**Import Bulk APs from CSV File Across Venues**

Bulk import access points across multiple venues from a CSV file. The file must follow the CSV template from the R1 website and use UTF-8 encoding. This API supports partial success; venues that fail due to insufficient permissions are skipped without halting the overall operation. Returns a request ID that can be used with POST /venues/aps/importRequests/query to retrieve per venue import status and results.

operationId: `importBulkApsCsv`


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/importResults`

**Get Result for Import APs from CSV File**

Retrieve the import operation results and status for access points imported from CSV files including success and error details. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/importResults can be used for this content.

operationId: `getImportApsResults`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `requestId` | query | ✓ | `string` | The request ID of import aps request for querying the result. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ImportDetails`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Validation error [WIFI-10008: "Query parameter of requestId is required"] → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}`

**Delete AP**

Delete an AP by its serial number, permanently deleting the AP and its configurations from the system. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber} can be used for this content.

operationId: `deleteAP`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be deleted. |
| `resetFirmware` | query |  | `boolean` | Reset AP firmware to Standalone image. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}`

**Get AP**

Retrieve detailed operational and configuration data for a specific access point by its serial number. The response includes general AP information, configuration settings, and operational status. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber} can be used for this content.

operationId: `getAP`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be retrieved. |
| `operational` | query |  | `boolean` | Include operational data in response. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApDeep`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/venues/aps/{serialNumber}`

**Trigger AP Action**

Trigger an action on this access point. This operation executes administrative commands such as reboot, reset, ping, or traceroute on the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/systemCommands can be used for this content.

operationId: `TriggerApAction`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which the action is to be triggered. |


**Request Body:** `Wi-Fi_Services_ApPatchRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `['string', 'null']` | ✓ |  |
| `targetHost` | `string` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApPatchResponseOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}`

**Update AP**

Update the configuration of an existing access point by its serial number. This operation allows you to update AP settings, properties, and associations while maintaining the AP identity.

operationId: `updateAP`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be modified. |


**Request Body:** `Wi-Fi_Services_ApRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apGroupId` | `string` |  |  |
| `description` | `string` |  |  |
| `deviceGps` | `Wi-Fi_Services_DeviceGps` |  |  |
| `model` | `['string', 'null']` |  |  |
| `name` | `string` | ✓ |  |
| `position` | `Wi-Fi_Services_ApPosition` |  |  |
| `serialNumber` | `string` | ✓ |  |
| `tags` | `array` |  |  |
| `venueId` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/bssColoringSettings`

**Get AP Basic Service Set Coloring Settings**

Retrieve basic service set coloring settings configured for this access point. The response includes BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/bssColoringSettings can be used for this content.

operationId: `getApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose BSS coloring settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApBssColoring`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/bssColoringSettings`

**Update AP Basic Service Set Coloring Settings**

Update BSS coloring settings for this AP to improve spatial reuse and reduce interference in Wi-Fi 6 networks. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/bssColoringSettings can be used for this content.

operationId: `updateApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose BSS coloring settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApBssColoring`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bssColoringEnabled` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/capabilities`

**Get AP Capabilities**

Retrieve capability information for this access point. The response includes detailed feature support information and hardware capabilities of the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/capabilities can be used for this content.

operationId: `getApCapabilities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The serial number of the AP. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Capabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/channels`

**Get AP Default Regulatory Channels**

Retrieve available Wi-Fi channels for this access point based on regulatory domain and country settings. The response includes all supported channels across different frequency bands. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/wifiAvailableChannels can be used for this content.

operationId: `getValidChannelsBySerialNumber`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose available channels are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRegulatoryChannels`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/clientAdmissionControlSettings`

**Reset AP Client Admission Control Settings**

Reset client admission control settings for this access point to default values. This operation removes AP specific admission control configurations and restores system default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId}/apClientAdmissionControlSettings can be used for this content.

operationId: `resetApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose client admission control settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/clientAdmissionControlSettings`

**Get AP Client Admission Control Settings**

Retrieve client admission control settings configured for this access point. The response includes thresholds and policies that control when new clients are allowed to connect to the AP. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `getApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose client admission control settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApClientAdmissionControl`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/clientAdmissionControlSettings`

**Update AP Client Admission Control Settings**

Update client admission control settings for this access point. This operation allows you to update thresholds and policies that control when new clients are allowed to connect to the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId}/apClientAdmissionControlSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2

operationId: `updateApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose client admission control settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApClientAdmissionControl`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `maxRadioLoad24G` | `integer` |  |  |
| `maxRadioLoad50G` | `integer` |  |  |
| `minClientCount24G` | `integer` |  |  |
| `minClientCount50G` | `integer` |  |  |
| `minClientThroughput24G` | `integer` |  |  |
| `minClientThroughput50G` | `integer` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/dhcpLeases`

**Get DHCP Lease Times**

Retrieve DHCP lease time information for this access point. The response includes active DHCP client leases with IP addresses, MAC addresses, and lease expiration times. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/wifiDhcpClientLeases can be used for this content.

operationId: `getDhcpLeaseTimes`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose DHCP lease time information is to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/dhcpPoolUsages`

**Get DHCP Pool Usages**

Retrieve DHCP pool usage information for this access point. The response includes IP address allocation statistics and pool utilization data for DHCP services. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/wifiDhcpPoolUsages can be used for this content.

operationId: `getDhcpPoolUsages`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose DHCP pool usage information is to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/directedMulticastSettings`

**Reset AP Directed Multicast Settings**

Reset directed multicast settings for this access point to default values. This operation removes AP specific multicast configurations and restores system default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/directedMulticastSettings can be used for this content.

operationId: `resetApDirectedMulticast`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose directed multicast settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/directedMulticastSettings`

**Get AP Directed Multicast Settings**

Retrieve directed multicast settings configured for this access point. The response includes multicast optimization configurations that improve efficiency for multicast traffic delivery to clients. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/directedMulticastSettings can be used for this content.

operationId: `getApDirectedMulticast`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose directed multicast settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApDirectedMulticast`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/directedMulticastSettings`

**Update AP Directed Multicast Settings**

Update directed multicast settings for this access point. This operation allows you to update multicast optimization configurations that improve efficiency for multicast traffic delivery to clients. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/directedMulticastSettings can be used for this content.

operationId: `updateApDirectedMulticast`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose directed multicast settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApDirectedMulticast`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkEnabled` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |
| `wiredEnabled` | `boolean` |  |  |
| `wirelessEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/floorPositions`

**Update AP Position**

Update the floor plan position of this AP by updating the physical location coordinates for visualization and management. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/floorplans/{floorplanId}/aps/{serialNumber}/floorPositions can be used for this content.

operationId: `updateAPPosition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose floor plan position is to be updated. |


**Request Body:** `Wi-Fi_Services_ApPosition`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `floorplanId` | `string` |  |  |
| `xPercent` | `number` |  |  |
| `yPercent` | `number` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/lanPortSettings`

**Reset AP LAN ports**

Reset LAN port settings for this access point to default values. This operation removes AP specific port configurations and restores system default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/settings can be used for this content.

operationId: `resetAPLanPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/lanPortSettings`

**Get AP LAN ports**

Retrieve LAN port settings configured for this access point. The response includes Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/settings can be used for this content.

operationId: `getAPLanPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLanPorts`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/lanPortSettings`

**Update AP LAN ports**

Update LAN port settings for this access point. This operation allows you to update Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/settings can be used for this content.

operationId: `updateAPLanPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApLanPorts`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `lanPorts` | `array` |  |  |
| `poeOut` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/ledSettings`

**Reset AP LED**

Reset LED indicator settings for this access point to default values. This operation removes AP specific LED configurations and restores system default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/ledSettings can be used for this content.

operationId: `resetAPLED`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LED settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/ledSettings`

**Get AP LED**

Retrieve LED indicator settings configured for this access point. The response includes LED behavior and status indicator configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/ledSettings can be used for this content.

operationId: `getAPLed`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LED settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLed`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/ledSettings`

**Update AP LED**

Update LED indicator settings for this access point. This operation allows you to update LED behavior and status indicator configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/ledSettings can be used for this content.

operationId: `updateAPLED`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LED settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApLed`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ledEnabled` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/logs`

**Download AP Log**

Download log files from this access point. The response includes system logs, event logs, and diagnostic information generated by the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/logs can be used for this content.

operationId: `downloadAPLog`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose log files are to be downloaded. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApDownloadLog`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/meshSettings`

**Get AP Mesh Settings**

Retrieve mesh network settings configured for this access point. The response includes mesh enablement status and configuration parameters for AP mesh networking. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/meshSettings can be used for this content.

operationId: `getApMeshOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose mesh settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApMesh`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/meshSettings`

**Update AP Mesh Settings**

Update mesh network settings for this access point. This operation allows you to enable or disable mesh networking and configure mesh parameters for the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/meshSettings can be used for this content.

operationId: `UpdateApMeshOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose mesh settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApMesh`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `meshMode` | `string` |  |  |
| `uplinkMacAddresses` | `array` |  |  |
| `uplinkMode` | `string` |  |  |
| `venueMeshEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/networkSettings`

**Reset AP Network Settings**

Reset network settings for this access point to default values. This operation removes AP specific network configurations and restores system default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/networkSettings can be used for this content.

operationId: `resetApNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose network settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/networkSettings`

**Get AP Network Settings**

Retrieve network settings configured for this access point. The response includes IP configuration, network interface settings, and connectivity parameters. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/networkSettings can be used for this content.

operationId: `getApNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose network settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_NetworkSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/networkSettings`

**Update AP Network Settings**

Update network settings for this access point. This operation allows you to update IP configuration, network interface settings, and connectivity parameters.

operationId: `updateApNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose network settings are to be modified. |


**Request Body:** `Wi-Fi_Services_NetworkSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `gateway` | `string` |  |  |
| `ip` | `string` |  |  |
| `ipType` | `['string', 'null']` |  |  |
| `netmask` | `string` |  |  |
| `primaryDnsServer` | `string` |  |  |
| `secondaryDnsServer` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/packets`

**Stop Packet Capture**

Stop packet capture for this access point. This operation terminates active network packet capture sessions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/packets can be used for this content.

operationId: `stopPacketCapture`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which packet capture is to be stopped. |


**Request Body:** `Wi-Fi_Services_ACXApPacketCaptureStopRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `sessionId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/packets`

**Get Packet Capture State**

Retrieve packet capture state for this access point. The response includes the current status of packet capture sessions including active capture information and session details. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/packets can be used for this content.

operationId: `getPacketCaptureState`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose packet capture state is to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ACXApPacketCaptureStateResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/aps/{serialNumber}/packets`

**Start Packet Capture**

Start packet capture for this access point. This operation initiates network packet capture sessions for network analysis and troubleshooting. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/packets can be used for this content.

operationId: `startPacketCapture`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which packet capture is to be started. |


**Request Body:** `Wi-Fi_Services_ApPacketCaptureStartRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `captureInterface` | `['string', 'null']` | ✓ |  |
| `frameTypeFilter` | `array` |  |  |
| `macAddressFilter` | `string` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_ACXApPacketCaptureStartResponseOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `409` Conflict [WIFI-10477: "Duplicate sessionId exists"] → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/pictures`

**Delete AP Picture**

Delete the existing picture image for the AP removing visual identification information from the system. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/pictures can be used for this content.

operationId: `DeleteApPicture`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for deleting picture information. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/pictures`

**Get AP Picture**

Retrieve the AP picture image file for visual identification and reference in the management interface. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/pictures can be used for this content.

operationId: `getApPicture`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for retrieving picture information. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApPicture`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/pictures`

**Upload AP Picture**

Upload a new picture image for the AP to enable visual identification in the management interface. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/pictures can be used for this content.

operationId: `UploadApPicture`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for uploading picture information. |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/radioSettings`

**Reset AP Radio Customization**

Reset radio settings for this access point to default values. This operation removes AP specific radio customizations and restores system default configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/radioSettings can be used for this content.

operationId: `resetAPRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose radio settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/radioSettings`

**Get AP Radio**

Retrieve radio settings configured for this access point. The response includes channel selection, power levels, and frequency band configurations for the AP radios. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/radioSettings can be used for this content.

operationId: `getAPRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose radio settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApRadioCustomization`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/radioSettings`

**Update AP Radio**

Update radio settings for this access point. This operation allows you to update channel selection, power levels, and frequency band configurations for the AP radios. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/radioSettings can be used for this content.

operationId: `updateAPRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose radio settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApRadioCustomization`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apRadioParams24G` | `Wi-Fi_Services_ApRadioParams24G` |  |  |
| `apRadioParams50G` | `Wi-Fi_Services_ApRadioParams50G` |  |  |
| `apRadioParams6G` | `Wi-Fi_Services_ApRadioParams6G` |  |  |
| `apRadioParamsDual5G` | `Wi-Fi_Services_ApRadioParamsDual5G` |  |  |
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `enable6G` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/snmpAgentSettings`

**Reset AP SNMP Agent Settings**

Reset SNMP agent settings for this access point to default values. This operation removes AP specific SNMP configurations and restores system default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/snmpAgentProfileSettings can be used for this content.

operationId: `resetApSnmpAgent`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose SNMP agent settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/snmpAgentSettings`

**Get AP SNMP Agent Settings**

Retrieve SNMP agent settings configured for this access point. The response includes SNMP configuration parameters used for network management and monitoring. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/snmpAgentProfileSettings can be used for this content.

operationId: `getApSnmpAgent`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose SNMP agent settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApSnmpAgent`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/snmpAgentSettings`

**Update AP SNMP Agent Settings**

Update SNMP agent settings for this access point. This operation allows you to update SNMP configuration parameters used for network management and monitoring. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/snmpAgentProfileSettings can be used for this content.

operationId: `updateApSnmpAgent`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose SNMP agent settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApSnmpAgent`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSnmpAgentProfileId` | `string` |  |  |
| `enableApSnmp` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/aps/{serialNumber}/wifiOverwriteSettings`

**Reset AP Customization**

Reset customization settings for this access point to default values. This operation removes AP specific customizations and restores venue default settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/meshSettings can be used for this content.

operationId: `resetApCustomization`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose customization settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/aps/{serialNumber}/wifiOverwriteSettings`

**Get AP Customization**

Retrieve customization details configured for this access point. The response includes AP model specific settings and configurations that override default venue settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/meshSettings can be used for this content.

operationId: `getApCustomization`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose customization details are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApModelSpecific`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/aps/{serialNumber}/wifiOverwriteSettings`

**Update AP Customization**

Update customization settings for this access point. This operation allows you to update AP model specific settings and configurations that override default venue settings. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/meshSettings can be used for this content.

operationId: `updateApCustomization`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose customization settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApModelSpecific`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bandMode` | `['string', 'null']` |  |  |
| `externalAntenna` | `Wi-Fi_Services_ExternalAntenna` |  |  |
| `id` | `string` |  |  |
| `lanPorts` | `array` |  |  |
| `ledEnabled` | `boolean` |  |  |
| `poeOut` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/apGroups/{apGroupId}/aps`

**Add AP with AP Group**

Create an AP and associate it with a specific AP group, registering the AP in the system and assigning it for centralized management and configuration.

operationId: `addApWithApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP will be added. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to which the AP will be associated. |


**Request Body:** `Wi-Fi_Services_ApCreationV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `deviceGps` | `Wi-Fi_Services_DeviceGps` |  |  |
| `model` | `['string', 'null']` |  |  |
| `name` | `string` | ✓ |  |
| `serialNumber` | `string` | ✓ |  |
| `tags` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apGroups/{apGroupId}/aps/{serialNumber}`

**Move AP Into AP Group**

Associate an access point with a specific AP group. This operation moves the AP into the group, enabling centralized management and configuration through the group settings.

operationId: `activateApOnApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP and AP group are located. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group to which the AP will be moved. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be moved into the AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/aps`

**Add AP or Import APs**

Create an AP or import multiple APs using a CSV file, registering and associating them with the specified venue.

operationId: `addAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point or configuration is deployed. |


**Request Body:** `Wi-Fi_Services_ApCreationV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `deviceGps` | `Wi-Fi_Services_DeviceGps` |  |  |
| `model` | `['string', 'null']` |  |  |
| `name` | `string` | ✓ |  |
| `serialNumber` | `string` | ✓ |  |
| `tags` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OptionalEntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/importResults`

**Get Import Venue APs Results**

Retrieve the import operation results and status for venue access points imported from CSV files with detailed feedback.

operationId: `getImportVenueApsResults`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point or configuration is deployed. |
| `operationRequestId` | query | ✓ | `string` | The unique request identifier for tracking the import venue access points operation status and results. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApsImportResults`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Validation error [WIFI-10008: "Query parameter of requestId is required"] → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{originalSerialNumber}/replacements/{replacingSerialNumber}`

**Replace AP**

Associate a replacement AP with an original device, establishing the relationship so the new AP can inherit configurations and settings from the original AP.

operationId: `replaceAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the APs are located. |
| `originalSerialNumber` | path | ✓ | `string` | The unique serial number of the original access point to be replaced. |
| `replacingSerialNumber` | path | ✓ | `string` | The unique serial number of the replacement access point. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}`

**Delete AP**

Delete an AP by serial number, permanently deleting the AP and its configurations from the system after ensuring it is not actively in use. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber} can be used for this content.

operationId: `deleteAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be deleted. |
| `resetFirmware` | query |  | `boolean` | Reset AP firmware to standalone image for recovery. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}`

**Get AP**

Retrieve detailed information about a specific AP by its serial number, including general AP information, configuration settings, and operational status for management decisions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber} can be used for this content.

operationId: `getAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}`

**Update AP**

Update the configuration of an existing AP by serial number, updating AP settings, properties, and associations while maintaining AP identity.

operationId: `updateAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to be modified. |


**Request Body:** `Wi-Fi_Services_ApV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `deviceGps` | `Wi-Fi_Services_DeviceGps` |  |  |
| `loginPassword` | `string` |  |  |
| `model` | `['string', 'null']` |  |  |
| `name` | `string` | ✓ |  |
| `tags` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/antennaTypeSettings`

**Get AP Antenna Type**

Retrieve antenna type settings configured for this access point. The response includes antenna configuration used for radio transmissions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/antennaTypeSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getAPAntennaType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose antenna type settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApAntennaTypeSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/antennaTypeSettings`

**Update AP Antenna Type**

Update antenna type settings for this access point. This operation allows you to update antenna configuration used for radio transmissions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/antennaTypeSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateAPAntennaType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose antenna type settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApAntennaTypeSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/bandModeSettings`

**Get AP Band Mode**

Retrieve band mode settings configured for this access point. The response includes radio frequency band configurations that control available Wi-Fi bands for the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/bandModeSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getAPBandMode`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose band mode settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApBandModeSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/bandModeSettings`

**Update AP Band Mode**

Update band mode settings for this access point. This operation allows you to update radio frequency band configurations that control available Wi-Fi bands for the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/bandModeSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateAPBandMode`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose band mode settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApBandModeSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bandMode` | `['string', 'null']` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/bssColoringSettings`

**Get AP Basic Service Set Coloring Settings**

Retrieve basic service set coloring settings configured for this access point. The response includes BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/bssColoringSettings can be used for this content.

operationId: `GetApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose BSS coloring settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApBssColoringSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/bssColoringSettings`

**Update AP Basic Service Set Coloring Settings**

Update BSS coloring settings for this AP to improve spatial reuse and reduce interference in Wi-Fi 6 networks. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/bssColoringSettings can be used for this content.

operationId: `UpdateApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose BSS coloring settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApBssColoringSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bssColoringEnabled` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/capabilities`

**Get AP Capabilities**

Retrieve capability information for this access point. The response includes detailed feature support information and hardware capabilities of the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/capabilities can be used for this content.

operationId: `getApCapabilitiesV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose capabilities are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApCapabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/clientAdmissionControlSettings`

**Get AP Client Admission Control Settings**

Retrieve client admission control settings configured for this access point. The response includes thresholds and policies that control when new clients are allowed to connect to the AP. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `GetApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose client admission control settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApClientAdmissionControlSettingsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/clientAdmissionControlSettings`

**Update AP Client Admission Control Settings**

Update client admission control settings for this access point. This operation allows you to update thresholds and policies that control when new clients are allowed to connect to the AP. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apGroups/{apGroupId}/apClientAdmissionControlSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2

operationId: `UpdateApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose client admission control settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApClientAdmissionControlSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `maxRadioLoad24G` | `integer` |  |  |
| `maxRadioLoad50G` | `integer` |  |  |
| `minClientCount24G` | `integer` |  |  |
| `minClientCount50G` | `integer` |  |  |
| `minClientThroughput24G` | `integer` |  |  |
| `minClientThroughput50G` | `integer` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/dhcpSettings`

**Get AP DHCP Settings**

Retrieve DHCP settings configured for this access point. The response includes DHCP server configurations and IP address pool settings for the AP.

operationId: `getApDhcpSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose DHCP settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApDhcpSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/aps/{serialNumber}/diagnosisCommands`

**Trigger AP Diagnosis Commands**

Trigger diagnosis commands for this access point. This operation executes diagnostic tests and collects troubleshooting information to help identify and resolve network issues.

operationId: `TriggerApDiagnosisCommands`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which diagnosis commands are to be triggered. |


**Request Body:** `Wi-Fi_Services_ApDiagnosisCommand`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `targetHost` | `string` |  |  |
| `type` | `['string', 'null']` | ✓ |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApDiagnosisCommandResponseOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/directedMulticastSettings`

**Get AP Directed Multicast Settings**

Retrieve directed multicast settings configured for this access point. The response includes multicast optimization configurations that improve efficiency for multicast traffic delivery to clients.

operationId: `getApDirectedMulticastSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose directed multicast settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApDirectedMulticastSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/directedMulticastSettings`

**Update AP Directed Multicast Settings**

Update directed multicast settings for this access point. This operation allows you to update multicast optimization configurations that improve efficiency for multicast traffic delivery to clients.

operationId: `updateApDirectedMulticastSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose directed multicast settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApDirectedMulticastSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkEnabled` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |
| `wiredEnabled` | `boolean` |  |  |
| `wirelessEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/externalAntennaSettings`

**Get AP External Antenna Settings**

Retrieve external antenna settings configured for this access point. The response includes external antenna configurations for radio transmissions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/externalAntennaSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getApExternalAntennaSettingsV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose external antenna settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApExternalAntennaSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/externalAntennaSettings`

**Update AP External Antenna Settings**

Update external antenna settings for this access point. This operation allows you to update external antenna configurations for radio transmissions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/externalAntennaSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateApExternalAntennaSettingsV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose external antenna settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApExternalAntennaSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `externalAntenna` | `Wi-Fi_Services_ExternalAntenna` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/iotSettings`

**Get AP IoT Settings**

Retrieve IoT settings configured for this access point. The response includes IoT device configurations and connectivity settings.

operationId: `GetApIotSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose IoT settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApIotSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/iotSettings`

**Update AP IoT Settings**

Update IoT settings for this access point. This operation allows you to update IoT device configurations and connectivity settings.

operationId: `UpdateApIotSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose IoT settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApIotSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `useVenueSettings` | `boolean` |  | When enabled, the AP uses IoT settings from the venue configuration, overriding any AP specific IoT settings. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/lanPortSettings`

**Get AP LAN ports**

Retrieve LAN port settings configured for this access point. The response includes Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /ethernetPortProfiles/query can be used for this content.

operationId: `getApLanPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be retrieved. |
| `defaultOnly` | query |  | `boolean` | Only get the details of default LAN port settings of the AP. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLanPortSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/lanPortSettings`

**Update AP LAN ports**

Update LAN port settings for this access point. This operation allows you to update Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId} can be used for this content.

operationId: `updateApLanPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApLanPortSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `lanPorts` | `array` |  |  |
| `poeMode` | `['string', 'null']` |  |  |
| `poeOut` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/ledSettings`

**Get AP LED**

Retrieve LED indicator settings configured for this access point. The response includes LED behavior and status indicator configurations.

operationId: `getApLedSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LED settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLedSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/ledSettings`

**Update AP LED**

Update LED indicator settings for this access point. This operation allows you to update LED behavior and status indicator configurations.

operationId: `updateApLedSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LED settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApLedSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ledEnabled` | `boolean` |  |  |
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/logs`

**Get the AP Log Info**

Retrieve log information for this access point. The response includes system logs, event logs, and diagnostic information generated by the AP.

operationId: `getApLogs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose log information is to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApLogs`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/managementTrafficVlanSettings`

**Get AP Management Traffic VLAN Settings**

Retrieve AP management traffic VLAN settings configured for this access point. The response includes VLAN configuration used for managing access point traffic and communications.

operationId: `GetApManagementTrafficVlanSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose management traffic VLAN settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApManagementTrafficVlanSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/managementTrafficVlanSettings`

**Update AP Management Traffic VLAN Settings**

Update AP management traffic VLAN settings for this access point. This operation allows you to update VLAN configuration used for managing access point traffic and communications.

operationId: `UpdateApManagementTrafficVlanSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose management traffic VLAN settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApManagementTrafficVlanSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `useVenueSettings` | `boolean` |  |  |
| `vlanId` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/meshSettings`

**Get AP Mesh Settings**

Retrieve mesh network settings configured for this access point. The response includes mesh enablement status and configuration parameters for AP mesh networking.

operationId: `getApMeshSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose mesh settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApMeshSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/meshSettings`

**Update AP Mesh Settings**

Update mesh network settings for this access point. This operation allows you to enable or disable mesh networking and configure mesh parameters for the AP.

operationId: `updateApMeshSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose mesh settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApMeshSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `meshMode` | `string` |  |  |
| `uplinkMacAddresses` | `array` |  |  |
| `uplinkMode` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/aps/{serialNumber}/neighbors`

**Patch AP Neighbors**

Request this access point to collect neighbor information. This operation triggers the AP to scan and discover nearby access points for network topology analysis and optimization.

operationId: `patchApNeighbors`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which neighbor collection is to be triggered. |


**Request Body:** `Wi-Fi_Services_ApNeighbors`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `status` | `['string', 'null']` | ✓ |  |
| `type` | `['string', 'null']` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/aps/{serialNumber}/neighbors/query`

**Query AP Neighbors**

Query and retrieve the access point neighbor information including RF neighbors and LLDP neighbors for network topology mapping.

operationId: `queryApNeighbors`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point is deployed. |
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for device identification and management. |


**Request Body:** `Wi-Fi_Services_ApNeighborQuery`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `array` |  |  |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `sortField` | `string` |  |  |
| `sortOrder` | `['string', 'null']` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApNeighborQueryData`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/networkSettings`

**Get AP Network Settings**

Retrieve network settings configured for this access point. The response includes IP configuration, network interface settings, and connectivity parameters. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/networkSettings can be used for this content.

operationId: `GetApNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose network settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApNetworkSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/networkSettings`

**Update AP Network Settings**

Update network settings for this access point. This operation allows you to update IP configuration, network interface settings, and connectivity parameters.

operationId: `UpdateApNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose network settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApNetworkSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `gateway` | `string` |  |  |
| `ip` | `string` |  |  |
| `ipType` | `['string', 'null']` |  |  |
| `netmask` | `string` |  |  |
| `primaryDnsServer` | `string` |  |  |
| `secondaryDnsServer` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/packets`

**Get AP Packets**

Retrieve packet capture results for this access point. The response includes captured network packets and analysis data collected during packet capture sessions.

operationId: `getApPackets`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose packet capture results are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApPackets`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/aps/{serialNumber}/packets`

**Patch AP Packets**

Start or stop packet capture for this access point. This operation allows you to initiate or terminate network packet capture sessions for network analysis and troubleshooting.

operationId: `patchApPackets`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which packet capture is to be started or stopped. |


**Request Body:** `Wi-Fi_Services_ApPacketAction`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `['string', 'null']` |  |  |
| `captureInterface` | `['string', 'null']` |  |  |
| `frameTypeFilter` | `array` |  |  |
| `macAddressFilter` | `string` |  |  |
| `sessionId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_ApPacketActionResponseOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `409` Conflict [WIFI-10477: "Duplicate sessionId exists"] → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/passwords`

**Get AP Password**

Retrieve the current password for a specific access point. This operation returns the password used for AP authentication and management access.

operationId: `getApPassword`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApPassword`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/pictures`

**Delete AP Pictures**

Delete all picture images associated with the AP removing visual identification information from the system.

operationId: `deleteApPictures`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point is deployed. |
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for device identification and management. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/pictures`

**Get AP Pictures**

Retrieve all picture images associated with the AP for visual identification and management interface display.

operationId: `getApPictures`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point is deployed. |
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for device identification and management. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApPictures`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/pictures`

**Update AP Pictures**

Update or replace the existing picture images for the AP with new visual identification information.

operationId: `updateApPictures`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point is deployed. |
| `serialNumber` | path | ✓ | `string` | The unique serial number identifier of the access point for device identification and management. |


**Request Body:** Yes

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `file` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/radioSettings`

**Get AP Radio**

Retrieve radio settings configured for this access point. The response includes channel selection, power levels, and frequency band configurations for the AP radios. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/radioSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getApRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose radio settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApRadioSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/radioSettings`

**Update AP Radio**

Update radio settings for this access point. This operation allows you to update channel selection, power levels, and frequency band configurations for the AP radios. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/radioSettings can be used for this content. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateApRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose radio settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApRadioSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apRadioParams24G` | `Wi-Fi_Services_ApRadio24GHzSettings` |  |  |
| `apRadioParams50G` | `Wi-Fi_Services_ApRadio5GHzSettings` |  |  |
| `apRadioParams6G` | `Wi-Fi_Services_ApRadio6GHzSettings` |  |  |
| `apRadioParamsDual5G` | `Wi-Fi_Services_ApRadioDual5GHzSettings` |  |  |
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `enable6G` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/replacements`

**Cancel Replacing AP**

Remove the replacement relationship between the original and replacement APs, cancelling the association without deleting either AP.

operationId: `cancelReplacingAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the original access point whose replacement relationship is to be cancelled. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/replacements`

**Get Replacement AP Information**

Retrieve information about the replacement AP associated with the original device, including the serial number and details of the replacing AP for tracking.

operationId: `getReplacingAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the original access point whose replacement information is to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApReplacement`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/smartMonitorSettings`

**Get AP Smart Monitor Settings**

Retrieve smart monitor settings configured for this access point. The response includes monitoring configurations that enable intelligent network analysis and performance optimization for the AP.

operationId: `GetApSmartMonitorSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose smart monitor settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApSmartMonitorSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/smartMonitorSettings`

**Update AP Smart Monitor Settings**

Update smart monitor settings for this access point. This operation allows you to update monitoring configurations that enable intelligent network analysis and performance optimization for the AP.

operationId: `UpdateApSmartMonitorSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose smart monitor settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApSmartMonitorSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `interval` | `integer` |  | The time interval in seconds between smart monitor uplink status checks. Valid range is 5 to 60 seconds. |
| `threshold` | `integer` |  | The number of consecutive failed uplink checks required before WLANs are disabled. Valid range is 1 to 10 attempts. |
| `useVenueSettings` | `boolean` |  | Indicates whether to use venue-level smart monitor settings, overriding AP specific settings. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/stickyClientSteeringSettings`

**Reset AP Sticky Client Steering Settings**

Reset the sticky client steering settings of this access point to use the venue's default settings. This operation removes AP specific configurations and restores venue level settings.

operationId: `ResetApStickyClientSteeringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose sticky client steering settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/stickyClientSteeringSettings`

**Get AP Sticky Client Steering Settings**

Retrieve sticky client steering settings configured for this access point. The response includes configurations that control how clients are steered between access points based on signal strength and connection quality.

operationId: `GetApStickyClientSteeringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose sticky client steering settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApStickyClientSteeringSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/stickyClientSteeringSettings`

**Update AP Sticky Client Steering Settings**

Update sticky client steering settings for this AP to control client steering based on signal strength and connection quality.

operationId: `UpdateApStickyClientSteeringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose sticky client steering settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApStickyClientSteeringSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  | True if sticky client steering is enabled. |
| `neighborApPercentageThreshold` | `integer` |  |  |
| `snrThreshold` | `integer` |  |  |
| `useVenueSettings` | `boolean` |  | True if using venue settings (overriding AP settings). |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/aps/{serialNumber}/systemCommands`

**Trigger AP System Commands**

Trigger system commands for this access point. This operation executes administrative commands such as reboot, reset, or firmware update operations on the AP.

operationId: `TriggerApSystemCommands`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point for which system commands are to be triggered. |


**Request Body:** `Wi-Fi_Services_ApSystemCommand`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `type` | `['string', 'null']` | ✓ |  |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/usbPortSettings`

**Get AP USB Port**

Retrieve USB port settings configured for this access point. The response includes USB port configurations and functionality settings.

operationId: `getApUsbPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose USB port settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApUsbPortSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/usbPortSettings`

**Update AP USB Port**

Update USB port settings for this access point. This operation allows you to update USB port configurations and functionality settings.

operationId: `updateApUsbPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose USB port settings are to be modified. |


**Request Body:** `Wi-Fi_Services_ApUsbPortSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `useVenueSettings` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/wifiAvailableChannels`

**Get AP Available Channels**

Retrieve available Wi-Fi channels for this access point based on regulatory domain and country settings. The response includes all supported channels across different frequency bands. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `getWifiAvailableChannelsOfAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose available channels are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiAvailableChannelsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/floorplans/{floorplanId}/aps/{serialNumber}/floorPositions`

**Deactivate AP Floor Position**

Deactivate an access point on a floor plan and remove its position information. This operation disassociates the AP from the floor plan without deleting the AP itself.

operationId: `deactivateApFloorPosition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the floor plan. |
| `floorplanId` | path | ✓ | `string` | The unique identifier of the floor plan. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/floorplans/{floorplanId}/aps/{serialNumber}/floorPositions`

**Get AP Floor Position**

Retrieve the position coordinates of an access point on a specific floor plan.

operationId: `getApFloorPosition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the floor plan. |
| `floorplanId` | path | ✓ | `string` | The unique identifier of the floor plan. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApFloorPosition`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/floorplans/{floorplanId}/aps/{serialNumber}/floorPositions`

**Activate AP Floor Position**

Activate an AP on a floor plan or update its position using X-coordinate and Y-coordinate.

operationId: `activateApFloorPosition`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the floor plan. |
| `floorplanId` | path | ✓ | `string` | The unique identifier of the floor plan. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP. |


**Request Body:** `Wi-Fi_Services_ApFloorPosition`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `xPercent` | `number` |  |  |
| `yPercent` | `number` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## SoftGRE Profile

*Manage SoftGRE profiles that configure GRE tunnels, gateways, and keep alive monitoring for reliable traffic forwarding.*


*10 endpoints*


### `POST` `/softGreProfiles`

**Add SoftGRE Profile**

Create a new SoftGRE profile with gateway addresses, MTU settings, and keep alive parameters for GRE tunneling.

operationId: `addSoftGreProfile`


**Request Body:** `Wi-Fi_Services_SoftGreProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `disassociateClientEnabled` | `boolean` |  |  |
| `gatewayFailbackEnabled` | `boolean` |  |  |
| `gatewaySecondaryToPrimaryTimer` | `integer` |  |  |
| `id` | `string` |  |  |
| `keepAliveInterval` | `integer` |  |  |
| `keepAliveRetryTimes` | `integer` |  |  |
| `mtuSize` | `integer` |  | The MTU size in bytes. This field is required when the MTU type is set to manual. |
| `mtuType` | `string` |  |  |
| `name` | `string` | ✓ |  |
| `primaryGatewayAddress` | `string` | ✓ |  |
| `secondaryGatewayAddress` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/softGreProfiles/{softGreProfileId}`

**Delete SoftGRE Profile**

Remove a SoftGRE profile by its unique identifier. This operation permanently deletes the profile and its configurations; ensure it is not associated with Wi-Fi networks or LAN ports before deletion.

operationId: `deleteSoftGreProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/softGreProfiles/{softGreProfileId}`

**Get SoftGRE Profile**

Retrieve detailed information about a specific SoftGRE profile by its unique identifier, including configuration settings, gateway addresses, MTU settings, and keep alive parameters associated with the profile.

operationId: `getSoftGreProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_SoftGreProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/softGreProfiles/{softGreProfileId}`

**Update SoftGRE Profile**

Update an existing SoftGRE profile including gateway addresses, MTU settings, and keep alive parameters.

operationId: `updateSoftGreProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be updated. |


**Request Body:** `Wi-Fi_Services_SoftGreProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `disassociateClientEnabled` | `boolean` |  |  |
| `gatewayFailbackEnabled` | `boolean` |  |  |
| `gatewaySecondaryToPrimaryTimer` | `integer` |  |  |
| `id` | `string` |  |  |
| `keepAliveInterval` | `integer` |  |  |
| `keepAliveRetryTimes` | `integer` |  |  |
| `mtuSize` | `integer` |  | The MTU size in bytes. This field is required when the MTU type is set to manual. |
| `mtuType` | `string` |  |  |
| `name` | `string` | ✓ |  |
| `primaryGatewayAddress` | `string` | ✓ |  |
| `secondaryGatewayAddress` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/softGreProfiles/{softGreProfileId}`

**Deactivate SoftGRE Profile On Venue AP Model LAN Port**

Remove the association between a SoftGRE profile and a LAN port for an AP model.

operationId: `deactivateSoftGreProfileOnVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP model. |
| `apModel` | path | ✓ | `string` | The AP model name for which the SoftGRE profile will be deactivated on the LAN port. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port where the SoftGRE profile will be deactivated. |
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be disassociated from the LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/softGreProfiles/{softGreProfileId}`

**Activate SoftGRE Profile On Venue AP Model LAN Port**

Associate a SoftGRE profile with a LAN port for an AP model to enable GRE tunneling.

operationId: `activateSoftGreProfileOnVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP model. |
| `apModel` | path | ✓ | `string` | The AP model name for which the SoftGRE profile will be activated on the LAN port. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port where the SoftGRE profile will be activated. |
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be associated with the LAN port. |


**Request Body:** `Wi-Fi_Services_LanPortSoftGreProfileSettings`


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/softGreProfiles/{softGreProfileId}`

**Deactivate SoftGRE Profile On Venue AP LAN Port**

Remove the association between a SoftGRE profile and a LAN port for an AP.

operationId: `deactivateSoftGreProfileOnVenueApLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP for which the SoftGRE profile will be deactivated on the LAN port. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port where the SoftGRE profile will be deactivated. |
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be disassociated from the LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/softGreProfiles/{softGreProfileId}`

**Activate SoftGRE Profile On Venue AP LAN Port**

Associate a SoftGRE profile with a LAN port for an AP to enable GRE tunneling.

operationId: `activateSoftGreProfileOnVenueApLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP for which the SoftGRE profile will be activated on the LAN port. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port where the SoftGRE profile will be activated. |
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be associated with the LAN port. |


**Request Body:** `Wi-Fi_Services_LanPortSoftGreProfileSettings`


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/softGreProfiles/{softGreProfileId}`

**Deactivate SoftGRE Profile On Venue Wi-Fi Network**

Remove the association between a SoftGRE profile and a Wi-Fi network.

operationId: `deactivateSoftGreProfileOnVenueWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the SoftGRE profile will be deactivated. |
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/softGreProfiles/{softGreProfileId}`

**Activate SoftGRE Profile On Venue Wi-Fi Network**

Associate a SoftGRE profile with a specific Wi-Fi network to enable GRE tunneling, establishing the relationship so the profile configuration tunnels traffic on the specified Wi-Fi network.

operationId: `activateSoftGreProfileOnVenueWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the SoftGRE profile will be activated. |
| `softGreProfileId` | path | ✓ | `string` | The unique identifier of the SoftGRE profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## VLAN Pool Profile

*Manage VLAN pool profiles.*


*8 endpoints*


### `DELETE` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}/vlanPoolProfiles/{vlanPoolProfileId}`

**Deactivate VLAN Pool Profile On AP Group**

Remove the association between a VLAN pool profile and an AP group.

operationId: `deactivateVlanPoolProfileOnVenueWifiNetworkApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network and AP group. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network containing the AP group. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group where the VLAN pool profile will be deactivated. |
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be disassociated from the AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/apGroups/{apGroupId}/vlanPoolProfiles/{vlanPoolProfileId}`

**Activate VLAN Pool Profile On AP Group**

Associate a VLAN pool profile with an AP group to enable VLAN pool assignment.

operationId: `activateVlanPoolProfileOnVenueWifiNetworkApGroup`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the Wi-Fi network and AP group. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network containing the AP group. |
| `apGroupId` | path | ✓ | `string` | The unique identifier of the AP group where the VLAN pool profile will be activated. |
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be associated with the AP group. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/vlanPoolProfiles`

**Add VLAN Pool Profile**

Create a new VLAN pool profile with VLAN members and settings for managing VLAN pool configurations.

operationId: `addVlanPoolProfile`


**Request Body:** `Wi-Fi_Services_VlanPoolProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `vlanMembers` | `array` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/vlanPoolProfiles/{vlanPoolProfileId}`

**Delete VLAN Pool Profile**

Remove a VLAN pool profile and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteVlanPoolProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/vlanPoolProfiles/{vlanPoolProfileId}`

**Get VLAN Pool**

Retrieve detailed information about a specific VLAN pool profile by its unique identifier. The response includes all configuration settings, VLAN members, and policies associated with the profile.

operationId: `getVlanPoolProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VlanPoolProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/vlanPoolProfiles/{vlanPoolProfileId}`

**Update VLAN Pool Profile**

Update an existing VLAN pool profile configuration including VLAN members, description, and settings.

operationId: `updateVlanPoolProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be updated. |


**Request Body:** `Wi-Fi_Services_VlanPoolProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `vlanMembers` | `array` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/vlanPoolProfiles/{vlanPoolProfileId}`

**Deactivate VLAN Pool Profile On Wi-Fi Network**

Remove the association between a VLAN pool profile and a Wi-Fi network.

operationId: `deactivateVlanPoolProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the VLAN pool profile will be deactivated. |
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/vlanPoolProfiles/{vlanPoolProfileId}`

**Activate VLAN Pool Profile On Wi-Fi Network**

Associate a VLAN pool profile with a Wi-Fi network to enable VLAN pool assignment.

operationId: `activateVlanPoolProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the VLAN pool profile will be activated. |
| `vlanPoolProfileId` | path | ✓ | `string` | The unique identifier of the VLAN pool profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Calling Service Profile

*Manage Wi-Fi calling service profiles.*


*8 endpoints*


### `DELETE` `/wifiCallingServiceProfiles`

**Delete Wi-Fi Calling Service Profiles**

Delete a list of Wi-Fi calling service profiles. Use DELETE /wifiCallingServiceProfiles/{wifiCallingServiceProfileId} instead. This method will be removed no sooner than 06/30/2026. The following URL /wifiCallingServiceProfiles/{wifiCallingServiceProfileId} can be used for this content.

operationId: `deleteWifiCallingServiceProfilesBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiCallingServiceProfiles`

**Get Wi-Fi Calling Service Profiles**

Get the Wi-Fi calling service profiles. This method will be removed no sooner than 06/30/2026. The following URL /wifiCallingServiceProfiles/query can be used for this content.

operationId: `getWiFiCallingServiceProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/wifiCallingServiceProfiles`

**Create Wi-Fi Calling Service Profile**

Create a new Wi-Fi calling service profile. Content-Type: "application/vnd.ruckus.v1+json" will be deprecated on 2024/09/01. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `createWifiCallingServiceProfile`


**Request Body:** `Wi-Fi_Services_WifiCallingServiceProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `epdgs` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `networkIds` | `array` |  |  |
| `qosPriority` | `string` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Delete Wi-Fi Calling Service Profile**

Delete a Wi-Fi calling service profile. Content-Type: "application/vnd.ruckus.v1+json" will be deprecated on 2024/09/01.

operationId: `deleteWifiCallingServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Get Wi-Fi Calling Service Profile**

Get the Wi-Fi calling service profile details. Content-Type: "application/vnd.ruckus.v1+json" will be deprecated on 2024/09/01. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getWiFiCallingServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | Wi-Fi calling profile ID. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiCallingServiceProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Update Wi-Fi Calling Service Profile**

Update a Wi-Fi calling service profile. Content-Type: "application/vnd.ruckus.v1+json" will be deprecated on 2024/09/01. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateWifiCallingServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile. |


**Request Body:** `Wi-Fi_Services_WifiCallingServiceProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `epdgs` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `networkIds` | `array` |  |  |
| `qosPriority` | `string` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Deactivate Wi-Fi Calling Service Profile On Wi-Fi Network**

Deactivate a Wi-Fi calling service profile on a Wi-Fi network.

operationId: `deactivateWifiCallingServiceProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network. |
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Activate Wi-Fi Calling Service Profile On Wi-Fi Network**

Activate a Wi-Fi calling service profile on a Wi-Fi network.

operationId: `activateWifiCallingServiceProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network. |
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP Venue Template

*Manage Wi-Fi venue template configuration, including radio settings, mesh, LEDs, LAN ports, and syslog.*


*33 endpoints*


### `GET` `/templates/venues/{venueId}/apBssColoringSettings`

**Get Venue Template Basic Service Set Coloring Settings**

Retrieve basic service set coloring settings configured for this venue MSP template. The response includes BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks.

operationId: `getVenueTemplateApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose BSS coloring settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApBssColoringSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apBssColoringSettings`

**Update Venue Template Basic Service Set Coloring Settings**

Update basic service set coloring settings for this venue MSP template including BSS color configuration.

operationId: `updateVenueTemplateApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose BSS coloring settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApBssColoringSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bssColoringEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apCellularSettings`

**Get Venue Template AP model Cellular**

Retrieve AP model cellular settings and LTE band lock channels configured for this venue MSP template. The response includes cellular connectivity configurations and locked LTE frequency bands for access points.

operationId: `getVenueTemplateApCellularSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose cellular settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApCellularSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apCellularSettings`

**Update Venue Template AP model Cellular**

Update AP model cellular settings and LTE band lock channels for this venue MSP template.

operationId: `updateVenueTemplateApCellularSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose cellular settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApCellularSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `model` | `string` |  |  |
| `primarySim` | `Wi-Fi_Services_SimSettings` |  |  |
| `primaryWanRecoveryTimer` | `integer` | ✓ |  |
| `secondarySim` | `Wi-Fi_Services_SimSettings` |  |  |
| `wanConnection` | `['string', 'null']` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apClientAdmissionControlSettings`

**Get Venue Template Client Admission Control Settings**

Retrieve client admission control settings configured for this venue MSP template. The response includes thresholds and policies that control when new clients are allowed to connect to access points.

operationId: `getVenueTemplateApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose client admission control settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApClientAdmissionControlSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apClientAdmissionControlSettings`

**Update Venue Template Client Admission Control Settings**

Update client admission control settings for this venue MSP template including thresholds and connection policies.

operationId: `updateVenueTemplateApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose client admission control settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApClientAdmissionControlSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `maxRadioLoad24G` | `integer` |  |  |
| `maxRadioLoad50G` | `integer` |  |  |
| `minClientCount24G` | `integer` |  |  |
| `minClientCount50G` | `integer` |  |  |
| `minClientThroughput24G` | `integer` |  |  |
| `minClientThroughput50G` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apDirectedMulticastSettings`

**Get Venue Template Directed Multicast Settings**

Retrieve directed multicast settings configured for this venue MSP template. The response includes multicast optimization configurations that improve efficiency for multicast traffic delivery to clients.

operationId: `getVenueTemplateApDirectedMulticastSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose directed multicast settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApDirectedMulticastSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apDirectedMulticastSettings`

**Update Venue Template Directed Multicast Settings**

Update directed multicast settings for this venue MSP template. This operation allows you to update multicast optimization configurations that improve efficiency for multicast traffic delivery to clients.

operationId: `updateVenueTemplateApDirectedMulticastSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose directed multicast settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApDirectedMulticastSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkEnabled` | `boolean` |  |  |
| `wiredEnabled` | `boolean` |  |  |
| `wirelessEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apDosProtectionSettings`

**Get Venue Template DoS Protection**

Retrieve DoS protection settings configured for this venue MSP template. The response includes denial-of-service protection configurations and thresholds for access points.

operationId: `getVenueTemplateApDosProtectionSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose DoS protection settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApDosProtectionSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apDosProtectionSettings`

**Update Venue Template DoS Protection**

Update DoS protection settings for this venue MSP template. This operation allows you to update denial-of-service protection configurations and thresholds for access points.

operationId: `updateVenueTemplateApDosProtectionSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose DoS protection settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApDosProtectionSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `blockingPeriod` | `integer` |  |  |
| `checkPeriod` | `integer` |  |  |
| `enabled` | `boolean` |  |  |
| `failThreshold` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apLoadBalancingSettings`

**Get Venue Template Load Balancing Settings**

Retrieve load balancing settings configured for this venue MSP template. The response includes client distribution configurations that optimize client connections across access points.

operationId: `getVenueTemplateApLoadBalancingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose load balancing settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApLoadBalancingSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apLoadBalancingSettings`

**Update Venue Template Load Balancing Settings**

Update load balancing settings for this venue MSP template. This operation allows you to update client distribution configurations that optimize client connections across access points.

operationId: `updateVenueTemplateApLoadBalancingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose load balancing settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApLoadBalancingSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bandBalancingClientPercent24G` | `integer` |  |  |
| `bandBalancingEnabled` | `boolean` |  |  |
| `enabled` | `boolean` |  |  |
| `loadBalancingMethod` | `string` |  |  |
| `steeringMode` | `string` |  |  |
| `stickyClientNbrApPercentageThreshold` | `integer` |  |  |
| `stickyClientSnrThreshold` | `integer` |  |  |
| `stickyClientSteeringEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apMeshSettings`

**Get Mesh Settings**

Retrieve mesh network settings configured for this venue MSP template. The response includes mesh enablement status and configuration parameters for access point mesh networking.

operationId: `getVenueTemplateApMeshSettingsV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose mesh settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApMeshSettingsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apMeshSettings`

**Update Mesh**

Update mesh network settings for this venue MSP template. This operation allows you to enable or disable mesh networking and configure mesh parameters for access points.

operationId: `updateVenueTemplateApMeshSettingsV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose mesh settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApMeshSettingsV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `passphrase` | `string` |  |  |
| `radioType` | `string` |  |  |
| `ssid` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apModelBandModeSettings`

**Get Venue Template Band Mode Settings**

Retrieve venue MSP template band mode settings configured for access points. The settings are defined per AP model and control the radio frequency bands available for Wi-Fi operations.

operationId: `getVenueTemplateBandModeSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose band mode settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apModelBandModeSettings`

**Update Template Venue Band Mode Settings**

Update venue MSP template band mode settings for access points. The settings are defined per AP model and control the radio frequency bands available for Wi-Fi operations.

operationId: `updateVenueTemplateBandModeSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose band mode settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apModelCapabilities`

**Get Venue Template AP model Capabilities**

Retrieve AP model capabilities information for this venue MSP template. The response includes detailed feature support information for each AP model configured in the venue template.

operationId: `getVenueTemplateApModelCapabilities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose AP model capabilities are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelCapabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apModelExternalAntennaSettings`

**Get Venue Template AP Model External Antenna Settings**

Retrieve venue MSP template external antenna settings configured for access points. The settings are defined per AP model and specify external antenna configurations for radio transmissions.

operationId: `getVenueTemplateApModelExternalAntennaSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose external antenna settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apModelExternalAntennaSettings`

**Update Venue Template AP Model External Antenna Settings**

Update venue MSP template external antenna settings for access points. The settings are defined per AP model and specify external antenna configurations for radio transmissions.

operationId: `updateVenueTemplateApModelExternalAntennaSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose external antenna settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apModelLanPortSettings`

**Get Venue Template LAN ports**

Retrieve venue MSP template LAN port settings configured for access points. The settings are defined per AP model and control Ethernet port configurations including VLAN assignments and port types.

operationId: `getVenueTemplateApModelLanPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose LAN port settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apModelLedSettings`

**Get Venue Template LED**

Retrieve venue MSP template LED indicator settings configured for access points. The settings are defined per AP model and control LED behavior and status indicators.

operationId: `getVenueTemplateApModelLedSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose LED settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apModelLedSettings`

**Update Venue LED**

Update venue MSP template LED indicator settings for access points. The settings are defined per AP model and control LED behavior and status indicators.

operationId: `updateVenueTemplateApModelLedSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose LED settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apMulticastDnsFencingSettings`

**Get Venue Template Multicast DNS Fencing Settings**

Retrieve multicast DNS fencing settings configured for access points in this venue MSP template. The response includes mDNS isolation configurations that control service discovery across network segments.

operationId: `getVenueTemplateApMulticastDnsFencingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose multicast DNS fencing settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApMulticastDnsFencingSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apMulticastDnsFencingSettings`

**Update Venue Template Multicast DNS Fencing Settings**

Update multicast DNS fencing settings for access points in this venue MSP template. This operation allows you to update mDNS isolation configurations that control service discovery across network segments.

operationId: `updateVenueTemplateApMulticastDnsFencingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose multicast DNS fencing settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApMulticastDnsFencingSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apRadioSettings`

**Get Venue Template AP Radio Settings**

Retrieve radio settings configured for this venue MSP template. The response includes channel selection, power levels, and frequency band configurations for access point radios.

operationId: `getVenueTemplateApRadioSettingsV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose radio settings are to be retrieved. |
| `defaultOnly` | query |  | `boolean` | Only get the details of default radio settings in this venue template. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApRadioSettingsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apRadioSettings`

**Update Venue Template Radio Settings**

Update radio settings for this venue MSP template. This operation allows you to update channel selection, power levels, and frequency band configurations for access point radios.

operationId: `updateVenueTemplateApRadioSettingsV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose radio settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApRadioSettingsV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `radioParams24G` | `Wi-Fi_Services_VenueApRadio24GHzSettings` |  |  |
| `radioParams50G` | `Wi-Fi_Services_VenueApRadio5GHzSettings` |  |  |
| `radioParams6G` | `Wi-Fi_Services_VenueApRadio6GHzSettingsV1_1` |  |  |
| `radioParamsDual5G` | `Wi-Fi_Services_VenueApRadioDual5GHzSettings` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apRadiusOptions`

**Get Venue Template RADIUS Options Settings**

Retrieve RADIUS options settings configured for this venue MSP template. The response includes RADIUS authentication and accounting configuration parameters for access points.

operationId: `getVenueTemplateApRadiusOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose RADIUS options settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApRadiusOptionSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apRadiusOptions`

**Update Venue Template RADIUS Options Settings**

Update RADIUS options settings for this venue MSP template. This operation allows you to update RADIUS authentication and accounting configuration parameters for access points.

operationId: `updateVenueTemplateApRadiusOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose RADIUS options settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApRadiusOptionSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `calledStationIdType` | `string` |  |  |
| `nasIdDelimiter` | `string` |  |  |
| `nasIdType` | `string` |  |  |
| `nasMaxRetry` | `integer` |  |  |
| `nasReconnectPrimaryMin` | `integer` |  |  |
| `nasRequestTimeoutSec` | `integer` |  |  |
| `overrideEnabled` | `boolean` |  |  |
| `singleSessionIdAccounting` | `boolean` |  |  |
| `userDefinedNasId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apRebootTimeoutSettings`

**Get Venue Template AP Reboot Timeout**

Retrieve reboot timeout settings configured for this venue MSP template. The response includes timeout configurations that control how long access points wait before rebooting during configuration updates or recovery scenarios.

operationId: `getVenueTemplateApRebootTimeoutSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose reboot timeout settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApRebootTimeoutSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apRebootTimeoutSettings`

**Update Venue Template AP Reboot Timeout**

Update reboot timeout settings for this venue MSP template including timeout configurations for access points.

operationId: `updateVenueTemplateApRebootTimeoutSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose reboot timeout settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApRebootTimeoutSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `gatewayLossTimeout` | `integer` |  | The timeout in seconds for rebooting AP if it cannot reach the default gateway. Set to 0 to never reboot. |
| `serverLossTimeout` | `integer` |  | The timeout in seconds for rebooting AP if it cannot reach the controller. Set to 0 to never reboot. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/apSmartMonitorSettings`

**Get Venue Template AP Smart Monitor**

Retrieve smart monitor settings configured for this venue MSP template. The response includes monitoring configurations that enable intelligent network analysis and performance optimization for access points.

operationId: `getVenueTemplateApSmartMonitorSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose smart monitor settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApSmartMonitorSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueId}/apSmartMonitorSettings`

**Update Venue Template AP Smart Monitor**

Update smart monitor settings for this venue MSP template. This operation allows you to update monitoring configurations that enable intelligent network analysis and performance optimization for access points.

operationId: `updateVenueTemplateApSmartMonitorSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose smart monitor settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApSmartMonitorSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `interval` | `integer` |  | The interval in seconds for how often smart monitor checks uplink status. |
| `threshold` | `integer` |  | The retry threshold for turning off the WLANs when connectivity issues are detected. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueId}/wifiAvailableChannels`

**Get Venue Template Available Channels**

Retrieve available Wi-Fi channels for this venue MSP template based on regulatory domain and country settings. The response includes all supported channels across different frequency bands.

operationId: `getWifiAvailableChannelsOfVenueTemplateV1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue MSP template whose available channels are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiAvailableChannelsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Network Directory Profile Assignment

*Manage directory server profiles for LDAP and active directory integration enabling enterprise user authentication and authorization.*


*1 endpoint*


### `PUT` `/wifiNetworks/{wifiNetworkId}/directoryServerProfiles/{directoryServerProfileId}`

**Activate Directory Server Profile On Wi-Fi Network**

Activate and associate a directory server profile with a Wi-Fi network enabling authentication for network users.

operationId: `activateDirectoryServerProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network for configuration and management operations. |
| `directoryServerProfileId` | path | ✓ | `string` | The unique identifier of the directory server profile for LDAP or active directory integration. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## DHCP Configuration Service Profile Template

*Manage DHCP configuration service profile templates.*


*8 endpoints*


### `POST` `/templates/dhcpConfigServiceProfiles`

**Create DHCP Configuration Service Profile Template**

Create a DHCP configuration service profile MSP template to manage DHCP server functionality and IP address assignment for venue templates.

operationId: `createDhcpConfigServiceProfileTemplate`


**Request Body:** `Wi-Fi_Services_DhcpConfigServiceProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpMode` | `string` |  |  |
| `dhcpPools` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Delete DHCP Configuration Service Profile Template**

Delete a DHCP configuration service profile MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteDhcpConfigServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Get DHCP Configuration Service Profile Template**

Retrieve detailed information about a DHCP configuration service profile MSP template by its unique identifier including pools, lease times, and DNS settings.

operationId: `getDhcpConfigServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_DhcpConfigServiceProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Update DHCP Configuration Service Profile Template**

Update an existing DHCP configuration service profile MSP template by its unique identifier, updating pools, lease times, and DNS settings.

operationId: `updateDhcpConfigServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_DhcpConfigServiceProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpMode` | `string` |  |  |
| `dhcpPools` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueTemplateId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Deactivate DHCP Configuration Service Profile On Venue Template**

Remove the association between a DHCP configuration service profile MSP template and a venue MSP template without deleting the template.

operationId: `deactivateDhcpConfigServiceProfileOnVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template from which the DHCP configuration service profile MSP template will be deactivated. |
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile MSP template to be disassociated from the venue MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueTemplateId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Get DHCP Service Profile Settings of Venue Template**

Retrieve DHCP configuration service profile MSP template settings for a venue MSP template including active pools and AP assignments.

operationId: `getVenueTemplateDhcpConfigServiceProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template for which to retrieve DHCP service profile settings. |
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile MSP template for which to retrieve settings. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueDhcpConfigServiceProfileSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Activate DHCP Configuration Service Profile On Venue Template**

Associate a DHCP configuration service profile MSP template with a venue MSP template to configure active pools, AP assignments, and WAN port selection.

operationId: `activateDhcpConfigServiceProfileOnVenueTemplateAndUpdateSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template where the DHCP configuration service profile MSP template will be activated. |
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile MSP template to be associated with the venue MSP template. |


**Request Body:** `Wi-Fi_Services_VenueDhcpConfigServiceProfileSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `activeDhcpPoolNames` | `array` |  |  |
| `dhcpServiceAps` | `array` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `wanPortSelectionMode` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueTemplateId}/wifiDhcpPoolUsages`

**Get DHCP Pools Usage in Venue Template**

Retrieve DHCP pool usage details for a venue MSP template including IP address allocation, utilization, total IP count, and used IP count.

operationId: `getVenueTemplateWifiDhcpPoolUsages`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue MSP template for which to retrieve DHCP pool usage. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiDhcpPoolUsages`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Rogue AP Detection Policy Template

*Manage rogue AP detection policy templates.*


*8 endpoints*


### `POST` `/templates/roguePolicies`

**Create Rogue AP Detection Policy Template**

Create a new rogue AP detection policy template with detection rules and policies for automatically classifying unknown APs.

operationId: `addRoguePolicyTemplate`


**Request Body:** `Wi-Fi_Services_RoguePolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/roguePolicies/{roguePolicyTemplateId}`

**Delete Rogue AP Detection Policy Template**

Remove a rogue AP detection policy template and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteRoguePolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/roguePolicies/{roguePolicyTemplateId}`

**Get Rogue AP Detection Policy Template**

Retrieve detailed information about a specific rogue AP detection policy template by its unique identifier. The response includes all configuration settings, rules, and policies associated with the template.

operationId: `getRoguePolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_RoguePolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/roguePolicies/{roguePolicyTemplateId}`

**Update Rogue AP Detection Policy Template**

Update an existing rogue AP detection policy template including detection rules, classification policies, and settings.

operationId: `updateRoguePolicyTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy template to be updated. |


**Request Body:** `Wi-Fi_Services_RoguePolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueTemplateId}/roguePolicies/{roguePolicyTemplateId}`

**Deactivate Rogue AP Detection Policy On Venue Template**

Remove the association between a rogue AP detection policy template and a venue template.

operationId: `deactivateRoguePolicyOnVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template where the rogue AP detection policy template will be deactivated. |
| `roguePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy template to be disassociated from the venue template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/roguePolicies/{roguePolicyTemplateId}`

**Activate Rogue AP Detection Policy On Venue Template**

Associate a rogue AP detection policy template with a venue template to enable automatic rogue AP classification.

operationId: `activateRoguePolicyOnVenueTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template where the rogue AP detection policy template will be activated. |
| `roguePolicyTemplateId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy template to be associated with the venue template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueTemplateId}/roguePolicySettings`

**Get Venue Template Rogue Policy Settings**

Retrieve detailed information about the rogue AP detection policy settings configured for a specific venue template. The response includes all configuration settings such as report threshold and other detection parameters.

operationId: `getVenueTemplateRoguePolicySettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template for which to retrieve rogue policy settings. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRoguePolicySettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/roguePolicySettings`

**Update Venue Template Rogue Policy Settings**

Update rogue AP detection policy settings for a venue template including report threshold and detection parameters.

operationId: `updateVenueTemplateRoguePolicySettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template for which to update rogue policy settings. |


**Request Body:** `Wi-Fi_Services_VenueRoguePolicySettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `reportThreshold` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Calling Service Profile Template

*Manage Wi-Fi calling service profile templates.*


*7 endpoints*


### `POST` `/templates/wifiCallingServiceProfiles`

**Create Wi-Fi Calling Service Profile Template**

Create a new Wi-Fi calling service profile MSP template with ePDG servers, service name, and QoS priority settings.

operationId: `createWifiCallingServiceProfileTemplate`


**Request Body:** `Wi-Fi_Services_WifiCallingServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `epdgs` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `qosPriority` | `string` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Delete Wi-Fi Calling Service Profile Template**

Remove a Wi-Fi calling service profile MSP template and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteWifiCallingServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Get Wi-Fi Calling Service Profile Template**

Retrieve detailed information about a Wi-Fi calling service profile MSP template including ePDG servers, service name, and QoS settings.

operationId: `getWiFiCallingServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiCallingServiceProfileV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Update Wi-Fi Calling Service Profile Template**

Update an existing Wi-Fi calling service profile MSP template configuration including ePDG servers, service name, and QoS priority settings.

operationId: `updateWifiCallingServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_WifiCallingServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `epdgs` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `qosPriority` | `string` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/templates/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}/cloneSettings`

**Clone Wi-Fi Calling Service Profile Template**

Create a copy of an existing Wi-Fi calling service profile MSP template including all configuration settings and ePDG servers.

operationId: `cloneWifiCallingServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile MSP template to be cloned. |


**Request Body:** `Wi-Fi_Services_CloneSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/wifiNetworks/{wifiNetworkTemplateId}/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Deactivate Wi-Fi Calling Service Profile Template On Wi-Fi Network Template**

Remove the association between a Wi-Fi calling service profile MSP template and a Wi-Fi network MSP template.

operationId: `deactivateWifiCallingServiceProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template from which the Wi-Fi calling service profile MSP template will be deactivated. |
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile MSP template to be disassociated from the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/wifiCallingServiceProfiles/{wifiCallingServiceProfileId}`

**Activate Wi-Fi Calling Service Profile Template On Wi-Fi Network Template**

Associate a Wi-Fi calling service profile MSP template with a Wi-Fi network MSP template to enable Wi-Fi calling functionality.

operationId: `activateWifiCallingServiceProfileTemplateOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template where the Wi-Fi calling service profile MSP template will be activated. |
| `wifiCallingServiceProfileId` | path | ✓ | `string` | The unique identifier of the Wi-Fi calling service profile MSP template to be associated with the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Network

*Query Wi-Fi network configuration settings deployed on venues including SSID, security parameters, and network activation details.*


*23 endpoints*


### `DELETE` `/networks`

**Delete Networks**

Perform a batch deletion of multiple Wi-Fi networks by providing a list of network identifiers. This operation permanently removes all specified networks and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `deleteNetworksBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/networks`

**Get Networks**

Retrieve a complete list of all Wi-Fi networks configured in the system. The response includes general network information, SSID details, and configuration settings for each network. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/query can be used for this content.

operationId: `getNetworks`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/networks`

**Create Network**

Create a Wi-Fi network profile with SSID, security settings, authentication methods, QoS policies, and access control rules for venues. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks can be used for this content.

operationId: `createNetwork`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_NetworkOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/networks/qosMapSets`

**Get Default Rules for QoS Map Set**

Retrieve default QoS map set rules available for Wi-Fi networks. The response includes predefined QoS mapping rules and configuration options for quality of service management. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/qosMapSetOptions can be used for this content.

operationId: `getDefaultQosMapSets`


**Responses:**

- `200` OK → `Wi-Fi_Services_QosMapSetOptions`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/networks/wisprProviders`

**Get External WISPr Providers**

Retrieve a list of external WISPr providers available for captive portal networks. These providers have integrated their service with the RUCKUS cloud. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/wisprProviders can be used for this content.

operationId: `getExternalProviders`


**Responses:**

- `200` OK → `Wi-Fi_Services_ExternalProviders`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/networks/{networkId}`

**Delete Network**

Delete a Wi-Fi network by its unique identifier, permanently deleting the network profile and its configurations. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `deleteNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/networks/{networkId}`

**Get Network**

Retrieve detailed information about a specific Wi-Fi network by its unique identifier. The response includes all configuration settings, security parameters, SSID details, and advanced customization options. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `getNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be retrieved. |
| `deep` | query |  | `boolean` | Get deep details of this network. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Network`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/networks/{networkId}`

**Update Network**

Update an existing Wi-Fi network by its unique identifier, updating SSID, security settings, advanced configurations, and all associated policies. This method will be removed no sooner than 06/30/2026. The following URL /wifiNetworks/{wifiNetworkId} can be used for this content.

operationId: `updateNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `networkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/wifiNetworks/query`

**Query Wi-Fi Network Settings On Venues**

Query and retrieve Wi-Fi network configuration settings deployed on venues including network activation status and configuration details.

operationId: `queryWifiNetworkSettingsOnVenues`


**Request Body:** `Wi-Fi_Services_VenueWifiNetworkSettingsQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkIds` | `array` |  |  |
| `venueIds` | `array` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueWifiNetworkSettingsQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}`

**Deactivate Wi-Fi Network On Venue**

Remove the association between a Wi-Fi network and a venue.

operationId: `deactivateWifiNetworkOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the Wi-Fi network will be deactivated. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}`

**Activate Wi-Fi Network On Venue**

Associate a Wi-Fi network with a venue to enable wireless connectivity.

operationId: `activateWifiNetworkOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the Wi-Fi network will be activated. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be associated with the venue. |


**Request Body:** `Wi-Fi_Services_VenueWifiNetwork`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `isAllApGroups` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/settings`

**Get Venue Wi-Fi Network Settings**

Retrieve Wi-Fi network settings for a venue including VLAN assignments, radio type selections, and network parameters.

operationId: `getVenueWifiNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose Wi-Fi network settings are to be retrieved. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network whose venue settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueWifiNetworkSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/settings`

**Update Venue Wi-Fi Network Settings**

Update Wi-Fi network settings for a venue including VLAN assignments, radio type selections, and network parameters.

operationId: `updateVenueWifiNetworkSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose Wi-Fi network settings are to be modified. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network whose venue settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueWifiNetworkSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allApGroupsRadioTypes` | `array` |  |  |
| `allApGroupsVlanId` | `integer` |  |  |
| `isAllApGroups` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `scheduler` | `Wi-Fi_Services_NetworkVenueScheduler` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/wifiNetworks`

**Create Wi-Fi Network**

Create a Wi-Fi network profile with SSID, security settings, authentication methods, QoS policies, and access control rules for venues.

operationId: `addWifiNetwork`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/hotspot20IdentityProviders`

**Get Predefined Hotspot 2.0 Identity Providers**

Retrieve a list of predefined Hotspot 2.0 identity providers available for configuration. The response includes provider identifiers and names that can be used when setting up Hotspot 2.0 authentication.

operationId: `getWifiNetworkPredefinedHotspot20IdentityProviders`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/hotspot20Operators`

**Get Predefined Hotspot 2.0 Operators**

Retrieve a list of predefined Hotspot 2.0 operators available for configuration. The response includes operator identifiers and names that can be used when setting up Hotspot 2.0 networks.

operationId: `getWifiNetworkPredefinedHotspot20Operators`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/qosMapSetOptions`

**Get Default Options for QoS Map Set**

Retrieve default QoS map set options available for Wi-Fi networks. The response includes predefined QoS mapping rules and configuration options for quality of service management.

operationId: `getWifiNetworkDefaultQosMapSetOptions`


**Responses:**

- `200` OK → `Wi-Fi_Services_QosMapSetOptions`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/recoveryPassphraseSettings`

**Get Wi-Fi Recovery Network Passphrase Settings**

Retrieve passphrase settings configured for the Wi-Fi recovery network. The response includes the recovery network passphrase configuration used for emergency network access.

operationId: `getRecoveryPassphraseSettings`


**Responses:**

- `200` OK → `Wi-Fi_Services_RecoveryPassphraseSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/recoveryPassphraseSettings`

**Update Wi-Fi Recovery Network Passphrase Settings**

Update passphrase settings for the Wi-Fi recovery network. This operation allows you to update the recovery network passphrase configuration used for emergency network access.

operationId: `updateRecoveryPassphraseSettings`


**Request Body:** `Wi-Fi_Services_RecoveryPassphraseSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `passphrase` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/wisprProviders`

**Get External WISPr Providers**

Retrieve a list of external WISPr providers available for captive portal networks. These providers have integrated their service with the RUCKUS cloud.

operationId: `getWifiNetworkWisprProviders`


**Responses:**

- `200` OK → `Wi-Fi_Services_WisprProviders`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}`

**Delete Wi-Fi Network**

Delete a Wi-Fi network by its unique identifier, permanently deleting the network profile and its configurations.

operationId: `deleteWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be removed. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/wifiNetworks/{wifiNetworkId}`

**Get Wi-Fi Network**

Retrieve detailed information about a specific Wi-Fi network by its unique identifier. The response includes all configuration settings, security parameters, SSID details, and advanced customization options.

operationId: `getWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiNetwork`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}`

**Update Wi-Fi Network**

Update an existing Wi-Fi network by its unique identifier, updating SSID, security settings, advanced configurations, and all associated policies.

operationId: `updateWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Syslog Server Profile

*Manage Syslog server profiles.*


*8 endpoints*


### `DELETE` `/syslogServerProfiles`

**Delete Syslog Server Profiles**

Perform a batch deletion of multiple syslog server profiles by providing a list of their unique identifiers. This operation permanently removes all specified profiles and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /syslogServerProfiles/{syslogServerProfileId} can be used for this content.

operationId: `deleteSyslogServerProfileBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/syslogServerProfiles`

**Get Syslog Server Profiles**

Retrieve a complete list of all syslog server profiles including name, servers, facility, priority, and flow level. This method will be removed no sooner than 06/30/2026. The following URL /syslogServerProfiles/query can be used for this content.

operationId: `getSyslogServerProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/syslogServerProfiles`

**Create Syslog Server Profile**

Create a new syslog server profile with syslog servers, facility, priority, and flow level settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `createSyslogServerProfile`


**Request Body:** `Wi-Fi_Services_SyslogServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `facility` | `string` |  |  |
| `flowLevel` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `primary` | `Wi-Fi_Services_SyslogServer` | ✓ |  |
| `priority` | `string` |  |  |
| `secondary` | `Wi-Fi_Services_SyslogServer` |  |  |
| `venues` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/syslogServerProfiles/{syslogServerProfileId}`

**Delete Syslog Server Profile**

Remove a syslog server profile and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteSyslogServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `syslogServerProfileId` | path | ✓ | `string` | The unique identifier of the syslog server profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/syslogServerProfiles/{syslogServerProfileId}`

**Get Syslog Server Profile**

Retrieve detailed information about a syslog server profile including syslog servers, facility, priority, and flow level. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getSyslogServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `syslogServerProfileId` | path | ✓ | `string` | The unique identifier of the syslog server profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_SyslogServerProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/syslogServerProfiles/{syslogServerProfileId}`

**Update Syslog Server Profile**

Update an existing syslog server profile including syslog servers, facility, priority, and flow level settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateSyslogServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `syslogServerProfileId` | path | ✓ | `string` | The unique identifier of the syslog server profile to be modified. |


**Request Body:** `Wi-Fi_Services_SyslogServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `facility` | `string` |  |  |
| `flowLevel` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `primary` | `Wi-Fi_Services_SyslogServer` | ✓ |  |
| `priority` | `string` |  |  |
| `secondary` | `Wi-Fi_Services_SyslogServer` |  |  |
| `venues` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/syslogServerProfiles/{syslogServerProfileId}`

**Deactivate Syslog Server Profile On Venue**

Remove the association between a syslog server profile and a venue.

operationId: `deactivateSyslogServerProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue from which the syslog server profile will be deactivated. |
| `syslogServerProfileId` | path | ✓ | `string` | The unique identifier of the syslog server profile to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/syslogServerProfiles/{syslogServerProfileId}`

**Activate Syslog Server Profile On Venue**

Associate a syslog server profile with a venue to enable syslog forwarding from access points.

operationId: `activateSyslogServerProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the syslog server profile will be activated. |
| `syslogServerProfileId` | path | ✓ | `string` | The unique identifier of the syslog server profile to be associated with the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Radius Service Certificate Assignments

*Manage certificate bindings for entities.*


*2 endpoints*


### `DELETE` `/radiusServerProfiles/{radiusId}/certificates/{certificateId}`

**Deactivate Certificate On RADIUS Server Profile**

Remove the association between a certificate and a RADIUS server profile without deleting the certificate.

operationId: `deactivateCertificateOnRadiusServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile. |
| `certificateId` | path | ✓ | `string` | The unique identifier of the certificate. |
| `certType` | query |  | `string` | Deactivate the certificate type [CLIENT, SERVER] in the RADIUS server profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/radiusServerProfiles/{radiusId}/certificates/{certificateId}`

**Activate Certificate On RADIUS Server Profile**

Associate a certificate with a RADIUS server profile to enable certificate based authentication.

operationId: `activateCertificateOnRadiusServerProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `radiusId` | path | ✓ | `string` | The unique identifier of the RADIUS server profile. |
| `certificateId` | path | ✓ | `string` | The unique identifier of the certificate. |
| `certType` | query |  | `string` | Activate the certificate type [CLIENT, SERVER] in the RADIUS server profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Application Policy

*Manage application policy profiles.*


*10 endpoints*


### `DELETE` `/accessControlProfiles/{accessControlProfileId}/applicationPolicies/{applicationPolicyId}`

**Deactivate Application Policy On Access Control Profile**

Remove the association between an application policy and an access control profile without deleting the policy.

operationId: `deactivateApplicationPolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile from which the application policy will be deactivated. |
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be disassociated from the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/accessControlProfiles/{accessControlProfileId}/applicationPolicies/{applicationPolicyId}`

**Activate Application Policy On Access Control Profile**

Associate an application policy with an access control profile to enforce traffic control and bandwidth policies.

operationId: `activateApplicationPolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile where the application policy will be activated. |
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be associated with the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/applicationPolicies`

**Delete Application Policies**

Perform a batch deletion of multiple application policies by providing a list of policy identifiers. This operation permanently removes all specified policies and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /applicationPolicies/{applicationPolicyId} can be used for this content.

operationId: `deleteApplicationPolicies`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/applicationPolicies`

**Get Application Policies**

Retrieve a complete list of all application policies configured in the system. This method will be removed no sooner than 06/30/2026. The following URL /applicationPolicies/query can be used for this content.

operationId: `getApplicationPolicies`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/applicationPolicies`

**Add Application Policy**

Create an application policy with traffic control and QoS rules that can be applied to Wi-Fi networks or access control profiles. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `addApplicationPolicy`


**Request Body:** `Wi-Fi_Services_ApplicationPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_ApplicationPolicyOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/applicationPolicies/{applicationPolicyId}`

**Delete Application Policy**

Delete an application policy by its unique identifier, permanently deleting the policy and its configurations.

operationId: `deleteApplicationPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/applicationPolicies/{applicationPolicyId}`

**Get Application Policy**

Retrieve detailed information about a specific application policy by its unique identifier. The response includes all configuration settings, rules, and policies associated with the policy. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getApplicationPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ApplicationPolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/applicationPolicies/{applicationPolicyId}`

**Update Application Policy**

Update an existing application policy by its unique identifier, updating rules, policies, and settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateApplicationPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be updated. |


**Request Body:** `Wi-Fi_Services_ApplicationPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/applicationPolicies/{applicationPolicyId}`

**Deactivate Application Policy On Wifi Network**

Remove the association between an application policy and a Wi-Fi network without deleting the policy.

operationId: `deactivateApplicationPolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the application policy will be deactivated. |
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/applicationPolicies/{applicationPolicyId}`

**Activate Application Policy On Wifi Network**

Associate an application policy with a Wi-Fi network to enforce traffic control and bandwidth policies.

operationId: `activateApplicationPolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the application policy will be activated. |
| `applicationPolicyId` | path | ✓ | `string` | The unique identifier of the application policy to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Client

*Manage client connections.*


*2 endpoints*


### `PATCH` `/aps/clients`

**Clients Control**

Perform control actions on multiple clients across different access points. This operation allows you to disconnect clients by specifying their MAC addresses and associated AP serial numbers. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{serialNumber}/clients/{clientMacAddress} can be used for this content.

operationId: `clientControl`


**Request Body:** `Wi-Fi_Services_ClientControlAction`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `action` | `['string', 'null']` | ✓ |  |
| `clients` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/venues/{venueId}/aps/{serialNumber}/clients/{clientMacAddress}`

**Patch AP Client**

Update the connection status of a specific client connected to an access point. This operation allows you to disconnect the client from the network by updating its status.

operationId: `patchApClient`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point to which the client is connected. |
| `clientMacAddress` | path | ✓ | `string` | The MAC address of the client whose connection status is to be modified. |


**Request Body:** `Wi-Fi_Services_ApClient`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `status` | `['string', 'null']` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Layer 2 ACL Policy

*Manage layer 2 ACL policy profiles covering creation, updates, and assignments.*


*10 endpoints*


### `DELETE` `/accessControlProfiles/{accessControlProfileId}/l2AclPolicies/{l2AclPolicyId}`

**Deactivate Layer 2 ACL Policy On Access Control Profile**

Remove the association between a layer 2 ACL policy and an access control profile without deleting the policy.

operationId: `deactivateL2AclPolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile from which the layer 2 ACL policy will be deactivated. |
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be disassociated from the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/accessControlProfiles/{accessControlProfileId}/l2AclPolicies/{l2AclPolicyId}`

**Activate Layer 2 ACL Policy On Access Control Profile**

Associate a layer 2 ACL policy with an access control profile to enforce MAC based access control.

operationId: `activateL2AclPolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile where the layer 2 ACL policy will be activated. |
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be associated with the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/l2AclPolicies`

**Delete Layer 2 ACL Policies.**

Perform a batch deletion of multiple layer 2 ACL policies by providing a list of their unique identifiers. This operation permanently removes all specified policies and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /l2AclPolicies/{l2AclPolicyId} can be used for this content.

operationId: `deleteBulkL2AclPolicies`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/l2AclPolicies`

**Get Layer 2 ACL Policies.**

Retrieve a complete list of all layer 2 ACL policies in the system including name, description, MAC addresses, and access actions. This method will be removed no sooner than 06/30/2026. The following URL /l2AclPolicies/query can be used for this content.

operationId: `getAllL2AclPolicies`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/l2AclPolicies`

**Add Layer 2 ACL**

Create a layer 2 ACL policy to control network access based on MAC addresses for access control profiles or Wi-Fi networks. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `addL2AclPolicy`


**Request Body:** `Wi-Fi_Services_L2AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `access` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `macAddresses` | `array` | ✓ |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_L2AclPolicyOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/l2AclPolicies/{l2AclPolicyId}`

**Delete Layer 2 ACL**

Delete a layer 2 ACL policy by its unique identifier, permanently deleting the policy and its configurations.

operationId: `deleteL2AclPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/l2AclPolicies/{l2AclPolicyId}`

**Get Layer 2 ACL**

Retrieve detailed information about a specific layer 2 ACL policy by its unique identifier. The response includes all configured MAC addresses, access actions, and other policy settings.

operationId: `getL2AclPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_L2AclPolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/l2AclPolicies/{l2AclPolicyId}`

**Update Layer 2 ACL**

Update an existing layer 2 ACL policy by its unique identifier, updating MAC addresses and access actions. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateL2AclPolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be modified. |


**Request Body:** `Wi-Fi_Services_L2AclPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `access` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `macAddresses` | `array` | ✓ |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/l2AclPolicies/{l2AclPolicyId}`

**Deactivate Layer 2 ACL Policy On Wi-Fi Network**

Remove the association between a layer 2 ACL policy and a Wi-Fi network without deleting the policy.

operationId: `deactivateL2AclPolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the layer 2 ACL policy will be deactivated. |
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/l2AclPolicies/{l2AclPolicyId}`

**Activate Layer 2 ACL Policy On Wi-Fi Network**

Associate a layer 2 ACL policy with a Wi-Fi network to enforce MAC based access control on the network.

operationId: `activateL2AclPolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the layer 2 ACL policy will be activated. |
| `l2AclPolicyId` | path | ✓ | `string` | The unique identifier of the layer 2 ACL policy to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## DHCP Configuration Service Profile

*Manage DHCP configuration service profiles.*


*13 endpoints*


### `DELETE` `/dhcpConfigServiceProfiles`

**Delete DHCP Configuration Service Profiles**

Perform a batch deletion of multiple DHCP configuration service profiles by providing a list of profile identifiers. This operation permanently removes all specified profiles and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId} can be used for this content.

operationId: `deleteDhcpConfigServiceProfileBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/dhcpConfigServiceProfiles`

**Get DHCP Configuration Service Profiles**

Retrieve a complete list of all DHCP configuration service profiles configured in the system. The response includes all profiles that define DHCP server functionality and IP address assignment configurations. This method will be removed no sooner than 06/30/2026. The following URL /dhcpConfigServiceProfiles/query can be used for this content.

operationId: `getDhcpConfigServiceProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/dhcpConfigServiceProfiles`

**Create DHCP Configuration Service Profile**

Create a DHCP configuration service profile to manage DHCP server functionality and IP address assignment for venues. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `createDhcpConfigServiceProfile`


**Request Body:** `Wi-Fi_Services_DhcpConfigServiceProfileDeep`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpMode` | `string` |  |  |
| `dhcpPools` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `serviceName` | `string` | ✓ |  |
| `usage` | `array` |  |  |
| `venueIds` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_DhcpConfigServiceProfileDeepOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Delete DHCP Configuration Service Profile**

Delete a DHCP configuration service profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteDhcpConfigServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Get DHCP Configuration Service Profile**

Retrieve detailed information about a DHCP configuration service profile by its unique identifier including pools, lease times, and DNS settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getDhcpConfigServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_DhcpConfigServiceProfileDeep`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Update DHCP Configuration Service Profile**

Update an existing DHCP configuration service profile by its unique identifier, updating DHCP pools, lease times, and DNS settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateDhcpConfigServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile to be modified. |


**Request Body:** `Wi-Fi_Services_DhcpConfigServiceProfileDeep`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpMode` | `string` |  |  |
| `dhcpPools` | `array` | ✓ |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `serviceName` | `string` | ✓ |  |
| `usage` | `array` |  |  |
| `venueIds` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/wifiDhcpClientLeases`

**Get AP DHCP Client Leases**

Retrieve DHCP client leases for an access point within a venue including IP addresses, MAC addresses, hostnames, and lease expiration times.

operationId: `getApWifiDhcpClientLeases`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose DHCP client leases are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiDhcpClientLeases`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/{serialNumber}/wifiDhcpPoolUsages`

**Get DHCP Pools Usage in This AP**

Retrieve DHCP pool usage details for an access point within a venue including IP address allocation and utilization.

operationId: `getApWifiDhcpPoolUsages`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose DHCP pool usage is to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiDhcpPoolUsages`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Deactivate DHCP Configuration Service Profile On Venue**

Remove the association between a DHCP configuration service profile and a venue without deleting the profile.

operationId: `deactivateDhcpConfigServiceProfileOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue from which the DHCP configuration service profile will be deactivated. |
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Get DHCP Service Profile Settings of Venue**

Retrieve the activated DHCP configuration service profile settings on a venue including active DHCP pools and AP assignments.

operationId: `getVenueDhcpConfigServiceProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP service profile settings are to be retrieved. |
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile whose settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueDhcpConfigServiceProfileSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId}`

**Activate DHCP Configuration Service Profile On Venue**

Associate a DHCP configuration service profile with a venue and configure active DHCP pools, AP assignments, and WAN port selection.

operationId: `activateDhcpConfigServiceProfileOnVenueAndUpdateSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the DHCP configuration service profile will be activated. |
| `dhcpConfigServiceProfileId` | path | ✓ | `string` | The unique identifier of the DHCP configuration service profile to be associated with the venue. |


**Request Body:** `Wi-Fi_Services_VenueDhcpConfigServiceProfileSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `activeDhcpPoolNames` | `array` |  |  |
| `dhcpServiceAps` | `array` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `wanPortSelectionMode` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/wifiDhcpClientLeases`

**Get Venue DHCP Leases**

Retrieve a list of DHCP client leases for a venue including IP addresses, MAC addresses, hostnames, and lease expiration times.

operationId: `getVenueWifiDhcpClientLeases`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP client leases are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiDhcpClientLeases`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/wifiDhcpPoolUsages`

**Get DHCP Pools Usage in Venue**

Retrieve a list of DHCP pool usage details for a specific venue. The response includes information about IP address allocation and utilization within DHCP pools configured for the venue.

operationId: `getVenueWifiDhcpPoolUsages`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP pool usage is to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiDhcpPoolUsages`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## MAC Registration Pool

*Manage MAC registration pool profiles.*


*2 endpoints*


### `DELETE` `/wifiNetworks/{wifiNetworkId}/macRegistrationPools/{macRegistrationPoolId}`

**Deactivate MAC Registration Pool On Wi-Fi Network**

Remove the association between a MAC registration pool and a Wi-Fi network without deleting the pool.

operationId: `deactivateMacRegistrationPoolOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the MAC registration pool will be deactivated. |
| `macRegistrationPoolId` | path | ✓ | `string` | The unique identifier of the MAC registration pool to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/macRegistrationPools/{macRegistrationPoolId}`

**Activate MAC Registration Pool On Wi-Fi Network**

Associate a MAC registration pool with a Wi-Fi network to enable MAC address registration functionality.

operationId: `activateMacRegistrationPoolOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the MAC registration pool will be activated. |
| `macRegistrationPoolId` | path | ✓ | `string` | The unique identifier of the MAC registration pool to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Client Isolation Profile

*Manage client isolation profiles and their configurations including creation, retrieval, update, and deletion.*


*10 endpoints*


### `POST` `/clientIsolationProfiles`

**Create Client Isolation Profile**

Create a client isolation profile with MAC addresses that can be applied to Wi-Fi networks or LAN ports as isolation exceptions.

operationId: `createClientIsolationProfile`


**Request Body:** `Wi-Fi_Services_ClientIsolationProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowlist` | `array` | ✓ |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/clientIsolationProfiles/{clientIsolationProfileId}`

**Delete Client Isolation Profile**

Delete a client isolation profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteClientIsolationProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/clientIsolationProfiles/{clientIsolationProfileId}`

**Get Client Isolation Profile**

Retrieve detailed information about a specific client isolation profile by its unique identifier. The response includes all configuration settings and allowlist entries that define exceptions to client isolation behavior.

operationId: `getClientIsolationProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ClientIsolationProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/clientIsolationProfiles/{clientIsolationProfileId}`

**Update Client Isolation Profile**

Update an existing client isolation profile by its unique identifier, updating allowlist entries and settings.

operationId: `updateClientIsolationProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be modified. |


**Request Body:** `Wi-Fi_Services_ClientIsolationProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowlist` | `array` | ✓ |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/clientIsolationProfiles/{clientIsolationProfileId}`

**Deactivate Client Isolation Profile On Venue AP Model LAN Port**

Remove the association between a client isolation profile and an AP model LAN port configuration without deleting the profile.

operationId: `deactivateClientIsolationProfileOnVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP model LAN port settings are configured. |
| `apModel` | path | ✓ | `string` | The name of the AP model whose LAN port settings will be modified. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port from which the client isolation profile will be deactivated. |
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be disassociated from the AP model LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/clientIsolationProfiles/{clientIsolationProfileId}`

**Activate Client Isolation Profile On Venue AP Model LAN Port**

Associate a client isolation profile with a LAN port configuration for an AP model within a venue.

operationId: `activateClientIsolationProfileOnVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP model LAN port settings are configured. |
| `apModel` | path | ✓ | `string` | The name of the AP model whose LAN port settings will be configured. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port where the client isolation profile will be activated. |
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be associated with the AP model LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/clientIsolationProfiles/{clientIsolationProfileId}`

**Deactivate Client Isolation Profile On AP LAN Port**

Remove the association between a client isolation profile and a LAN port on an AP without deleting the profile.

operationId: `deactivateClientIsolationProfileOnApLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port configuration will be modified. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port from which the client isolation profile will be deactivated. |
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be disassociated from the LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/lanPorts/{portId}/clientIsolationProfiles/{clientIsolationProfileId}`

**Activate Client Isolation Profile On AP LAN Port**

Associate a client isolation profile with a LAN port on an AP to enable client isolation exceptions.

operationId: `activateClientIsolationProfileOnApLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the AP is located. |
| `serialNumber` | path | ✓ | `string` | The unique serial number of the access point whose LAN port will be configured. |
| `portId` | path | ✓ | `string` | The unique identifier of the LAN port where the client isolation profile will be activated. |
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be associated with the LAN port. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/clientIsolationProfiles/{clientIsolationProfileId}`

**Deactivate Client Isolation Profile On Wi-Fi Network**

Remove the association between a client isolation profile and a Wi-Fi network without deleting the profile.

operationId: `deactivateClientIsolationProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the Wi-Fi network is located. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the client isolation profile will be deactivated. |
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/wifiNetworks/{wifiNetworkId}/clientIsolationProfiles/{clientIsolationProfileId}`

**Activate Client Isolation Profile On Wi-Fi Network**

Associate a client isolation profile with a Wi-Fi network to enable client isolation exceptions.

operationId: `activateClientIsolationProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the Wi-Fi network is located. |
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the client isolation profile will be activated. |
| `clientIsolationProfileId` | path | ✓ | `string` | The unique identifier of the client isolation profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## IPsec Profile

*Manage IPsec profile lifecycle and associations, including create, update, delete, retrieve, and activate/deactivate profile bindings across tunnel service profiles and SoftGRE targets.*


*6 endpoints*


### `POST` `/ipsecProfiles`

**Add IPsec Profile**

Create an IPsec profile to manage IPsec tunnel configurations with encryption algorithms, authentication methods, and tunnel parameters that can be applied to tunnel service profiles.

operationId: `addIpsecProfile`


**Request Body:** `Wi-Fi_Services_IpsecProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `advancedOption` | `Wi-Fi_Services_IpsecAdvancedOption` |  | Advanced IPSec options including NAT-T, IPComp, DPD, keep-alive, and failover settings. |
| `authType` | `string` |  | The authentication type for the IPSec tunnel. PSK uses pre-shared keys, CERTIFICATE uses X.509 certificates for mutual authentication. |
| `espRekeyTime` | `integer` |  | The time interval for ESP rekeying. Value 0 disables ESP rekeying. Valid range is 0-16384. The unit is determined by espRekeyTimeUnit. |
| `espRekeyTimeUnit` | `string` |  | The time unit for ESP rekeying interval. Used in conjunction with espRekeyTime to determine when ESP keys are regenerated. |
| `espSecurityAssociation` | `Wi-Fi_Services_EspSecurityAssociation` |  | The ESP (Encapsulating Security Payload) security association configuration. This defines encryption and authentication algorithms for IPSec data encryption. |
| `id` | `string` |  |  |
| `ikeRekeyTime` | `integer` |  | The time interval for IKE rekeying. Value 0 disables IKE rekeying. Valid range is 0-16384. The unit is determined by ikeRekeyTimeUnit. |
| `ikeRekeyTimeUnit` | `string` |  | The time unit for IKE rekeying interval. Used in conjunction with ikeRekeyTime to determine when IKE keys are regenerated. |
| `ikeSecurityAssociation` | `Wi-Fi_Services_IkeSecurityAssociation` |  | The IKE (Internet Key Exchange) security association configuration. This defines encryption, authentication, PRF algorithms, and Diffie-Hellman groups for IKE phase 1 negotiations. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ | The unique name of the IPSec profile used for identification and management. Must be between 2 and 32 characters. |
| `preSharedKey` | `string` |  | The pre-shared key used for IPSec authentication when authType is PSK. This key must match the configuration on the IPSec server. |
| `serverAddress` | `string` |  | The IP address, IPv6 address, or hostname of the IPSec server. Can be empty for some tunnel types. Must be a valid IPv4 address, IPv6 address, or fully qualified domain name. |
| `tunnelUsageType` | `string` |  | Tunnel usage type that determines how this IPSec profile is applied and managed in system configuration. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/ipsecProfiles/{ipsecProfileId}`

**Delete IPsec Profile**

Delete an IPsec profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteIpsecProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ipsecProfileId` | path | ✓ | `string` | The unique identifier of the IPsec profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/ipsecProfiles/{ipsecProfileId}`

**Get IPsec Profile**

Retrieve detailed information about a specific IPsec profile by its unique identifier. The response includes all configuration settings, encryption algorithms, authentication methods, and tunnel parameters associated with the profile.

operationId: `getIpsecProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ipsecProfileId` | path | ✓ | `string` | The unique identifier of the IPsec profile. |


**Responses:**

- `200` OK → `Wi-Fi_Services_IpsecProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/ipsecProfiles/{ipsecProfileId}`

**Update IPsec Profile**

Update the configuration of an existing IPsec profile by its unique identifier. This operation allows you to update encryption algorithms, authentication methods, and tunnel parameters while maintaining the profile identity.

operationId: `updateIpsecProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ipsecProfileId` | path | ✓ | `string` | The unique identifier of the IPsec profile. |


**Request Body:** `Wi-Fi_Services_IpsecProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `advancedOption` | `Wi-Fi_Services_IpsecAdvancedOption` |  | Advanced IPSec options including NAT-T, IPComp, DPD, keep-alive, and failover settings. |
| `authType` | `string` |  | The authentication type for the IPSec tunnel. PSK uses pre-shared keys, CERTIFICATE uses X.509 certificates for mutual authentication. |
| `espRekeyTime` | `integer` |  | The time interval for ESP rekeying. Value 0 disables ESP rekeying. Valid range is 0-16384. The unit is determined by espRekeyTimeUnit. |
| `espRekeyTimeUnit` | `string` |  | The time unit for ESP rekeying interval. Used in conjunction with espRekeyTime to determine when ESP keys are regenerated. |
| `espSecurityAssociation` | `Wi-Fi_Services_EspSecurityAssociation` |  | The ESP (Encapsulating Security Payload) security association configuration. This defines encryption and authentication algorithms for IPSec data encryption. |
| `id` | `string` |  |  |
| `ikeRekeyTime` | `integer` |  | The time interval for IKE rekeying. Value 0 disables IKE rekeying. Valid range is 0-16384. The unit is determined by ikeRekeyTimeUnit. |
| `ikeRekeyTimeUnit` | `string` |  | The time unit for IKE rekeying interval. Used in conjunction with ikeRekeyTime to determine when IKE keys are regenerated. |
| `ikeSecurityAssociation` | `Wi-Fi_Services_IkeSecurityAssociation` |  | The IKE (Internet Key Exchange) security association configuration. This defines encryption, authentication, PRF algorithms, and Diffie-Hellman groups for IKE phase 1 negotiations. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ | The unique name of the IPSec profile used for identification and management. Must be between 2 and 32 characters. |
| `preSharedKey` | `string` |  | The pre-shared key used for IPSec authentication when authType is PSK. This key must match the configuration on the IPSec server. |
| `serverAddress` | `string` |  | The IP address, IPv6 address, or hostname of the IPSec server. Can be empty for some tunnel types. Must be a valid IPv4 address, IPv6 address, or fully qualified domain name. |
| `tunnelUsageType` | `string` |  | Tunnel usage type that determines how this IPSec profile is applied and managed in system configuration. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/tunnelServiceProfiles/{tunnelServiceProfileId}/ipsecProfiles/{ipsecProfileId}`

**Deactivate IPsec Profile On The Tunnel Service Profile**

Deactivate the IPsec profile on the tunnel service profile.

operationId: `deactivateIpsecProfileOnVxlanGpeTunnelServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileId` | path | ✓ | `string` | Tunnel Service Profile ID. |
| `ipsecProfileId` | path | ✓ | `string` | The unique identifier of the IPsec profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/tunnelServiceProfiles/{tunnelServiceProfileId}/ipsecProfiles/{ipsecProfileId}`

**Activate IPsec Profile On The Tunnel Service Profile**

Activate the IPsec profile on the tunnel service profile.

operationId: `activateIpsecProfileOnVxlanGpeTunnelServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileId` | path | ✓ | `string` | Tunnel Service Profile ID. |
| `ipsecProfileId` | path | ✓ | `string` | The unique identifier of the IPsec profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## AP Venue

*Manage Wi-Fi venue configuration, including radio settings, mesh, LEDs, LAN ports, and syslog.*


*91 endpoints*


### `GET` `/venues/apAvailableLteBands`

**Get Available LTE Bands**

Retrieve a list of available LTE bands for each region. The response includes all supported LTE frequency bands that can be configured for cellular connectivity on access points.

operationId: `getVenueApAvailableLteBands`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/apModelCapabilities`

**Get Venue All AP model Capabilities**

Retrieve AP model capabilities information for all venues in the system. The response includes detailed feature support information for each AP model available across all venues.

operationId: `getApModelCapabilities`


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelCapabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/lteBands`

**Get Available LTE Bands**

Retrieve a list of available LTE bands for each region. The response includes all supported LTE frequency bands that can be configured for cellular connectivity on access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/apAvailableLteBands can be used for this content.

operationId: `getAvailableLteBands`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/wifiSettings`

**Get Venues Wi-Fi Settings**

Retrieve a paginated list of all venues with their Wi-Fi configuration details. The response includes venue settings, radio configurations, and network parameters for each venue. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadioSettings can be used for this content.

operationId: `getVenuesWifiSettings`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apBssColoringSettings`

**Get Venue Basic Service Set Coloring Settings**

Retrieve basic service set coloring settings configured for this venue. The response includes BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks.

operationId: `getVenueApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose BSS coloring settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApBssColoringSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apBssColoringSettings`

**Update Venue Basic Service Set Coloring Settings**

Update basic service set coloring settings for this venue. This operation allows you to update BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks.

operationId: `updateVenueApBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose BSS coloring settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApBssColoringSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bssColoringEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apCellularSettings`

**Get Venue AP model Cellular**

Retrieve AP model cellular settings and LTE band lock channels configured for this venue. The response includes cellular connectivity configurations and locked LTE frequency bands for access points.

operationId: `getVenueApCellularSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose cellular settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApCellularSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apCellularSettings`

**Update Venue AP model Cellular**

Update AP model cellular settings and LTE band lock channels for this venue.

operationId: `updateVenueApCellularSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose cellular settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApCellularSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `model` | `string` |  |  |
| `primarySim` | `Wi-Fi_Services_SimSettings` |  |  |
| `primaryWanRecoveryTimer` | `integer` | ✓ |  |
| `secondarySim` | `Wi-Fi_Services_SimSettings` |  |  |
| `wanConnection` | `['string', 'null']` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apClientAdmissionControlSettings`

**Get Venue Client Admission Control Settings**

Retrieve client admission control settings configured for this venue. The response includes thresholds and policies that control when new clients are allowed to connect to access points.

operationId: `getVenueApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose client admission control settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApClientAdmissionControlSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apClientAdmissionControlSettings`

**Update Venue Client Admission Control Settings**

Update client admission control settings for this venue. This operation allows you to update thresholds and policies that control when new clients are allowed to connect to access points.

operationId: `updateVenueApClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose client admission control settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApClientAdmissionControlSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `maxRadioLoad24G` | `integer` |  |  |
| `maxRadioLoad50G` | `integer` |  |  |
| `minClientCount24G` | `integer` |  |  |
| `minClientCount50G` | `integer` |  |  |
| `minClientThroughput24G` | `integer` |  |  |
| `minClientThroughput50G` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apDirectedMulticastSettings`

**Get Venue Directed Multicast Settings**

Retrieve directed multicast settings configured for this venue. The response includes multicast optimization configurations that improve efficiency for multicast traffic delivery to clients.

operationId: `getVenueApDirectedMulticastSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose directed multicast settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApDirectedMulticastSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apDirectedMulticastSettings`

**Update Venue Directed Multicast Settings**

Update directed multicast settings for this venue. This operation allows you to update multicast optimization configurations that improve efficiency for multicast traffic delivery to clients.

operationId: `updateVenueApDirectedMulticastSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose directed multicast settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApDirectedMulticastSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkEnabled` | `boolean` |  |  |
| `wiredEnabled` | `boolean` |  |  |
| `wirelessEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apDosProtectionSettings`

**Get Venue DoS Protection**

Retrieve DoS protection settings configured for this venue. The response includes denial-of-service protection configurations and thresholds for access points.

operationId: `getVenueApDosProtectionSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DoS protection settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApDosProtectionSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apDosProtectionSettings`

**Update Venue DoS Protection**

Update DoS protection settings for this venue. This operation allows you to update denial-of-service protection configurations and thresholds for access points.

operationId: `updateVenueApDosProtectionSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DoS protection settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApDosProtectionSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `blockingPeriod` | `integer` |  |  |
| `checkPeriod` | `integer` |  |  |
| `enabled` | `boolean` |  |  |
| `failThreshold` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apLoadBalancingSettings`

**Get Venue Load Balancing Settings**

Retrieve load balancing settings configured for this venue. The response includes client distribution configurations that optimize client connections across access points.

operationId: `getVenueApLoadBalancingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose load balancing settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApLoadBalancingSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apLoadBalancingSettings`

**Update Venue Load Balancing Settings**

Update load balancing settings for this venue. This operation allows you to update client distribution configurations that optimize client connections across access points.

operationId: `updateVenueApLoadBalancingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose load balancing settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApLoadBalancingSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bandBalancingClientPercent24G` | `integer` |  |  |
| `bandBalancingEnabled` | `boolean` |  |  |
| `enabled` | `boolean` |  |  |
| `loadBalancingMethod` | `string` |  |  |
| `steeringMode` | `string` |  |  |
| `stickyClientNbrApPercentageThreshold` | `integer` |  |  |
| `stickyClientSnrThreshold` | `integer` |  |  |
| `stickyClientSteeringEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apManagementTrafficVlanSettings`

**Get Venue AP Management VLAN Settings**

Retrieve AP management traffic VLAN settings configured for this venue. The response includes VLAN configuration used for managing access point traffic and communications.

operationId: `getVenueApManagementVlanSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP management VLAN settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApManagementTrafficVlanSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apManagementTrafficVlanSettings`

**Update Venue AP Management VLAN Settings**

Update AP management traffic VLAN settings for this venue. This operation allows you to update VLAN configuration used for managing access point traffic and communications.

operationId: `updateVenueApManagementVlanSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP management VLAN settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApManagementTrafficVlanSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `vlanId` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apMeshSettings`

**Get Mesh Settings**

Retrieve mesh network settings configured for this venue. The response includes mesh enablement status and configuration parameters for access point mesh networking. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `getVenueApMeshSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose mesh settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApMeshSettingsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apMeshSettings`

**Update Mesh**

Update mesh network settings for this venue. This operation allows you to enable or disable mesh networking and configure mesh parameters for access points. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `updateVenueApMeshSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose mesh settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApMeshSettingsV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `passphrase` | `string` |  |  |
| `radioType` | `string` |  |  |
| `ssid` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelAntennaTypeSettings`

**Get Venue Antenna Type**

Retrieve venue antenna type settings configured for access points. The settings are defined per AP model and specify the antenna configuration used for radio transmissions.

operationId: `getVenueAntennaType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose antenna type settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModelAntennaTypeSettings`

**Update Venue Antenna Type**

Update venue antenna type settings for access points. The settings are defined per AP model and specify the antenna configuration used for radio transmissions.

operationId: `updateVenueAntennaType`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose antenna type settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelBandModeSettings`

**Get Venue Band Mode**

Retrieve venue band mode settings configured for access points. The settings are defined per AP model and control the radio frequency bands available for Wi-Fi operations.

operationId: `getVenueBandMode`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose band mode settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModelBandModeSettings`

**Update Venue Band Mode**

Update venue band mode settings for access points. The settings are defined per AP model and control the radio frequency bands available for Wi-Fi operations.

operationId: `updateVenueBandMode`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose band mode settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelCapabilities`

**Get Venue AP model Capabilities**

Retrieve AP model capabilities information for this venue. The response includes detailed feature support information for each AP model configured in the venue.

operationId: `getVenueAPModelCapabilities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP model capabilities are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelCapabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelExternalAntennaSettings`

**Get Venue AP Model External Antenna Settings**

Retrieve venue external antenna settings configured for access points. The settings are defined per AP model and specify external antenna configurations for radio transmissions.

operationId: `getVenueApModelExternalAntennaSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose external antenna settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModelExternalAntennaSettings`

**Update Venue AP Model External Antenna Settings**

Update venue external antenna settings for access points. The settings are defined per AP model and specify external antenna configurations for radio transmissions.

operationId: `updateVenueApModelExternalAntennaSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose external antenna settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelLanPortSettings`

**Get Venue LAN ports**

Retrieve venue LAN port settings configured for access points. The settings are defined per AP model and control Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /ethernetPortProfiles/query can be used for this content.

operationId: `getVenueApModelLanPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LAN port settings are to be retrieved. |
| `defaultOnly` | query |  | `boolean` | Only get the details of default LAN port settings in this venue. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModelLanPortSettings`

**Update Venue LAN ports**

Update venue LAN port settings for access points. The settings are defined per AP model and control Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId} can be used for this content.

operationId: `updateVenueApModelLanPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LAN port settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelLedSettings`

**Get Venue LED**

Retrieve venue LED indicator settings configured for access points. The settings are defined per AP model and control LED behavior and status indicators.

operationId: `getVenueApModelLedSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LED settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModelLedSettings`

**Update Venue LED**

Update venue LED indicator settings for access points. The settings are defined per AP model and control LED behavior and status indicators.

operationId: `updateVenueApModelLedSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LED settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apModelUsbPortSettings`

**Get Venue USB Port**

Retrieve venue USB port settings configured for access points. The settings are defined per AP model and control USB port configurations and functionality.

operationId: `getVenueApModelUsbPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose USB port settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apModelUsbPortSettings`

**Update Venue USB Port**

Update venue USB port settings for access points. The settings are defined per AP model and control USB port configurations and functionality.

operationId: `updateVenueApModelUsbPortSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose USB port settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apMulticastDnsFencingSettings`

**Get Venue Multicast DNS Fencing Settings**

Retrieve multicast DNS fencing settings configured for access points in this venue. The response includes mDNS isolation configurations that control service discovery across network segments.

operationId: `getVenueApMulticastDnsFencingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose multicast DNS fencing settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApMulticastDnsFencingSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apMulticastDnsFencingSettings`

**Update Venue Multicast DNS Fencing Settings**

Update multicast DNS fencing settings for access points in this venue. This operation allows you to update mDNS isolation configurations that control service discovery across network segments.

operationId: `updateVenueApMulticastDnsFencingSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose multicast DNS fencing settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApMulticastDnsFencingSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apRadioSettings`

**Get Venue Radio**

Retrieve radio settings configured for this venue. The response includes channel selection, power levels, and frequency band configurations for access point radios. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `getVenueApRadioSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose radio settings are to be retrieved. |
| `defaultOnly` | query |  | `boolean` | Only get the details of default radio settings in this venue. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApRadioSettingsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apRadioSettings`

**Update Venue Radio**

Update radio settings for this venue. This operation allows you to update channel selection, power levels, and frequency band configurations for access point radios. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `updateVenueApRadioSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose radio settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApRadioSettingsV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `radioParams24G` | `Wi-Fi_Services_VenueApRadio24GHzSettings` |  |  |
| `radioParams50G` | `Wi-Fi_Services_VenueApRadio5GHzSettings` |  |  |
| `radioParams6G` | `Wi-Fi_Services_VenueApRadio6GHzSettingsV1_1` |  |  |
| `radioParamsDual5G` | `Wi-Fi_Services_VenueApRadioDual5GHzSettings` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apRadiusOptions`

**Get Venue RADIUS Options Settings**

Retrieve RADIUS options settings configured for this venue. The response includes RADIUS authentication and accounting configuration parameters for access points.

operationId: `getVenueApRadiusOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose RADIUS options settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApRadiusOptionSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apRadiusOptions`

**Update Venue RADIUS Options Settings**

Update RADIUS options settings for this venue. This operation allows you to update RADIUS authentication and accounting configuration parameters for access points.

operationId: `updateVenueApRadiusOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose RADIUS options settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApRadiusOptionSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `calledStationIdType` | `string` |  |  |
| `nasIdDelimiter` | `string` |  |  |
| `nasIdType` | `string` |  |  |
| `nasMaxRetry` | `integer` |  |  |
| `nasReconnectPrimaryMin` | `integer` |  |  |
| `nasRequestTimeoutSec` | `integer` |  |  |
| `overrideEnabled` | `boolean` |  |  |
| `singleSessionIdAccounting` | `boolean` |  |  |
| `userDefinedNasId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apRebootTimeoutSettings`

**Get Venue Reboot Timeout Settings**

Retrieve reboot timeout settings configured for this venue. The response includes timeout configurations that control how long access points wait before rebooting during configuration updates or recovery scenarios.

operationId: `getVenueApRebootTimeoutSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose reboot timeout settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApRebootTimeoutSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apRebootTimeoutSettings`

**Update Venue Reboot Timeout Settings**

Update reboot timeout settings for this venue. This operation allows you to update timeout configurations that control how long access points wait before rebooting during configuration updates or recovery scenarios.

operationId: `updateVenueRebootTimeoutSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose reboot timeout settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApRebootTimeoutSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `gatewayLossTimeout` | `integer` |  | The timeout in seconds for rebooting AP if it cannot reach the default gateway. Set to 0 to never reboot. |
| `serverLossTimeout` | `integer` |  | The timeout in seconds for rebooting AP if it cannot reach the controller. Set to 0 to never reboot. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apSmartMonitorSettings`

**Get Venue Smart Monitor Settings**

Retrieve smart monitor settings configured for this venue. The response includes monitoring configurations that enable intelligent network analysis and performance optimization for access points.

operationId: `getVenueApSmartMonitorSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose smart monitor settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApSmartMonitorSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apSmartMonitorSettings`

**Update Venue Smart Monitor Settings**

Update smart monitor settings for this venue. This operation allows you to update monitoring configurations that enable intelligent network analysis and performance optimization for access points.

operationId: `updateVenueSmartMonitorSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose smart monitor settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApSmartMonitorSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `interval` | `integer` |  | The interval in seconds for how often smart monitor checks uplink status. |
| `threshold` | `integer` |  | The retry threshold for turning off the WLANs when connectivity issues are detected. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/apTlsKeyEnhancedSettings`

**Get Venue TLS KEY Settings for APs**

Retrieve transport layer security key enhanced mode settings configured for access points in this venue. The response includes TLS key management configurations that enhance security for AP-to-cloud communications.

operationId: `getVenueApTlsKeyEnhancedModeSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose TLS key enhanced mode settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApTlsKeyEnhancedModeSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/apTlsKeyEnhancedSettings`

**Update Venue TLS KEY Settings for APs**

Update transport layer security key enhanced mode settings for access points in this venue. This operation allows you to update TLS key management configurations that enhance security for AP-to-cloud communications.

operationId: `updateVenueApTlsKeyEnhancedModeSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose TLS key enhanced mode settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApTlsKeyEnhancedModeSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `tlsKeyEnhancedModeEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/aps/capabilities`

**Get Venue AP model Capabilities**

Retrieve AP model capabilities information for this venue. The response includes detailed feature support information for each AP model configured in the venue. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModelCapabilities can be used for this content.

operationId: `getVenueApModelCapabilities`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP model capabilities are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Capabilities`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/bssColoringSettings`

**Get Venue Basic Service Set Coloring Settings**

Retrieve basic service set coloring settings configured for this venue. The response includes BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apBssColoringSettings can be used for this content.

operationId: `getVenueBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose BSS coloring settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_BssColoring`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/bssColoringSettings`

**Update Venue Basic Service Set Coloring Settings**

Update basic service set coloring settings for this venue. This operation allows you to update BSS color configuration used to improve spatial reuse and reduce interference in Wi-Fi 6 networks. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apBssColoringSettings can be used for this content.

operationId: `updateVenueBssColoringSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose BSS coloring settings are to be modified. |


**Request Body:** `Wi-Fi_Services_BssColoring`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bssColoringEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/cellularSettings`

**Get Venue AP model Cellular**

Retrieve AP model cellular settings and LTE band lock channels configured for this venue. The response includes cellular connectivity configurations and locked LTE frequency bands for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apCellularSettings can be used for this content.

operationId: `getVenueApModelCellular`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose cellular settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelCellular`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/cellularSettings`

**Update Venue AP model Cellular**

Update AP model cellular settings and LTE band lock channels for this venue, updating cellular connectivity configurations for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apCellularSettings can be used for this content.

operationId: `updateVenueApModelCellular`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose cellular settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueApModelCellular`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `model` | `string` |  |  |
| `primarySim` | `Wi-Fi_Services_SimSettings` |  |  |
| `primaryWanRecoveryTimer` | `integer` | ✓ |  |
| `secondarySim` | `Wi-Fi_Services_SimSettings` |  |  |
| `wanConnection` | `['string', 'null']` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/channels`

**Get Venue Default Regulatory Channels**

Retrieve default regulatory channels available for this venue based on regulatory domain and country settings. The response includes all supported channels across different frequency bands. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiAvailableChannels can be used for this content.

operationId: `getVenueDefaultRegulatoryChannels`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose default regulatory channels are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRegulatoryChannels`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/clientAdmissionControlSettings`

**Get Venue Client Admission Control Settings**

Retrieve client admission control settings configured for this venue. The response includes thresholds and policies that control when new clients are allowed to connect to access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apClientAdmissionControlSettings can be used for this content.

operationId: `getVenueClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose client admission control settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueClientAdmissionControl`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/clientAdmissionControlSettings`

**Update Venue Client Admission Control Settings**

Update client admission control settings for this venue. This operation allows you to update thresholds and policies that control when new clients are allowed to connect to access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apClientAdmissionControlSettings can be used for this content.

operationId: `updateVenueClientAdmissionControlSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose client admission control settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueClientAdmissionControl`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enable24G` | `boolean` |  |  |
| `enable50G` | `boolean` |  |  |
| `maxRadioLoad24G` | `integer` |  |  |
| `maxRadioLoad50G` | `integer` |  |  |
| `minClientCount24G` | `integer` |  |  |
| `minClientCount50G` | `integer` |  |  |
| `minClientThroughput24G` | `integer` |  |  |
| `minClientThroughput50G` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/dhcpConfigServiceProfileSettings`

**Get DHCP Service Profile Settings of This Venue**

Retrieve DHCP service profile settings configured for this venue. The response includes DHCP service profile associations and IP address pool configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId} can be used for this content.

operationId: `getVenueDhcpConfigServiceProfileSetting`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP service profile settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueDhcpConfigServiceProfileSetting`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/dhcpConfigServiceProfileSettings`

**Update DHCP Service Profile Settings of This Venue**

Update DHCP service profile settings for this venue. This operation allows you to update DHCP service profile associations and IP address pool configurations. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId} can be used for this content.

operationId: `updateVenueDhcpConfigServiceProfileSetting`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP service profile settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueDhcpConfigServiceProfileSetting`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dhcpServiceAps` | `array` |  |  |
| `enabled` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `serviceProfileId` | `string` |  |  |
| `wanPortSelectionMode` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/dhcpPoolLeases`

**Get Venue DHCP Leases**

Retrieve a list of active DHCP leases for this venue. The response includes lease information including IP addresses, MAC addresses, and lease expiration times. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiDhcpClientLeases can be used for this content.

operationId: `getDhcpConfigLeaseByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP leases are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/dhcpPools`

**Get DHCP Pools Usage in Venue**

Retrieve DHCP pool data and usage information for this venue. The response includes pool utilization statistics and allocation details for each configured DHCP pool. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/wifiDhcpPoolUsages can be used for this content.

operationId: `getVenueDhcpPoolUsage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DHCP pool usage is to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/dhcpPools/{dhcpPoolId}`

**Deactivate DHCP Pools in Venue**

Deactivate a DHCP pool for this venue. This operation disables the specified DHCP pool from providing IP address allocation services, allowing it to be reused with other venues. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId} can be used for this content.

operationId: `deactivateVenueDhcpPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the DHCP pool will be deactivated. |
| `dhcpPoolId` | path | ✓ | `string` | The unique identifier of the DHCP pool to be deactivated. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/dhcpPools/{dhcpPoolId}`

**Activate DHCP Pools in Venue**

Activate a DHCP pool for this venue. This operation enables the specified DHCP pool to provide IP address allocation services to clients in the venue. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/dhcpConfigServiceProfiles/{dhcpConfigServiceProfileId} can be used for this content.

operationId: `activateVenueDhcpPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the DHCP pool will be activated. |
| `dhcpPoolId` | path | ✓ | `string` | The unique identifier of the DHCP pool to be activated. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/directedMulticastSettings`

**Get Venue Directed Multicast Settings**

Retrieve directed multicast settings configured for this venue. The response includes multicast optimization configurations that improve efficiency for multicast traffic delivery to clients. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apDirectedMulticastSettings can be used for this content.

operationId: `getVenueDirectedMulticast`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose directed multicast settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueDirectedMulticast`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/directedMulticastSettings`

**Update Venue Directed Multicast Settings**

Update directed multicast settings for this venue. This operation allows you to update multicast optimization configurations that improve efficiency for multicast traffic delivery to clients. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apDirectedMulticastSettings can be used for this content.

operationId: `updateVenueDirectedMulticast`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose directed multicast settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueDirectedMulticast`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `networkEnabled` | `boolean` |  |  |
| `wiredEnabled` | `boolean` |  |  |
| `wirelessEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/dosProtectionSettings`

**Get Venue DoS Protection**

Retrieve DoS protection settings configured for this venue. The response includes denial-of-service protection configurations and thresholds for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apDosProtectionSettings can be used for this content.

operationId: `getDenialOfServiceProtection`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DoS protection settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_DenialOfServiceProtection`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/dosProtectionSettings`

**Update Venue DoS Protection**

Update DoS protection settings for this venue. This operation allows you to update denial-of-service protection configurations and thresholds for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apDosProtectionSettings can be used for this content.

operationId: `updateDenialOfServiceProtection`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose DoS protection settings are to be modified. |


**Request Body:** `Wi-Fi_Services_DenialOfServiceProtection`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `blockingPeriod` | `integer` |  |  |
| `checkPeriod` | `integer` |  |  |
| `enabled` | `boolean` |  |  |
| `failThreshold` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/externalAntennaSettings`

**Get Venue External Antenna**

Retrieve venue external antenna settings configured for access points. The settings are defined per AP model and specify external antenna configurations for radio transmissions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModelExternalAntennaSettings can be used for this content.

operationId: `getVenueExternalAntenna`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose external antenna settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/externalAntennaSettings`

**Update Venue External Antenna**

Update venue external antenna settings for access points. The settings are defined per AP model and specify external antenna configurations for radio transmissions. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModelExternalAntennaSettings can be used for this content.

operationId: `updateVenueExternalAntenna`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose external antenna settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/isolationAllowlists/query`

**Get Venue Client Isolation Allowlists**

Query client isolation allowlists associated with this venue. The response includes a paginated list of allowlists that control client-to-client communication restrictions. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/query can be used for this content.

operationId: `GetClientIsolationAllowlistUsageByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose client isolation allowlists are to be queried. |


**Request Body:** `Wi-Fi_Services_VenueClientIsolationAllowlistQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `sortField` | `string` |  | Sort field support. Only name field is supported. |
| `sortOrder` | `['string', 'null']` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueClientIsolationAllowlistQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/lanPortSettings`

**Get Venue LAN ports**

Retrieve venue LAN port settings configured for access points. The settings are defined per AP model and control Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /ethernetPortProfiles/query can be used for this content.

operationId: `getVenueLanPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LAN port settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/lanPortSettings`

**Update Venue LAN ports**

Update venue LAN port settings for access points. The settings are defined per AP model and control Ethernet port configurations including VLAN assignments and port types. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModels/{apModel}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileId} can be used for this content.

operationId: `updateVenueLanPorts`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LAN port settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/ledSettings`

**Get Venue LED**

Retrieve venue LED indicator settings configured for access points. The settings are defined per AP model and control LED behavior and status indicators. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModelLedSettings can be used for this content.

operationId: `getVenueLed`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LED settings are to be retrieved. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/ledSettings`

**Update Venue LED**

Update venue LED indicator settings for access points. The settings are defined per AP model and control LED behavior and status indicators. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apModelLedSettings can be used for this content.

operationId: `updateVenueLed`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose LED settings are to be modified. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/loadBalancingSettings`

**Get Venue Load Balancing Settings**

Retrieve load balancing settings configured for this venue. The response includes client distribution configurations that optimize client connections across access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apLoadBalancingSettings can be used for this content.

operationId: `getVenueLoadBalancing`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose load balancing settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueLoadBalancing`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/loadBalancingSettings`

**Update Venue Load Balancing Settings**

Update load balancing settings for this venue. This operation allows you to update client distribution configurations that optimize client connections across access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apLoadBalancingSettings can be used for this content.

operationId: `updateVenueLoadBalancing`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose load balancing settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueLoadBalancing`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `bandBalancingClientPercent24G` | `integer` |  |  |
| `bandBalancingEnabled` | `boolean` |  |  |
| `enabled` | `boolean` |  |  |
| `loadBalancingMethod` | `string` |  |  |
| `steeringMode` | `string` |  |  |
| `stickyClientNbrApPercentageThreshold` | `integer` |  |  |
| `stickyClientSnrThreshold` | `integer` |  |  |
| `stickyClientSteeringEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/mDnsFencingSettings`

**Get Multicast DNS Fencing Settings**

Retrieve multicast DNS fencing settings configured for access points in this venue. The response includes mDNS isolation configurations that control service discovery across network segments. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apMulticastDnsFencingSettings can be used for this content.

operationId: `getVenueMulticastDnsFencing`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose multicast DNS fencing settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueMdnsFencing`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/mDnsFencingSettings`

**Update Multicast DNS Fencing Settings**

Update multicast DNS fencing settings for access points in this venue. This operation allows you to update mDNS isolation configurations that control service discovery across network segments. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apMulticastDnsFencingSettings can be used for this content.

operationId: `updateVenueMulticastDnsFencing`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose multicast DNS fencing settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueMdnsFencing`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `services` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/meshSettings`

**Update Mesh**

Update mesh network settings for this venue. This operation allows you to enable or disable mesh networking and configure mesh parameters for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apMeshSettings can be used for this content.

operationId: `updateMesh`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose mesh settings are to be modified. |


**Request Body:** `Wi-Fi_Services_Mesh`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `passphrase` | `string` |  |  |
| `radioType` | `string` |  |  |
| `ssid` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/radioSettings`

**Reset Venue Radio**

Reset venue radio settings to their default values. This operation restores all radio configurations including channel selection, power levels, and frequency band settings to system defaults. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadioSettings can be used for this content.

operationId: `resetVenueRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose radio settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/radioSettings`

**Get Venue Radio**

Retrieve radio settings configured for this venue. The response includes channel selection, power levels, and frequency band configurations for access point radios. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadioSettings can be used for this content.

operationId: `getVenueRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose radio settings are to be retrieved. |
| `defaultOnly` | query |  | `boolean` | Only get the details of default radio settings in this venue. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRadioCustomization`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/radioSettings`

**Update Venue Radio**

Update radio settings for this venue. This operation allows you to update channel selection, power levels, and frequency band configurations for access point radios. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadioSettings can be used for this content.

operationId: `updateVenueRadio`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose radio settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueRadioCustomization`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `radioParams24G` | `Wi-Fi_Services_RadioParams24G` |  |  |
| `radioParams50G` | `Wi-Fi_Services_RadioParams50G` |  |  |
| `radioParams6G` | `Wi-Fi_Services_RadioParams6G` |  |  |
| `radioParamsDual5G` | `Wi-Fi_Services_RadioParamsDual5G` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/radiusOptions`

**Get Venue RADIUS Options Settings**

Retrieve RADIUS options settings configured for this venue. The response includes RADIUS authentication and accounting configuration parameters for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadiusOptions can be used for this content.

operationId: `getVenueRadiusOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose RADIUS options settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRadiusOptions`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/radiusOptions`

**Update Venue RADIUS Options Settings**

Update RADIUS options settings for this venue. This operation allows you to update RADIUS authentication and accounting configuration parameters for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadiusOptions can be used for this content.

operationId: `updateVenueRadiusOptions`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose RADIUS options settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueRadiusOptions`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `calledStationIdType` | `string` |  |  |
| `nasIdDelimiter` | `string` |  |  |
| `nasIdType` | `string` |  |  |
| `nasMaxRetry` | `integer` |  |  |
| `nasReconnectPrimaryMin` | `integer` |  |  |
| `nasRequestTimeoutSec` | `integer` |  |  |
| `overrideEnabled` | `boolean` |  |  |
| `singleSessionIdAccounting` | `boolean` |  |  |
| `userDefinedNasId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/rogueApSettings`

**Get Venue Rogue AP**

Retrieve rogue access point detection settings configured for this venue. Use GET /venues/{venueId}/roguePolicySettings instead. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/roguePolicySettings can be used for this content.

operationId: `getVenueRogueAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose rogue AP settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRogueAp`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/rogueApSettings`

**Update Venue Rogue AP**

Update rogue access point detection settings for this venue. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/roguePolicySettings can be used for this content.

operationId: `updateVenueRogueAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose rogue AP settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueRogueAp`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `reportThreshold` | `integer` |  |  |
| `roguePolicyId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/snmpAgentSettings`

**Get Venue AP SNMP Agent Settings**

Retrieve AP SNMP agent settings configured for this venue. The response includes SNMP monitoring and management configurations for access points. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/query can be used for this content.

operationId: `getVenueApSnmpAgent`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP SNMP agent settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueSnmpAgent`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/snmpAgentSettings`

**Update Venue AP SNMP Agent Settings**

Update AP SNMP agent settings for this venue. This operation allows you to update SNMP monitoring and management configurations for access points.

operationId: `updateVenueApSnmpAgent`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose AP SNMP agent settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueSnmpAgent`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `apSnmpAgentProfileId` | `string` |  |  |
| `enableApSnmp` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/syslogServerProfileSettings`

**Get Venue Syslog Server Profile Settings**

Retrieve syslog server profile settings configured for this venue. The response includes syslog server profile associations and logging configurations for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/query can be used for this content.

operationId: `getVenueSyslogServerProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose syslog server profile settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueSyslogServerProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/venues/{venueId}/syslogServerProfileSettings`

**Update Venue Syslog Server Profile Settings**

Update syslog server profile settings for this venue. This operation allows you to update syslog server profile associations and logging configurations for access points. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/syslogServerProfiles/{syslogServerProfileId} can be used for this content.

operationId: `updateVenueSyslogServerProfileSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose syslog server profile settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueSyslogServerProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `serviceProfileId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/syslogSettings`

**Reset Venue Syslog**

Reset venue syslog settings to their default values. This operation restores all syslog server configurations and logging parameters to system defaults. This method will be removed no sooner than 06/30/2026. The following URL /syslogServerProfiles/{syslogServerProfileId} can be used for this content.

operationId: `resetVenueSyslog`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose syslog settings are to be reset. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/syslogSettings`

**Get Venue Syslog**

Retrieve syslog server settings configured for this venue. The response includes syslog server configurations and logging parameters for access points. This method will be removed no sooner than 06/30/2026. The following URL /syslogServerProfiles/query can be used for this content.

operationId: `getVenueSyslog`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose syslog settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueSyslog`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/syslogSettings`

**Update Venue Syslog**

Update syslog server settings for this venue. This operation allows you to update syslog server configurations and logging parameters for access points. This method will be removed no sooner than 06/30/2026. The following URL /syslogServerProfiles/{syslogServerProfileId} can be used for this content.

operationId: `updateVenueSyslog`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose syslog settings are to be modified. |


**Request Body:** `Wi-Fi_Services_VenueSyslog`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enabled` | `boolean` |  |  |
| `facility` | `string` |  |  |
| `flowLevel` | `string` |  |  |
| `port` | `integer` |  |  |
| `priority` | `string` |  |  |
| `protocol` | `string` |  |  |
| `secondaryPort` | `integer` |  |  |
| `secondaryProtocol` | `string` |  |  |
| `secondaryServer` | `string` |  |  |
| `server` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/wifiAvailableChannels`

**Get Venue Available Channels**

Retrieve available Wi-Fi channels for this venue based on regulatory domain and country settings. The response includes all supported channels across different frequency bands. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. Both application/json and application/vnd.ruckus.v1.1+json are now available.

operationId: `getWifiAvailableChannelsOfVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose available channels are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_WifiAvailableChannelsV1_1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/wifiSettings`

**Get Venue Wi-Fi Settings**

Retrieve detailed Wi-Fi configuration information for a specific venue. The response includes all venue settings, radio configurations, and network parameters. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/apRadioSettings can be used for this content.

operationId: `getVenueWifiSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue whose Wi-Fi settings are to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_Venue`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## VRIoT Management

*Manage VRIoT with venue or AP.*


*4 endpoints*


### `DELETE` `/venues/{venueId}/aps/{serialNumber}/iotControllers/{iotControllerId}`

**Disassociate IoT Controller from AP**

Remove the association between a VRIoT controller and an AP without deleting the controller.

operationId: `disassociateIotControllerFromAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP where the IoT controller will be disassociated. |
| `iotControllerId` | path | ✓ | `string` | The unique identifier of the IoT controller to be disassociated from the AP. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{serialNumber}/iotControllers/{iotControllerId}`

**Associate IoT Controller with AP**

Associate a VRIoT controller with a specific AP to enable IoT device management and monitoring on the AP.

operationId: `associateIotControllerWithAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue containing the AP. |
| `serialNumber` | path | ✓ | `string` | The serial number of the AP where the IoT controller will be associated. |
| `iotControllerId` | path | ✓ | `string` | The unique identifier of the IoT controller to be associated with the AP. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/iotControllers/{iotControllerId}`

**Disassociate IoT Controller from Venue**

Remove the association between a VRIoT controller and a venue without deleting the controller.

operationId: `disassociateIotControllerFromVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the IoT controller will be disassociated. |
| `iotControllerId` | path | ✓ | `string` | The unique identifier of the IoT controller to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/iotControllers/{iotControllerId}`

**Associate IoT Controller with Venue**

Associate a VRIoT controller with a venue to enable IoT device management and monitoring on all APs in the venue.

operationId: `associateIotControllerWithVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the IoT controller will be associated. |
| `iotControllerId` | path | ✓ | `string` | The unique identifier of the IoT controller to be associated with the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Tunnel Service Profile

*Manage tunnel service profiles.*


*5 endpoints*


### `POST` `/tunnelServiceProfiles`

**Add Tunnel Service Profile**

Create a new tunnel service profile with tunnel type, destination IP, MTU, NAT traversal, and keep-alive parameters.

operationId: `createTunnelServiceProfile`


**Request Body:** `Wi-Fi_Services_TunnelServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ageTimeMinutes` | `integer` |  | The aging time in minutes for tunnel entries. After this time period, inactive tunnel entries will be removed. Valid range is 5 to 10080 minutes (7 days). |
| `destinationIpAddress` | `string` |  | The destination IP address for the tunnel endpoint. Must be a valid IPv4 address in dotted-decimal notation. |
| `forceFragmentation` | `boolean` |  | When enabled, forces packet fragmentation for tunnel traffic. This ensures that packets exceeding the MTU size are fragmented before transmission, preventing packet loss in networks with smaller MTU sizes. |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `keepAliveInterval` | `integer` |  | The time interval in seconds between keep-alive packets sent to maintain the tunnel connection. Valid range is 1 to 5 seconds, default is 2 seconds. |
| `keepAliveRetry` | `integer` |  | The number of keep-alive retry attempts before considering the tunnel connection as failed, default is 5 retries. Valid range depends on the tunnel type: 3 to 10 retries for `VXLAN_GPE`, and 3 to 5 retries for `L2GRE`. |
| `mtuRequestRetry` | `integer` |  | This setting is only effective in path maximum transmission unit auto mode. |
| `mtuRequestTimeout` | `integer` |  | The unit is milliseconds. This setting is only effective in path maximum transmission unit auto mode. |
| `mtuSize` | `integer` |  | The MTU (Maximum Transmission Unit) size in bytes for the tunnel when the MTU type is set to `MANUAL`. This determines the maximum packet size that can be transmitted through the tunnel. Valid range is 1280 to 1450 bytes. |
| `mtuType` | `string` |  | The MTU (Maximum Transmission Unit) type for the tunnel. The `AUTO` mode automatically determines the optimal MTU size, while MANUAL mode allows manual configuration of the MTU size. |
| `name` | `string` | ✓ | The unique name of the tunnel service profile used for identification and management. The name must be between 2 and 32 characters and cannot contain backticks or dollar signs with parentheses. |
| `natTraversalEnabled` | `boolean` |  | For toggling whether NAT traversal support is needed for the tunnel. |
| `tag` | `string` |  |  |
| `tunnelType` | `string` |  | The tunnel encapsulation protocol type using VXLAN-GPE (Generic Protocol Extension for VXLAN) or VXLAN (Virtual Extensible LAN). |
| `type` | `string` |  | The tunnel network segmentation type determining how traffic is segmented. Options include VXLAN for Layer 2 extension or VLAN_VXLAN for VLAN based VxLAN segmentation. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/tunnelServiceProfiles/{tunnelServiceProfileId}`

**Delete Tunnel Service Profile**

Remove a tunnel service profile by its unique identifier. This operation permanently deletes the profile and its associated configurations. Ensure the profile is not actively in use before deletion.

operationId: `deleteTunnelServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileId` | path | ✓ | `string` | The unique identifier of the tunnel service profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/tunnelServiceProfiles/{tunnelServiceProfileId}`

**Get Tunnel Service Profile**

Retrieve detailed information about a tunnel service profile including tunnel type, IP address, MTU, and NAT settings.

operationId: `getTunnelServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileId` | path | ✓ | `string` | The unique identifier of the tunnel service profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_TunnelServiceProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/tunnelServiceProfiles/{tunnelServiceProfileId}`

**Partial Update Tunnel Service Profile**

Partially modifies specific fields of an existing tunnel service profile without affecting other configuration settings.

operationId: `patchTunnelServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileId` | path | ✓ | `string` | The unique identifier of the tunnel service profile to be partially updated. |


**Request Body:** `Wi-Fi_Services_TunnelServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ageTimeMinutes` | `integer` |  | The aging time in minutes for tunnel entries. After this time period, inactive tunnel entries will be removed. Valid range is 5 to 10080 minutes (7 days). |
| `destinationIpAddress` | `string` |  | The destination IP address for the tunnel endpoint. Must be a valid IPv4 address in dotted-decimal notation. |
| `forceFragmentation` | `boolean` |  | When enabled, forces packet fragmentation for tunnel traffic. This ensures that packets exceeding the MTU size are fragmented before transmission, preventing packet loss in networks with smaller MTU sizes. |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `keepAliveInterval` | `integer` |  | The time interval in seconds between keep-alive packets sent to maintain the tunnel connection. Valid range is 1 to 5 seconds, default is 2 seconds. |
| `keepAliveRetry` | `integer` |  | The number of keep-alive retry attempts before considering the tunnel connection as failed, default is 5 retries. Valid range depends on the tunnel type: 3 to 10 retries for `VXLAN_GPE`, and 3 to 5 retries for `L2GRE`. |
| `mtuRequestRetry` | `integer` |  | This setting is only effective in path maximum transmission unit auto mode. |
| `mtuRequestTimeout` | `integer` |  | The unit is milliseconds. This setting is only effective in path maximum transmission unit auto mode. |
| `mtuSize` | `integer` |  | The MTU (Maximum Transmission Unit) size in bytes for the tunnel when the MTU type is set to `MANUAL`. This determines the maximum packet size that can be transmitted through the tunnel. Valid range is 1280 to 1450 bytes. |
| `mtuType` | `string` |  | The MTU (Maximum Transmission Unit) type for the tunnel. The `AUTO` mode automatically determines the optimal MTU size, while MANUAL mode allows manual configuration of the MTU size. |
| `name` | `string` | ✓ | The unique name of the tunnel service profile used for identification and management. The name must be between 2 and 32 characters and cannot contain backticks or dollar signs with parentheses. |
| `natTraversalEnabled` | `boolean` |  | For toggling whether NAT traversal support is needed for the tunnel. |
| `tag` | `string` |  |  |
| `tunnelType` | `string` |  | The tunnel encapsulation protocol type using VXLAN-GPE (Generic Protocol Extension for VXLAN) or VXLAN (Virtual Extensible LAN). |
| `type` | `string` |  | The tunnel network segmentation type determining how traffic is segmented. Options include VXLAN for Layer 2 extension or VLAN_VXLAN for VLAN based VxLAN segmentation. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/tunnelServiceProfiles/{tunnelServiceProfileId}`

**Update Tunnel Service Profile**

Update an existing tunnel service profile including tunnel type, destination IP, MTU, NAT traversal, and keep-alive parameters.

operationId: `updateTunnelServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileId` | path | ✓ | `string` | The unique identifier of the tunnel service profile to be modified. |


**Request Body:** `Wi-Fi_Services_TunnelServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ageTimeMinutes` | `integer` |  | The aging time in minutes for tunnel entries. After this time period, inactive tunnel entries will be removed. Valid range is 5 to 10080 minutes (7 days). |
| `destinationIpAddress` | `string` |  | The destination IP address for the tunnel endpoint. Must be a valid IPv4 address in dotted-decimal notation. |
| `forceFragmentation` | `boolean` |  | When enabled, forces packet fragmentation for tunnel traffic. This ensures that packets exceeding the MTU size are fragmented before transmission, preventing packet loss in networks with smaller MTU sizes. |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `keepAliveInterval` | `integer` |  | The time interval in seconds between keep-alive packets sent to maintain the tunnel connection. Valid range is 1 to 5 seconds, default is 2 seconds. |
| `keepAliveRetry` | `integer` |  | The number of keep-alive retry attempts before considering the tunnel connection as failed, default is 5 retries. Valid range depends on the tunnel type: 3 to 10 retries for `VXLAN_GPE`, and 3 to 5 retries for `L2GRE`. |
| `mtuRequestRetry` | `integer` |  | This setting is only effective in path maximum transmission unit auto mode. |
| `mtuRequestTimeout` | `integer` |  | The unit is milliseconds. This setting is only effective in path maximum transmission unit auto mode. |
| `mtuSize` | `integer` |  | The MTU (Maximum Transmission Unit) size in bytes for the tunnel when the MTU type is set to `MANUAL`. This determines the maximum packet size that can be transmitted through the tunnel. Valid range is 1280 to 1450 bytes. |
| `mtuType` | `string` |  | The MTU (Maximum Transmission Unit) type for the tunnel. The `AUTO` mode automatically determines the optimal MTU size, while MANUAL mode allows manual configuration of the MTU size. |
| `name` | `string` | ✓ | The unique name of the tunnel service profile used for identification and management. The name must be between 2 and 32 characters and cannot contain backticks or dollar signs with parentheses. |
| `natTraversalEnabled` | `boolean` |  | For toggling whether NAT traversal support is needed for the tunnel. |
| `tag` | `string` |  |  |
| `tunnelType` | `string` |  | The tunnel encapsulation protocol type using VXLAN-GPE (Generic Protocol Extension for VXLAN) or VXLAN (Virtual Extensible LAN). |
| `type` | `string` |  | The tunnel network segmentation type determining how traffic is segmented. Options include VXLAN for Layer 2 extension or VLAN_VXLAN for VLAN based VxLAN segmentation. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## IPsec Profile Template

*Manage IPsec profile templates.*


*6 endpoints*


### `POST` `/templates/ipsecProfiles`

**Add IPsec Profile Template**

Create an IPsec profile MSP template with encryption algorithms and authentication methods for tunnel service profile templates.

operationId: `addIpsecProfileTemplate`


**Request Body:** `Wi-Fi_Services_IpsecProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `advancedOption` | `Wi-Fi_Services_IpsecAdvancedOption` |  | Advanced IPSec options including NAT-T, IPComp, DPD, keep-alive, and failover settings. |
| `authType` | `string` |  | The authentication type for the IPSec tunnel. PSK uses pre-shared keys, CERTIFICATE uses X.509 certificates for mutual authentication. |
| `espRekeyTime` | `integer` |  | The time interval for ESP rekeying. Value 0 disables ESP rekeying. Valid range is 0-16384. The unit is determined by espRekeyTimeUnit. |
| `espRekeyTimeUnit` | `string` |  | The time unit for ESP rekeying interval. Used in conjunction with espRekeyTime to determine when ESP keys are regenerated. |
| `espSecurityAssociation` | `Wi-Fi_Services_EspSecurityAssociation` |  | The ESP (Encapsulating Security Payload) security association configuration. This defines encryption and authentication algorithms for IPSec data encryption. |
| `id` | `string` |  |  |
| `ikeRekeyTime` | `integer` |  | The time interval for IKE rekeying. Value 0 disables IKE rekeying. Valid range is 0-16384. The unit is determined by ikeRekeyTimeUnit. |
| `ikeRekeyTimeUnit` | `string` |  | The time unit for IKE rekeying interval. Used in conjunction with ikeRekeyTime to determine when IKE keys are regenerated. |
| `ikeSecurityAssociation` | `Wi-Fi_Services_IkeSecurityAssociation` |  | The IKE (Internet Key Exchange) security association configuration. This defines encryption, authentication, PRF algorithms, and Diffie-Hellman groups for IKE phase 1 negotiations. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ | The unique name of the IPSec profile used for identification and management. Must be between 2 and 32 characters. |
| `preSharedKey` | `string` |  | The pre-shared key used for IPSec authentication when authType is PSK. This key must match the configuration on the IPSec server. |
| `serverAddress` | `string` |  | The IP address, IPv6 address, or hostname of the IPSec server. Can be empty for some tunnel types. Must be a valid IPv4 address, IPv6 address, or fully qualified domain name. |
| `tunnelUsageType` | `string` |  | Tunnel usage type that determines how this IPSec profile is applied and managed in system configuration. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/ipsecProfiles/{ipsecProfileTemplateId}`

**Delete IPsec Profile Template**

Delete an IPsec profile MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteIpsecProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ipsecProfileTemplateId` | path | ✓ | `string` | The unique identifier of the IPsec profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/ipsecProfiles/{ipsecProfileTemplateId}`

**Get IPsec Profile Template**

Retrieve detailed information about an IPsec profile MSP template by its unique identifier including encryption algorithms and authentication methods.

operationId: `getIpsecProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ipsecProfileTemplateId` | path | ✓ | `string` | The unique identifier of the IPsec profile MSP template. |


**Responses:**

- `200` OK → `Wi-Fi_Services_IpsecProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/ipsecProfiles/{ipsecProfileTemplateId}`

**Update IPsec Profile Template**

Update an existing IPsec profile MSP template by its unique identifier, updating encryption algorithms, authentication methods, and tunnel parameters.

operationId: `updateIpsecProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ipsecProfileTemplateId` | path | ✓ | `string` | The unique identifier of the IPsec profile MSP template. |


**Request Body:** `Wi-Fi_Services_IpsecProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `advancedOption` | `Wi-Fi_Services_IpsecAdvancedOption` |  | Advanced IPSec options including NAT-T, IPComp, DPD, keep-alive, and failover settings. |
| `authType` | `string` |  | The authentication type for the IPSec tunnel. PSK uses pre-shared keys, CERTIFICATE uses X.509 certificates for mutual authentication. |
| `espRekeyTime` | `integer` |  | The time interval for ESP rekeying. Value 0 disables ESP rekeying. Valid range is 0-16384. The unit is determined by espRekeyTimeUnit. |
| `espRekeyTimeUnit` | `string` |  | The time unit for ESP rekeying interval. Used in conjunction with espRekeyTime to determine when ESP keys are regenerated. |
| `espSecurityAssociation` | `Wi-Fi_Services_EspSecurityAssociation` |  | The ESP (Encapsulating Security Payload) security association configuration. This defines encryption and authentication algorithms for IPSec data encryption. |
| `id` | `string` |  |  |
| `ikeRekeyTime` | `integer` |  | The time interval for IKE rekeying. Value 0 disables IKE rekeying. Valid range is 0-16384. The unit is determined by ikeRekeyTimeUnit. |
| `ikeRekeyTimeUnit` | `string` |  | The time unit for IKE rekeying interval. Used in conjunction with ikeRekeyTime to determine when IKE keys are regenerated. |
| `ikeSecurityAssociation` | `Wi-Fi_Services_IkeSecurityAssociation` |  | The IKE (Internet Key Exchange) security association configuration. This defines encryption, authentication, PRF algorithms, and Diffie-Hellman groups for IKE phase 1 negotiations. |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ | The unique name of the IPSec profile used for identification and management. Must be between 2 and 32 characters. |
| `preSharedKey` | `string` |  | The pre-shared key used for IPSec authentication when authType is PSK. This key must match the configuration on the IPSec server. |
| `serverAddress` | `string` |  | The IP address, IPv6 address, or hostname of the IPSec server. Can be empty for some tunnel types. Must be a valid IPv4 address, IPv6 address, or fully qualified domain name. |
| `tunnelUsageType` | `string` |  | Tunnel usage type that determines how this IPSec profile is applied and managed in system configuration. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/tunnelServiceProfiles/{tunnelServiceProfileTemplateId}/ipsecProfiles/{ipsecProfileTemplateId}`

**Deactivate Ipsec Profile Template On Tunnel Service Profile Template**

Remove the association between an IPsec profile MSP template and a tunnel service profile MSP template without deleting the template.

operationId: `deactivateIpsecProfileTemplateOnTunnelServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileTemplateId` | path | ✓ | `string` |  |
| `ipsecProfileTemplateId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/tunnelServiceProfiles/{tunnelServiceProfileTemplateId}/ipsecProfiles/{ipsecProfileTemplateId}`

**Activate Ipsec Profile Template On Tunnel Service Profile Template**

Associate an IPsec profile MSP template with a tunnel service profile MSP template to enable IPsec encryption for tunnel communications.

operationId: `activateIpsecProfileTemplateOnTunnelServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileTemplateId` | path | ✓ | `string` |  |
| `ipsecProfileTemplateId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Device Policy

*Manage device policies.*


*10 endpoints*


### `DELETE` `/accessControlProfiles/{accessControlProfileId}/devicePolicies/{devicePolicyId}`

**Deactivate Device Policy On Access Control Profile**

Remove the association between a device policy and an access control profile without deleting the policy.

operationId: `deactivateDevicePolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile from which the device policy will be deactivated. |
| `devicePolicyId` | path | ✓ | `string` | The unique identifier of the device policy to be disassociated from the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/accessControlProfiles/{accessControlProfileId}/devicePolicies/{devicePolicyId}`

**Activate Device Policy On Access Control Profile**

Associate a device policy with an access control profile to enforce device access control policies.

operationId: `activateDevicePolicyOnAccessControlProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `accessControlProfileId` | path | ✓ | `string` | The unique identifier of the access control profile where the device policy will be activated. |
| `devicePolicyId` | path | ✓ | `string` | The unique identifier of the device policy to be associated with the access control profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/devicePolicies`

**Delete Device Policies**

Perform a batch deletion of multiple device policies by providing a list of policy identifiers. This operation permanently removes all specified policies and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /devicePolicies/{devicePolicyId} can be used for this content.

operationId: `deleteDevicePoliciesBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/devicePolicies`

**Get All Device Policies**

Retrieve a complete list of all device policies configured in the system. The response includes all policies that define device access control rules and network policies. This method will be removed no sooner than 06/30/2026. The following URL /devicePolicies/query can be used for this content.

operationId: `getAllDevicePolicies`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/devicePolicies`

**Create Device Policy**

Create a device policy with rules based on device types and operating systems for access control. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `addDevicePolicy`


**Request Body:** `Wi-Fi_Services_DevicePolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_DevicePolicyOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/devicePolicies/{devicePolicyId}`

**Delete Device Policy**

Delete a device policy by its unique identifier, permanently deleting the policy and its configurations.

operationId: `deleteDevicePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `devicePolicyId` | path | ✓ | `string` | The unique identifier of the device policy to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/devicePolicies/{devicePolicyId}`

**Get Device Policy**

Retrieve detailed information about a specific device policy by its unique identifier. The response includes all configuration settings, rules, and policies associated with the policy. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `getDevicePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `devicePolicyId` | path | ✓ | `string` | The unique identifier of the device policy to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_DevicePolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/devicePolicies/{devicePolicyId}`

**Update Device Policy**

Update an existing device policy by its unique identifier, updating rules, policies, and settings. The application/vnd.ruckus.v1+json will be removed no sooner than 06/30/2026. The application/json is currently tied to application/vnd.ruckus.v1+json and will be moved to application/vnd.ruckus.v1.1+json on 06/30/2026.

operationId: `updateDevicePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `devicePolicyId` | path | ✓ | `string` | The unique identifier of the device policy to be modified. |


**Request Body:** `Wi-Fi_Services_DevicePolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `defaultAccess` | `string` |  |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/wifiNetworks/{wifiNetworkId}/devicePolicies/{policyId}`

**Deactivate Device Policy On Wi-Fi Network**

Remove the association between a device policy and a Wi-Fi network without deleting the policy.

operationId: `deactivateDevicePolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the device policy will be deactivated. |
| `policyId` | path | ✓ | `string` | The unique identifier of the device policy to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/devicePolicies/{policyId}`

**Activate Device Policy On Wi-Fi Network**

Associate a device policy with a Wi-Fi network to enforce device access control policies.

operationId: `activateDevicePolicyOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the device policy will be activated. |
| `policyId` | path | ✓ | `string` | The unique identifier of the device policy to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## MDNS Proxy Service Profile

*Manage Multicast DNS proxy service profiles.*


*15 endpoints*


### `DELETE` `/mDnsProxyServiceProfiles`

**Delete Multicast DNS Proxy Service Profiles**

Perform a batch deletion of multiple multicast DNS proxy service profiles by providing a list of profile identifiers. This operation permanently removes all specified profiles and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/{multicastDnsProxyProfileId} can be used for this content.

operationId: `deleteMulticastDnsProxyServiceProfilesBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/mDnsProxyServiceProfiles`

**Get Multicast DNS Proxy Service Profiles**

Retrieve a complete list of all multicast DNS proxy service profiles configured in the system. The response includes general profile information and configuration settings for each profile. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/query can be used for this content.

operationId: `getMulticastDnsProxyServiceProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/mDnsProxyServiceProfiles`

**Create Multicast DNS Proxy Service Profile**

Create a multicast DNS proxy service profile to manage mDNS traffic across different VLANs with specific rules to allow or deny mDNS service discovery. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles can be used for this content.

operationId: `createMulticastDnsProxyServiceProfile`


**Request Body:** `Wi-Fi_Services_MulticastDnsProxyServiceProfileRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `aps` | `array` |  |  |
| `id` | `string` |  |  |
| `rules` | `array` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/mDnsProxyServiceProfiles/{mDnsProxyProfileId}`

**Delete Multicast DNS Proxy Service Profile**

Delete a multicast DNS proxy service profile by its unique identifier, permanently deleting the profile and its configurations. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/{multicastDnsProxyProfileId} can be used for this content.

operationId: `deleteMulticastDnsProxyServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/mDnsProxyServiceProfiles/{mDnsProxyProfileId}`

**Get Multicast DNS Proxy Service Profile**

Retrieve detailed information about a specific multicast DNS proxy service profile by its unique identifier. The response includes all configured rules and settings for proxying mDNS traffic. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/{multicastDnsProxyProfileId} can be used for this content.

operationId: `getMulticastDnsProxyServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile. |


**Responses:**

- `200` OK → `Wi-Fi_Services_MulticastDnsProxyServiceProfileResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/mDnsProxyServiceProfiles/{mDnsProxyProfileId}`

**Update Multicast DNS Proxy Service Profile**

Update the configuration of an existing multicast DNS proxy service profile by its unique identifier. This operation allows you to update rules and settings while maintaining the profile identity. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/{multicastDnsProxyProfileId} can be used for this content.

operationId: `updateMulticastDnsProxyServiceProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile. |


**Request Body:** `Wi-Fi_Services_MulticastDnsProxyServiceProfileRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `aps` | `array` |  |  |
| `id` | `string` |  |  |
| `rules` | `array` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/mDnsProxyServiceProfiles/{mDnsProxyProfileId}/aps`

**Deactivate Multicast DNS Proxy Service Profile for APs**

Deactivate a multicast DNS proxy service profile on multiple access points without deleting the profile. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{apSerialNumber}/multicastDnsProxyProfiles/{multicastDnsProxyProfileId} can be used for this content.

operationId: `deactivateMulticastDnsProxyServiceProfileAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/mDnsProxyServiceProfiles/{mDnsProxyProfileId}/aps`

**Activate Multicast DNS Proxy Service Profile for APs**

Activate a multicast DNS proxy service profile on multiple access points to enable mDNS traffic proxying and service discovery for clients. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/aps/{apSerialNumber}/multicastDnsProxyProfiles/{multicastDnsProxyProfileId} can be used for this content.

operationId: `activateMulticastDnsProxyServiceProfileAp`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/multicastDnsProxyProfiles`

**Create Multicast DNS Proxy Service Profile**

Create a multicast DNS proxy service profile to enable mDNS service discovery and proxy functionality across VLANs for access points.

operationId: `createMulticastDnsProxyProfile`


**Request Body:** `Wi-Fi_Services_MulticastDnsProxyProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `rules` | `array` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/multicastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Delete Multicast DNS Proxy Service Profile**

Delete a multicast DNS proxy service profile by its unique identifier, permanently deleting the profile and its configurations.

operationId: `deleteMulticastDnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/multicastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Get Multicast DNS Proxy Service Profile**

Retrieve detailed information about a specific multicast DNS proxy service profile by its unique identifier. The response includes all configured service rules, service names, and other profile settings.

operationId: `getMulticastDnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_MulticastDnsProxyProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/multicastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Update Multicast DNS Proxy Service Profile**

Update an existing multicast DNS proxy service profile by its unique identifier, updating service rules, service names, and other profile settings.

operationId: `updateMulticastDnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile to be modified. |


**Request Body:** `Wi-Fi_Services_MulticastDnsProxyProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `id` | `string` |  |  |
| `rules` | `array` |  |  |
| `serviceName` | `string` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/aps/{apSerialNumber}/multicastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Deactivate Multicast DNS Proxy Service Profile On the AP**

Remove the association between a multicast DNS proxy service profile and an access point without deleting the profile.

operationId: `deactivateMulticastDnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point is located. |
| `apSerialNumber` | path | ✓ | `string` | The serial number of the access point from which the multicast DNS proxy service profile will be deactivated. |
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile to be disassociated from the access point. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/aps/{apSerialNumber}/multicastDnsProxyProfiles/{multicastDnsProxyProfileId}`

**Activate Multicast DNS Proxy Service Profile On the AP**

Associate a multicast DNS proxy service profile with an access point to enable mDNS service discovery and proxy functionality across VLANs.

operationId: `activateMulticastDnsProxyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the access point is located. |
| `apSerialNumber` | path | ✓ | `string` | The serial number of the access point where the multicast DNS proxy service profile will be activated. |
| `multicastDnsProxyProfileId` | path | ✓ | `string` | The unique identifier of the multicast DNS proxy service profile to be associated with the access point. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/mDnsProxyProfileAps`

**Get Multicast DNS Proxy Service Profile APs by Venue**

Retrieve multicast DNS proxy service profile activation details for access points within a venue including their mDNS proxy configurations. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/query can be used for this content.

operationId: `getMulticastDnsProxyServiceProfileApByVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue. |


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Ethernet Port Profile Template

*Manage ethernet port profiles templates.*


*10 endpoints*


### `POST` `/templates/ethernetPortProfiles`

**Create Ethernet Port Profile Template**

Create an Ethernet port profile MSP template to manage port configurations with VLAN assignments and port types for AP LAN ports.

operationId: `createEthernetPortProfileTemplate`


**Request Body:** `Wi-Fi_Services_EthernetPortProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authType` | `string` |  |  |
| `bypassMacAddressAuthentication` | `boolean` |  |  |
| `dynamicVlanEnabled` | `boolean` |  |  |
| `enableAccountingProxy` | `boolean` |  |  |
| `enableAuthProxy` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `supplicantAuthenticationOptions` | `Wi-Fi_Services_SupplicantAuthenticationOptions` |  |  |
| `type` | `['string', 'null']` | ✓ |  |
| `unauthenticatedGuestVlan` | `integer` |  |  |
| `untagId` | `integer` |  |  |
| `vlanMembers` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/ethernetPortProfiles/{ethernetPortProfileTemplateId}`

**Delete Ethernet Port Profile Template**

Delete an Ethernet port profile MSP template by its unique identifier, permanently deleting the template and its configurations.

operationId: `deleteEthernetPortProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileTemplateId` | path | ✓ | `string` | The unique identifier of the Ethernet port profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/ethernetPortProfiles/{ethernetPortProfileTemplateId}`

**Get Ethernet Port Profile Template**

Retrieve detailed information about an Ethernet port profile MSP template by its unique identifier including VLAN assignments and port type configurations.

operationId: `getEthernetPortProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileTemplateId` | path | ✓ | `string` | The unique identifier of the Ethernet port profile MSP template. |


**Responses:**

- `200` OK → `Wi-Fi_Services_EthernetPortProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/ethernetPortProfiles/{ethernetPortProfileTemplateId}`

**Update Ethernet Port Profile Template**

Update an existing Ethernet port profile MSP template by its unique identifier, updating VLAN assignments, port types, and other settings.

operationId: `updateEthernetPortProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `ethernetPortProfileTemplateId` | path | ✓ | `string` | The unique identifier of the Ethernet port profile MSP template. |


**Request Body:** `Wi-Fi_Services_EthernetPortProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authType` | `string` |  |  |
| `bypassMacAddressAuthentication` | `boolean` |  |  |
| `dynamicVlanEnabled` | `boolean` |  |  |
| `enableAccountingProxy` | `boolean` |  |  |
| `enableAuthProxy` | `boolean` |  |  |
| `id` | `string` |  |  |
| `isDefault` | `boolean` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `supplicantAuthenticationOptions` | `Wi-Fi_Services_SupplicantAuthenticationOptions` |  |  |
| `type` | `['string', 'null']` | ✓ |  |
| `unauthenticatedGuestVlan` | `integer` |  |  |
| `untagId` | `integer` |  |  |
| `vlanMembers` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueTemplateId}/apModels/{apModel}/lanPortSpecificSettings`

**Get Venue Template AP Model LAN Port Specific Settings**

Get venue template AP model LAN port specific settings.

operationId: `getVenueTemplateApModelLanPortSpecificSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template. |
| `apModel` | path | ✓ | `string` | The model name of the AP. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelLanPortSpecificSettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/apModels/{apModel}/lanPortSpecificSettings`

**Update Venue Template AP Model LAN Port Specific Settings**

Update venue template AP model LAN port specific settings.

operationId: `updateVenueTemplateApModelLanPortSpecificSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template. |
| `apModel` | path | ✓ | `string` | The model name of the AP. |


**Request Body:** `Wi-Fi_Services_VenueApModelLanPortSpecificSettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `poeMode` | `['string', 'null']` |  |  |
| `poeOut` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/venues/{venueTemplateId}/apModels/{apModel}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileTemplateId}`

**Deactivate Ethernet Port Profile On Venue Template AP Model**

Deactivate ethernet port profile template on venue template, specific to AP model and LAN ports.

operationId: `deactivateEthernetPortProfileTemplateToVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template. |
| `apModel` | path | ✓ | `string` | The model name of the AP. |
| `portId` | path | ✓ | `string` | Port ID. |
| `ethernetPortProfileTemplateId` | path | ✓ | `string` | The unique identifier of the Ethernet port profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/apModels/{apModel}/lanPorts/{portId}/ethernetPortProfiles/{ethernetPortProfileTemplateId}`

**Activate Ethernet Port Profile On Venue Template AP Model**

Associate an Ethernet port profile MSP template with an AP model LAN port on a venue MSP template, applying VLAN and port type configurations.

operationId: `activateEthernetPortProfileTemplateToVenueApModelLanPort`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template. |
| `apModel` | path | ✓ | `string` | The model name of the AP. |
| `portId` | path | ✓ | `string` | Port ID. |
| `ethernetPortProfileTemplateId` | path | ✓ | `string` | The unique identifier of the Ethernet port profile MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/venues/{venueTemplateId}/apModels/{apModel}/lanPorts/{portId}/settings`

**Get Venue Template AP Model LAN Port Settings**

Get venue template AP model LAN port settings.

operationId: `getVenueTemplateApModelLanPortOverwriteSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template. |
| `apModel` | path | ✓ | `string` | The model name of the AP. |
| `portId` | path | ✓ | `string` | Port ID. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueApModelLanPortSettingsV1`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/venues/{venueTemplateId}/apModels/{apModel}/lanPorts/{portId}/settings`

**Update Venue Template AP Model LAN Port Settings**

Update venue template AP model LAN port settings.

operationId: `updateVenueTemplateApModelLanPortOverwriteSettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueTemplateId` | path | ✓ | `string` | The unique identifier of the venue template. |
| `apModel` | path | ✓ | `string` | The model name of the AP. |
| `portId` | path | ✓ | `string` | Port ID. |


**Request Body:** `Wi-Fi_Services_VenueApModelLanPortSettingsV1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `clientIsolationEnabled` | `boolean` |  |  |
| `clientIsolationSettings` | `Wi-Fi_Services_LanPortClientIsolationSettings` |  |  |
| `dhcpOption82Enabled` | `boolean` |  |  |
| `dhcpOption82Settings` | `Wi-Fi_Services_DhcpOption82Settings` |  |  |
| `enabled` | `boolean` |  |  |
| `softGreEnabled` | `boolean` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Tunnel Service Profile Template

*Manage tunnel service profile templates.*


*4 endpoints*


### `POST` `/templates/tunnelServiceProfiles`

**Add Tunnel Service Profile Template**

Create a new tunnel service profile MSP template with tunnel type, destination IP, MTU, NAT traversal, and keep-alive parameters.

operationId: `createTunnelServiceProfileTemplate`


**Request Body:** `Wi-Fi_Services_TunnelServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ageTimeMinutes` | `integer` |  | The aging time in minutes for tunnel entries. After this time period, inactive tunnel entries will be removed. Valid range is 5 to 10080 minutes (7 days). |
| `destinationIpAddress` | `string` |  | The destination IP address for the tunnel endpoint. Must be a valid IPv4 address in dotted-decimal notation. |
| `forceFragmentation` | `boolean` |  | When enabled, forces packet fragmentation for tunnel traffic. This ensures that packets exceeding the MTU size are fragmented before transmission, preventing packet loss in networks with smaller MTU sizes. |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `keepAliveInterval` | `integer` |  | The time interval in seconds between keep-alive packets sent to maintain the tunnel connection. Valid range is 1 to 5 seconds, default is 2 seconds. |
| `keepAliveRetry` | `integer` |  | The number of keep-alive retry attempts before considering the tunnel connection as failed, default is 5 retries. Valid range depends on the tunnel type: 3 to 10 retries for `VXLAN_GPE`, and 3 to 5 retries for `L2GRE`. |
| `mtuRequestRetry` | `integer` |  | This setting is only effective in path maximum transmission unit auto mode. |
| `mtuRequestTimeout` | `integer` |  | The unit is milliseconds. This setting is only effective in path maximum transmission unit auto mode. |
| `mtuSize` | `integer` |  | The MTU (Maximum Transmission Unit) size in bytes for the tunnel when the MTU type is set to `MANUAL`. This determines the maximum packet size that can be transmitted through the tunnel. Valid range is 1280 to 1450 bytes. |
| `mtuType` | `string` |  | The MTU (Maximum Transmission Unit) type for the tunnel. The `AUTO` mode automatically determines the optimal MTU size, while MANUAL mode allows manual configuration of the MTU size. |
| `name` | `string` | ✓ | The unique name of the tunnel service profile used for identification and management. The name must be between 2 and 32 characters and cannot contain backticks or dollar signs with parentheses. |
| `natTraversalEnabled` | `boolean` |  | For toggling whether NAT traversal support is needed for the tunnel. |
| `tag` | `string` |  |  |
| `tunnelType` | `string` |  | The tunnel encapsulation protocol type using VXLAN-GPE (Generic Protocol Extension for VXLAN) or VXLAN (Virtual Extensible LAN). |
| `type` | `string` |  | The tunnel network segmentation type determining how traffic is segmented. Options include VXLAN for Layer 2 extension or VLAN_VXLAN for VLAN based VxLAN segmentation. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/templates/tunnelServiceProfiles/{tunnelServiceProfileTemplateId}`

**Delete Tunnel Service Profile Template**

Remove a tunnel service profile MSP template and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteTunnelServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileTemplateId` | path | ✓ | `string` | The unique identifier of the tunnel service profile MSP template to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/templates/tunnelServiceProfiles/{tunnelServiceProfileTemplateId}`

**Get Tunnel Service Profile Template**

Retrieve detailed information about a tunnel service profile MSP template including tunnel type, IP address, MTU, and NAT settings.

operationId: `getTunnelServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileTemplateId` | path | ✓ | `string` | The unique identifier of the tunnel service profile MSP template to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_TunnelServiceProfile`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/templates/tunnelServiceProfiles/{tunnelServiceProfileTemplateId}`

**Update Tunnel Service Profile Template**

Update an existing tunnel service profile MSP template including tunnel type, destination IP, MTU, NAT traversal, and keep-alive parameters.

operationId: `updateTunnelServiceProfileTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `tunnelServiceProfileTemplateId` | path | ✓ | `string` | The unique identifier of the tunnel service profile MSP template to be modified. |


**Request Body:** `Wi-Fi_Services_TunnelServiceProfileV1_1`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `ageTimeMinutes` | `integer` |  | The aging time in minutes for tunnel entries. After this time period, inactive tunnel entries will be removed. Valid range is 5 to 10080 minutes (7 days). |
| `destinationIpAddress` | `string` |  | The destination IP address for the tunnel endpoint. Must be a valid IPv4 address in dotted-decimal notation. |
| `forceFragmentation` | `boolean` |  | When enabled, forces packet fragmentation for tunnel traffic. This ensures that packets exceeding the MTU size are fragmented before transmission, preventing packet loss in networks with smaller MTU sizes. |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `keepAliveInterval` | `integer` |  | The time interval in seconds between keep-alive packets sent to maintain the tunnel connection. Valid range is 1 to 5 seconds, default is 2 seconds. |
| `keepAliveRetry` | `integer` |  | The number of keep-alive retry attempts before considering the tunnel connection as failed, default is 5 retries. Valid range depends on the tunnel type: 3 to 10 retries for `VXLAN_GPE`, and 3 to 5 retries for `L2GRE`. |
| `mtuRequestRetry` | `integer` |  | This setting is only effective in path maximum transmission unit auto mode. |
| `mtuRequestTimeout` | `integer` |  | The unit is milliseconds. This setting is only effective in path maximum transmission unit auto mode. |
| `mtuSize` | `integer` |  | The MTU (Maximum Transmission Unit) size in bytes for the tunnel when the MTU type is set to `MANUAL`. This determines the maximum packet size that can be transmitted through the tunnel. Valid range is 1280 to 1450 bytes. |
| `mtuType` | `string` |  | The MTU (Maximum Transmission Unit) type for the tunnel. The `AUTO` mode automatically determines the optimal MTU size, while MANUAL mode allows manual configuration of the MTU size. |
| `name` | `string` | ✓ | The unique name of the tunnel service profile used for identification and management. The name must be between 2 and 32 characters and cannot contain backticks or dollar signs with parentheses. |
| `natTraversalEnabled` | `boolean` |  | For toggling whether NAT traversal support is needed for the tunnel. |
| `tag` | `string` |  |  |
| `tunnelType` | `string` |  | The tunnel encapsulation protocol type using VXLAN-GPE (Generic Protocol Extension for VXLAN) or VXLAN (Virtual Extensible LAN). |
| `type` | `string` |  | The tunnel network segmentation type determining how traffic is segmented. Options include VXLAN for Layer 2 extension or VLAN_VXLAN for VLAN based VxLAN segmentation. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Client Isolation Allowlist

*Manage client isolation allowlists that define exceptions allowing specified devices to communicate despite isolation policies.*


*7 endpoints*


### `DELETE` `/isolationAllowlists`

**Delete Isolation Allowlists**

Perform a batch deletion of multiple client isolation allowlists by providing a list of allowlist identifiers. This operation permanently removes all specified allowlists and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/{clientIsolationProfileId} can be used for this content.

operationId: `deleteClientIsolationAllowlistsBulk`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/isolationAllowlists`

**Get Client Isolation Allowlists**

Retrieve a paginated list of all client isolation allowlists configured in the system. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/query can be used for this content.

operationId: `getClientIsolationAllowlists`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/isolationAllowlists`

**Create Client Isolation Allowlist**

Create a client isolation allowlist with MAC addresses that can be applied to Wi-Fi networks as isolation exceptions. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles can be used for this content.

operationId: `createClientIsolationAllowlist`


**Request Body:** `Wi-Fi_Services_ClientIsolationAllowlist`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowlist` | `array` | ✓ |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_ClientIsolationAllowlistOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/isolationAllowlists/{clientIsolationAllowlistId}`

**Delete Client Isolation Allowlist**

Delete a client isolation allowlist by its unique identifier, permanently deleting the allowlist and its configurations. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/{clientIsolationProfileId} can be used for this content.

operationId: `deleteClientIsolationAllowlist`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationAllowlistId` | path | ✓ | `string` | The unique identifier of the client isolation allowlist to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/isolationAllowlists/{clientIsolationAllowlistId}`

**Get Client Isolation Allowlist**

Retrieve detailed information about a specific client isolation allowlist by its unique identifier. The response includes all configuration settings and allowlist entries that define exceptions to client isolation behavior. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/{clientIsolationProfileId} can be used for this content.

operationId: `getClientIsolationAllowlist`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationAllowlistId` | path | ✓ | `string` | The unique identifier of the client isolation allowlist to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_ClientIsolationAllowlist`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/isolationAllowlists/{clientIsolationAllowlistId}`

**Update Client Isolation Allowlist**

Update an existing client isolation allowlist by its unique identifier, updating allowlist entries and settings. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/{clientIsolationProfileId} can be used for this content.

operationId: `updateClientIsolationAllowlist`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationAllowlistId` | path | ✓ | `string` | The unique identifier of the client isolation allowlist to be modified. |


**Request Body:** `Wi-Fi_Services_ClientIsolationAllowlist`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `allowlist` | `array` | ✓ |  |
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `name` | `string` | ✓ |  |
| `tenantId` | `string` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/isolationAllowlists/{clientIsolationAllowlistId}/venues/query`

**Get Venue Usage**

Query venues associated with this client isolation allowlist. The response includes a paginated list of venues where the allowlist is configured, along with associated network information. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/query can be used for this content.

operationId: `GetVenueUsage`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `clientIsolationAllowlistId` | path | ✓ | `string` | The unique identifier of the client isolation allowlist whose venue usage is to be queried. |


**Request Body:** `Wi-Fi_Services_ClientIsolationAllowlistVenueQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `searchVenueNameString` | `string` |  | Search venue name. |
| `sortField` | `string` |  | The field name used to sort the query results in ascending or descending order. |
| `sortOrder` | `['string', 'null']` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_ClientIsolationAllowlistVenueQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## VLAN Pool

*Manage VLAN pool profiles.*


*9 endpoints*


### `DELETE` `/vlanPools`

**Delete VLAN Pools**

Perform a batch deletion of multiple VLAN pools by providing a list of pool identifiers. This operation permanently removes all specified pools and their associated configurations. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/{vlanPoolProfileId} can be used for this content.

operationId: `deleteVlanPools`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/vlanPools`

**Get VLAN Pools**

Retrieve a complete list of all VLAN pools configured in the system. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/query can be used for this content.

operationId: `getVlanPools`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/vlanPools`

**Add VLAN Pool**

Create a new VLAN pool with specific VLAN ID ranges for managing VLAN assignments. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles can be used for this content.

operationId: `addVlanPool`


**Request Body:** `Wi-Fi_Services_VlanPool`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `tenantId` | `string` |  |  |
| `vlanMembers` | `array` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_VlanPoolOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/vlanPools/query`

**Query VLAN Pool**

Query VLAN pools using filter criteria. The response includes all VLAN pools matching the specified query parameters. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/query can be used for this content.

operationId: `getVlanPoolByQuery`


**Request Body:** `Wi-Fi_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  |  |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `searchString` | `string` |  |  |
| `searchTargetFields` | `array` |  |  |
| `sortField` | `string` |  |  |
| `sortOrder` | `['string', 'null']` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_VlanPoolQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/vlanPools/{vlanPoolId}`

**Delete VLAN Pool**

Remove a VLAN pool and its associated configurations by its unique identifier, permanently deleting all settings. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/{vlanPoolProfileId} can be used for this content.

operationId: `deleteVlanPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolId` | path | ✓ | `string` | The unique identifier of the VLAN pool. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/vlanPools/{vlanPoolId}`

**Get VLAN Pool**

Retrieve detailed information about a specific VLAN pool by its unique identifier. The response includes all configuration settings and VLAN ID ranges associated with the pool. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/{vlanPoolProfileId} can be used for this content.

operationId: `getVlanPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolId` | path | ✓ | `string` | The unique identifier of the VLAN pool. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VlanPool`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PATCH` `/vlanPools/{vlanPoolId}`

**Partial Update VLAN Pool**

Perform a partial update on an existing VLAN pool by its unique identifier. This operation allows you to modify specific VLAN pool parameters without replacing the entire configuration. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/{vlanPoolProfileId} can be used for this content.

operationId: `patchVlanPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolId` | path | ✓ | `string` | The unique identifier of the VLAN pool. |


**Request Body:** `Wi-Fi_Services_PartialVlanPool`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` |  |  |
| `tenantId` | `string` |  |  |
| `vlanMembers` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/vlanPools/{vlanPoolId}`

**Update VLAN Pool**

Update the configuration of an existing VLAN pool by its unique identifier. This operation allows you to update VLAN ID ranges and other settings while maintaining the pool identity. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/{vlanPoolProfileId} can be used for this content.

operationId: `updateVlanPool`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolId` | path | ✓ | `string` | The unique identifier of the VLAN pool. |


**Request Body:** `Wi-Fi_Services_VlanPool`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `tenantId` | `string` |  |  |
| `vlanMembers` | `array` | ✓ |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/vlanPools/{vlanPoolId}/venues`

**Get VLAN Pool Venues Activations**

Query venue activations for VLAN pools using filter criteria. The response includes all venues where the specified VLAN pools are activated. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/query can be used for this content.

operationId: `getVlanPoolVenues`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `vlanPoolId` | path | ✓ | `string` | The unique identifier of the VLAN pool. |


**Request Body:** `Wi-Fi_Services_QueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `fields` | `array` |  |  |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  |  |
| `searchString` | `string` |  |  |
| `searchTargetFields` | `array` |  |  |
| `sortField` | `string` |  |  |
| `sortOrder` | `['string', 'null']` |  |  |


**Responses:**

- `200` OK → `Wi-Fi_Services_VlanPoolVenueDataQueryResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## DPSK Service Template

*Manage DPSK service templates.*


*1 endpoint*


### `PUT` `/templates/wifiNetworks/{wifiNetworkTemplateId}/dpskServices/{dpskServiceTemplateId}`

**Activate DPSK Service Template On Wi-Fi Network Template**

Associate a DPSK service MSP template with a Wi-Fi network MSP template to enable per user or per device authentication.

operationId: `activateDpskServiceOnWifiNetworkTemplate`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkTemplateId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network MSP template where the DPSK service MSP template will be activated. |
| `dpskServiceTemplateId` | path | ✓ | `string` | The unique identifier of the DPSK service MSP template to be associated with the Wi-Fi network MSP template. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Wi-Fi Network Workflow Assignment

*Manage the assignment of a workflow to a Wi-Fi network.*


*1 endpoint*


### `PUT` `/wifiNetworks/{wifiNetworkId}/workflowProfiles/{workflowProfileId}`

**Activate Workflow Profile On Wi-Fi Network**

Associate a workflow profile with a Wi-Fi network to enable workflow onboarding.

operationId: `activateWorkflowProfileOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the workflow profile will be activated. |
| `workflowProfileId` | path | ✓ | `string` | The unique identifier of the workflow profile to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Certificate Template Activation

*Manage certificate templates.*


*2 endpoints*


### `DELETE` `/wifiNetworks/{wifiNetworkId}/certificateTemplates/{certificateTemplateId}`

**Deactivate Certificate Template On Wi-Fi Network**

Remove the association between a certificate template and a Wi-Fi network without deleting the template.

operationId: `deactivateCertificateTemplateOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network from which the certificate template will be deactivated. |
| `certificateTemplateId` | path | ✓ | `string` | The unique identifier of the certificate template to be disassociated from the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/wifiNetworks/{wifiNetworkId}/certificateTemplates/{certificateTemplateId}`

**Activate Certificate Template On Wi-Fi Network**

Associate a certificate template with a Wi-Fi network to enable certificate based authentication.

operationId: `activateCertificateTemplateOnWifiNetwork`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `wifiNetworkId` | path | ✓ | `string` | The unique identifier of the Wi-Fi network where the certificate template will be activated. |
| `certificateTemplateId` | path | ✓ | `string` | The unique identifier of the certificate template to be associated with the Wi-Fi network. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---



## Rogue AP Detection Policy

*Manage rogue AP detection policies and their configurations including creation, retrieval, update, and deletion.*


*16 endpoints*


### `DELETE` `/rogueApPolicyProfiles`

**Delete AP Detection Policies**

Perform a batch deletion of multiple rogue AP detection policies, permanently deleting all specified policies and their configurations. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies/{roguePolicyId} can be used for this content.

operationId: `deleteRogueApPolicyProfiles`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/rogueApPolicyProfiles`

**Get Rogue AP Detection Policies**

Retrieve a complete list of all rogue AP detection policies configured in the system. Use POST /roguePolicies/query instead. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies/query can be used for this content.

operationId: `getRogueApPolicyProfiles`


**Responses:**

- `200` OK
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/rogueApPolicyProfiles`

**Create Rogue AP Detection Policy**

Create a new rogue AP detection policy with detection rules and policies for automatically classifying unknown APs. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies can be used for this content.

operationId: `addRogueApPolicyProfile`


**Request Body:** `Wi-Fi_Services_RogueClassificationPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |
| `venues` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_RogueClassificationPolicyOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/rogueApPolicyProfiles/{roguePolicyId}`

**Delete Rogue AP Detection Policy**

Remove a rogue AP detection policy and its associated configurations by its unique identifier, permanently deleting all settings. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies/{roguePolicyId} can be used for this content.

operationId: `deleteRogueApPolicyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/rogueApPolicyProfiles/{roguePolicyId}`

**Get Rogue AP Detection Policy**

Retrieve detailed information about a rogue AP detection policy including configuration settings, rules, and policies. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies/{roguePolicyId} can be used for this content.

operationId: `getRogueApPolicyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy. |


**Responses:**

- `200` OK → `Wi-Fi_Services_RogueClassificationPolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/rogueApPolicyProfiles/{roguePolicyId}`

**Update Rogue AP Detection Policy**

Update an existing rogue AP detection policy including detection rules, classification policies, and settings. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies/{roguePolicyId} can be used for this content.

operationId: `updateRogueApPolicyProfile`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy. |


**Request Body:** `Wi-Fi_Services_RogueClassificationPolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |
| `venues` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/rogueApPolicyProfiles/{roguePolicyId}/venues`

**Unbind Rogue AP Detection Policy from Venues**

Remove the associations between a rogue AP detection policy and multiple venues. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/roguePolicies/{roguePolicyId} can be used for this content.

operationId: `unbindRogueApPolicyProfileFromVenues`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/rogueApPolicyProfiles/{roguePolicyId}/venues`

**Create Rogue AP Detection Policy Venue Bindings**

Associate a rogue AP detection policy with multiple venues to enable automatic rogue AP classification. This method will be removed no sooner than 06/30/2026. The following URL /venues/{venueId}/roguePolicies/{roguePolicyId} can be used for this content.

operationId: `bindRogueApPolicyProfileToVenues`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy. |


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `POST` `/roguePolicies`

**Create Rogue AP Detection Policy**

Create a new rogue AP detection policy with detection rules and policies for automatically classifying unknown APs.

operationId: `addRoguePolicy`


**Request Body:** `Wi-Fi_Services_RoguePolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_EntityIdOperationResponse`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/roguePolicies/{roguePolicyId}`

**Delete Rogue AP Detection Policy**

Remove a rogue AP detection policy and its associated configurations by its unique identifier, permanently deleting all settings.

operationId: `deleteRoguePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy to be deleted. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/roguePolicies/{roguePolicyId}`

**Get Rogue AP Detection Policy**

Retrieve detailed information about a specific rogue AP detection policy by its unique identifier. The response includes all configuration settings, rules, and policies associated with the policy.

operationId: `getRoguePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy to be retrieved. |


**Responses:**

- `200` OK → `Wi-Fi_Services_RoguePolicy`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/roguePolicies/{roguePolicyId}`

**Update Rogue AP Detection Policy**

Update an existing rogue AP detection policy including detection rules, classification policies, and settings.

operationId: `updateRoguePolicy`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy to be updated. |


**Request Body:** `Wi-Fi_Services_RoguePolicy`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `id` | `string` |  |  |
| `isEnforced` | `boolean` |  | A flag that indicates if a template/instance is enforced. The default is always false. |
| `name` | `string` | ✓ |  |
| `rules` | `array` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `DELETE` `/venues/{venueId}/roguePolicies/{roguePolicyId}`

**Deactivate Rogue AP Detection Policy On Venue**

Remove the association between a rogue AP detection policy and a venue.

operationId: `deactivateRoguePolicyOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the rogue AP detection policy will be deactivated. |
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy to be disassociated from the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/roguePolicies/{roguePolicyId}`

**Activate Rogue AP Detection Policy On Venue**

Associate a rogue AP detection policy with a venue to enable automatic rogue AP classification.

operationId: `activateRoguePolicyOnVenue`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue where the rogue AP detection policy will be activated. |
| `roguePolicyId` | path | ✓ | `string` | The unique identifier of the rogue AP detection policy to be associated with the venue. |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `GET` `/venues/{venueId}/roguePolicySettings`

**Get Venue Rogue Policy Settings**

Retrieve detailed information about the rogue AP detection policy settings configured for a specific venue. The response includes all configuration settings such as report threshold and other detection parameters.

operationId: `getVenueRoguePolicySettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue for which to retrieve rogue policy settings. |


**Responses:**

- `200` OK → `Wi-Fi_Services_VenueRoguePolicySettings`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---

### `PUT` `/venues/{venueId}/roguePolicySettings`

**Update Venue Rogue Policy Settings**

Update rogue AP detection policy settings for a venue including report threshold and detection parameters.

operationId: `updateVenueRoguePolicySettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | The unique identifier of the venue for which to update rogue policy settings. |


**Request Body:** `Wi-Fi_Services_VenueRoguePolicySettings`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `reportThreshold` | `integer` |  |  |


**Responses:**

- `202` Accepted → `Wi-Fi_Services_OperationResponseRequestIdOnly`
- `400` Bad Request → `Wi-Fi_Services_ErrorResponse`
- `404` Not Found → `Wi-Fi_Services_ErrorResponse`
- `422` Unprocessable Content → `Wi-Fi_Services_ErrorResponse`
- `500` Internal Server Error → `Wi-Fi_Services_ErrorResponse`


---


