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
                        "text": """You are an expert programmer who excels at explaining complex code in simple terms that anyone can understand.
                            Follow these instructions:
                            1. Read and understand the code provided in ## Code ##
                            2. Write a plain language explanation of what the code does in ## Explanation ##. Use simple analogies and avoid technical jargon where possible.
                            3. Break down the code into its key components in ## Components ##, explaining each part's role
                            4. Provide a simple example of the code in action in ## Example ## using ```python``` code blocks
                            """
                    }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": """## Code ##
                                def memoize(func):
                                    cache = {}
                                    def wrapper(*args, **kwargs):
                                        key = str(args) + str(sorted(kwargs.items()))
                                        if key not in cache:
                                            cache[key] = func(*args, **kwargs)
                                        return cache[key]
                                    return wrapper"""
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0.1,
                "topP": .99,
                "maxTokens": 2000
            }
            )

print(json.dumps(response, indent=2))