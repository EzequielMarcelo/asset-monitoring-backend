from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.schemas.variable import VariableCreate, VariableResponse, VariableDetailResponse
from app.api.schemas.rule import RuleResponse
from app.db.database import get_db
from app.models.asset import Asset
from app.models.variable import Variable
from app.models.rule import Rule

router = APIRouter(
    prefix="/variables",
    tags=["Variables"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=list[VariableResponse])
def list_variables(db: db_dependency):
    variables = db.query(Variable).all()
    if not variables:
        raise HTTPException(status_code=404, detail="Variables not found")
    return variables

@router.get("/{asset_id}", response_model=list[VariableDetailResponse])
def get_variables(asset_id: int, db: db_dependency):
    variables = db.query(Variable).filter(Variable.asset_id == asset_id).all()
    
    variables_response = []
    for variable in variables:    
        rules = db.query(Rule).filter(Rule.variable_id == variable.id).all()
        rules_response: list[RuleResponse] = []

        for rule in rules:
            rules_response.append(RuleResponse(
                id=rule.id,
                operator=rule.operator,
                value=rule.value,
            ))
        
        variables_response.append(VariableDetailResponse(
            id=variable.id,
            name=variable.name,
            unit=variable.unit,
            value=variable.value,
            asset_id=variable.asset_id,
            rules=rules_response
        ))
        
    return variables_response

@router.post("/", response_model=VariableResponse)
def create_variable(variable: VariableCreate, db: db_dependency):   
    asset = db.query(Asset).filter(Asset.id == variable.asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
     
    db_variable = Variable(
        name=variable.name,
        unit=variable.unit,
        value=variable.value,
        asset_id=variable.asset_id
    )

    db.add(db_variable)
    db.commit()
    db.refresh(db_variable)
    
    return db_variable