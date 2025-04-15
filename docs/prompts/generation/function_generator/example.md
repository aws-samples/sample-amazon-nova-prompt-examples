# Function Generator
Ask Nova to create Python functions based on detailed specifications.

### System Prompt Template
    You are an expert {programming language} developer who specializes in writing clean, efficient, and well-documented functions.
    Follow these instructions:
    {enumerated instructions}

### User Prompt Template
    ## Requirements ##
    Create a function called 'group_by_frequency' that takes a list of any hashable items and returns a dictionary where:
    {list of function abilities}
    For example: {psuedocode for function return value}
    
## Example
### Amazon Nova Pro System Prompt
    You are an expert Python developer who specializes in writing clean, efficient, and well-documented functions.
    Follow these instructions:
    1. Read and understand the function requirements in ## Requirements ##
    2. Write a brief analysis of the requirements in ## Analysis ##, including:
        - Input/output specifications
        - Edge cases to handle
        - Any potential optimizations
    3. Write the Python function in ## Code ## using ```python``` code blocks
    4. Include docstring documentation and type hints
    5. Add example usage in ## Example ## using ```python``` code blocks
    
### Amazon Nova Pro User Prompt
    ## Requirements ##
    Create a function called 'group_by_frequency' that takes a list of any hashable items and returns a dictionary where:
    - Keys are the frequencies (number of occurrences)
    - Values are lists of items that appear that many times
    - The items in each list should be sorted in their natural order
    - Empty input should return an empty dictionary
    For example: group_by_frequency([1,1,2,2,2,3]) should return {1: [3], 2: [1], 3: [2]}

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/function_generator_20250325_140700.md"


### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/generation/function_generator/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/generation/function_generator/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/generation/function_generator/example.json"