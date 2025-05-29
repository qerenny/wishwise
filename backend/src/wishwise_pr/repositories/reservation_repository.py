from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.reservation import Reservation
from wishwise_pr.repositories.base_repository import BaseRepository
from sqlmodel import select
from typing import Optional


class ReservationRepository(BaseRepository[Reservation]):
    def __init__(self, session: AsyncSession):
        super().__init__(Reservation, session)

    async def get_by_gift_id(self, gift_id: int) -> Optional[Reservation]:
        result = await self.session.exec(select(Reservation).where(Reservation.gift_id == gift_id))
        return result.first()

    async def get_by_gift_and_email(self, gift_id: int, email: str) -> Optional[Reservation]:
        result = await self.session.exec(
            select(Reservation).where(
                Reservation.gift_id == gift_id,
                Reservation.email == email
            )
        )
        return result.first()

    async def delete_by_gift_id(self, gift_id: int) -> None:
        result = await self.session.exec(select(Reservation).where(Reservation.gift_id == gift_id))
        obj = result.first()
        if obj:
            await self.session.delete(obj)
            await self.session.commit()