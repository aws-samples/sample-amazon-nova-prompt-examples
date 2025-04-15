import boto3

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )


bedrock_runtime.invoke_model(
                modelId="amazon.nova-canvas-v1:0",
                body={
                    "taskType": "TEXT_IMAGE",
                    "textToImageParams": {
                        "text": "whimsical and ethereal soft-shaded story illustration: A woman in a large hat stands at the ship's railing looking out across the ocean",  # A description of the image you want
                        "negativeText": "clouds, waves",  # List things to avoid
                    },
                    "imageGenerationConfig": {
                        "numberOfImages": 1,  # Number of variations to generate. 1 to 5.
                        "quality": "standard",  # Allowed values are "standard" and "premium"
                        "width": 1280,  # See README for supported output resolutions
                        "height": 720,  # See README for supported output resolutions
                        "cfgScale": 7.0,  # How closely the prompt will be followed
                        "seed": 858,  # Use a random seed
                    },
                },
                accept="application/json",
                contentType="application/json",
            )