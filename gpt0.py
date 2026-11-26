from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()
# client = OpenAI()

client = OpenAI(api_key='api-key')

response = client.responses.create(
    model="gpt-4.1-mini",
    input="What is Machine Learning?"
)

print(response.output_text)

# Suppose you want to ask GPT a question.
# Without LangChain:
# So the first question should be:
# Why do we even need LangChain?             GPT-Brain    input Model output
                # Langchain         Constrcn Toolkit      input Model Tool Memory Agent output
#openAI API -> Langchain chatModel -> Prompt Template -> model(parser/temp).invoke() -> output

#Calling LLM in langchain
#Messages in langchain
#chat(Prompt) templates
#LCEL(expression Language) and pipe()
#RunnableLambda and RunnablePassthrough

#tim
from langchain.chat_models import ChatopenAI
from langchain.schema import HumnMessage, BaseOutputParser
from langchain.prompts.chat import ChatPromptTemplate


#Neural
from langchain.agents import create_agent
from langchain.tools import tool

from langchain.chat_models import init_chat_model
from langchain.messages import HumnMessage, AIMessage, SystemMessage

from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool, ToolRuntime

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool

from langchain.agents.middleware import ModelRequest, ModelResponse, dynamic_prompt,
# wrap_model_call,      AgentMiddleware, AgentState,     SummzMiddleware



# LangGraph(tim)
from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict


#Llama Index(wf)         LlamaParse, LlamaExtract, LlamaCloud(non-tech), Agent Framework(build your own workflows below)
#Creating a Basic Agent
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.workflow import Context
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
#Adding Context/Memory
#simple RAG pipeline(added essay)
#Doing RAG onn the data




# openai
from openai import OpenAI

from dotenv import load_dotenv()
load_dotenv()

client = OpenAI(apikey)
response = client.responses.create('' \
'model': 'gpt',
'input': 'what is pythoon' )

priint(response.output_text)




#langchain
from langchain.chat_model import ChatOpenAI

from dotenv import load_dotenv()
load_dotenv()

chat_model = ChatOpenAI(apikey)

result = chat_model.predict('what is python?')
print(result)




agent = create_agent(
    model = 'gpt-4.1', 
    tools = [get_weather], 
    system_prompt = 'You are a helpful weather assistant who provides the weather of different places'
)

response = agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'what is the weather in pokhara?'}
    ]
})
print(response)
print(response['messages'][-1].content)