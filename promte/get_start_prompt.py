# One - we need to give a system prompt what we need to actually focus on and we can say if it is not that query we ask to make them not give any response  just say sorry.

# Zero - shot prompting ----
# Giving the instruction directly.

# example - message{role:'system', "content': 'You are an expert in Maths and only and only ans maths. if not you need just sorry .'  "}

# FEW -SHOT PROMOPTING:
# ------ Giving examples along with the Instructions

# 'You are an expert in Maths and only and only ans maths. if not you need just sorry .'
# example:
# Q:Hey can you tell about trump?
#  A: sorry.
# Q: Hey can you  explain about mahts formula pithogrous?
#  A: yes sure, pithogrouse is C= A+B

# -- Few -shot Promoting OUTPUT STRUCTURE:

# ADD A RULE FOR OUTPUT FORMAT:

# RULE:
# -STRICTLY FOLLOW THE OUTPUT IN JSON FORMAT

# OUTPUT FORMAT:
# {{
#     "CODE":"STRING"OR "NULL",
#     "IS CODINGQUESTION ": "bOOLEAN"
# }}

# Chain of thought for Reasoning PROMPTING:
