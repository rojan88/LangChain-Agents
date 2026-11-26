from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings = OpenAIEmbeddings(model = 'text-embedding-3-large')
# texts = {
#     'I love apples', 
#     'apples makes very good computers', 
#     'I believe apple is an innovatiion'
#     'I am a fan of macbooks', 
#     'I enjoy orranges', 
#     'I like lenovo thinkpads', 
#     'I think pears taste very good'
# }

# vector_store = FAISS.from_texts(texts, embedding = embeddings )
# print(vector_store.similarity_search('apples are my favourite food.', k = 7))
# print(vector_store.similarity_search('Linux is a great operating system', k = 7))

























































































































































































































































texts = [
    'I love apples', 
    'I enjoy orranges', 
    'I think pears taste very good', 
    'I hate cherries', 
    'I dislike raspbeeries', 
    'I despise mangoes', 
    'I love linux', 
    'I hate windows'
]

vector_store = FAISS.from_texts(texts, embedding = embeddings )
print(vector_store.similarity_search('What fruits does the person like?', k = 3))
print(vector_store.similarity_search('What fruits does the person hate?', k = 3))




from langchain_core.tools import create_retriever_tool
retriever = vector_store.as_retriever(search_lwargs = {'k':3})
retriever_tool = create_retriever_tool(retriever, name = 'know_base search', description = 'search the small product/ fruit'
'knowledge base from retriever')

from langchain.agents import create_agent
agent = create_agent(
    model = 'gpt-4.1-mini', 
    tools = [retriever_tool], 
    system_prompt = (
        'You are a helpful assistant. For questions about macs, apples or laptops'
        'first call the kb_search tool to retrieve context, then answer clearly. Maybe use the models multiple' \
        'times before answering'
    )
)
result = agent.invoke({
    'messages': [{'role':'user', 'content': 'what three frutis does the prsn like and what'
    'fruits does the persn dislike?'}]
})
print(result)
print(result['messages'][-1].content)
