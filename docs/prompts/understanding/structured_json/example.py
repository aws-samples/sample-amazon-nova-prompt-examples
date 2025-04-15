import boto3
import json

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )


response = bedrock_runtime.converse(
                modelId='us.amazon.nova-lite-v1:0',
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": """Provide 5 examples of the best selling full-frame cameras in past three years.
                            
You MUST answer in JSON format only. Please follow the output schema below.

**Output Schema:**
```json
[
  {
    "name": "string, the name of the camera",
    "brand": "string, the brand name",
    "price": "integer or string with price",
    "summary": "string, brief product description"
  }
]
```

DO NOT provide any preamble text. Return ONLY the JSON object."""
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
                "maxTokens": 1000,
                "stopSequences": ["```"]
            }
            )

print(json.dumps(response, indent=2))