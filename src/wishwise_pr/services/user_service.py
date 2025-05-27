from sqlmodel.ext.asyncio.session import AsyncSession
from wishwise_pr.models.user import User
from wishwise_pr.repositories.user_repository import UserRepository
from wishwise_pr.services.base_service import BaseService
from wishwise_pr.schemas.user_schema import UserRegistrationSchema, UserLoginSchema
from wishwise_pr.utils.auth import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status

class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.repo: UserRepository = repository

    async def registration(self, body: UserRegistrationSchema) -> User:
        hashed = hash_password(body.password)
        return await self.repo.create(
            User(email=body.email, username=body.username, password_hash=hashed)
        )

    async def login(self, body: UserLoginSchema) -> str:
        user = await self.repo.get_by_email(body.email)
        if not user or not verify_password(body.password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return create_access_token({"sub": str(user.id)})
