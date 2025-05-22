from typing import TypeVar, Generic, Type, Optional, List
from sqlmodel import SQLModel
from wishwise_pr.repositories.base_repository import BaseRepository

T = TypeVar("T", bound=SQLModel)

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    async def get(self, id: int) -> Optional[T]:
        return await self.repository.get(id)

    async def list(self) -> List[T]:
        return await self.repository.get_all()

    async def create(self, obj: T) -> T:
        return await self.repository.create(obj)

    async def update(self, obj: T) -> T:
        return await self.repository.update(obj)

    async def delete(self, id: int) -> None:
        await self.repository.delete(id)
