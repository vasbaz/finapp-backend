from typing import TypeVar, Generic, Type

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_all(self, db: AsyncSession) -> list[Type[ModelType]]:
        db_result = await db.execute(select(self.model))
        return db_result.scalars().all()

    async def create_item(
        self, db: AsyncSession, item: Type[CreateSchemaType]
    ) -> Type[ModelType]:
        db_item = self.model(**item.dict())
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item
