from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserRegistrationSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class UserUpdateSchema(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=6)
