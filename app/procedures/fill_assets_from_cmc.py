from sqlalchemy.ext.asyncio import AsyncSession

from app.db.crud.crypto_asset import crypto_asset
from app.db.schemas.crypto_asset import CryptoAssetCreate
from app.repositories.coin_market_cap.repository import CMCRepository
from app.repositories.coin_market_cap.schemas.map import CMCMapSchema


async def create_asset_from_map(db: AsyncSession, cmc_map: CMCMapSchema):
    return await crypto_asset.create_item(
        db=db,
        item=CryptoAssetCreate(
            ticker=cmc_map.symbol, name=cmc_map.name, cmc_id=cmc_map.id
        ),
    )


async def fill_assets_from_cmc(db: AsyncSession, cmc_repository: CMCRepository):
    maps = await cmc_repository.get_maps()
    created_crypto_assets = [
        await create_asset_from_map(cmc_map, db) for cmc_map in maps
    ]

    return created_crypto_assets
