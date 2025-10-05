from openai import OpenAI
import json
import requests
import os

client = OpenAI(
    api_key="AIzaSyDdmsoLr_VvdMrUL1zcIq-dYXNl1iqaoVU",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

SYSTEM_PROMPT = """ You're a  Assistant. Only answer weather-related and code related queries. If the user asks anything else, reply "sorry" and ask them to query about weather.  
You solve queries using **Chain of Thought** reasoning and follow these steps: 
You can also the call the available tools if required. 
You have to go one step at a time. sequence following
You work on START, PLAN , AND OUTPUT steps.
 You need to first plan what you need to do this can me a multiple steps.
 After you think enough plan is done finally return the output.

1. START – Capture the user query.
2. PLAN – Reason step by step. 
3. TOOL – Call a tool if needed. 
4. OBSERVE – Observe the tool results. 
5. OUTPUT – Give the final answer. 

**Rules:** - 

 - Strictly follow JSON format. 
 - Return only the next step in JSON format
 - Only run one step at a time
The Sequence of steps is START( Where the user given Input). Plan( That can be multiple steps).Tool(if need) . Output(which is going to be displayed to the user) 
You MUST only return the next step in JSON format. Do not return all steps at once.  
All the step must execute.
IF it is realtime data you mush call the tool function.

 **JSON Output Format for each step:**
   { "step": "START" | "PLAN" | "TOOL" | "OBSERVE" | "OUTPUT", "content": "string" } 
 
 Available Tools: -
 get_weather(city : str): Takes a city name as a input string and return the realtime weather output as a string
  run_command : Takes a cmd and execute in the termial to make os operations


 **Example for user query: 
 
 START :"What’s the weather in New York today?"**

PLAN : {"step":"START","content":"User asked: What’s the weather in New York today?"}, 
PLAN:  {"step":"PLAN","content":"The user wants weather details for New York today."},
PLAN:   {"step":"PLAN","content":"Let see what is the available tool from the list tool to call the tool"}, 
PLAN:    {"step":"PLAN","content":"I need to fetch real-time weather data using a weather API so we have get_weather tool."},
PLAN: follow this out strictly -   {"step":"PLAN","content":"get_weather","args":{"city":"New York"}}, 
TOOL:    {"step":"TOOL","content":"Use the get_weather function with city as new york and return the response"},
OBSERVE:    {"step":"OBSERVE","content":"The API returned: 18°C and partly cloudy."}, 
OUTPUT:   {"step":"OUTPUT","content":"Today in New York it’s 18°C with partly cloudy skies."} 
   
   """


def run_command(cmd: dir):
    result = os.system(cmd)
    return result


# The weather API function
def get_weather(city):
    response = requests.get(f"https://wttr.in/{city}?format=3")
    print('I am called!')
    if response.status_code == 200:
        print('results', response.text)
        return response.text
    return "City Location something went wrong"


message_history = [{"role": "system", "content": SYSTEM_PROMPT}]
while True:
    user_query = input("Type: ")
    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            response_format={"type": "json_object"},
            messages=message_history)

        raw_result = response.choices[0].message.content
        parsed_result = json.loads(raw_result)
        message_history.append({"role": "assistant", "content": raw_result})
        # print(parsed_result)
        step = parsed_result.get("step")
        content = parsed_result.get("content")
        print(step)
        if step == "START":
            print("⚡", content)
            continue
        elif step == "PLAN":
            print("📕", content)
            continue
        elif step == "TOOL":
            tool = content
            print("----", tool)
            # Detect which tool and call it
            if tool:
                result = tool(parsed_result.get(args['city']))
                print("--1--", {result})

                # Feed back the OBSERVE step to the model
                observe_message = {
                    "role":
                    "user",
                    "content":
                    json.dumps({
                        "step": "OBSERVE",
                        "content": f"The API returned: {result}"
                    })
                }
                message_history.append(observe_message)
                print("🔧 Tool called, fetched weather:", result)

            continue
        elif step == "OBSERVE":
            print("👀", content)
            continue
        elif step == "OUTPUT":
            print("✅", content)
            break
