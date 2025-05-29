from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.configs.database.engine import get_db_connection
from wishwise_pr.services.wishlist_service import WishlistService
from wishwise_pr.schemas.wishlist_schema import WishlistCreateSchema, WishlistPublicSchema, WishlistUpdateSchema
from wishwise_pr.repositories.wishlist_repository import WishlistRepository
from wishwise_pr.utils.auth import get_current_user_id


WishlistRouter = APIRouter(prefix="/wishlists", tags=["wishlist"])


def get_wishlist_service(session: AsyncSession = Depends(get_db_connection)) -> WishlistService:
    return WishlistService(WishlistRepository(session))


@WishlistRouter.post(
    "/",
    response_model=WishlistPublicSchema,
    description="Создать новый вишлист для пользователя"
)
async def create_wishlist(
    body: WishlistCreateSchema,
    user_id: int,
    service: WishlistService = Depends(get_wishlist_service),
):
    return await service.create(user_id=user_id, title=body.title, slug=body.slug)


@WishlistRouter.get(
    "/my",
    response_model=List[WishlistPublicSchema],
    description="Получить список вишлистов текущего пользователя"
)
async def get_user_wishlists(
    user_id: int = Depends(get_current_user_id),
    service: WishlistService = Depends(get_wishlist_service),
):
    return await service.get_user_lists(user_id)



@WishlistRouter.get(
    "/{slug}",
    response_model=WishlistPublicSchema,
    description="Получить вишлист по его уникальному slug"
)
async def get_by_slug(
    slug: str,
    service: WishlistService = Depends(get_wishlist_service),
):
    return await service.get_by_slug(slug)


@WishlistRouter.get(
    "/{id}",
    response_model=WishlistPublicSchema,
    description="Получить вишлист по его ID"
)
async def get_by_id(
    id: int,
    service: WishlistService = Depends(get_wishlist_service),
):
    return await service.get(id)


@WishlistRouter.get(
    "/",
    response_model=List[WishlistPublicSchema],
    description="Получить список всех вишлистов"
)
async def list_all(
    service: WishlistService = Depends(get_wishlist_service),
):
    return await service.list()


@WishlistRouter.patch(
    "/{id}",
    response_model=WishlistPublicSchema,
    description="Обновить вишлист по его ID"
)
async def update_wishlist(
    id: int,
    body: WishlistUpdateSchema,
    service: WishlistService = Depends(get_wishlist_service),
):
    return await service.update(id, body)


@WishlistRouter.delete(
    "/{id}",
    description="Удалить вишлист по его ID"
)
async def delete_wishlist(
    id: int,
    service: WishlistService = Depends(get_wishlist_service),
):
    await service.delete(id)
    return {"message": "Wishlist удалён"}

