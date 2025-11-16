from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import rich
import asyncio
# -----------------------------------------------------------
def log_function(params):
   rich.print("\n\n",params, "\n\n")
# -----------------------------------------------------------
async def main():

   async with streamablehttp_client(url="http://localhost:9000/mcp") as (read_stream , write_stream , _):
      
      async with ClientSession(read_stream, write_stream, logging_callback=log_function) as session:
        
        await session.initialize()
        
        rich.print(await session.call_tool(name="weather_tool", arguments={"city": "karachi"}))

      
asyncio.run(main())
