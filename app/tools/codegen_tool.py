from groq import Groq
from dotenv import load_dotenv
from prompts.templates import CODEGEN_PROMPT
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_code(ui_description: str) -> str:
    """
    Takes a UI description and returns HTML/CSS code using Groq/LLaMA.
    """
    try:
        prompt = CODEGEN_PROMPT.format(ui_description=ui_description)
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error generating code: {str(e)}"