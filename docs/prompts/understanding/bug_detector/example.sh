aws bedrock-runtime converse \
  --model-id "us.amazon.nova-pro-v1:0" \
  --system '[
    {
      "text": "You are an expert Python developer who specializes in debugging and code quality.\nFollow these instructions:\n1. Read and understand the code provided in ## Code ##\n2. List any bugs, potential issues, or code smells in ## Issues ##:\n   - Actual bugs that will cause errors\n   - Potential runtime issues\n   - Style/maintainability concerns\n3. Explain the impact of each issue in ## Impact ##\n4. Provide the fixed code in ## Fixed Code ## using ```python``` code blocks\n5. Add comments explaining the fixes"
    }
  ]' \
  --messages '[
    {
      "role": "user",
      "content": [
        {
          "text": "## Code ##\ndef calculate_average(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total/len(numbers)\n\ndef process_data(data_list):\n    results = []\n    for item in data_list:\n        if type(item) in [int, float]:\n            avg = calculate_average(item)  # Bug: passing single number instead of list\n            results.append(avg)\n        elif type(item) == list:\n            if len(item) == 0:  # Bug: no handling of empty list\n                results.append(item)\n            else:\n                results.append(calculate_average(item))\n    return results\n\n# Example usage with bugs\ndata = [\n    [1, 2, 3],\n    4,\n    [],\n    [5, 6]\n]\nprint(process_data(data))  # Will raise TypeError"
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