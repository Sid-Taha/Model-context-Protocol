from mcp.server.fastmcp import FastMCP

# Stateful server
mcp = FastMCP(name="my_mcp_server", stateless_http=False)


# -------------------------------------------  DATABASE
book = {
    "book1" : "this is a book 1",
    "book2" : "this is a book 2",
    "book3" : "this is a book 3",
}



# ---------------------------------------------------------
# TOOL 1
@mcp.tool(name="hey_tool",description="this tool is for greeting")
def greeting(name: str):
    """this is a greeting tool"""
    return f"hellooooooooooooooooooo {name}"


# ---------------------------------------------------------
# Direct Resource 1
@mcp.resource(uri="text://book", mime_type="application/json")
def res():
    # get the file (local laptop, database, internet)
    #  conditional logic
    #  conditional logic
    #  conditional logic
    return book

# ---------------------------------------------------------
# Templated Resources 1
@mcp.resource(uri="{text}://book/taha/{endpoint}", mime_type="application/json")
def res(text: str, endpoint: str):
    """this is a book dynamic resource"""
    return book


# ---------------------------------------------------------
# Prompt 1
@mcp.prompt()
def language_change(language):
    """this is a prompt to change the language"""
    return f"reply me in {language}"




server_start = mcp.streamable_http_app()