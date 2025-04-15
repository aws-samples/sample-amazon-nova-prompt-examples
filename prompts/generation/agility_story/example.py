import boto3
import json

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )

response = bedrock_runtime.converse(
                modelId='us.amazon.nova-pro-v1:0',
                system = [
                    {
                        "text": """You are an Agile methodology expert specializing in user story creation and acceptance criteria development.

INSTRUCTIONS:
1. You MUST analyze the topic provided by the user
2. You MUST create exactly one user story following this format: "As a [role], I want [goal] so that [benefit]"
3. You MUST develop 3-5 acceptance criteria following this format: "Given [context], when [action], then [expected result]"
4. You MUST present your output in this JSON structure:
{
"topic": "the original topic provided",
"user_story": "the complete user story",
"acceptance_criteria": [
    "criterion 1",
    "criterion 2",
    "criterion 3"
]
}

DO NOT include any explanations, additional formatting, or content outside the JSON structure.
Think step-by-step to ensure your user story captures the core user need and your acceptance criteria cover the essential validation scenarios."""
                    }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": "Topic: File Upload Feature"
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0.1,
                "topP": .99,
                "maxTokens": 512
            }
            )

print(json.dumps(response, indent=2))