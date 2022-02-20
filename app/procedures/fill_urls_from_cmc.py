from sqlalchemy.ext.asyncio import AsyncSession

from app.db.crud.asset_urls import asset_urls
from app.db.crud.crypto_asset import crypto_asset
from app.db.models.crypto_asset import CryptoAsset
from app.db.schemas.asset_urls import AssetUrlsCreate
from app.repositories.coin_market_cap.repository import CMCRepository
from app.repositories.coin_market_cap.schemas.metadata import CMCMetadataSchema


async def add_url_from_metadata(
    db: AsyncSession, asset: CryptoAsset, cmc_metadata: CMCMetadataSchema
):
    source_code = None
    cmc_metadata_source_code = cmc_metadata.urls.source_code
    if cmc_metadata_source_code:
        source_code = cmc_metadata_source_code[0]

    # ToDo: Check if not GitHub
    await asset_urls.create_item(
        db=db,
        item=AssetUrlsCreate(crypto_asset_id=asset.id, github=source_code),
    )


async def fill_urls_from_cmc(db: AsyncSession, cmc_repository: CMCRepository):
    crypto_assets = await crypto_asset.get_all(db)
    cmc_ids_for_metadata = list(map(lambda asset: asset.cmc_id, crypto_assets))
    metadata = await cmc_repository.get_metadata(cmc_ids=cmc_ids_for_metadata)

    for asset in crypto_assets:
        await add_url_from_metadata(db, asset, metadata[asset.cmc_id])

    return crypto_assets
