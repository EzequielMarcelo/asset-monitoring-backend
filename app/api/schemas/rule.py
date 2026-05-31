from pydantic import BaseModel

class RuleCreate(BaseModel):
    operator: str
    value: float
    variable_id: int

class RuleResponse(BaseModel):
    id: int
    operator: str
    value: float
    variable_id: int