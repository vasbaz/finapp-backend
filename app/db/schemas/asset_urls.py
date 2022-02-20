from pydantic import BaseModel


class AssetUrlsBase(BaseModel):
    crypto_asset_id: int
    github: str | None = None


class AssetUrlsCreate(AssetUrlsBase):
    pass


class AssetUrls(AssetUrlsBase):
    id: int

    class Config:
        orm_mode = True
