from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    CMC_API_KEY: str
    DATABASE_URL: str


settings = Settings()
