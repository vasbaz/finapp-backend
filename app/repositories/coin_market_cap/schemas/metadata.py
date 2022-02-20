import datetime

from pydantic import BaseModel, Field

from .platform import CMCPlatformSchema
from .urls import CMCUrlsSchema


class CMCMetadataSchema(BaseModel):
    urls: CMCUrlsSchema | None = None
    logo: str = Field(
        example="https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"
    )
    id: int = Field(example=1027)
    name: str = Field(example="Ethereum")
    symbol: str = Field(example="ETH")
    slug: str = Field(example="ethereum")
    description: str = Field(example="long description...")
    notice: str | None = Field(example=None, default=None)
    date_added: datetime.datetime = Field(example="2015-08-07T00:00:00.000Z")
    date_launched: datetime.datetime | None = Field(
        example="2015-08-07T00:00:00.000Z", default=None
    )
    tags: list[str] = Field(example=["mineable"])
    platform: CMCPlatformSchema | None = None
    category: str = Field(example="coin")
    self_reported_circulating_supply: str | None = Field(example=None, default=None)
    self_reported_market_cap: str | None = Field(example=None, default=None)
    self_reported_tags: list[str] | None = Field(example=None, default=None)
