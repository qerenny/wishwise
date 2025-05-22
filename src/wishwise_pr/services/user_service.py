from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.user import User
from wishwise_pr.repositories.user_repository import UserRepository
from wishwise_pr.services.base_service import BaseService
from wishwise_pr.schemas.user_schema import UserRegistrationSchema, UserLoginSchema


class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.repo: UserRepository = repository

    async def registration(self, body: UserRegistrationSchema) -> User:
        return await self.repo.create(
            User(email=body.email, password_hash=body.password)
        )

    async def login(self, body: UserLoginSchema) -> User:
        # TODO: реализовать валидацию по email + password
        return await self.repo.create(
            User(email=body.email, password_hash=body.password)
        )
