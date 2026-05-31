from fastapi import FastAPI
from app.api.routers import assets

app = FastAPI(
    title="Asset Telemetry Monitoring API",
    version="0.1.0"
)

app.include_router(assets.router)

@app.get("/health")
def health():
    return {"status": "ok"}