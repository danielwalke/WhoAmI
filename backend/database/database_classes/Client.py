from typing import Annotated
from datetime import datetime
from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    