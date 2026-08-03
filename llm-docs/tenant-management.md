# Tenant Management

> RUCKUS One API Reference

---


## Notification Recipient

*Manage notification recipient configurations for tenants.*


*4 endpoints*


### `DELETE` `/tenants/notificationRecipients`

**Delete Notification Recipients**

[DEPRECATED: Use deleteNotificationRecipientsV2 with Content-Type application/vnd.ruckus.v2+json and a list of recipient IDs.] Delete notification recipient list.

operationId: `deleteNotificationRecipientsV2`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseVoid`
- `400` Indicates that a bad request was made. → `Tenant_Management_OperationResponseVoid`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseVoid`


---

### `GET` `/tenants/notificationRecipients`

**Get Notification Recipients**

Get notification recipient list.

operationId: `getNotificationRecipients`


**Responses:**

- `200` OK
- `415` Unsupported Media Type


---

### `POST` `/tenants/notificationRecipients`

**Add Notification Recipient**

Add a new notification recipient to the tenant.

operationId: `addNotificationRecipient`


**Request Body:** `Tenant_Management_NotificationRecipientRBACDTO`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `description` | `string` |  |  |
| `emailCapPerDay` | `integer` |  | Daily email send cap (Nuvo workflow). |
| `emailPreferences` | `boolean` |  | Indicates whether email notifications are enabled for this recipient. |
| `endpoints` | `array` |  | List of notification endpoints configured for this recipient. |
| `id` | `string` |  |  |
| `notificationProfile` | `Tenant_Management_NotificationProfileSummaryDTO` |  | Linked notification profile summary (Nuvo workflow). Populated on reads when nuvo-notification-workflow-toggle is on and a profile is set; omitted from request bodies. |
| `notificationProfileId` | `string` |  | Optional notification profile id (Nuvo workflow). Accepted on create/update request bodies when feature flag nuvo-notification-workflow-toggle is on; not serialized on responses (use notificationProfile). |
| `privilegeGroupId` | `string` |  | Identifier of the privilege group associated with this notification recipient. |
| `recipientType` | `string` |  | Type of notification recipient such as privilege group or global. |
| `sendCapEmailReminder` | `boolean` |  | Notify when the daily email cap is approached or reached (Nuvo workflow). |
| `sendCapSmsReminder` | `boolean` |  | Notify when the daily SMS cap is approached or reached (Nuvo workflow). |
| `sendPlainTextEmail` | `boolean` |  | Send notification emails as plain text (Nuvo workflow). |
| `smsCapPerDay` | `integer` |  | Daily SMS send cap (Nuvo workflow). |
| `smsPreferences` | `boolean` |  | Indicates whether SMS notifications are enabled for this recipient. |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseNotificationRecipientRBACDTO`
- `400` Bad/Malformed Request → `Tenant_Management_OperationResponseNotificationRecipientRBACDTO`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseNotificationRecipientRBACDTO`


---

### `POST` `/tenants/notifications/recipients/query`

**Query Notification Recipients**

Query notification recipient list.

operationId: `queryNotificationRecipients`


**Request Body:** `Tenant_Management_NotificationRecipientQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | Additional filter criteria as key value pairs for refined searching. |
| `page` | `integer` |  |  |
| `pageSize` | `integer` |  | Number of records per page for pagination. |
| `searchString` | `string` |  | Search text string to match against target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when filtering notification recipients. |
| `sortField` | `string` |  | Field by which to sort the notification recipient results. |
| `sortOrder` | `string` |  | Sort order direction (ascending or descending). |


**Responses:**

- `200` OK → `Tenant_Management_NotificationRecipientPageResponse`
- `400` Bad/Malformed Request
- `500` Internal Server Error


---



## Administrator

*Manage administrator accounts and roles.*


*7 endpoints*


### `DELETE` `/admins`

**Delete Administrators**

Delete administrators in bulk.

operationId: `deleteBulkAdmin`


**Request Body:** Yes


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseVoid`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseVoid`


---

### `GET` `/admins`

**Get Administrator**

Get list of administrators.

operationId: `getAdminList`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `withExternalId` | query |  | `boolean` |  |


**Responses:**

- `200` OK
- `415` Unsupported Media Type


---

### `POST` `/admins`

**Add Administrator**

Add a new administrator to the tenant.

operationId: `addAdmin`


**Request Body:** `Tenant_Management_AdminView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authenticationId` | `string` |  | Identifier for the authentication method associated with this administrator. |
| `delegateToAllECs` | `boolean` |  | If set to true, this admin is permitted to manage all delegated account IDs (RECs or MSP-ECs). |
| `delegatedECs` | `array` |  | List of delegated account IDs (RECs or MSP-ECs) that this admin is permitted to manage. |
| `detailLevel` | `string` |  | Detail level for events. <table><tr><td><b>Enum</b></td><td><b>Meaning</b></td></tr><tr><td>ba</td><td>Show events appropriate for a basic user.</td></tr><tr><td>it</td><td>Show events appropriate for someone having training as an IT administrator.</ |
| `email` | `string` | ✓ | Email address used as the administrator's login username. Follow RFC standards for email pattern. |
| `externalId` | `string` |  | External identifier from RUCKUS cloud authentication system. |
| `id` | `string` |  | Unique identifier for the administrator account. |
| `lastName` | `string` |  | Last name of the administrator. |
| `name` | `string` |  | First name of the administrator. |
| `phoneNumber` | `string` |  | Contact phone number for the administrator. |
| `role` | `string` | ✓ | Role assigned to the administrator, such as prime admin, admin, or readonly. |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseAdmin`
- `400` Bad/Malformed Request → `Tenant_Management_OperationResponseAdmin`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseAdmin`


---

### `PUT` `/admins`

**Update Administrator**

Update administrator role and settings for the tenant.

operationId: `updateAdminRole`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `updateSwuId` | query |  | `boolean` |  |


**Request Body:** `Tenant_Management_AdminView`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authenticationId` | `string` |  | Identifier for the authentication method associated with this administrator. |
| `delegateToAllECs` | `boolean` |  | If set to true, this admin is permitted to manage all delegated account IDs (RECs or MSP-ECs). |
| `delegatedECs` | `array` |  | List of delegated account IDs (RECs or MSP-ECs) that this admin is permitted to manage. |
| `detailLevel` | `string` |  | Detail level for events. <table><tr><td><b>Enum</b></td><td><b>Meaning</b></td></tr><tr><td>ba</td><td>Show events appropriate for a basic user.</td></tr><tr><td>it</td><td>Show events appropriate for someone having training as an IT administrator.</ |
| `email` | `string` | ✓ | Email address used as the administrator's login username. Follow RFC standards for email pattern. |
| `externalId` | `string` |  | External identifier from RUCKUS cloud authentication system. |
| `id` | `string` |  | Unique identifier for the administrator account. |
| `lastName` | `string` |  | Last name of the administrator. |
| `name` | `string` |  | First name of the administrator. |
| `phoneNumber` | `string` |  | Contact phone number for the administrator. |
| `role` | `string` | ✓ | Role assigned to the administrator, such as prime admin, admin, or readonly. |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseAdmin`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseAdmin`


---

### `POST` `/admins/query`

**Query administrators**

Paged list; optional flags switch response shape.

operationId: `queryAdminList`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `withExternalId` | query |  | `boolean` | Include external (SWU) ID in each row |
| `withDelegatedECs` | query |  | `boolean` | Include delegated EC tenant IDs per admin (default true) |
| `includeDelegatedAdmins` | query |  | `boolean` | Minimal delegated-admin rows; body mspEcTenantIds scopes the list |
| `includeSelectedAdmins` | query |  | `boolean` | MSP-EC selection mode with includeSystemRoles or includePrivilegeGroups (body mspEcTenantIds) |
| `includeSystemRoles` | query |  | `boolean` | With includeSelectedAdmins: would be returning system admins only |
| `includePrivilegeGroups` | query |  | `boolean` | With includePrivilegeGroups: would be returning privilege groups and associated admins |


**Request Body:** `Tenant_Management_AdminQueryRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `filters` | `object` |  | Additional filter criteria as key value pairs for refined searching. |
| `mspEcTenantIds` | `array` |  | MSP delegated child tenant ids: MSP_EC, MSP_INTEGRATOR, or MSP_INSTALLER under the MSP (delegated-admin mode; or includeSelectedAdmins with system-role / privilege-group selection). |
| `page` | `integer` |  | Page number for pagination starting from 0. |
| `pageSize` | `integer` |  | Number of records per page for pagination. |
| `searchString` | `string` |  | Search text string to match against target fields. |
| `searchTargetFields` | `array` |  | List of fields to search within when filtering administrators. |
| `sortField` | `string` |  | Field by which to sort the administrator results. |
| `sortOrder` | `string` |  | Sort order direction (ascending or descending). |


**Responses:**

- `200` OK — page type depends on query flags (default: full admin rows).
- `415` Unsupported Media Type


---

### `DELETE` `/admins/{adminId}`

**Delete Administrator**

Delete administrator by identifier.

operationId: `deleteAdmin`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `adminId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseVoid`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseVoid`


---

### `GET` `/admins/{adminId}`

**Get Administrator**

Get administrator by identifier.

operationId: `getAdminById`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `adminId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Tenant_Management_AdminView`
- `415` Unsupported Media Type


---



## Delegation

*Manage tenant delegation access rights.*


*7 endpoints*


### `GET` `/tenants/delegations`

**Get Delegations**

Get delegation list for the authenticated tenant.

operationId: `getDelegations`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `type` | query |  | `string` |  |


**Responses:**

- `200` OK
- `415` Unsupported Media Type


---

### `POST` `/tenants/delegations`

**Invite VAR**

Send invitation to VAR (aka delegate) to manage my account.This operation is not supported using client credentials.

operationId: `inviteVAR`


**Request Body:** `Tenant_Management_InviteVAR`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `username` | `string` |  | Username or email address of the VAR to invite. |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseDelegation`
- `400` Bad/Malformed Request → `Tenant_Management_OperationResponseDelegation`
- `404` Requested resource or related entity not found → `Tenant_Management_OperationResponseDelegation`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseDelegation`


---

### `DELETE` `/tenants/delegations/{delegationId}`

**Revoke VAR Delegation**

Revoke VAR delegation by ID.

operationId: `deleteDelegation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegationId` | path | ✓ | `string` |  |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseVoid`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseVoid`


---

### `GET` `/tenants/delegations/{delegationId}`

**Get Delegation**

Get delegation by ID.

operationId: `getDelegation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegationId` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `Tenant_Management_Delegation`
- `415` Unsupported Media Type


---

### `PUT` `/tenants/delegations/{delegationId}`

**Respond to Delegation**

A VAR uses this endpoint to respond to a delegation invitation; the response is either accept or reject.

operationId: `acceptOrRejectDelegation`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `delegationId` | path | ✓ | `string` |  |


**Request Body:** `Tenant_Management_DelegationAction`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `accept` | `boolean` | ✓ | Indicates whether to accept or reject the delegation request. |
| `fromTenantId` | `string` | ✓ | Identifier of the tenant requesting the delegation. |


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseDelegation`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseDelegation`


---

### `DELETE` `/tenants/supportDelegations`

**Revoke Access**

Revoke RUCKUS customer support's access to my account.

operationId: `deleteSupportDelegation`


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseVoid`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseVoid`


---

### `POST` `/tenants/supportDelegations`

**Grant Access**

Grant RUCKUS customer support access to my account.

operationId: `inviteSupport`


**Responses:**

- `202` Accepted → `Tenant_Management_OperationResponseDelegation`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseDelegation`


---



## Privacy Features

*Manage tenant privacy feature settings.*


*3 endpoints*


### `GET` `/tenants/privacySettings`

**Get Configured Privacy Settings**

Get configured privacy settings.

operationId: `getPrivacySettings`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `id` | query |  | `string` |  |


**Responses:**

- `200` OK → `Tenant_Management_PrivacyFeatureResponse`
- `415` Unsupported Media Type


---

### `PATCH` `/tenants/privacySettings`

**Add or Update Privacy Settings**

Configure, add or update tenant specific privacy settings such as arc, visibility controls and related features.

operationId: `patchPrivacySettings`


**Request Body:** `Tenant_Management_PrivacyFeatureRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `privacyFeatures` | `array` |  | Manage privacy settings, including arc and related features. |


**Responses:**

- `200` OK → `Tenant_Management_PrivacyFeatureResponse`


---

### `POST` `/tenants/privacySettings`

**Clear and Save Privacy Settings**

Clear and save privacy settings.

operationId: `postPrivacySettings`


**Request Body:** `Tenant_Management_PrivacyFeatureRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `privacyFeatures` | `array` |  | Manage privacy settings, including arc and related features. |


**Responses:**

- `200` OK → `Tenant_Management_PrivacyFeatureResponse`


---



## User Profile

*Manage administrator user profile settings.*


*3 endpoints*


### `GET` `/tenants/accounts`

**Get Account**

Get account details for the authenticated administrator.

operationId: `getAccountDetails`


**Responses:**

- `200` OK → `Tenant_Management_AccountInfo`


---

### `GET` `/tenants/userProfiles`

**Get User Profile**

Get user profile for the authenticated administrator.

operationId: `getUserProfile`


**Responses:**

- `200` OK → `Tenant_Management_UserProfile`
- `415` Unsupported Media Type


---

### `PUT` `/tenants/userProfiles`

**Update User Profile**

Update user profile settings for the authenticated administrator.

operationId: `updateUser`


**Request Body:** `Tenant_Management_UserProfile`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `adminId` | `string` |  | Administrator identifier unique to this administrator account. |
| `allowedRegions` | `array` |  | Regions are the continents to which the user is allowed. Currently permitted regions are North America, European Union and Asia. |
| `alphaStatus` | `string` |  | Alpha feature access status for the administrator. |
| `companyName` | `string` |  | Company name associated with the administrator's account. |
| `customRoleName` | `string` |  | Custom role name assigned to the administrator. |
| `customRoleType` | `string` |  | Custom role type defining the administrator's permissions. |
| `dateFormat` | `string` | ✓ | Date format preference for displaying dates in the user interface. |
| `delegatedDogfood` | `boolean` |  | Delegation to a dog food account (internal RUCKUS test accounts, named per the saying, eat your own dog food). |
| `detailLevel` | `string` | ✓ | Detail level for event log information displayed to the administrator. |
| `dogfood` | `boolean` |  | Flag indicating whether this is a RUCKUS internal dog food account. |
| `edgeBeta` | `string` |  | Edge beta feature access level for the administrator. |
| `email` | `string` |  | Email address of the administrator user. |
| `externalId` | `string` |  | External identifier for the user from the identity management system. |
| `firstName` | `string` |  | First name of the administrator user. |
| `hasSupportReadOnlyDelegations` | `boolean` |  | Flag indicating whether active SUPPORT_READ_ONLY delegations exist for this user. |
| `lastName` | `string` |  | Last name of the administrator user. |
| `newDateFormat` | `string` |  | New date format string for customizing date display. |
| `phoneNumber` | `string` |  | Phone number associated with the administrator account. |
| `preferredLanguage` | `string` |  | Preferred language code for the user interface display. |
| `preferredNotifications` | `Tenant_Management_PreferredNotifications` |  | Preferred notification delivery methods for the administrator. |
| `privilegeGroupName` | `string` |  | Privilege group name defining the administrator's access level. |
| `privilegeGroupType` | `string` |  | Privilege group type categorizing the administrator's permissions. |
| `pver` | `string` |  | Protocol version for API compatibility. |
| `region` | `string` |  | Current geographic region for the user's API access. |
| `role` | `string` |  | Deprecated administrator role name for backward compatibility. |
| *… 7 more fields* | | | |


**Responses:**

- `200` Accepted → `Tenant_Management_OperationResponseUserProfile`
- `415` Unsupported Media Type
- `500` Internal Server Error → `Tenant_Management_OperationResponseUserProfile`


---



## Tenant

*Manage tenant accounts and configurations.*


*6 endpoints*


### `GET` `/tenants/betaFeatures`

**Get Beta Feature Identifiers**

Get list of beta features.

operationId: `getFeatureIds`


**Responses:**

- `200` OK → `Tenant_Management_BetaFeatureResponse`
- `415` Unsupported Media Type


---

### `PUT` `/tenants/betaFeatures`

**Update Beta Feature Identifiers**

Update beta feature identifiers.

operationId: `updateFeatureIds`


**Request Body:** `Tenant_Management_BetaFeatureRequest`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `betaFeatureIds` | `array` |  | Set of beta feature identifiers to configure. |


**Responses:**

- `200` OK → `Tenant_Management_BetaFeatureResponse`
- `415` Unsupported Media Type


---

### `GET` `/tenants/self`

**Get Tenant**

Get tenant by identifier.

operationId: `get`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `deep` | query |  | `boolean` |  |


**Responses:**

- `200` OK → `Tenant_Management_Tenant`
- `415` Unsupported Media Type


---

### `PUT` `/tenants/self`

**Update a Tenant**

Update tenant information such as tenant name, tenant type, and external identifier.

operationId: `updateTenant`


**Request Body:** `Tenant_Management_TenantDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `enableAlpha` | `boolean` |  | Indicates whether alpha features are enabled for this tenant. |
| `enableBeta` | `boolean` |  | Indicates whether beta features are enabled for this tenant. |
| `enableMfa` | `string` |  | Indicates whether multifactor authentication is enabled for the tenant. |
| `enableSa` | `boolean` |  | Indicates whether service account functionality is enabled. |
| `entitlementId` | `string` |  | Entitlement identifier for license and subscription management. |
| `missingAdminIds` | `array` |  | List of administrator IDs that were not found during the operation. |
| `newIdmId` | `string` |  | New identity management identifier for the tenant. |
| `requestId` | `string` |  | Unique identifier for tracking this API request. |
| `response` | `string` |  | Response message or status from the operation. |
| `subscribes` | `string` |  | Notification subscription preferences for the tenant. |
| `tenantName` | `string` |  | Name of the tenant or organization. |
| `userName` | `string` |  | Username of the person performing the operation. |
| `var` | `boolean` |  | Indicates whether this tenant is a value added reseller. |


**Responses:**

- `200` OK → `Tenant_Management_APICallInfo`


---

### `GET` `/tenants/subscriptionPreferences`

**Get subscription preferences**

Get tenant subscription display preferences from the tenant preferences column.

operationId: `getSubscriptionPreferences`


**Responses:**

- `200` OK → `Tenant_Management_TenantSubscriptionPreferencesDTO`


---

### `PUT` `/tenants/subscriptionPreferences`

**Update subscription preferences**

Update tenant subscription display preferences in the tenant preferences column.

operationId: `updateSubscriptionPreferences`


**Request Body:** `Tenant_Management_TenantSubscriptionPreferencesDTO`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `subscription` | `Tenant_Management_SubscriptionPreferences` |  | Subscription visibility and messaging preferences. |


**Responses:**

- `204` No Content
- `415` Unsupported Media Type


---



## authentication-controller

*2 endpoints*


### `GET` `/tenants/authentications`

**Get Authentications**

Get all authentication configurations for the tenant.

operationId: `getAuthentications`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `withExtendedRole` | query |  | `boolean` |  |


**Responses:**

- `200` OK
- `415` Unsupported Media Type


---

### `POST` `/tenants/authentications`

**Add Authentication**

Add a new authentication configuration for the tenant.

operationId: `addAuthentication`


**Request Body:** `Tenant_Management_AuthenticationInfo`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `authenticationType` | `string` | ✓ | Type of authentication method (e.g., OAuth, SAML, local). |
| `authorizationURL` | `string` |  | URL for OAuth authorization endpoint. |
| `clientID` | `string` |  | OAuth client identifier used for authentication. |
| `clientIDStatus` | `string` |  | Status of the client ID configuration. |
| `clientSecret` | `string` |  | OAuth client secret for secure authentication. |
| `domains` | `array` |  | List of email domains associated with this authentication configuration. |
| `id` | `string` |  |  |
| `name` | `string` | ✓ | Name of the authentication configuration. |
| `parentTenantId` | `string` |  | Parent tenant identifier for hierarchical authentication configuration. |
| `samlEncryptionCertificateId` | `string` |  | Identifier for the certificate used for SAML encryption. |
| `samlEncryptionPrivateKey` | `string` |  | Private key content for SAML encryption. |
| `samlEncryptionPublicCertificate` | `string` |  | Public certificate content for SAML encryption. |
| `samlFileType` | `string` |  | Type of SAML file (metadata or certificate). |
| `samlFileURL` | `string` |  | URL to the SAML metadata or configuration file. |
| `samlSignatureEnabled` | `boolean` |  | Indicates whether SAML signature validation is enabled. |
| `scopes` | `string` |  | OAuth scopes defining the level of access requested. |
| `tokenURL` | `string` |  | URL for obtaining OAuth tokens. |


**Responses:**

- `200` OK → `Tenant_Management_AuthenticationInfo`
- `415` Unsupported Media Type


---



## acx-mobile-push-notification-endpoint-controller

*1 endpoint*


### `POST` `/tenants/mobilePushNotifications`

**Add Mobile Push Notification**

Add mobile push notification.

operationId: `addMobilePushNotifications`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `app` | query |  | `string` |  |


**Request Body:** `Tenant_Management_MobilePushNotificationEndpoint`


**Responses:**

- `200` OK → `Tenant_Management_OperationResponseMobilePushNotificationEndpoint`
- `415` Unsupported Media Type


---


