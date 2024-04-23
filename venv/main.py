from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

if not client.api_key:
  print("DIO BESTIA")
else:
  print("la chiave c'è dio merda")


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a Human Resources representative, in charge of dealing with the data of all employees, specifically the holidays taken and how many are left."},
    {"role": "user", "content": "."}
  ]
)

print(completion.choices[0].message.content)






