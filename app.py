from fastapi import FastAPI
from mcp_server import mcp

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "working"
    }

app.mount(
    "/mcp",
    mcp.streamable_http_app()
)
