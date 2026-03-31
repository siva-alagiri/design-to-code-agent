import groq
from PIL import Image
from dotenv import load_dotenv
import os
import base64
import io

load_dotenv()

client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

def image_to_base64(image: Image.Image) -> str:
    """Convert PIL image to base64 string."""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def analyze_image(image: Image.Image) -> str:
    """
    Takes a PIL image and returns a detailed UI description using Groq Vision.
    """
    try:
        from prompts.templates import VISION_PROMPT
        
        image_data = image_to_base64(image)
        
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_data}"
                            }
                        },
                        {
                            "type": "text",
                            "text": VISION_PROMPT
                        }
                    ]
                }
            ],
            max_tokens=1000,
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error analyzing image: {str(e)}"