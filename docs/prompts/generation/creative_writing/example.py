import boto3
import json 

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )

response = bedrock_runtime.converse(
    modelId="us.amazon.nova-pro-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": """##PROMPT## Write a story about an AI artist who discovers an unusual glitch in their latest digital creation - a self-portrait that seems to change every time they look away. 
                    ##STORY##
                    """
                }
            ]
        }
    ],
    system=[
        {
            "text": """You are a creative writing assistant skilled in crafting engaging stories. Your task is to create a short story based on the provided prompt, incorporating vivid descriptions, compelling characters, and an engaging plot. Follow these instructions: 
            1. Read and understand the theme and elements in the ##PROMPT## 
            2. Include descriptive language and sensory details 
            3. Develop at least one main character with clear motivations 
            4. Create a clear beginning, middle, and end 
            5. Keep the story between 300-500 words
            6. Put your story under ##STORY##"""
        }
    ],
    inferenceConfig={
        "temperature": 0.7,
        "topP": 0.9,
        "maxTokens": 2048,
        "stopSequences": ["##END##"]
    }
)

print(json.dumps(response, indent=2))