from enum import Enum
from typing import Any

from httpx import AsyncClient
from pydantic import parse_obj_as

from .schemas.map import CMCMapSchema
from .schemas.metadata_response import CMCMetadataResponse
from app.types.app_exception import InternalAppClientApiException
from ...config import settings

CMC_API_URL = "https://pro-api.coinmarketcap.com"
API_KEY_HEADER = "X-CMC_PRO_API_KEY"


class CMCApis(str, Enum):
    MAP = CMC_API_URL + "/v1/cryptocurrency/map"
    METADATA = CMC_API_URL + "/v2/cryptocurrency/info"


class CMCRepository:
    def __init__(self, api_key: str):
        self.auth_header = {API_KEY_HEADER: api_key}

    async def __get_data(self, api: CMCApis, parsing_type: Any) -> Any:
        async with AsyncClient() as client:
            api_response = await client.get(api.value, headers=self.auth_header)

        status_code = api_response.status_code
        if status_code == 200:
            raw_json_api_response = api_response.json()
            api_data = list(
                map(
                    lambda item: parse_obj_as(parsing_type, item),
                    raw_json_api_response["data"],
                )
            )
            return api_data

        raise InternalAppClientApiException(
            api_name=api.__str__(),
            http_code=status_code,
            raw_response=api_response.text,
        )

    async def get_maps(self) -> list[CMCMapSchema]:
        return await self.__get_data(CMCApis.MAP, CMCMapSchema)

    async def get_metadata(self) -> list[CMCMetadataResponse]:
        return await self.__get_data(CMCApis.METADATA, CMCMetadataResponse)


main_cmc_repository = CMCRepository(api_key=settings.CMC_API_KEY)
