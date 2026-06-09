# Policy Evaluation

> RUCKUS One API Reference

---


## Criteria Evaluation

*Evaluates policy criteria provided and identifies the matching policy.*


*2 endpoints*


### `POST` `/policySetEvaluations`

**Evaluate Policy Criteria**

Evaluates provided policy criteria against all policies within a specified policy set to determine which policy matches the criteria. The evaluation process compares string, number, boolean, and date-time criteria against policy requirements. Returns the first matching policy with detailed evaluation results, or indicates no match was found. If a policy requires additional criteria that are not provided in the evaluation request, the evaluation will fail for that policy. Extra criteria provided

operationId: `evaluateReport_1`


**Request Body:** `Policy_Evaluation_Evaluation Report`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Policy_Evaluation_Links` |  |  |
| `evaluationCriteria` | `array` | ✓ | The complete list of criteria to evaluate against this policy set. |
| `identityGroupId` | `string` |  | Identity group identifier. If provided policy set associated to the identity group is evaluated prior to user provided policy set. |
| `onMatchResponse` | `string` |  | The response value that was defined in the policy that was matched. |
| `policyId` | `string` |  | The unique identifier of the specific policy that was found during evaluation. It will be ignored on the post and will not be set if no matching policy was found. |
| `policyName` | `string` |  | The name of the specific policy that was matched. Ignored on the post, and will not be set if no match was made. |
| `policyOverrideEnabled` | `boolean` |  | Indicates if policy override is enabled. |
| `policySetId` | `string` |  | The identifier for the policy set to evaluate. |
| `policyType` | `string` |  | The type of policy that was found during evaluation. Optional, and will be used on the post if it is a valid policy type, and can be evaluated. UNMATCHED, DPSK and RADIUS map to the existing policy types, any other policy types are not available. |
| `wasMatched` | `boolean` |  | The overall results of the matched request. This will be ignored on the post if it is provided. |


**Responses:**

- `200` Policy set was evaluated and results are returned. → `Policy_Evaluation_Evaluation Report`
- `400` Invalid evaluation criteria provided. → `Policy_Evaluation_ErrorResource`
- `404` Policy set to evaluate is not found. → `Policy_Evaluation_ErrorResource`
- `409` The Date range criteria provided could not be properly parsed. → `Policy_Evaluation_ErrorResource`


---

### `POST` `/policySets/{policySetId}/evaluationReports`

**Evaluate Criteria**

Evaluates the criteria provided and returns the matched response from the first matching policy within the specified set, or it will indicate that no match was found. A policy has additional required criteria and no matching test criteria is provided, that will be considered a failure. Additional test attributes that are provided but are not required within a policy will be ignored and not considered a match failure.

operationId: `evaluateReport`


**Parameters:**

| Name | In | Required | Type | Description |
|------|----|:--------:|------|-------------|
| `policySetId` | path | ✓ | `string` |  |


**Request Body:** `Policy_Evaluation_Evaluation Report V2`

| Field | Type | Required | Description |
|-------|------|:--------:|-------------|
| `_links` | `Policy_Evaluation_Links` |  |  |
| `evaluationCriteria` | `array` | ✓ | The complete list of criteria to evaluate against this policy set. |
| `identityGroupId` | `string` |  | Identity group identifier. If provided policy set associated to the identity group is evaluated prior to user provided policy set. |
| `onMatchResponse` | `string` |  | The response value that was defined in the policy that was matched. |
| `policyId` | `string` |  | The unique identifier of the specific policy that was found during evaluation. It will be ignored on the post and will not be set if no matching policy was found. |
| `policyName` | `string` |  | The name of the specific policy that was matched. Ignored on the post, and will not be set if no match was made. |
| `policyOverrideEnabled` | `boolean` |  | Indicates if policy override is enabled. |
| `policySetId` | `string` |  | The identifier for the policy set to evaluate. |
| `policyType` | `string` |  | The type of policy that was found during evaluation. Optional, and will be used on the post if it is a valid policy type, and can be evaluated. UNMATCHED, DPSK and RADIUS map to the existing policy types, any other policy types are not available. |
| `wasMatched` | `boolean` |  | The overall results of the matched request. This will be ignored on the post if it is provided. |


**Responses:**

- `200` Policy set was evaluated and results are returned. → `Policy_Evaluation_Evaluation Report V2`
- `400` Invalid evaluation criteria provided. → `Policy_Evaluation_ErrorResource`
- `404` Policy set to evaluate is not found. → `Policy_Evaluation_ErrorResource`
- `409` The Date range criteria provided could not be properly parsed. → `Policy_Evaluation_ErrorResource`


---


