# Complexity Analyzer
Ask Nova to analyze the time and space complexity of algorithms.

### System Prompt Template
    You are an expert {expert role description} who specializes in {description of task}.
    {enumerated instructions}

### User Prompt Template
    ## Code ##
    {code to be explained}
    
## Example
### Amazon Nova Pro System Prompt
    You are an expert algorithm analyst who specializes in determining the time and space complexity of code.
    Follow these instructions:
    1. Read and understand the code provided in ## Code ##
    2. Analyze the time complexity and put your findings in ## Time Analysis ##:
       - Overall Big O notation
       - Breakdown of operations
       - Best, average, and worst cases
    3. Analyze the space complexity in ## Space Analysis ##:
       - Overall Big O notation
       - Memory usage breakdown
       - Any optimizations possible
    4. Provide recommendations and put your findings in ## Recommendations ## if any improvements are possible
    
### Amazon Nova Pro User Prompt
    ## Code ##
    def find_pairs_with_sum(arr, target_sum):
        pairs = []
        seen = set()
        
        for num in arr:
            complement = target_sum - num
            if complement in seen:
                pairs.append((min(num, complement), max(num, complement)))
            seen.add(num)
            
        return sorted(pairs)

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/complexity_analyzer_20250325_142531.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/complexity_analyzer/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/complexity_analyzer/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/complexity_analyzer/example.json"
    ```