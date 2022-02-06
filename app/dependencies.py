from functools import lru_cache

from app.config import Settings


@lru_cache()
def settings() -> Settings:
    return Settings()
