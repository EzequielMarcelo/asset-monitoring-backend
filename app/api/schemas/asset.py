from pydantic import BaseModel

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
    variables: list = []