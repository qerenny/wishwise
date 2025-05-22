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


@UserRouter.post("/registration")
async def registration(
    body: UserRegistrationSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.registration(body)


@UserRouter.post("/login")
async def login(
    body: UserLoginSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.login(body)


@UserRouter.get("/", response_model=List[User])
async def get_all(
    service: UserService = Depends(get_user_service),
):
    return await service.list()


@UserRouter.get("/{id}", response_model=User)
async def get_user(
    id: int,
    service: UserService = Depends(get_user_service),
):
    return await service.get(id)



@UserRouter.patch("/{id}", response_model=UserPublicSchema)
async def update_user(
    id: int,
    body: UserUpdateSchema,
    service: UserService = Depends(get_user_service),
):
    return await service.update(id, body)


@UserRouter.delete("/{id}")
async def delete_user(
    id: int,
    service: UserService = Depends(get_user_service),
):
    await service.delete(id)
    return {"message": "User deleted"}

# @UserRouter.post(
#     "/",
#     response_model=AuthorSchema,
#     status_code=status.HTTP_201_CREATED,
# )
# def create(
#     author: AuthorPostRequestSchema,
#     authorService: AuthorService = Depends(),
# ):
#     return authorService.create(author).normalize()
#
#
# @UserRouter.patch("/{id}", response_model=AuthorSchema)
# def update(
#     id: int,
#     author: AuthorPostRequestSchema,
#     authorService: AuthorService = Depends(),
# ):
#     return authorService.update(id, author).normalize()
#
#
# @UserRouter.delete(
#     "/{id}", status_code=status.HTTP_204_NO_CONTENT
# )
# def delete(
#     id: int, authorService: AuthorService = Depends()
# ):
#     return authorService.delete(id)
