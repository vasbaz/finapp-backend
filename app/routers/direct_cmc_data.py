from fastapi import APIRouter, Depends

from app.dependencies import app_settings
from app.repositories.coin_market_cap.schemas.map import CMCMapSchema
from app.repositories.coin_market_cap.schemas.metadata import CMCMetadataSchema
from app.repositories.coin_market_cap.repository import CMCRepository

router = APIRouter(
    prefix="/direct_cmc_data",
    tags=["Direct CMC data"],
    responses={502: {"model": str}},
)


@router.get("/cmc_map_list", response_model=list[CMCMapSchema])
async def cmc_map_list(settings: app_settings = Depends()):
    cmc_repository = CMCRepository(settings.cmc_api_key)
    return await cmc_repository.get_maps()


@router.get("/cmc_metadata_list", response_model=list[CMCMetadataSchema])
async def cmc_metadata_list(settings: app_settings = Depends()):
    cmc_repository = CMCRepository(settings.cmc_api_key)
    return await cmc_repository.get_metadata()
