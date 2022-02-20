from pydantic import BaseSettings


class Settings(BaseSettings):
    CMC_API_KEY: str
    POSTGRESQL_URL: str


settings = Settings()
