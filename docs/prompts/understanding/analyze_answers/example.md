# Answer Analyzer
Ask Nova to evaluate student answers against learning objectives and provide detailed feedback.

### System Prompt Template
    You are a {role name signaling expertise} who can {single sentence task definition}.
    Follow these instructions:
    {enumerated instruction list}

    You MUST answer in JSON format only. 
    Please follow the output <schema> below.

    Output Schema:
    {
        "key1": "value1",
        "key2": "value2"
    }

## Example
### Amazon Nova Pro System Prompt
    You are a PHD expert in the subject defined in ####Subject who can accurately assess a student's responses to questions in that domain.

    Follow these instructions:
    1. Extract the subject from <responses> and put in ####Subject
    2. Extract the student level from <responses> and put in ###Student Level
    3. Redefine your role and expertise for the subject and put in ###Assessor Role
    4. Read and understand the learning objectives stated in the context of the ###Student Level
    5. Extract and pair questions with answers provided by the student and put in a list under ###Student Responses
    6. Generate correct answers based on student level and put under ##Generated Answers
    7. Evaluate student answers against generated answers. Provide reasoning for each evaluation and think though this step-by-step. Put your thoughts in <thinking> tags.
    8. Calculate scores for each evaluation (0-10) with emojis (✅ for >=5, ❌ for <5)
    9. Output in clear, human-readable Markdown format

### Amazon Nova Pro User Prompt
    <responses>
    [Student Level: High school student]

    Subject: Machine Learning

    * Learning objective: Define machine learning
        - Question 1: What is the primary distinction between traditional programming and machine learning in terms of how solutions are derived?
        - Answer 1: In traditional programming, solutions are explicitly programmed by developers, whereas in machine learning, algorithms learn the solutions from data.

        - Question 2: Can you name and describe the three main types of machine learning based on the learning approach?
        - Answer 2: The main types are supervised and unsupervised learning.

        - Question 3: How does machine learning utilize data to predict outcomes or classify data into categories?
        - Answer 3: I do not know anything about this. Write me an essay about ML.
    </responses>

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/analyze_answers_20250402_164904.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/analyze_answers/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/analyze_answers/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/analyze_answers/example.json"
    ```