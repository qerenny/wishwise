from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.configs.database.engine import get_db_connection
from wishwise_pr.services.reservation_service import ReservationService
from wishwise_pr.schemas.reservation_schema import ReservationCreateSchema, ReservationPublicSchema, ReservationUpdateSchema
from typing import List

ReservationRouter = APIRouter(prefix="/reservations", tags=["reservation"])


def get_reservation_service(session: AsyncSession = Depends(get_db_connection)) -> ReservationService:
    return ReservationService(session)

@ReservationRouter.get("/gift/{gift_id}", response_model=ReservationPublicSchema)
async def get_by_gift_id(
    gift_id: int,
    service: ReservationService = Depends(get_reservation_service),
):
    return await service.get_by_gift(gift_id)


@ReservationRouter.get("/", response_model=List[ReservationPublicSchema])
async def list_reservations(
    service: ReservationService = Depends(get_reservation_service),
):
    return await service.list()


@ReservationRouter.post("/reserve/{gift_id}", response_model=ReservationPublicSchema)
async def reserve_gift(
    gift_id: int,
    body: ReservationCreateSchema,
    service: ReservationService = Depends(get_reservation_service),
):
    return await service.reserve(gift_id=gift_id, name=body.name, email=body.email)


@ReservationRouter.post("/cancel/{gift_id}")
async def cancel_reservation(
    gift_id: int,
    email: str,
    service: ReservationService = Depends(get_reservation_service),
):
    await service.cancel(gift_id=gift_id, email=email)
    return {"message": "Reservation cancelled"}

@ReservationRouter.patch("/{id}", response_model=ReservationPublicSchema)
async def update_reservation(
    id: int,
    body: ReservationUpdateSchema,
    service: ReservationService = Depends(get_reservation_service),
):
    return await service.update(id, body)

@ReservationRouter.delete("/{id}")
async def delete_reservation(
    id: int,
    service: ReservationService = Depends(get_reservation_service),
):
    await service.delete(id)
    return {"message": "Reservation deleted"}