from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.gift import Gift
from wishwise_pr.repositories.gift_repository import GiftRepository
from wishwise_pr.repositories.reservation_repository import ReservationRepository
from wishwise_pr.services.base_service import BaseService


class GiftService(BaseService[Gift]):
    def __init__(self, gift_repository: GiftRepository, reservation_repository: ReservationRepository):
        super().__init__(gift_repository)
        self.repo: GiftRepository = gift_repository
        self.reservation_repo: ReservationRepository = reservation_repository

    async def add_gift(self, wishlist_id: int, title: str, url: str | None = None) -> Gift:
        gift = Gift(wishlist_id=wishlist_id, title=title, url=str(url) if url is not None else None)
        return await self.repo.create(gift)

    async def get_by_wishlist(self, wishlist_id: int) -> List[Gift]:
        return await self.repo.list_by_wishlist(wishlist_id)

    async def delete(self, gift_id: int) -> None:
        await self.reservation_repo.delete_by_gift_id(gift_id)
        await self.repo.delete(gift_id)
