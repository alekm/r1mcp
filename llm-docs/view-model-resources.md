# View Model Resources

> RUCKUS One API Reference

---


## View Switch

*View Switch information. Note: this set of endpoints is used to view operational data. They don't provide the means to manage configuration.*


*10 endpoints*


### `POST` `/switches/aggregationDetails`

**Get Switches Aggregation Details**

Get parameters and operational data for a list of switches with aggregation details. This method will be removed no sooner than 06/30/2026. The following URL /venues/switches/aggregationDetails can be used for this content.

operationId: `getSwitchesAggregationDetails`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseGroupedSwitchDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseGroupedSwitchDto`


---

### `POST` `/switches/clients/query`

**Get Switch Clients**

Get a list of switch clients (i.e., end user devices). This method will be removed no sooner than 06/30/2026. The following URL /venues/switches/clients/query can be used for this content.

operationId: `getSwitchClients`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseSwitchClientDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseSwitchClientDto`


---

### `POST` `/switches/ports/query`

**Get Ports**

Get a list of parameters for the switch's ports. This method will be removed no sooner than 06/30/2026. The following URL /venues/switches/switchPorts/query can be used for this content.

operationId: `getPortList`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseSwitchPortDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseSwitchPortDto`


---

### `POST` `/switches/query/csvFiles`

**Export Switch Inventory**

Export the list of switches belong to the tenant. This method will be removed no sooner than 06/30/2026. The following URL /venues/switches/query/csvFiles can be used for this content.

operationId: `exportDeviceInventory`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_StreamingResponseBody`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_StreamingResponseBody`


---

### `POST` `/venues/switches/aggregationDetails`

**Get Switches Aggregation Details**

Get parameters and operational data for a list of switches with aggregation details.

operationId: `getSwitchesAggregationDetailsRbac`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseGroupedSwitchDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseGroupedSwitchDto`


---

### `POST` `/venues/switches/clients/query`

**Get Switch Clients**

Get a list of switch clients (i.e., end user devices).

operationId: `getSwitchClientsRbac`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseSwitchClientDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseSwitchClientDto`


---

### `POST` `/venues/switches/members/query`

**Query Members of Switches**

Get a list of members of switches.

operationId: `GetMembersOfSwitches`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseMembersOfSwitchDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseMembersOfSwitchDto`


---

### `POST` `/venues/switches/query`

**Get Switches of Venue**

Get a list of switches of venue.

operationId: `GetSwitchesOfVenue`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseSwitchDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseSwitchDto`


---

### `POST` `/venues/switches/query/csvFiles`

**Export Switch Inventory**

Export the list of switches belong to the tenant.

operationId: `exportDeviceInventoryRbac`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_StreamingResponseBody`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_StreamingResponseBody`


---

### `POST` `/venues/switches/switchPorts/query`

**Query Switch Ports**

Get a list of parameters for the switch's ports.

operationId: `QuerySwitchPorts`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseSwitchPortDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseSwitchPortDto`


---



## View Client Isolation Profiles

*Manage client isolation profiles for tenant queries and policy visibility.*


*1 endpoint*


### `POST` `/clientIsolationProfiles/query`

**Query Client Isolation Profiles**

Query client isolation profiles for tenant specific lists and configuration visibility.

operationId: `queryClientIsolationProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseClientIsolationProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseClientIsolationProfileQueryData`


---



## View VLAN Pool Profiles

*Manage VLAN (Virtual Local Area Network) pool profiles for viewing and queries.*


*1 endpoint*


### `POST` `/vlanPoolProfiles/query`

**Query VLAN Pool Profiles**

Query VLAN (Virtual Local Area Network) pool profiles available for tenant use.

operationId: `queryVlanPoolProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseVlanPoolProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseVlanPoolProfileQueryData`


---



## View SoftGRE Profile

*Provides SoftGRE profile API operations for querying tenant configurations and results.*


*1 endpoint*


### `POST` `/softGreProfiles/query`

**Query SoftGRE Profiles**

Retrieves SoftGRE profiles based on supplied dynamic query payload and filters.

operationId: `QuerySoftGreProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Request succeeded and returns SoftGRE profile data in the expected format. → `View_Model_Resources_QueryResponseSoftGreProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Feature not implemented for SoftGRE profile queries in this API. → `View_Model_Resources_QueryResponseSoftGreProfileQueryData`


---



## View Wi-Fi Profile

*View Wi-Fi service and policy profile information for VLAN pool policies.*


*28 endpoints*


### `POST` `/accessControlProfiles/query`

**Get Access Control Profiles**

Get data for a list of access control profiles available to tenants.

operationId: `getAccessControlPolicyProfiles_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/applicationPolicies/query`

**Get Application Policies**

Get data for a list of application policies available for wireless services.

operationId: `getApplicationProfiles_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseApplicationPolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/devicePolicies/query`

**Get Device Policies**

Get data for a list of device policies available for enforcement.

operationId: `getDeviceProfiles_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseDevicePolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/dhcpConfigServiceProfiles/query`

**Get DHCP Configuration Service Profiles**

Query DHCP configuration service profiles for the list.

operationId: `queryDhcpConfigServiceProfilesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseDhcpConfigServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedAccessControlProfiles/query`

**Get Access Control Profiles**

Get data for a list of access control profiles. This method will be removed no sooner than 06/30/2026. The following URL /accessControlProfiles/query can be used for this content.

operationId: `getAccessControlPolicyProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlPolicyProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedApplicationPolicies/query`

**Get Application Policies**

Get data for a list of application policies. This method will be removed no sooner than 06/30/2026. The following URL /applicationPolicies/query can be used for this content.

operationId: `getApplicationProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlSubProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedDevicePolicies/query`

**Get Device Policies**

Get data for a list of device policies. This method will be removed no sooner than 06/30/2026. The following URL /devicePolicies/query can be used for this content.

operationId: `getDeviceProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlSubProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedDhcpConfigServiceProfiles/query`

**Get DHCP Configuration Service Profiles**

Get data for a list of DHCP configuration service profiles. This method will be removed no sooner than 06/30/2026. The following URL /dhcpConfigServiceProfiles/query can be used for this content.

operationId: `getEnhancedDhcpConfigServiceProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseDhcpConfigServiceProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedIsolationAllowlists/query`

**Get Client Isolation Allowlists**

Get data for a list of client isolation allowlists. This method will be removed no sooner than 06/30/2026. The following URL /clientIsolationProfiles/query can be used for this content.

operationId: `getClientIsolationAllowlistsForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseIsolationAllowlistDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedL2AclPolicies/query`

**Get Layer 2 Policies**

Get data for a list of layer 2 policies. This method will be removed no sooner than 06/30/2026. The following URL /l2AclPolicies/query can be used for this content.

operationId: `getLayer2Profiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlSubProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedL3AclPolicies/query`

**Get Layer 3 Policies**

Get data for a list of layer 3 policies. This method will be removed no sooner than 06/30/2026. The following URL /l3AclPolicies/query can be used for this content.

operationId: `getLayer3Profiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlSubProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedMdnsProxyProfiles/query`

**Get Multicast DNS Proxy Profiles**

Get data for a list of multicast DNS proxy service profiles. This method will be removed no sooner than 06/30/2026. The following URL /multicastDnsProxyProfiles/query can be used for this content.

operationId: `getMulticastDnsProxyServiceProfilesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseMulticastDnsProxyServiceProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedRadiusServerProfiles/query`

**Get RADIUS Server Profiles**

Get data for a list of RADIUS server profiles. This method will be removed no sooner than 06/30/2026. The following URL /radiusServerProfiles/query can be used for this content.

operationId: `getRadiusServerProfiles_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseRadiusServerProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedRogueApPolicyProfiles/query`

**Get Rogue AP Policy Profiles**

Get data for a list of rogue AP policies. This method will be removed no sooner than 06/30/2026. The following URL /roguePolicies/query can be used for this content.

operationId: `getEnhancedRogueAPPolicyProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseRogueApPolicyProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedSyslogServerProfiles/query`

**Get Syslog Server Profiles**

Get data for a list of syslog server profiles. This method will be removed no sooner than 06/30/2026. The following URL /syslogServerProfiles/query can be used for this content.

operationId: `getSyslogServerProfilesForView_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseSyslogServerProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedVlanPoolProfiles/query`

**Get VLAN Pool Profiles**

Get data for a list of VLAN pool policy profiles. This method will be removed no sooner than 06/30/2026. The following URL /vlanPoolProfiles/query can be used for this content.

operationId: `getVlanPoolPolicyProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseVlanPoolVenueDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/enhancedWifiCallingProfiles/query`

**Get Wifi Calling Profiles**

Get data for a list of Wi-Fi calling service profiles. This method will be removed no sooner than 06/30/2026. The following URL /wifiCallingServiceProfiles/query can be used for this content.

operationId: `getWifiCallingServiceProfiles_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseWifiCallingServiceProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/hotspot20IdentityProviders/query`

**Get Hotspot 2.0 Identity Providers**

Get data for a list of Hotspot 2.0 identity providers.

operationId: `getHotspot20IdentityProviderForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseHotspot20IdentityProviderQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/hotspot20Operators/query`

**Get Hotspot 2.0 Operators**

Get data for a list of Hotspot 2.0 operators.

operationId: `getHotspot20OperatorForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseHotspot20OperatorQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/l2AclPolicies/query`

**Get Layer 2 Policies**

Get data for a list of layer 2 policies available for configuration.

operationId: `getLayer2Policies`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseL2AclPolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/l3AclPolicies/query`

**Get Layer 3 Policies**

Get data for a list of layer 3 policies available for configuration.

operationId: `getLayer3Policies`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseL3AclPolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/lbsServerProfiles/query`

**Get Location Based Service Server Profiles**

Get data for a list of location based service server profiles.

operationId: `getLbsServerProfileForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseLbsServerProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/multicastDnsProxyProfiles/query`

**Get Multicast DNS Proxy Profiles**

Get data for a list of multicast DNS proxy service profiles.

operationId: `queryMulticastDnsProxyProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseMulticastDnsProxyProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/radiusServerProfiles/query`

**Get RADIUS Server Profiles**

Get data for a list of RADIUS server profiles available to tenants.

operationId: `getRadiusServerProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseRadiusServerProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/roguePolicies/query`

**Get Rogue Policies**

Get the list of rogue policies in this tenant.

operationId: `getRoguePoliciesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseRoguePolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseRoguePolicyQueryData`


---

### `POST` `/syslogServerProfiles/query`

**Get Syslog Server Profiles**

Get data for a list of syslog server profiles.

operationId: `getSyslogServerProfilesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseSyslogServerProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/tunnelServiceProfiles/query`

**Get Tunnel Profiles**

Get data for a list of tunnel profiles. This is only permitted for users with feature flag edge role.

operationId: `getTunnelProfileProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` The operation was successful. → `View_Model_Resources_QueryResponseTunnelProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/wifiCallingServiceProfiles/query`

**Get Wifi Calling Profiles**

Get data for a list of Wi-Fi calling service profiles.

operationId: `getWifiCallingServiceProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseWifiCallingServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## View IPsec Profile

*Provides IPsec profile API operations for querying tenant configurations and results.*


*1 endpoint*


### `POST` `/ipsecProfiles/query`

**Query IPsec Profiles**

Query IPsec profiles based on specified criteria.

operationId: `QueryIPsecProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseIpsecProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseIpsecProfileQueryData`


---



## View Template

*View template information using /rec/templates for REC templates when needed.*


*1 endpoint*


### `POST` `/templates/query`

**Get Templates**

Get template information.

operationId: `getTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_TemplateData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseTemplateQueryData`


---



## View Portal Service Profiles

*Manage portal service profiles for tenant viewing and template queries.*


*2 endpoints*


### `POST` `/portalServiceProfiles/query`

**Query Portal Service Profiles**

Query portal service profile for the list.

operationId: `QueryPortalServiceProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponsePortalServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponsePortalServiceProfileQueryData`


---

### `POST` `/templates/portalServiceProfiles/query`

**Query Portal Service Profile Templates**

Query portal service profile template for the list.

operationId: `QueryPortalServiceProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponsePortalServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponsePortalServiceProfileQueryData`


---



## View Venue Template

*View venue template information using /rec/templates for REC templates when needed.*


*1 endpoint*


### `POST` `/templates/venues/query`

**Get Venue Templates**

Get venue templates.

operationId: `getVenueTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_VenueData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` internal server error → `View_Model_Resources_QueryResponseVenueDto`


---



## View Platform

*View platform information. Note: this group of endpoints is used to view operational data. They don't provide the means to manage configuration.*


*4 endpoints*


### `POST` `/venues/query`

**Get Venues**

Return a list of venue records.

operationId: `venue`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_VenueData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseVenueDto`


---

### `GET` `/venues/{venueId}/apModels`

**Get Venue AP Models**

Get the AP models deployed in this venue. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/clients/query can be used for this content.

operationId: `getVenueAPModels_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue ID |


**Responses:**

- `200` OK → `View_Model_Resources_AggregatedDeviceModelDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `GET` `/venues/{venueId}/aps/models`

**Get Venue AP Models**

Get the AP models deployed in this venue.

operationId: `getVenueAPModels`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue ID |


**Responses:**

- `200` OK → `View_Model_Resources_AggregatedDeviceModelDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/venues/{venueId}/rogueAps/query`

**Get Venue Rogue APs**

Get the list of rogue APs located in this venue.

operationId: `getVenueRogueAPs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue ID |


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseRogueApDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseRogueApDto`


---



## View Wi-Fi

*View Wi-Fi information. Note: this group of endpoints is used to view operational data. They don't provide the means to manage configuration.*


*10 endpoints*


### `POST` `/aps/aggregationDetails`

**Get APs Aggregation Details**

Get parameters and operational data for a list of APs with aggregation details. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/query can be used for this content.

operationId: `getAPsAggregationDetails`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseGroupedApDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/aps/query`

**Get APs**

Get parameters and operational data for a list of APs or mesh APs. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/query can be used for this content.

operationId: `GetAPs_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mesh` | query |  | `boolean` | Get mesh aps |


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseDeviceDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/aps/query/csvFiles`

**Export AP Inventory**

Export the list of APs belong to the tenant. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/query can be used for this content.

operationId: `exportDeviceInventory_1`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_StreamingResponseBody`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_StreamingResponseBody`


---

### `GET` `/clients`

**Get AP Clients**

Retrieve client end user device parameters and related operational data set. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/clients/query can be used for this content.

operationId: `getClients`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `apSerialNumber` | query |  | `string` |  |
| `page` | query |  | `integer` |  |
| `size` | query |  | `integer` |  |


**Responses:**

- `200` OK
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `GET` `/clients/{mac}`

**Get Client by MAC**

Get extended set of parameters and operational data for the client having this MAC address. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/clients/query can be used for this content.

operationId: `GetClientbyMAC`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mac` | path | ✓ | `string` |  |


**Responses:**

- `200` OK → `View_Model_Resources_ClientDeepPublicDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/cloudpaths/query`

**Get Cloudpath Servers**

Get a list of Cloudpath server information. This method will be removed no sooner than 06/30/2026.

operationId: `getCloudpathServers`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseCloudpathServerDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/guestUsers/query`

**Export Guest CSV**

Export guest to CSV.

operationId: `exportGuestCsv`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseGuestDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/guestUsers/query/csvFiles`

**Export Guest CSV**

Export guest to CSV. This method will be removed no sooner than 06/30/2026. The following URL /guestUsers/query can be used for this content.

operationId: `exportGuestCsv_1`


**Request Body:** `View_Model_Resources_GuestDetailsDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `dateFormat` | `string` |  |  |
| `guestIds` | `array` |  |  |
| `timezone` | `string` |  |  |


**Responses:**

- `200` Successful operation
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented


---

### `POST` `/venues/apGroups/query`

**Query AP Groups**

Query AP groups information.

operationId: `queryApGroups`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseApGroupQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/venues/aps/query`

**Get APs**

Get parameters and operational data for a list of APs or mesh APs.

operationId: `GetAPs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `mesh` | query |  | `boolean` | Get mesh aps |


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_ApQueryResponse`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## Network

*Network API (Application Programming Interface) for tenant network queries and counts.*


*1 endpoint*


### `POST` `/wifiNetworks/query`

**Get Wi-Fi Networks Data**

Retrieve Wi-Fi network information for tenants with filtering and pagination support.

operationId: `WifiNetworks`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_WifiNetworkQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseWifiNetworkQueryData`


---



## View Ethernet Port Profile

*Ethernet port profile API (Application Programming Interface) for tenant queries and management.*


*1 endpoint*


### `POST` `/ethernetPortProfiles/query`

**Get Ethernet Port Profiles**

Retrieve data for tenant Ethernet port profiles used across managed devices.

operationId: `getEthernetPortProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseEthernetPortProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## Quality of Service

*View Quality of Service (QoS) information for network performance insights.*


*1 endpoint*


### `POST` `/qosStatistics/query`

**Get the Statistics of Quality of Service**

Retrieve Quality of Service (QoS) statistics for tenant monitoring needs.

operationId: `viewQosStatistics`


**Request Body:** Yes


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseQosStatsDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## View Venue Topology

*View venue topology information for mesh and standard network layouts.*


*2 endpoints*


### `GET` `/venues/{venueId}/meshTopologies`

**Get Mesh Topology**

Get venue mesh topology data focused on mesh links and devices.

operationId: `getMeshTopology`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseTopologyResponseDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseTopologyResponseDto`


---

### `GET` `/venues/{venueId}/topologies`

**Get Topology**

Get venue topology data for visualizing devices and mesh connections.

operationId: `getTopology`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` |  |
| `meshOnly` | query | ✓ | `boolean` | Get mesh topology |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseTopologyResponseDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseTopologyResponseDto`


---



## View SNMP Agent Profiles

*Manage SNMP (Simple Network Management Protocol) agent profiles for tenants.*


*1 endpoint*


### `POST` `/snmpAgentProfiles/query`

**Query SNMP Agent Profiles**

Query SNMP (Simple Network Management Protocol) agent profiles for tenant lists.

operationId: `querySnmpAgentProfiles`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseSnmpAgentProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseSnmpAgentProfileQueryData`


---



## View Venue

*View venue information. Note: this group of endpoints is used to view operational data. They don't provide the means to manage configuration.*


*4 endpoints*


### `POST` `/venues/query`

**Get Venues**

Return a list of venue records.

operationId: `venue`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_VenueData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseVenueDto`


---

### `GET` `/venues/{venueId}/apModels`

**Get Venue AP Models**

Get the AP models deployed in this venue. This method will be removed no sooner than 06/30/2026. The following URL /venues/aps/clients/query can be used for this content.

operationId: `getVenueAPModels_1`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue ID |


**Responses:**

- `200` OK → `View_Model_Resources_AggregatedDeviceModelDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `GET` `/venues/{venueId}/aps/models`

**Get Venue AP Models**

Get the AP models deployed in this venue.

operationId: `getVenueAPModels`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue ID |


**Responses:**

- `200` OK → `View_Model_Resources_AggregatedDeviceModelDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/venues/{venueId}/rogueAps/query`

**Get Venue Rogue APs**

Get the list of rogue APs located in this venue.

operationId: `getVenueRogueAPs`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `venueId` | path | ✓ | `string` | Venue ID |


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseRogueApDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseRogueApDto`


---



## View Portal Service Template

*View portal service template information using /rec/templates for REC templates when needed.*


*1 endpoint*


### `POST` `/templates/portalServiceProfiles/query`

**Query Portal Service Profile Templates**

Query portal service profile template for the list.

operationId: `QueryPortalServiceProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponsePortalServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponsePortalServiceProfileQueryData`


---



## View Wi-Fi Template

*View Wi-Fi template information using /rec/templates for REC templates when needed.*


*16 endpoints*


### `POST` `/templates/accessControlProfiles/query`

**Get Access Control Profile Templates**

Get data for a list of access control profile templates.

operationId: `getAccessControlPolicyProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseAccessControlProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/applicationPolicies/query`

**Get Application Policy Templates**

Get data for a list of application policy templates.

operationId: `getApplicationPolicyTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseApplicationPolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/devicePolicies/query`

**Get Device Policy Templates**

Get data for a list of device policy templates.

operationId: `getDevicePolicyTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseDevicePolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/dhcpConfigServiceProfiles/query`

**Get DHCP Configuration Service Profile Templates**

Query DHCP configuration service profile templates for the list.

operationId: `queryDhcpConfigServiceProfileTemplatesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseDhcpConfigServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/ethernetPortProfiles/query`

**Get Ethernet Port Profile Templates**

Get data for a list of ethernet port profile templates.

operationId: `getEthernetPortProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseEthernetPortProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/ipsecProfiles/query`

**Query IPsec Profile Templates**

Query IPsec profile templates based on specified criteria.

operationId: `QueryIPsecProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseIpsecProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseIpsecProfileQueryData`


---

### `POST` `/templates/l2AclPolicies/query`

**Get Layer Two Policy Templates**

Get data for a list of layer 2 policy templates.

operationId: `getLayer2PolicyTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseL2AclPolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/l3AclPolicies/query`

**Get Layer Three Policy Templates**

Get data for a list of layer 3 policy templates.

operationId: `getLayer3PolicyTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseL3AclPolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/radiusServerProfiles/query`

**Get RADIUS Server Profile Templates**

Get data for a list of RADIUS server profile templates with enhanced query data.

operationId: `getRadiusServerProfileTemplatesV2`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseRadiusServerProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/roguePolicies/query`

**Get Rogue Policy Templates**

Get the list of rogue policy templates in this tenant.

operationId: `getRoguePolicyTemplatesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseRoguePolicyQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseRoguePolicyQueryData`


---

### `POST` `/templates/syslogServerProfiles/query`

**Get Syslog Server Profile Templates**

Get data for a list of syslog server profile templates.

operationId: `getSyslogServerProfileTemplatesForView`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseSyslogServerProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/tunnelServiceProfiles/query`

**Get Tunnel Profile Templates**

Get data for a list of tunnel profile templates. This is only permitted for users with feature flag edge role.

operationId: `getTunnelProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseTunnelProfileDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/venues/apGroups/query`

**Get AP Group Templates**

Get AP group template information.

operationId: `getApGroupTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseApGroupQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/vlanPoolProfiles/query`

**Query VLAN Pool Profile Templates**

Query VLAN pool profile templates.

operationId: `queryVlanPoolProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseVlanPoolProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` Not implemented → `View_Model_Resources_QueryResponseVlanPoolProfileQueryData`


---

### `POST` `/templates/wifiCallingServiceProfiles/query`

**Get Wifi Calling Profile Templates**

Get data for a list of wifi calling service profile templates.

operationId: `getWifiCallingServiceProfileTemplates`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseWifiCallingServiceProfileQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---

### `POST` `/templates/wifiNetworks/query`

**Get Wi-Fi Network Templates**

Get Wi-Fi network template information.

operationId: `WifiNetworkTemplate`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_WifiNetworkQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseWifiNetworkQueryData`


---



## Client API

*Client API (Application Programming Interface) for querying access point clients across venues.*


*1 endpoint*


### `POST` `/venues/aps/clients/query`

**Query AP Clients**

Query AP (Access Point) clients for tenant usage analytics and inventory.

operationId: `QueryApClients`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseApClientQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseApClientQueryData`


---



## Edge SD-LAN Status

*Edge SD-LAN status API.*


*1 endpoint*


### `POST` `/edgeSdLanServices/query`

**Query Edge SD-LAN List**

Query SD-LAN list of Edge.

operationId: `queryEdgeSdLans`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` The operation was successful. → `View_Model_Resources_QueryResponseEdgeSdLanStatusDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## View Device Import Requests

*View device import requests information.*


*1 endpoint*


### `POST` `/venues/aps/importRequests/query`

**Get APs Import Requests**

Retrieve per venue AP import status and results. Use a request ID to filter and track the progress of specific import operations.

operationId: `GetAPsImportRequests`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` Successful operation → `View_Model_Resources_QueryResponseImportRequestQueryData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## AP SNMP Agents

*1 endpoint*


### `POST` `/snmpAgents/query`

**Get AP SNMP Agents**

Get data for a list of AP SNMP agents. This method will be removed no sooner than 06/30/2026. The following URL /snmpAgentProfiles/query can be used for this content.

operationId: `getApSnmpAgents`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_QueryResponseApSnmpAgentDto`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error


---



## venue

*1 endpoint*


### `POST` `/venues/query`

**Get Venues**

Return a list of venue records.

operationId: `venue`


**Request Body:** `View_Model_Resources_DynamicQueryPayloadDto`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `excludeFilters` | `object` |  | Exclusion filters as key value pairs defining values to omit from results. |
| `exists` | `string` |  | Field name that must exist within each document matched by the query execution. |
| `fields` | `array` |  | Set of field names to include in response payload for each record. |
| `filters` | `object` |  | Filters provided as key value pairs defining inclusion criteria for query execution. |
| `groupBy` | `string` |  | Field name used to group aggregated results when producing grouped query responses. |
| `matchFields` | `array` |  | List of match field filters specifying terms that must align with query criteria. |
| `multiSortFields` | `array` |  | List of multiple field names applied for compound sorting logic in results. |
| `mustHaveFields` | `array` |  | List of fields that must exist on documents returned by the query. |
| `mustNotHaveFields` | `array` |  | List of fields that must not exist on documents included in results. |
| `mustNotMatchField` | `array` |  |  |
| `page` | `integer` |  | Page number indicating current position within paginated query results. |
| `pageByDate` | `object` |  | Pagination by date entry specifying anchor timestamp for search after pagination. |
| `pageSize` | `integer` |  | Number of items per page controlling volume of results returned per page. |
| `queryStringOrFilter` | `View_Model_Resources_QueryStringOrMacFilterDto` |  | Query string or MAC filter configuration combining text search and device matching. |
| `rangeDateFilter` | `View_Model_Resources_RangeFilterDto` |  | Range date filter configuration defining temporal boundaries for returned records. |
| `rangeFilter` | `View_Model_Resources_RangeFilterDto` |  | Range filter configuration defining numeric or date boundaries for query results. |
| `searchString` | `string` |  | Search string representing the user query applied across designated target fields. |
| `searchTargetFields` | `array` |  | List of target field names that should be queried for search string matching. |
| `search_after` | `array` |  | Search after values used to continue pagination without relying on offsets. |
| `sortDescriptors` | `array` |  | List of sort descriptors defining multi level sort behaviors for query responses. |
| `sortField` | `string` |  | Field name used to sort query results within the returned data. |
| `sortOrder` | `string` |  | Sort order specifying ascending or descending direction for query results. |
| `termField` | `View_Model_Resources_TermFieldDto` |  | Term field filter configuration specifying exact match criteria for a field. |
| `terms` | `object` |  | Filter terms represented as key value pairs applied to refine result sets. |


**Responses:**

- `200` successful operation → `View_Model_Resources_VenueData`
- `400` Bad/malformed request
- `401` Unauthorized
- `403` Forbidden
- `404` Requested resource or related entity not found
- `422` Validation error
- `500` Internal Server Error
- `501` not implemented → `View_Model_Resources_QueryResponseVenueDto`


---


