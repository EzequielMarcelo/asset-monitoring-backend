from pydantic import BaseModel
from app.api.schemas.variable import VariableResponse

class AssetCreate(BaseModel):
    name: str
    description: str | None = None


class AssetResponse(BaseModel):
    id: int
    name: str
    description: str | None = None


class AssetDetailResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    variables: list[VariableResponse] = []