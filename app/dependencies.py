from functools import lru_cache

from app.config import Settings


@lru_cache()
def app_settings() -> Settings:
    return Settings()
