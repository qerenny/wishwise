from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.gift import Gift
from wishwise_pr.repositories.base_repository import BaseRepository
from sqlmodel import select
from typing import List


class GiftRepository(BaseRepository[Gift]):
    def __init__(self, session: AsyncSession):
        super().__init__(Gift, session)

    async def list_by_wishlist(self, wishlist_id: int) -> List[Gift]:
        result = await self.session.exec(select(Gift).where(Gift.wishlist_id == wishlist_id))
        return result.all()