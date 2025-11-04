from typing import Annotated
from datetime import datetime
from sqlmodel import Field, SQLModel


class Room(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    password: str = Field(default=None)

    def __repr__(self):
        return f"Room(id={self.id}, name={self.name}, created_at={self.created_at})"