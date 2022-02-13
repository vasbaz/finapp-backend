from pydantic import BaseModel


class AssetUrlsBase(BaseModel):
    github: str | None = None


class AssetUrlsCreate(AssetUrlsBase):
    pass


class AssetUrls(AssetUrlsBase):
    id: int
    crypto_asset_id: int

    class Config:
        orm_mode = True
