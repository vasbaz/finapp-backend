import datetime

from pydantic import BaseModel, Field

from .platform import CMCPlatform


class CMCMap(BaseModel):
    id: int = Field(example=1839)
    rank: int = Field(example=3)
    name: str = Field(example="Binance Coin")
    symbol: str = Field(example="BNB")
    slug: str = Field(example="binance-coin")
    is_active: bool = Field(example=1)
    first_historical_data: datetime.datetime = Field(example="2017-07-25T04:30:05.000Z")
    last_historical_data: datetime.datetime = Field(example="2020-05-05T20:44:01.000Z")
    platform: CMCPlatform | None = None
