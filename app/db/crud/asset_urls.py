from ..models import asset_urls as models
from ..schemas import asset_urls as schemas
from ..crud.base import CRUDBase


class CRUDAssetUrls(CRUDBase[models.AssetUrls, schemas.AssetUrlsCreate]):
    pass


asset_urls = CRUDAssetUrls(models.AssetUrls)
