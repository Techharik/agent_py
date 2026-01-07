from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI")
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=GEMINI_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="which llm has most accurate results?")
print(response.text)
