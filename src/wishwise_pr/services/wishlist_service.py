from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.wishlist import Wishlist
from wishwise_pr.repositories.wishlist_repository import WishlistRepository


class WishlistService:
    def __init__(self, session: AsyncSession):
        self.repo = WishlistRepository(session)

    async def create(self, user_id: int, title: str, slug: str) -> Wishlist:
        wishlist = Wishlist(user_id=user_id, title=title, slug=slug)
        return await self.repo.create(wishlist)

    async def get_by_slug(self, slug: str) -> Wishlist:
        return await self.repo.get_by_slug(slug)

    async def get_user_lists(self, user_id: int) -> List[Wishlist]:
        return await self.repo.list_by_user_id(user_id)

    async def delete(self, wishlist_id: int) -> None:
        await self.repo.delete(wishlist_id)
