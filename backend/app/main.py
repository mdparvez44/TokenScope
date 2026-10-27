from fastapi import FastAPI
from tokenscope import analyze_context  # import from SDK (stub) – not used yet

app = FastAPI()

@app.get("/health")
async def health() -> dict:
    """Simple health check endpoint used by the frontend and CI tests."""
    return {"status": "ok"}
