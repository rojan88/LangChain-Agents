from dataclasses import dataclass

import requests
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain.chat_models import init_chat_model

from langgraph.checkpoint.memory import InMemorySaver

@dataclass
class Context:
    user_id: str

@dataclass
class ResponseFormat:
    summary: str
    temperature_celsius: float
    temperature_fahrenheit: float
    humidity: float
 
@tool('get_weather', description = 'Return weather information for a given city', return_direct = False)
async def get_weather(city: str) -> str:
        response = requests.get(f'https://wttr.in/{city}?format=j1')
        return await response.json()


@tool('locate_user', description="Look up a user's city based on the context")
def locate_user(runtime: ToolRuntime[Context]):
    match runtime.context.user_id:
        case 'ABC123':
            return 'Singapore'  
        case 'XYZ456':
            return 'London'
        case 'MNO789':
            return 'Paris'
        case _:
            return 'Unknown'
        
model = init_chat_model('gpt-4.1-mini', temperature = 0.4)

checkpointer = InMemorySaver()
        
agent = create_agent(
    model = model, 
    tools = [get_weather, locate_user], 
    system_prompt = 'You are a helpful weather assistant who provides the weather of different places',
    context_schema = Context, 
    response_format= ResponseFormat,
    checkpointer = checkpointer
)

config = {'configurable': {'thread_id': '1'}}

response = agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'what is the weather like?'}
    ]}, 
    config =config, 
    context = Context(user_id = 'ABC123')
)

print(response['structured_response'])
print(response['structured_response'].summary)
print(response['structured_response'].temperature_celsius)


config = {'configurable': {'thread_id': '2'}}          #different thread
# response = agent.invoke({
#     'messages': [
#         {'role': 'user', 'content': 'And is this usual?'}      
#     ]}, 
#     config =config, 
#     context = Context(user_id = 'ABC123')
# )

# print(response['structured_response'].summary)       #because of checkpointer/InmemorySaver