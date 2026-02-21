from google import genai
from utils.sanitize import sanitize_text

# ── Configuration ──
GEMINI_API_KEY = "AIzaSyDSgpH5BCgbyvL8pDcwZ4RtoNmRffs8an8"
client = genai.Client(api_key=GEMINI_API_KEY)

def ai_text(prompt: str) -> str:
    """Uses the modern google-genai SDK to generate professional content."""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"{prompt}\n\nSTRICT: Act as a pro career coach. Use active verbs. No conversational filler. No markdown stars."
        )
        return sanitize_text(response.text.strip())
    except Exception as e:
        print(f"AI Error: {e}")
        return "Professional content expansion currently unavailable."