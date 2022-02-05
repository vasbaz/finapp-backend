import enum

from httpx import AsyncClient

from .models.map import CMCMap

CMC_API_URL = "https://pro-api.coinmarketcap.com"
API_KEY_HEADER = "X-CMC_PRO_API_KEY"


class CMCApis(enum.Enum):
    map = CMC_API_URL + "/v1/cryptocurrency/map"


class CMCRepository:
    def __init__(self, api_key: str):
        self.auth_header = {API_KEY_HEADER: api_key}

    async def get_maps(self):
        async with AsyncClient() as ac:
            maps_response = await ac.get(CMCApis.map.value, headers=self.auth_header)

        if maps_response.status_code == 200:
            raw_maps_response = maps_response.json()
            maps = list(map(CMCMap.parse_obj, raw_maps_response["data"]))
            return maps
        return {"error": "error"}
