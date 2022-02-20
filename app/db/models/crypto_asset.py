from typing import TYPE_CHECKING

from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from app.db.database import Base

if TYPE_CHECKING:
    from .asset_urls import AssetUrls  # noqa: F401


class CryptoAsset(Base):
    __tablename__ = "crypto_assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    ticker = Column(String, unique=True, index=True)
    cmc_id = Column(Integer, unique=True)

    urls = relationship("AssetUrls", back_populates="owner", uselist=False)
