from fastapi import FastAPI
from mcp_server import mcp

app = FastAPI()


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

@app.get("/debug")
def debug():
    return {
        "status": "healthy",
        "tools": [
            "health_check",
            "hello",
            "cluster_report"
        ]
    }

@app.get("/mcp-check")
def mcp_check():
    return {
        "mcp_loaded": str(type(mcp)),
        "endpoint": "/mcp"
    }


app.mount(
    "/mcp/",
    mcp.streamable_http_app()
)
