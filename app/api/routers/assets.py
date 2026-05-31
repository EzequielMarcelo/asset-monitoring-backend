from fastapi import APIRouter
from app.api.schemas.asset import AssetCreate, AssetResponse, AssetDetailResponse

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)

@router.get("/", response_model=list[AssetResponse])
def list_assets():
    return []

@router.get("/{asset_id}", response_model=AssetDetailResponse)
def get_asset(asset_id: int):
    return AssetDetailResponse(
        id=asset_id,
        name="ESP32 Linha 3",
        description="Monitoramento do motor da linha 3",
        variables=[]
    )

@router.post("/", response_model=AssetResponse)
def create_asset(asset: AssetCreate):
    return AssetResponse(
        id=1,
        name=asset.name,
        description=asset.description
    )