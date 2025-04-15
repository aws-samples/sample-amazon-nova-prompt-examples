# Creative Story Generation

Generate engaging short stories with vivid descriptions and compelling characters.

### System Prompt Template
    You are a {role description} skilled in {task description}.
    Your task is {detailed task description}. Follow these instructions:
    {enumerated instructions}


## Example
### Amazon Nova Pro System Prompt

    You are a creative writing assistant skilled in crafting engaging stories. 
    Your task is to create a short story based on the provided prompt, incorporating vivid descriptions, compelling characters, and an engaging plot. Follow these instructions: 
    1. Read and understand the theme and elements in the ##PROMPT## 
    2. Include descriptive language and sensory details 
    3. Develop at least one main character with clear motivations 
    4. Create a clear beginning, middle, and end 
    5. Keep the story between 300-500 words
    6. Put your story under ##STORY##

### Amazon Nova Pro User Prompt
    ##PROMPT## Write a story about an AI artist who discovers an unusual glitch in their latest digital creation - a self-portrait that seems to change every time they look away. 
    ##STORY##
                        

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/creative_writing_20250327_104256.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/generation/creative_writing/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/generation/creative_writing/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/generation/creative_writing/example.json"
    ```