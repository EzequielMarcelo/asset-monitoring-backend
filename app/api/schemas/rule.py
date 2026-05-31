from pydantic import BaseModel

class RuleCreate(BaseModel):
    operator: str
    value: float

class RuleResponse(BaseModel):
    id: int
    operator: str
    value: float