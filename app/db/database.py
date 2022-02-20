from typing import Any

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_async_engine(settings.POSTGRESQL_URL)
session_local = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@as_declarative()
class Base:
    id: Any
