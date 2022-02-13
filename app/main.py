from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import PlainTextResponse, Response

from .db.crud.crypto_asset import crypto_asset
from .db.schemas.crypto_asset import CryptoAssetCreate
from .dependencies import get_db
from .api import direct_cmc_data
from .types.app_exception import InternalAppClientApiException
from .utils.app_log import app_log

app = FastAPI(
    title="Finapp api service",
    version="0.0.1",
)

app.include_router(direct_cmc_data.router)


@app.exception_handler(InternalAppClientApiException)
async def api_exception_handler(
    _, exception: InternalAppClientApiException
) -> Response:
    app_log(exception=exception)
    return PlainTextResponse(str(exception.message), status_code=502)


@app.get("/", response_model=str)
async def root() -> str:
    return "Finapp api service is working"


@app.get("/test_db_get")
def test_db_get(db: Session = Depends(get_db)):
    return crypto_asset.get_assets(db)


@app.get("/test_db_write")
def test_db_write(db: Session = Depends(get_db)):
    return crypto_asset.create_asset(
        db, CryptoAssetCreate(name="Etherum", ticker="ETH")
    )
