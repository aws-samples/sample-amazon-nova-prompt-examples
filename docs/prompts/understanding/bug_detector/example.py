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
                        "text": """You are an expert Python developer who specializes in debugging and code quality.
                            Follow these instructions:
                            1. Read and understand the code provided in ## Code ##
                            2. List any bugs, potential issues, or code smells in ## Issues ##:
                               - Actual bugs that will cause errors
                               - Potential runtime issues
                               - Style/maintainability concerns
                            3. Explain the impact of each issue in ## Impact ##
                            4. Provide the fixed code in ## Fixed Code ## using ```python``` code blocks
                            5. Add comments explaining the fixes
                            """
                    }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": """## Code ##
                                def calculate_average(numbers):
                                    total = 0
                                    for num in numbers:
                                        total += num
                                    return total/len(numbers)

                                def process_data(data_list):
                                    results = []
                                    for item in data_list:
                                        if type(item) in [int, float]:
                                            avg = calculate_average(item)  # Bug: passing single number instead of list
                                            results.append(avg)
                                        elif type(item) == list:
                                            if len(item) == 0:  # Bug: no handling of empty list
                                                results.append(item)
                                            else:
                                                results.append(calculate_average(item))
                                    return results

                                # Example usage with bugs
                                data = [
                                    [1, 2, 3],
                                    4,
                                    [],
                                    [5, 6]
                                ]
                                print(process_data(data))  # Will raise TypeError"""
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