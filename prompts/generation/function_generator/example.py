import json
import boto3

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )

response = bedrock_runtime.converse(
                modelId='us.amazon.nova-pro-v1:0',
                system = [
                    {
                        "text": """You are an expert Python developer who specializes in writing clean, efficient, and well-documented functions.
                            Follow these instructions:
                            1. Read and understand the function requirements in ## Requirements ##
                            2. Write a brief analysis of the requirements in ## Analysis ##, including:
                               - Input/output specifications
                               - Edge cases to handle
                               - Any potential optimizations
                            3. Write the Python function in ## Code ## using ```python``` code blocks
                            4. Include docstring documentation and type hints
                            5. Add example usage in ## Example ## using ```python``` code blocks
                            """
                    }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": """## Requirements ##
                                Create a function called 'group_by_frequency' that takes a list of any hashable items and returns a dictionary where:
                                - Keys are the frequencies (number of occurrences)
                                - Values are lists of items that appear that many times
                                - The items in each list should be sorted in their natural order
                                - Empty input should return an empty dictionary
                                For example: group_by_frequency([1,1,2,2,2,3]) should return {1: [3], 2: [1], 3: [2]}"""
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0.1,
                "topP": .99,
                "maxTokens": 1024
            }
            )

print(json.dumps(response, indent=2))