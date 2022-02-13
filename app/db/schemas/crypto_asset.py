from pydantic import BaseModel

from .assets_url import AssetUrls


class CryptoAssetBase(BaseModel):
    name: str
    ticker: str


class CryptoAssetCreate(CryptoAssetBase):
    pass


class CryptoAsset(CryptoAssetBase):
    id: int
    urls: list[AssetUrls]

    class Config:
        orm_mode = True
