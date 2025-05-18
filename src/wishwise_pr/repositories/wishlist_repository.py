from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from wishwise_pr.models.wishlist import Wishlist
from wishwise_pr.repositories.base_repository import BaseRepository
from typing import List, Optional


class WishlistRepository(BaseRepository[Wishlist]):
    def __init__(self, session: AsyncSession):
        super().__init__(Wishlist, session)

    async def get_by_slug(self, slug: str) -> Optional[Wishlist]:
        result = await self.session.exec(select(Wishlist).where(Wishlist.slug == slug))
        return result.first()

    async def list_by_user_id(self, user_id: int) -> List[Wishlist]:
        result = await self.session.exec(select(Wishlist).where(Wishlist.user_id == user_id))
        return result.all()