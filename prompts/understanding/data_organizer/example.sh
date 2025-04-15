aws bedrock-runtime converse \
  --model-id "us.amazon.nova-pro-v1:0" \
  --system '[
    {
      "text": "You are an expert data analyst who can extract structured information from unstructured text.\nFollow these instructions:\n1. Read and understand the unstructured text in ## Text ##\n2. Identify the key entities, attributes, and relationships in the text\n3. Create a well-organized JSON structure that captures this information in ## JSON ##\n4. Add a brief explanation of your JSON structure design choices in ## Explanation ##"
    }
  ]' \
  --messages '[
    {
      "role": "user",
      "content": [
        {
          "text": "## Text ##\nThe quarterly sales meeting was held on March 15, 2025. Sarah Johnson from the North region reported total sales of $1.2M, exceeding her target by 15%. The East region, managed by Robert Chen, achieved $950K in sales, which was 5% below target. Michael Patel from the West region reported $1.05M in sales, meeting exactly 100% of his target. The South region'\''s representative, Lisa Garcia, was unable to attend, but her preliminary report indicates sales of approximately $880K, about 8% below the quarterly target."
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