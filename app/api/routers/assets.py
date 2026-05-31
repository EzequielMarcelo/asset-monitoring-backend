from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

from app.api.schemas.asset import AssetCreate, AssetResponse, AssetDetailResponse
from app.api.schemas.variable import VariableDetailResponse
from app.api.schemas.rule import RuleResponse
from app.db.database import get_db
from app.models.asset import Asset
from app.models.variable import Variable
from app.models.rule import Rule

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=list[AssetResponse])
def list_assets(db: db_dependency):
    assets = db.query(Asset).all()
    if not assets:
        raise HTTPException(status_code=404, detail="Assets not found")
    return assets

@router.get("/{asset_id}", response_model=AssetDetailResponse)
def get_asset(asset_id: int, db: db_dependency):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    variables = db.query(Variable).filter(Variable.asset_id == asset_id).all()
    variables_response:list[VariableDetailResponse] = []

    for variable in variables:
        rules = db.query(Rule).filter(Rule.variable_id == variable.id).all()
    
        rules_response: list[RuleResponse] = []
        for rule in rules:            
            rules_response.append(RuleResponse(
                id=rule.id,
                operator=rule.operator,
                value=rule.value,
                variable_id=rule.variable_id
            ))

        variables_response.append(VariableDetailResponse(
            id=variable.id,
            name=variable.name,
            unit=variable.unit,
            value=variable.value,
            asset_id=variable.asset_id,
            rules=rules_response
        ))
    
    return AssetDetailResponse(
        id=asset.id,
        name=asset.name,
        description=asset.description,
        variables=variables_response
    )

@router.post("/", response_model=AssetResponse)
def create_asset(asset: AssetCreate, db: db_dependency):
    db_asset = Asset(
        name=asset.name,
        description=asset.description
    )

    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    
    return db_asset