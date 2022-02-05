from functools import lru_cache

from fastapi import FastAPI, Depends

from .config import Settings
from .repositories.coin_market_cap.models.map import CMCMap
from .repositories.coin_market_cap.repository import CMCRepository


app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test_repo", response_model=list[CMCMap])
async def test_repo(settings: Settings = Depends(get_settings)):
    cmc_repository = CMCRepository(settings.cmc_api_key)
    return await cmc_repository.get_maps()
