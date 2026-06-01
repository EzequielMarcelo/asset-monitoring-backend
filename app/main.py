from fastapi import FastAPI
from app.api.routers import assets, variables, rules
from app.models.asset import Asset
from app.models.variable import Variable
from app.models.rule import Rule
from app.db.database import Base, engine

app = FastAPI(
    title="Asset Telemetry Monitoring API",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(assets.router)
app.include_router(variables.router)
app.include_router(rules.router)

@app.get("/health")
def health():
    return {"status": "ok"}