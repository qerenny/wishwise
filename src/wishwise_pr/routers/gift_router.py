from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.configs.database.engine import get_db_connection
from wishwise_pr.services.gift_service import GiftService
from wishwise_pr.schemas.gift_schema import GiftCreateSchema, GiftPublicSchema, GiftUpdateSchema
from wishwise_pr.repositories.gift_repository import GiftRepository
from wishwise_pr.repositories.reservation_repository import ReservationRepository

GiftRouter = APIRouter(prefix="/gifts", tags=["gift"])


def get_gift_service(session: AsyncSession = Depends(get_db_connection)) -> GiftService:
    gift_repo = GiftRepository(session)
    reservation_repo = ReservationRepository(session)
    return GiftService(gift_repo, reservation_repo)



@GiftRouter.post("/{wishlist_id}", response_model=GiftPublicSchema)
async def add_gift(
    wishlist_id: int,
    body: GiftCreateSchema,
    service: GiftService = Depends(get_gift_service),
):
    return await service.add_gift(wishlist_id=wishlist_id, title=body.title, url=body.url)

@GiftRouter.get("/gift/{id}", response_model=GiftPublicSchema)
async def get_gift(
    id: int,
    service: GiftService = Depends(get_gift_service),
):
    return await service.get(id)


@GiftRouter.get("/", response_model=List[GiftPublicSchema])
async def list_all_gifts(
    service: GiftService = Depends(get_gift_service),
):
    return await service.list()


@GiftRouter.get("/{wishlist_id}", response_model=List[GiftPublicSchema])
async def get_gifts(
    wishlist_id: int,
    service: GiftService = Depends(get_gift_service),
):
    return await service.get_by_wishlist(wishlist_id)


@GiftRouter.patch("/{id}", response_model=GiftPublicSchema)
async def update_gift(
    id: int,
    body: GiftUpdateSchema,
    service: GiftService = Depends(get_gift_service),
):
    return await service.update(id, body)

@GiftRouter.delete("/{gift_id}")
async def delete_gift(
    gift_id: int,
    service: GiftService = Depends(get_gift_service),
):
    return await service.delete(gift_id)
