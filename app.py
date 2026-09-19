from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

mcp = FastMCP("Forge KPI MCP")

@mcp.tool()
def health_check():
    return {"status": "healthy"}

@mcp.tool()
def hello(name: str):
    return f"Hello {name}"

@mcp.tool()
def cluster_report(cluster_name: str):
    return {
        "cluster": cluster_name,
        "status": "success"
    }

@app.get("/")
def root():
    return {"status":"working-v11"}

@app.get("/routes")
def routes():
    return [route.path for route in app.routes]

app.mount(
    "/mcp",
    mcp.streamable_http_app()
)
