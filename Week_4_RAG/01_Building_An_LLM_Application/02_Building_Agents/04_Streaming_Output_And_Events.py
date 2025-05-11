import os
import asyncio
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.tools.tavily_research import TavilyToolSpec
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.workflow import Context
from llama_index.core.agent.workflow import (
    AgentInput,
    AgentOutput,
    ToolCall,
    ToolCallResult,
    AgentStream,
)

load_dotenv(dotenv_path='../.env')

google_api_key = os.getenv("GOOGLE_API")
tavily_api_key = os.getenv("TAVILY_API")

if not google_api_key or not tavily_api_key:
    raise ValueError("Missing GROQ_API or TAVILY_API in your .env file")

llm = Gemini(model="gemini-2.0-flash", api_key=google_api_key)
tavily_tool = TavilyToolSpec(api_key=tavily_api_key)

workflow = AgentWorkflow.from_tools_or_functions(
    tavily_tool.to_tool_list(),
    llm=llm,
    system_prompt="You're a helpful assistant that can search the web for information."
)

async def main():
    handler = workflow.run(user_msg="Summarize the latest news about the weather in San Francisco.")

    # handle streaming output
    async for event in handler.stream_events():
        if isinstance(event, AgentStream):
            print(event.delta, end="", flush=True)
        elif isinstance(event, AgentInput):
            print("Agent input: ", event.input)  # the current input messages
            print("Agent name:", event.current_agent_name)  # the current agent name
        elif isinstance(event, AgentOutput):
            print("Agent output: ", event.response)  # the current full response
            print("Tool calls made: ", event.tool_calls)  # the selected tool calls, if any
            print("Raw LLM response: ", event.raw)  # the raw llm api response
        elif isinstance(event, ToolCallResult):
            print("Tool called: ", event.tool_name)  # the tool name
            print("Arguments to the tool: ", event.tool_kwargs)  # the tool kwargs
            print("Tool output: ", event.tool_output)  # the tool output            

    # print final output
    print(str(await handler))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
