from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserRegistrationSchema(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(min_length=6)


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
class UserUpdateSchema(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=6)
