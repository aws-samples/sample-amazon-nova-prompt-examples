import json
import boto3
import base64
from botocore.config import Config


bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1",
            config=Config(read_timeout=300)
        )

# Read image from file and encode it as base64 string.
with open("mountain-lake.jpg", "rb") as image_file:
    b64_img = base64.b64encode(image_file.read()).decode('utf8')

response = bedrock_runtime.invoke_model(
    modelId="amazon.nova-canvas-v1:0",
    body=json.dumps({
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {
            "conditionImage": b64_img,
            "controlMode": "CANNY_EDGE", # "SEGMENTATION" or "CANNY_EDGE",
            "controlStrength": .7,
            "text": "Transform this photograph into an artistic watercolor painting: A serene mountain lake at sunset, with tall pine trees reflecting in the still water. It should have soft flowing pigments with visible paper texture throughout, brush strokes on the water, delicate color bleeds and gradients, traditional watercolor technique with natural light and shadow transitions, controlled wet-on-wet effects, preserved highlights, professional art style, masterful brush strokes, vibrant yet realistic color palette, slight pigment granulation, subtle paper showing through thin washes, Andrew Wyeth meets William Turner quality, 8k resolution, artstation trending",
            "negativeText": "sharp edges, photorealistic, digital art style"
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "quality": "premium",
            "width": 1024,
            "height": 768,
            "cfgScale": 8.0,
            "seed": 42
        }
    }),
    accept="application/json",
    contentType="application/json"
)

# Process the response to get the generated image
response_body = json.loads(response.get("body").read())

base64_image = response_body.get("images")[0]
base64_bytes = base64_image.encode('ascii')
image_bytes = base64.b64decode(base64_bytes)

# Write the image bytes to a file
output_file_path = "watercolor_mountain_lake.jpg"
try:
    with open(output_file_path, "wb") as output_file:
        output_file.write(image_bytes)
    print(f"Image successfully saved to {output_file_path}")
except Exception as e:
    print(f"Error saving the image: {str(e)}")