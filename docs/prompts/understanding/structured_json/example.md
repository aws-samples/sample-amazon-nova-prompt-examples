# Structured JSON Output
Output well-formatted JSON. Here we're letting the model come up with its own data, but the same prompt would work with RAG contents as well.
We've incorporate a pre-filled response to the model to ensure we get json back, as described in our [documentation](https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html).

### User Prompt Template
    {Decription of desired output}.
    You MUST answer in JSON format only. 
    Please follow the output schema below.

    Output Schema:
    {
        "key1": "value1",
        "key2": "value2"
    }

## Example
### Amazon Nova Lite User Prompt
    Provide 5 examples of the best selling full-frame cameras in past three years.
    Follow the Output Schema as described below.
    Output Schema:
    {
    "name" : <string, the name of product>,
    "brand" : <string, the name of product>,
    "price" : <integer price>,
    "summary": <string, the product summary>
    }
    Only Respond in Valid JSON, without Markdown

### Amazon Nova Lite Assistant Prefilled Response
    "```json"

### Amazon Nova Lite Sample Response
!!! success "Response"
    ```json
    --8<-- "results/structured_json_20250326_165907.md"
    ```

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/structured_json/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/structured_json/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/structured_json/example.json"
    ```

