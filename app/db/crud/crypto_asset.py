from ..models import crypto_asset as models
from ..schemas import crypto_asset as schemas
from ..crud.base import CRUDBase


class CRUDCryptoAsset(CRUDBase[models.CryptoAsset, schemas.CryptoAssetCreate]):
    pass


crypto_asset = CRUDCryptoAsset(models.CryptoAsset)
