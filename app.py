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

@app.get("/mcp-inspect")
def mcp_inspect():
    return {
        "methods": [
            m for m in dir(mcp)
            if "app" in m.lower()
               or "http" in m.lower()
               or "stream" in m.lower()
        ]
    }

@app.get("/version")
def version():
    import mcp

    return {
        "mcp_version": getattr(mcp, "__version__", "unknown"),
        "mcp_type": str(type(mcp))
    }
}


app.mount(
    "/mcp",
    mcp.streamable_http_app()
)
