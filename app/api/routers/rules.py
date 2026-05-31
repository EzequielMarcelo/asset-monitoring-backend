from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.schemas.rule import RuleCreate, RuleResponse
from app.db.database import get_db
from app.models.variable import Variable
from app.models.rule import Rule

router = APIRouter(
    prefix="/rules",
    tags=["Rules"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=list[RuleResponse])
def list_rules(db: db_dependency):
    rules = db.query(Rule).all()
    if not rules:
        raise HTTPException(status_code=404, detail="Rules not found")
    return rules

@router.get("/{variable_id}", response_model=list[RuleResponse])
def get_rules(variable_id: int, db: db_dependency):
    variables = db.query(Variable).filter(Variable.id == variable_id).first()
    if not variables:
        raise HTTPException(status_code=404, detail="Variable not found")
    
    rules = db.query(Rule).filter(Rule.variable_id == variable_id).all()
    
    rules_response = []
    for rule in rules:            
        rules_response.append(RuleResponse(
            id=rule.id,
            operator=rule.operator,
            value=rule.value
        ))
        
    return rules_response

@router.post("/", response_model=RuleResponse)
def create_rule(rule: RuleCreate, db: db_dependency):   
    variables = db.query(Variable).filter(Variable.id == rule.variable_id).first()
    if not variables:
        raise HTTPException(status_code=404, detail="Variable not found")
     
    db_rule = Rule(
        operator=rule.operator,
        value=rule.value,
        variable_id=rule.variable_id
    )

    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    
    return db_rule