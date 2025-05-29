from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Column, ForeignKey


class Gift(SQLModel, table=True):
    __tablename__ = "gifts"

    id: int = Field(default=None, primary_key=True)
    wishlist_id: int = Field(sa_column=Column(ForeignKey("wishlists.id", ondelete="CASCADE"), nullable=False))
    title: str = Field(max_length=255, nullable=False)
    url: Optional[str] = Field(default=None, max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
