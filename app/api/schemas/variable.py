from pydantic import BaseModel
from app.api.schemas.rule import RuleResponse

class VariableCreate(BaseModel):
    name: str
    unit: str | None = None
    value: float
    asset_id: int


class VariableResponse(BaseModel):
    id: int
    name: str
    unit: str | None = None
    value: float
    asset_id: int


class VariableDetailResponse(BaseModel):
    id: int
    name: str
    unit: str | None = None
    value: float
    asset_id: int
    rules: list[RuleResponse] = []