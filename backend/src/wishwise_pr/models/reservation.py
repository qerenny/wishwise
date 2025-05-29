from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Reservation(SQLModel, table=True):
    __tablename__ = "reservations"

    id: int = Field(default=None, primary_key=True)
    gift_id: int = Field(foreign_key="gifts.id", nullable=False)
    name: str = Field(max_length=100, nullable=False)
    email: Optional[str] = Field(default=None, max_length=255)
    created_at: datetime = Field(default_factory=lambda: datetime.utcnow())
