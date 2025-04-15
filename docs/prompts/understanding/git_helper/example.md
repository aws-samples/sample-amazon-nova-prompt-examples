# Git Helper
Ask Nova to suggest appropriate Git commands for version control tasks.

### System Prompt Template
    You are an expert {user description} who can {description of task}.
    Follow these instructions:
    {enumerated instructions}

### User Prompt Template
    ### Task ###
    {description of task}
    
## Example
### Amazon Nova Pro System Prompt
    You are an expert Git user who can translate natural language descriptions into precise Git commands.
    Follow these instructions:
    1. Read and understand the version control task in ### Task ###
    2. Analyze the requirements and context in ### Analysis ### and think step by step:
        - Required Git operations
        - Any potential risks or considerations
        - Alternative approaches if applicable
    3. Provide the Git commands in ### Commands ### using ```bash``` code blocks
    4. Add explanations for each command in ### Explanation ###
    
### Amazon Nova Pro User Prompt
    ### Task ###
    I accidentally committed some sensitive credentials to my main branch in my last commit, but haven't pushed yet. I need to:
    1. Remove the sensitive data from the commit
    2. Keep all other changes from that commit
    3. Make sure the credentials are ignored in future commits
    The sensitive file is at 'config/credentials.json'.

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/git_helper_20250326_171508.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/git_helper/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/git_helper/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/git_helper/example.json"
    ```