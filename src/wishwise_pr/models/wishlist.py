from datetime import datetime
from sqlmodel import SQLModel, Field


class Wishlist(SQLModel, table=True):
    __tablename__ = "wishlists"

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    title: str = Field(max_length=255, nullable=False)
    slug: str = Field(max_length=100, unique=True, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
