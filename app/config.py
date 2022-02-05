from pydantic import BaseSettings


class Settings(BaseSettings):
    cmc_api_key: str


settings = Settings()
