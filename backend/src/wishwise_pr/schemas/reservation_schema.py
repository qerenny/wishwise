from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class ReservationCreateSchema(BaseModel):
    name: str = Field(..., min_length=1)
    email: Optional[EmailStr] = None


class ReservationPublicSchema(BaseModel):
    id: int
    gift_id: int
    name: str
    email: Optional[EmailStr]
    created_at: datetime
    confirmed: bool

    model_config = {
        "from_attributes": True
    }
class ReservationUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    confirmed: Optional[bool] = None
