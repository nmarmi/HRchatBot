from dotenv import load_dotenv
from openai import OpenAI
from openai import AssistantEventHandler

# load .env file (contains API Key)
load_dotenv()

client = OpenAI()

knowledge_file = open("/Users/nicolomarmi/PycharmProjects/HRchatBot/venv/emplyee_info.txt", "r")
knowledge = knowledge_file.read()
knowledge_file.close()
emplid = "AA002"
question = input("How  can I help you?\n")

# Initialize HR assistant
assistant = client.beta.assistants.create(
    name="HR ChatBot",
    instructions="You are my company's HR representative, your main tasks are informing employees on upcoming holidays, personal holidays each employee has left in the year, and how many days sick they took this year",
    model="gpt-4-turbo",
    tools=[{"type": "file_search"}],
)

# A Thread represents a conversation between a user and one or many Assistants.
thread = client.beta.threads.create()

# get message from user
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=question
)

# run model to generate response
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions=f"Access this information to accuretely answer the question: {knowledge}.\nThis is the employee {emplid}, only answer questions about him/her, without revealing other employee's information",
)

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print(messages.data[0].content[0].text.value)
else:
    print("oh oh, something went wrong")
    print(run.status)

"""
TODO:
- pass knowledge (json file)
- create thread botta e risposta
"""