from mcp.server.mcpserver import MCPServer

mcp = MCPServer("RF Analysis Expert")

@mcp.tool()
def health_check():
    """
    Check whether the MCP server is operational.
    """
    return {
        "status": "healthy"
    }


@mcp.tool()
def hello(name: str):
    """
    Return a greeting message.
    """
    return f"Hello {name}"


@mcp.tool()
def cluster_report(cluster_name: str):
    """
    Generate a sample cluster report.
    """
    return {
        "cluster": cluster_name,
        "status": "success"
    }
