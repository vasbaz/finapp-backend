import datetime

from pydantic import BaseModel

from .platform import CMCPlatform


class CMCMap(BaseModel):
    id: int
    rank: int
    name: str
    symbol: str
    slug: str
    is_active: bool
    first_historical_data: datetime.datetime
    last_historical_data: datetime.datetime
    platform: CMCPlatform | None = None
