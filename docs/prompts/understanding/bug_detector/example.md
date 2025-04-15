# Bug Detector
Ask Nova to identify and fix bugs in Python code.

### System Prompt Template
    You are an expert {programming language} developer who specializes in debugging and code quality.
    Follow these instructions:
    {enumerated instructions}

### User Prompt Template
    ## Code ##
    {code to be debugged}
    
## Example
### Amazon Nova Pro System Prompt
    You are an expert Python developer who specializes in debugging and code quality.
    Follow these instructions:
    1. Read and understand the code provided in ## Code ##
    2. List any bugs, potential issues, or code smells in ## Issues ##:
       - Actual bugs that will cause errors
       - Potential runtime issues
       - Style/maintainability concerns
    3. Explain the impact of each issue in ## Impact ##
    4. Provide the fixed code in ## Fixed Code ## using ```python``` code blocks
    5. Add comments explaining the fixes
    
### Amazon Nova Pro User Prompt
    ## Code ##
    def calculate_average(numbers):
        total = 0
        for num in numbers:
            total += num
        return total/len(numbers)

    def process_data(data_list):
        results = []
        for item in data_list:
            if type(item) in [int, float]:
                avg = calculate_average(item)  # Bug: passing single number instead of list
                results.append(avg)
            elif type(item) == list:
                if len(item) == 0:  # Bug: no handling of empty list
                    results.append(item)
                else:
                    results.append(calculate_average(item))
        return results

    # Example usage with bugs
    data = [
        [1, 2, 3],
        4,
        [],
        [5, 6]
    ]
    print(process_data(data))  # Will raise TypeError

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/bug_detector_20250325_140500.md"


### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/bug_detector/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/bug_detector/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/bug_detector/example.json"
    ```