aws bedrock-runtime converse \
  --model-id "us.amazon.nova-pro-v1:0" \
  --system '[
    {
      "text": "You are an expert programmer who excels at explaining complex code in simple terms that anyone can understand.\nFollow these instructions:\n1. Read and understand the code provided in ## Code ##\n2. Write a plain language explanation of what the code does in ## Explanation ##. Use simple analogies and avoid technical jargon where possible.\n3. Break down the code into its key components in ## Components ##, explaining each part'\''s role\n4. Provide a simple example of the code in action in ## Example ## using ```python``` code blocks"
    }
  ]' \
  --messages '[
    {
      "role": "user",
      "content": [
        {
          "text": "## Code ##\ndef memoize(func):\n    cache = {}\n    def wrapper(*args, **kwargs):\n        key = str(args) + str(sorted(kwargs.items()))\n        if key not in cache:\n            cache[key] = func(*args, **kwargs)\n        return cache[key]\n    return wrapper"
        }
      ]
    }
  ]' \
  --inference-config '{
    "temperature": 0.1,
    "topP": 0.99,
    "maxTokens": 512
  }' \
  --region us-west-2