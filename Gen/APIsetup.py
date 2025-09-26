from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
# client = OpenAI(
#     key='',
#     base_url="gooleapis.com/v1/beteta"
# )  use google api in the open api sdk.

response = client.chat.completions.create(model="gpt-4o-mini",
                                          messages=[{
                                              "role": "user",
                                              "contect": "Hey There"
                                          }])

print(response.choices[0].message.content)
