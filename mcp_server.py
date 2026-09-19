from mcp.server.mcpserver import MCPServer

mcp = MCPServer("RF Analysis Expert")

@mcp.tool()
def hello():
    """Test tool"""
    return "Hello"

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8080
    )
