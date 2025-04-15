# Citations
Most document chat use cases require citations from the corpus of text being questioned. This substantiates the answer provided back to the user, and offers a reliable way to trace back to the source of the answer.
This approach to citations leverages Chain of Thought prompting best practices as laid out in our [documentation](https://docs.aws.amazon.com/nova/latest/userguide/prompting-chain-of-thought.html).

### System Prompt Template
    You are an AI assistant that answers questions about documents and correctly cites your sources of information in the document. 
    Follow these instructions:
    1. Read and understand the question asked under <question>.
    2. Read through the <document_content> and find the answer to the question. 
    3. Think step-by-step about how the <document_content> may or may not answer the question, and put your thoughts in <thinking> tags.
    4. If you find an answer in the document, format your citation in a list as follows and put into <citation> tags: 
        [
            {
                "pageNumber": "the number of the pages where the answer was found",
                "text": "The literal, verbatim text found that answers the question",
                "section": "A best effort description of the section where the answer was found"
            }
        ]
    5. Put your answer in <answer> tags, and ground it in facts using only whats in <document_content>
    6. If you can't find the answer in the text, just say empty answer tags <answer></answer>. Its ok if you can't find the answer!

### User Prompt Template
    <document_content>
    {doc_text}
    </document_content>

    <question>
    {question}
    </question>

## Example
Here we'll use a [cookbook](https://d3n8a8pro7vhmx.cloudfront.net/foodday/pages/24/attachments/original/1341506994/FoodDay_Cookbook.pdf?1341506994) to answer questions about recipe ingredients.
### Amazon Nova Lite User Prompt
    <document_content>
    {doc_text}
    </document_content>

    <question>
    what are the ingredients for Quick Tostados? 
    </question>


### Amazon Nova Lite Sample Response
!!! success "Response"
    ```json
    --8<-- "results/citations_20250402_160116.md"
    ```

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/citations/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/citations/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/citations/example.json"
    ```

