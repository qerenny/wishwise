from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.gift import Gift
from wishwise_pr.repositories.gift_repository import GiftRepository
from wishwise_pr.repositories.reservation_repository import ReservationRepository


class GiftService:
    def __init__(self, session: AsyncSession):
        self.repo = GiftRepository(session)
        self.reservation_repo = ReservationRepository(session)


    async def add_gift(self, wishlist_id: int, title: str, url: str | None = None) -> Gift:
        gift = Gift(wishlist_id=wishlist_id, title=title, url=url)
        return await self.repo.create(gift)

    async def get_by_wishlist(self, wishlist_id: int) -> List[Gift]:
        return await self.repo.list_by_wishlist(wishlist_id)

    async def delete(self, gift_id: int) -> None:
            # Удаляем бронь, если она есть
            await self.reservation_repo.delete_by_gift_id(gift_id)
            # Удаляем сам подарок
            await self.repo.delete(gift_id)
