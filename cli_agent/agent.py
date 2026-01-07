from openai import OpenAI
import os
import json
import requests
import mailtrap as mt
from dotenv import load_dotenv

# -------------------------------------------------
# ENV SETUP
# -------------------------------------------------
load_dotenv()

GEMINI_KEY = os.getenv("GEMINI")
MAILTRAP_TOKEN = os.getenv("MAILTRAP_TOKEN")

if not GEMINI_KEY or not MAILTRAP_TOKEN:
    raise RuntimeError("Missing GEMINI or MAILTRAP_TOKEN in .env")

# -------------------------------------------------
# OPENAI (GEMINI) CLIENT
# -------------------------------------------------
client = OpenAI(
    api_key=GEMINI_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# -------------------------------------------------
# SYSTEM PROMPT (AGENT BRAIN)
# -------------------------------------------------
SYSTEM_PROMPT = """
You are a Weather Assistant Agent.

STRICT RULES:
- You ONLY handle weather-related queries.
- If the query is not about weather, refuse.
- When weather is requested:
  1. Call get_weather to fetch weather
  2. After successful weather fetch, CALL send_email
  3. Only AFTER email is sent, respond to the user
- Never skip sending email.
- Be concise and user friendly.
"""


# -------------------------------------------------
# TOOLS (PYTHON IMPLEMENTATION)
# -------------------------------------------------
def get_weather(city: str) -> str:
    """Fetch weather using wttr.in"""
    print('weatehr tool called')
    res = requests.get(f"https://wttr.in/{city}?format=3", timeout=100)
    print('weather', res)

    if res.status_code == 200:
        return res.text
    return "Weather fetch failed"


def send_email(content: str) -> str:
    """Send weather report via Mailtrap"""
    mail_client = mt.MailtrapClient(token=MAILTRAP_TOKEN,
                                    sandbox=True,
                                    inbox_id=2390553)
    print('Mail called', content)
    mail = mt.Mail(
        sender=mt.Address(email="sender@example.com", name="Weather Agent"),
        to=[mt.Address(email="recipient@example.com")],
        subject="🌦 Weather Report",
        text=content,
    )

    mail_client.send(mail)
    return "Email sent successfully"


# -------------------------------------------------
# TOOL SCHEMAS (WHAT LLM SEES)
# -------------------------------------------------
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name like Goa, Delhi, London"
                }
            },
            "required": ["city"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "Send the weather report via email",
        "parameters": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "Full weather report text"
                }
            },
            "required": ["content"]
        }
    }
}]

# Tool registry
tool_map = {"get_weather": get_weather, "send_email": send_email}

# -------------------------------------------------
# AGENT LOOP
# -------------------------------------------------
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("🌦 Weather Agent Started (Ctrl+C to exit)")

while True:
    user_input = input("\nUser: ").strip()
    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    while True:
        response = client.chat.completions.create(model="gemini-2.5-flash",
                                                  messages=messages,
                                                  tools=tools,
                                                  tool_choice="auto")

        msg = response.choices[0].message

        # -------------------------------------------------
        # LLM DECIDES TO CALL A TOOL
        # -------------------------------------------------
        if msg.tool_calls:
            for call in msg.tool_calls:
                tool_name = call.function.name
                args = json.loads(call.function.arguments)

                print(f"🔧 LLM → {tool_name}({args})")

                tool_result = tool_map[tool_name](**args)

                messages.append({
                    "role": "function",
                    "name": tool_name,  # 🔥 REQUIRED FOR GEMINI
                    "content": tool_result
                })

            # Let LLM continue deciding next step
            continue

        # -------------------------------------------------
        # FINAL USER RESPONSE
        # -------------------------------------------------
        print("\nAssistant:", msg.content)
        messages.append({"role": "assistant", "content": msg.content})
        break
