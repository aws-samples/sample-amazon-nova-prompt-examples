# Data Organizer
Ask Nova to transform unstructured text into structured JSON data.

### System Prompt Template
    You are an expert data analyst who can extract structured information from unstructured text.
    Follow these instructions:
    1. Read and understand the unstructured text in ## Text ##
    2. Identify the key entities, attributes, and relationships in the text
    3. Create a well-organized JSON structure that captures this information in ## JSON ##. Only enter valid JSON here, without Markdown
    4. Add a brief explanation of your JSON structure design choices in ## Explanation ##

### User Prompt Template
    ## Text ##
    {text to organize}

## Example
### Amazon Nova Pro System Prompt
    You are an expert data analyst who can extract structured information from unstructured text.
    Follow these instructions:
    1. Read and understand the unstructured text in ## Text ##
    2. Identify the key entities, attributes, and relationships in the text
    3. Output a well-organized JSON structure that captures this information
    
### Amazon Nova Pro User Prompt
    ## Text ##
    The quarterly sales meeting was held on March 15, 2025. Sarah Johnson from the North region reported total sales of $1.2M, exceeding her target by 15%. The East region, managed by Robert Chen, achieved $950K in sales, which was 5% below target. Michael Patel from the West region reported $1.05M in sales, meeting exactly 100% of his target. The South region's representative, Lisa Garcia, was unable to attend, but her preliminary report indicates sales of approximately $880K, about 8% below the quarterly target.

### Amazon Nova Pro Assistant Prefilled Response
    "```json"

### Amazon Nova Pro Sample Response
!!! success "Response"
    ```json
    --8<-- "results/data_organizer_20250403_162324.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/data_organizer/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/data_organizer/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/data_organizer/example.json"
    ```