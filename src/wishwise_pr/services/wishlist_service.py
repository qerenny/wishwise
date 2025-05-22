from typing import List
from wishwise_pr.models.wishlist import Wishlist
from wishwise_pr.repositories.wishlist_repository import WishlistRepository
from wishwise_pr.services.base_service import BaseService


class WishlistService(BaseService[Wishlist]):
    def __init__(self, repository: WishlistRepository):
        super().__init__(repository)
        self.repository: WishlistRepository = repository

    async def get_by_slug(self, slug: str) -> Wishlist:
        return await self.repository.get_by_slug(slug)

    async def get_user_lists(self, user_id: int) -> List[Wishlist]:
        return await self.repository.list_by_user_id(user_id)

    async def create(self, user_id: int, title: str, slug: str) -> Wishlist:
        wishlist = Wishlist(user_id=user_id, title=title, slug=slug)
        return await self.repository.create(wishlist)

    async def update(self, id: int, data) -> Wishlist:
        existing = await self.get(id)
        if not existing:
            raise ValueError("Wishlist not found")
        for key, value in data.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        return await self.repository.update(existing)
