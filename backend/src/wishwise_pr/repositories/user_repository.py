from wishwise_pr.repositories.base_repository import BaseRepository
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.user import User
from sqlmodel import select
from typing import Optional


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.session.exec(select(User).where(User.email == email))
        return result.first()