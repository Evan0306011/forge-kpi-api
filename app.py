from fastapi import FastAPI
from mcp_server import mcp

app = FastAPI()

@app.get("/")
def root():
    return {"status": "working"}

@app.get("/routes")
def routes():
    return [route.path for route in app.routes]

app.mount("/mcp", mcp.streamable_http_app())
