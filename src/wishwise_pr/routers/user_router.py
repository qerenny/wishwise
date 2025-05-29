from typing import List
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.configs.database.engine import get_db_connection
from wishwise_pr.services.user_service import UserService
from wishwise_pr.schemas.user_schema import UserRegistrationSchema, UserLoginSchema, UserUpdateSchema, UserPublicSchema
from wishwise_pr.models.user import User
from wishwise_pr.repositories.user_repository import UserRepository

UserRouter = APIRouter(prefix="/users", tags=["user"])


def get_user_service(session: AsyncSession = Depends(get_db_connection)) -> UserService:
    return UserService(UserRepository(session))


@UserRouter.post(
    "/registration",
    description="Регистрация нового пользователя"
)
async def registration(
    body: UserRegistrationSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.registration(body)


@UserRouter.post(
    "/login",
    description="Вход пользователя в систему"
)
async def login(
    body: UserLoginSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.login(body)


@UserRouter.get(
    "/",
    response_model=List[User],
    description="Получение списка всех пользователей"
)
async def get_all(
    service: UserService = Depends(get_user_service),
):
    return await service.list()


@UserRouter.get(
    "/{id}",
    response_model=User,
    description="Получение информации о пользователе по его ID"
)
async def get_user(
    id: int,
    service: UserService = Depends(get_user_service),
):
    return await service.get(id)


@UserRouter.patch(
    "/{id}",
    response_model=UserPublicSchema,
    description="Обновление информации пользователя по ID"
)
async def update_user(
    id: int,
    body: UserUpdateSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.update(id, body)


@UserRouter.delete(
    "/{id}",
    description="Удаление пользователя по ID"
)
async def delete_user(
    id: int,
    service: UserService = Depends(get_user_service),
):
    await service.delete(id)
    return {"message": "User deleted"}
