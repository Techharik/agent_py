# One - we need to give a system prompt what we need to actually focus on and we can say if it is not that query we ask to make them not give any response  just say sorry.

#! Zero - shot prompting ----
#! Giving the instruction directly.

# example - message{role:'system', "content': 'You are an expert in Maths and only and only ans maths. if not you need just sorry .'  "}

#! FEW -SHOT PROMOPTING:
#! ------ Giving examples along with the Instructions

# 'You are an expert in Maths and only and only ans maths. if not you need just sorry .'
# example:
# Q:Hey can you tell about trump?
#  A: sorry.
# Q: Hey can you  explain about mahts formula pithogrous?
#  A: yes sure, pithogrouse is C= A+B

# -- Few -shot Promoting OUTPUT STRUCTURE:

#! ADD A RULE FOR OUTPUT FORMAT:

# RULE:
#! -STRICTLY FOLLOW THE OUTPUT IN JSON FORMAT

#! OUTPUT FORMAT:
# {{
#     "CODE":"STRING"OR "NULL",
#     "IS CODINGQUESTION ": "bOOLEAN"
# }}

#! Chain of thought for Reasoning PROMPTING:
# !Important: Think before act.

# BASICALLY ASKING THE LLM TO WORK IN THINK STEP BY STEP MANER
from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

SYSTEM_PROMPT = """
 You're a Math and Coding Assistant, only and only answer for maths and coding Problem . If other than that User ask, Say  sorry and ask them to query or breif related to Coding and Mathematics.
 You'r an Expert assistant sokve the user Query with Chain of thought.
 You work on START, PLAN , AND OUTPUT steps.
 You need to first plan what you need to do this can me a multiple steps.
 After you think enough plan is done finally return the output.

 Rules:
 Strictly follow the Given JSON output format
 Only run one step at a time.
 The Sequence of steps is START( Where the user given Input). Plan( That can be multiple steps).Output(which is going to be displayed to the user)

 OUTPUT JSON FORMAT:
 {"step":"START" |"PLAN"|"OUTPUT", "content":"string"}

 Example:
 
 START:'Hey, Solve the problem of 2-3+2/12
 PLAN : {"step":"START", "content":"Seems like I need to solve a Problem of Maths 2-3+2/12"}
 PLAN : {"step":"PLAN", "content":"For this we need to approach with the BODMAS theorm"}
 PLAN : {"step":"PLAN", "content":"First we need to divide 2/12"}
 PLAN : {"step":"PLAN", "content":"Now we need to Add the 3 with divided Value"}
 PLAN : {"step":"PLAN", "content":"Now we need to Sub the 2 with resulted Value"}
 OUTPUT:{"step":"OUTPUT","content":"The solution for this given Problem is resulted value"}

"""
import json

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

user_query = input("Type:")
message_history.append({"role": "user", "content": user_query})
while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history)
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    print(parsed_result, '----')
    if (parsed_result.get('step') == 'START'):
        print("⚡", parsed_result.get("content"))
        continue
    if (parsed_result.get('step') == 'PLAN'):
        print("📕", parsed_result.get("content"))
        continue
    if (parsed_result.get('step') == 'OUTPUT'):
        print("✅", parsed_result.get("content"))
        break
