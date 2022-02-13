from typing import Generator

from app.db.database import session_local
from app.repositories.coin_market_cap.repository import (
    main_cmc_repository,
    CMCRepository,
)


def get_db() -> Generator:
    db = session_local()
    try:
        yield db
    finally:
        db.close()


def get_main_cmc_repository() -> CMCRepository:
    return main_cmc_repository
