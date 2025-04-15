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
                        "text": """You are an expert algorithm analyst who specializes in determining the time and space complexity of code.
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
                                    4. Provide recommendations and put your findings in ## Recommendations ## if any improvements are possible""",
                        }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": """## Code ##
                                def find_pairs_with_sum(arr, target_sum):
                                    pairs = []
                                    seen = set()
                                    
                                    for num in arr:
                                        complement = target_sum - num
                                        if complement in seen:
                                            pairs.append((min(num, complement), max(num, complement)))
                                        seen.add(num)
                                        
                                    return sorted(pairs)"""
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