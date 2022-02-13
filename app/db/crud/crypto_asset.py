from sqlalchemy.orm import Session

from ..models import crypto_asset as models
from ..schemas import crypto_asset as schemas
from ..crud.base import CRUDBase


class CRUDCryptoAsset(CRUDBase[models.CryptoAsset]):
    def get_assets(self, db: Session):
        return db.query(self.model).all()

    def create_asset(self, db: Session, asset: schemas.CryptoAssetCreate):
        db_crypto_asset = self.model(**asset.dict())
        db.add(db_crypto_asset)
        db.commit()
        db.refresh(db_crypto_asset)
        return db_crypto_asset


crypto_asset = CRUDCryptoAsset(models.CryptoAsset)
