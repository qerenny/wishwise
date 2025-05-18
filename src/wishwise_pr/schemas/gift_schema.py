from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl, Field


class GiftCreateSchema(BaseModel):
    title: str = Field(..., min_length=1)
    url: Optional[HttpUrl] = None


class GiftPublicSchema(BaseModel):
    id: int
    wishlist_id: int
    title: str
    url: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class GiftUpdateSchema(BaseModel):
    title: Optional[str] = None
    url: Optional[HttpUrl] = None
