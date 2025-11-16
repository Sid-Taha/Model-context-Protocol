from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import rich
import asyncio

async def main():

   async with streamablehttp_client(url="http://localhost:8000/mcp") as (read_stream , write_stream , _):
      
      async with ClientSession(read_stream, write_stream) as session:
        

        show_prompt = await session.list_tools()
        rich.print(show_prompt)

      
asyncio.run(main())
