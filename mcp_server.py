from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Forge KPI MCP")


@mcp.tool()
def health_check():
    """
    Test MCP connection
    """
    return {
        "status": "healthy"
    }


@mcp.tool()
def cluster_summary(cluster_name: str):
    """
    Example cluster analysis tool
    """

    return {
        "cluster": cluster_name,
        "status": "completed"
    }