from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from .crypto_asset import CryptoAsset  # noqa: F401


class AssetUrls(Base):
    __tablename__ = "assets_urls"

    id = Column(Integer, primary_key=True, index=True)
    crypto_asset_id = Column(Integer, ForeignKey("crypto_assets.id"))
    github = Column(String, unique=True)

    owner = relationship("CryptoAsset", back_populates="urls")
