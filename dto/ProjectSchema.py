from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Project(BaseModel):
    project_name: str
    user_id: int

    class Config:
        orm_mode = True