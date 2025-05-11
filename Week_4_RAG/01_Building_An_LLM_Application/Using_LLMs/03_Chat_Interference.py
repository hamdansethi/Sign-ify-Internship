import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

groq_api_key = os.getenv("GROQ_API")

if groq_api_key:
    from llama_index.llms.groq import Groq
    from llama_index.core.llms import ChatMessage
    
    llm = Groq(model="llama3-70b-8192", api_key=groq_api_key)
    messages = [
        ChatMessage(role="system", content="You are a helpful assistant."),
        ChatMessage(role="user", content="Tell me a joke."),
    ]
    resp = llm.stream_chat(messages)
    for r in resp:
        print(r.delta, end="")
else:
    print("GROQ_API key not found.")
