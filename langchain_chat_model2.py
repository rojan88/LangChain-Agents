from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model = 'gpt-4.1-mini',
    # model = 'mistral-medium-2508',
    temperature = 0.1
)
response = model.invoke('Hello, what is python?')

print(response)
print(response.content)

