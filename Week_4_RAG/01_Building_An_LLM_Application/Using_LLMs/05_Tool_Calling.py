import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

groq_api_key = os.getenv("GROQ_API")

if groq_api_key:
    from llama_index.llms.groq import Groq
    from llama_index.core.tools import FunctionTool
    from typing import TypedDict

    class Song(TypedDict):
        name: str
        artist: str

    def generate_song(name: str, artist: str) -> Song:
        """Generates a song with provided name and artist."""
        return {"name": name, "artist": artist}


    tool = FunctionTool.from_defaults(fn=generate_song)

    llm = Groq(model="llama3-70b-8192", api_key=groq_api_key)
    response = llm.predict_and_call(
        [tool],
        "Pick a random song for me",
    )
    print(str(response))
else:
    print("GROQ_API key not found.")