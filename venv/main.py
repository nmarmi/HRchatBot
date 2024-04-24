from dotenv import load_dotenv
from openai import OpenAI
from openai import AssistantEventHandler

# load .env file (contains API Key)
load_dotenv()

client = OpenAI()

# Basic setup to test api is working:
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a Human Resources representative, in charge of dealing with the data of all employees, specifically the holidays taken and how many are left."},
#     {"role": "user", "content": "."}
#   ]
# )
# print(completion.choices[0].message.content)

# Initialize HR assistant
assistant = client.beta.assistants.create(
    name="HR ChatBot",
    instructions="You are my company's HR representative, your main tasks are informing employees on upcoming holidays, personal holidays each employee has left in the year, and how many days sick they took this year",
    model="gpt-4-turbo",
)

# A Thread represents a conversation between a user and one or many Assistants.
thread = client.beta.threads.create()

# messages from user
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=input("Hi! How can I help you? \n")
)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="The user is a junior employee"
)

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages)
else:
    print("oh oh, something went wrong")
    print(run.status)
