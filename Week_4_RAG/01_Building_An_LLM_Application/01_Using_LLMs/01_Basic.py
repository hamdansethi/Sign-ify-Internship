import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

groq_api_key = os.getenv("GROQ_API")

if groq_api_key:
    from llama_index.llms.groq import Groq
    
    llm = Groq(model="llama3-70b-8192", api_key=groq_api_key)
    response = llm.complete("William Shakespeare is ")
    print(response)
else:
    print("GROQ_API key not found.")
