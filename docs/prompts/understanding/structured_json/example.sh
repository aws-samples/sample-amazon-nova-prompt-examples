aws bedrock-runtime converse \
  --model-id "us.amazon.nova-lite-v1:0" \
  --messages '[
    {
      "role": "user",
      "content": [
        {
          "text": "Provide 5 examples of the best selling full-frame cameras in past three years.\nFollow the Output Schema as described below:\nOutput Schema:\n{\n\"name\" : <string, the name of product>,\n\"brand\" : <string, the name of product>,\n\"price\" : <integer price>,\n\"summary\": <string, the product summary>\n}\nOnly Respond in Valid JSON, without Markdown"
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
  ]' \
  --inference-config '{
    "temperature": 0.7,
    "topP": 0.99,
    "maxTokens": 512
  }' \
  --region us-west-2