from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession
# ---------------------------------------------------
mcp = FastMCP()
# ---------------------------------------------------
@mcp.tool()
async def weather_tool(city: str, ctx: Context[ServerSession, None]):
   
    # notification
    await ctx.info("process start ho gaya")

    # ye notification send karta he  
    await ctx.session.send_resource_list_changed()
    
    return f"{city} is hot" 

# ---------------------------------------------------
server_strat = mcp.streamable_http_app()


# await ctx.debug(f"Debug: Processing '{data}'")
# await ctx.info("Info: Starting processing")
# await ctx.warning("Warning: This is experimental")
# await ctx.error("Error: (This is just a demo)")