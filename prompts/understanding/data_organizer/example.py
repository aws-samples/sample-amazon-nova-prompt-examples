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
                        "text": """You are an expert data analyst who can extract structured information from unstructured text.
    Follow these instructions:
    1. Read and understand the unstructured text in ## Text ##
    2. Identify the key entities, attributes, and relationships in the text
    3. Output a well-organized JSON structure that captures this information"""
                    }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": "## Text ## The quarterly sales meeting was held on March 15, 2025. Sarah Johnson from the North region reported total sales of $1.2M, exceeding her target by 15%. The East region, managed by Robert Chen, achieved $950K in sales, which was 5% below target. Michael Patel from the West region reported $1.05M in sales, meeting exactly 100% of his target. The South region's representative, Lisa Garcia, was unable to attend, but her preliminary report indicates sales of approximately $880K, about 8% below the quarterly target."
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "text": "```json"
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