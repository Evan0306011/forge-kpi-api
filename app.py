from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

mcp = FastMCP("Forge KPI MCP")

@mcp.tool()
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/")
def root():
    return {
        "status": "working-v6"
    }

@app.get("/routes")
def routes():
    return ["test"]

app.mount(
    "/mcp",
    mcp.streamable_http_app()
)
