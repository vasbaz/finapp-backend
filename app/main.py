from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import PlainTextResponse, Response

from .db.crud.crypto_asset import crypto_asset
from .dependencies import get_db, get_main_cmc_repository
from .procedures.fill_assets_from_cmc import fill_assets_from_cmc
from .procedures.fill_urls_from_cmc import fill_urls_from_cmc
from .repositories.coin_market_cap.repository import CMCRepository
from .types.app_exception import InternalAppClientApiException
from .utils.app_log import app_log

app = FastAPI(
    title="Finapp api service",
    version="0.0.1",
)


@app.exception_handler(InternalAppClientApiException)
async def api_exception_handler(
    _, exception: InternalAppClientApiException
) -> Response:
    app_log(exception=exception)
    return PlainTextResponse(str(exception.message), status_code=502)


@app.get("/", response_model=str)
async def root() -> str:
    return "Finapp api service is working"


@app.get("/test_db_get_assets")
async def test_db_get_assets(db: AsyncSession = Depends(get_db)):
    return await crypto_asset.get_all(db)


@app.get("/test_db_fill_assets")
async def test_db_fill_assets(
    db: AsyncSession = Depends(get_db),
    cmc_repository: CMCRepository = Depends(get_main_cmc_repository),
):
    return await fill_assets_from_cmc(db, cmc_repository)


@app.get("/test_db_fill_urls")
async def test_db_fill_urls(
    db: AsyncSession = Depends(get_db),
    cmc_repository: CMCRepository = Depends(get_main_cmc_repository),
):
    return await fill_urls_from_cmc(db, cmc_repository)
