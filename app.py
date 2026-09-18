from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "working-v2"}

@app.get("/routes")
def routes():
    return ["test"]
