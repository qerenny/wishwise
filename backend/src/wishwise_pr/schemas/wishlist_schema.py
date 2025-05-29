from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class WishlistCreateSchema(BaseModel):
    title: str = Field(..., min_length=1)
    slug: str = Field(..., min_length=1)


class WishlistPublicSchema(BaseModel):
    id: int
    user_id: int
    title: str
    slug: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class WishlistUpdateSchema(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
