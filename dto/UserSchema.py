from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    isPremium: bool | None = None
    premium_purchased_date: datetime | None = None
    premium_expiry_date: datetime | None = None

    class Config:
        orm_mode = True