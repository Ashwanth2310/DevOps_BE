from fastapi import FastAPI
import os

PORT = os.getenv("PORT", "8000")

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/hello")
async def hello():
    return {"message": f"Hello, world! Running on port {PORT}"}

@app.get("/add")
async def add(a: int, b: int):
    return {"result": a + b}

@app.get("/status")
async def status():
    return {"status": "ok"}