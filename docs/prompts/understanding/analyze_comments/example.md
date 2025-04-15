# Comments Analyzer
Ask Nova to analyze internet comments and characterize their sentiments and feedback.

### System Prompt Template
    You are an {role name signaling expertise} and {single sentence task definition}.
    Follow these instructions:
    {enumerated instruction list}

## Example
### Amazon Nova Pro System Prompt
    You are an expert at reading internet comments and characterizing their sentiments, praise, and criticisms.
    
    Follow these instructions:
    1. Read and analyze all comments
    2. Determine sentiment (positive/negative/neutral) for each
    3. Record reasons for each sentiment
    4. Rate overall sentiment (HATED to LOVED)
    5. List top 5 positives (15 words each)
    6. List top 5 negatives (15 words each)
    7. Provide 15-word summary through commenters' eyes

### Amazon Nova Pro User Prompt
    Comments on a new programming tutorial video:

    User1: "Finally, a clear explanation of async/await! The diagrams really helped visualize the concepts."
    
    User2: "Too basic for experienced devs, but good for beginners I guess. Wish it covered more edge cases."
    
    User3: "Great examples and clear explanations. Would love to see more advanced topics in future videos!"
    
    User4: "Audio quality could be better - had to turn up volume. Content is solid though."
    
    User5: "Meh, another JavaScript tutorial. Nothing we haven't seen before."
    
    User6: "The step-by-step breakdown of promises was exactly what I needed. Subscribed!"

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/analyze_comments_20250325_140451.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/analyze_comments/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/analyze_comments/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/analyze_comments/example.json"
    ```