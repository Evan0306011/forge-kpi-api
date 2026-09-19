from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

# MCP Server
mcp = FastMCP("Forge KPI MCP")

# MCP Tools
@mcp.tool()
def health_check():
    return {
        "status": "healthy"
    }

@mcp.tool()
def hello(name: str):
    return f"Hello {name}"

@mcp.tool()
def cluster_report(cluster_name: str):
    return {
        "cluster": cluster_name,
        "status": "success"
    }


# REST Endpoints
@app.get("/")
def root():
    return {
        "status": "working-v12"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/health/tools")
def tools_health():
    return {
        "tools": [
            "health_check",
            "hello",
            "cluster_report"
        ]
    }


@app.get("/routes")
def routes():
    return [route.path for route in app.routes]


# MCP Endpoint
app.mount(
    "/mcp",
    mcp.streamable_http_app()
)
