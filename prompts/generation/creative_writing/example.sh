aws bedrock-runtime converse \
  --model-id us.amazon.nova-pro-v1:0 \
  --system "You are a creative writing assistant skilled in crafting engaging stories. Your task is to create a short story based on the provided prompt, incorporating vivid descriptions, compelling characters, and an engaging plot. Follow these guidelines:

##INSTRUCTIONS##
1. Create a story that matches the theme and elements in the ##PROMPT##
2. Include descriptive language and sensory details
3. Develop at least one main character with clear motivations
4. Create a clear beginning, middle, and end
5. Keep the story between 300-500 words" \
  --messages "[{\"role\":\"user\",\"content\":[{\"text\":\"##PROMPT##\nWrite a story about an AI artist who discovers an unusual glitch in their latest digital creation - a self-portrait that seems to change every time they look away.\n\n##STORY##\"}]}]" \
  --inference-config "{\"temperature\":0.7,\"topP\":0.9,\"maxTokens\":2048,\"stopSequences\":[\"##END##\"]}" \
  --region us-west-2