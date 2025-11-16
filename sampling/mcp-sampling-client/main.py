import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
from mcp.shared.context import RequestContext
from mcp.types import CreateMessageRequestParams, CreateMessageResult, TextContent
import rich
from openai import OpenAI
# ------------------------------------------------------------
LLM = OpenAI(api_key="your_api_key")
# ------------------------------------------------------------
async def llm_call(ctx:RequestContext[ClientSession, None], params: CreateMessageRequestParams)-> CreateMessageResult:
    # LLM Call 
    LLM_response = LLM.responses.create(
    model="gpt-4.1-mini",
    input= params.messages[0].content.text
    )
    
    # message send back to server
    return CreateMessageResult(
        role="assistant",
        content=TextContent(type="text", text=LLM_response.output_text),
        model="taha-4.1-mini"
        )
# ------------------------------------------------------------
async def main():

    async with streamablehttp_client("http://localhost:9000/mcp") as (read_stream, write_stream, _):

        async with ClientSession(read_stream, write_stream, sampling_callback=llm_call) as session:

            await session.initialize()

            rich.print(await session.call_tool(name="greeting", arguments={"name": "Alex"}))



# ------------------------------------------------------------
asyncio.run(main())