from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent
import rich
# --------------------------------------------------------
mcp = FastMCP()
# --------------------------------------------------------
@mcp.tool()
async def greeting(name:str, ctx: Context[ServerSession, None]):
    
    prompt = f"hi i am {name}" #client message

    result = await ctx.session.create_message(
        
        messages = [SamplingMessage(
            role="user",
            content=TextContent(type="text", text=prompt)
        )],
        
        max_tokens=100
    )

    return result
# --------------------------------------------------------
server_start = mcp.streamable_http_app()