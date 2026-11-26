import requests
from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

model = init_chat_model(
    model = 'gpt-4.1-mini',
    # model = 'mistral-medium-2508',
    temperature = 0.1
)
for chunk in model.stream('Hello, what is python?'):
    print(chunk.text, end = '', flusk = True)
