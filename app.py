from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

mcp = FastMCP("Forge KPI MCP")

@app.get("/")
def root():
    return {"status":"working-v3"}

@app.get("/routes")
def routes():
    return ["test"]
