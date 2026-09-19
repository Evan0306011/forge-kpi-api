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
        "status": "working-v5"
    }

@app.get("/routes")
def routes():
    return ["test"]
