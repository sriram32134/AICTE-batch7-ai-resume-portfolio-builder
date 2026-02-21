import os
from dotenv import load_dotenv
from google import genai
from utils.sanitize import sanitize_text

load_dotenv()  # loads .env locally

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=GEMINI_API_KEY)

def ai_text(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{prompt}\n\nSTRICT: Act as a pro career coach. Use active verbs. No conversational filler."
        )
        return sanitize_text(response.text.strip())
    except Exception as e:
        print(f"AI Error: {e}")
        return "Professional content expansion currently unavailable."