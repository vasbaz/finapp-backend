from pydantic import BaseModel

from .asset_urls import AssetUrls


class CryptoAssetBase(BaseModel):
    name: str
    ticker: str
    cmc_id: int


class CryptoAssetCreate(CryptoAssetBase):
    pass


class CryptoAsset(CryptoAssetBase):
    id: int
    urls: AssetUrls

    class Config:
        orm_mode = True
