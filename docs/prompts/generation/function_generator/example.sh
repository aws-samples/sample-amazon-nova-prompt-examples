aws bedrock-runtime converse \
  --model-id "us.amazon.nova-pro-v1:0" \
  --system '[
    {
      "text": "You are an expert Python developer who specializes in writing clean, efficient, and well-documented functions.\nFollow these instructions:\n1. Read and understand the function requirements in ## Requirements ##\n2. Write a brief analysis of the requirements in ## Analysis ##, including:\n   - Input/output specifications\n   - Edge cases to handle\n   - Any potential optimizations\n3. Write the Python function in ## Code ## using ```python``` code blocks\n4. Include docstring documentation and type hints\n5. Add example usage in ## Example ## using ```python``` code blocks"
    }
  ]' \
  --messages '[
    {
      "role": "user",
      "content": [
        {
          "text": "## Requirements ##\nCreate a function called '\''group_by_frequency'\'' that takes a list of any hashable items and returns a dictionary where:\n- Keys are the frequencies (number of occurrences)\n- Values are lists of items that appear that many times\n- The items in each list should be sorted in their natural order\n- Empty input should return an empty dictionary\nFor example: group_by_frequency([1,1,2,2,2,3]) should return {1: [3], 2: [1], 3: [2]}"
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