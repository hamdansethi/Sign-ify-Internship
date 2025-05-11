from dotenv import load_dotenv
from groq import Groq
import os

# Load .env file
load_dotenv(dotenv_path='../.env')

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API"))

# Use a direct image URL (not a Google search redirect)
image_url = "https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"

# Call the Groq LLaMA model with the image and prompt
completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the image"},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False
)


print(completion.choices[0].message.content)

# from llama_index.core.llms import ChatMessage, TextBlock, ImageBlock
# from llama_index.llms.openai import OpenAI

# llm = OpenAI(model="gpt-4o")

# messages = [
#     ChatMessage(
#         role="user",
#         blocks=[
#             ImageBlock(path="image.png"),
#             TextBlock(text="Describe the image in a few sentences."),
#         ],
#     )
# ]

# resp = llm.chat(messages)
# print(resp.message.content)

