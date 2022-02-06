from fastapi import FastAPI, Depends
from starlette.responses import PlainTextResponse

from .dependencies import app_settings
from .models.app_exception import InternalAppClientApiException
from .routers import direct_data
from .utils.app_log import app_log

app = FastAPI(
    title="Finapp api service",
    version="0.0.1",
    dependencies=[Depends(app_settings)],
)

app.include_router(direct_data.router)


@app.exception_handler(InternalAppClientApiException)
async def api_exception_handler(_, exception: InternalAppClientApiException):
    app_log(exception=exception)
    return PlainTextResponse(str(exception.message), status_code=502)


@app.get("/", response_model=str)
async def root() -> str:
    return "Finapp api service is working"
