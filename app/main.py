from fastapi import FastAPI, Depends

from .dependencies import settings
from .routers import direct_data


app = FastAPI(dependencies=[Depends(settings)])


app.include_router(direct_data.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
