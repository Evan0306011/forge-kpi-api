from fastapi import FastAPI
from mcp_server import mcp

from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

app = FastAPI()

app.add_middleware(
    ProxyHeadersMiddleware,
    trusted_hosts="*"
)

from fastapi import Request

@app.get("/request-info")
def request_info(request: Request):
    return {
        "url": str(request.url),
        "scheme": request.url.scheme,
        "headers": {
            "x-forwarded-proto": request.headers.get("x-forwarded-proto"),
            "host": request.headers.get("host")
        }
    }

@app.get("/mcp-type")
def mcp_type():
    return {
        "type": str(type(mcp)),
        "has_streamable": hasattr(mcp, "streamable_http_app"),
        "has_sse": hasattr(mcp, "sse_app")
    }

@app.get("/mcp-route-test")
def mcp_route_test():
    return {
        "mcp_type": str(type(mcp)),
        "streamable": hasattr(mcp, "streamable_http_app"),
        "sse": hasattr(mcp, "sse_app")
    }


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

@app.get("/version")
def version():
    import mcp
    return {
        "mcp_version": getattr(mcp, "__version__", "unknown")
    }



app.mount(
    "/mcp/",
    mcp.streamable_http_app()
)
