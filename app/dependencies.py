from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import session_local
from app.repositories.coin_market_cap.repository import (
    main_cmc_repository,
    CMCRepository,
)


async def get_db() -> AsyncSession:
    async with session_local() as session:
        yield session


def get_main_cmc_repository() -> CMCRepository:
    return main_cmc_repository
