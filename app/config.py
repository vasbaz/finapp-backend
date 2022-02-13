from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    CMC_API_KEY: str
    POSTGRESQL_URL: str


settings = Settings()
