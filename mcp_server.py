from mcp.server.mcpserver import MCPServer

# Create MCP Server
mcp = MCPServer("RF Analysis Expert")

# Test Tool
@mcp.tool()
def hello():
    """
    Test MCP tool.
    """
    return "Hello"

# Start MCP Server
if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8080,
        streamable_http_path="/mcp"
    )
`
