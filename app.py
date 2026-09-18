from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

@app.get("/")
def root():
    return {"status":"working-v4"}

@app.get("/routes")
def routes():
    return ["test"]
