from pydantic import BaseModel

class VariableCreate(BaseModel):
    name: str
    unit: str
    asset_id: int


class VariableResponse(BaseModel):
    id: int
    name: str
    unit: str
    asset_id: int


class VariableDetailResponse(BaseModel):
    id: int
    name: str
    unit: str
    asset_id: int
    rules: list = []