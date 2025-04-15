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
                        "text": """You are an expert Git user who can translate natural language descriptions into precise Git commands.
                            Follow these instructions:
                            1. Read and understand the version control task in ### Task ###
                            2. Analyze the requirements and the scenario, think step by step, and put your thoughts in ### Analysis ### in markdown formatting. Consider the following:
                               - Required Git operations
                               - Any potential risks or considerations
                               - Alternative approaches if applicable
                            3. Provide the Git commands in ### Commands ### using ```bash``` code blocks
                            4. Add explanations for each command in ### Explanation ### in markdown formatting.
                            """
                    }
                ],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": """### Task ###
                                I accidentally committed some sensitive credentials to my main branch in my last commit, but haven't pushed yet. I need to:
                                1. Remove the sensitive data from the commit
                                2. Keep all other changes from that commit
                                3. Make sure the credentials are ignored in future commits
                                The sensitive file is at 'config/credentials.json'."""
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