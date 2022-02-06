from fastapi import APIRouter, Depends

from app.dependencies import settings
from app.repositories.coin_market_cap.models.map import CMCMap
from app.repositories.coin_market_cap.repository import CMCRepository

router = APIRouter(
    prefix="/direct_data",
    tags=["Direct data"],
)


@router.get("/crypto_maps", response_model=list[CMCMap])
async def crypto_maps(settings: settings = Depends()):
    cmc_repository = CMCRepository(settings.cmc_api_key)
    return await cmc_repository.get_maps()
