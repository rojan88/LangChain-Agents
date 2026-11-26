from dotenv import load_dotenv
from base64 import b64encode
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model('gpt-4.1-mini')

message = {
    'role': 'User', 
    'content': [
        {'type': 'text', 'text': 'Describe the contents of this image'},
        {'type': 'image', 'url': 'https://..image.png'},
        {
            'type': 'image', 
            'base64': b64encode(open('logo.png', 'rb').read()).decode(),
            'mime_type': 'image/png'
        }
    ]
}

response= model.invoke([message])
print(response.content)
