from typing import Annotated
from datetime import datetime
from sqlmodel import Field, SQLModel


class Image(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str = Field(index=True, default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    url: str = Field(default=None)
    room_id: str = Field(foreign_key="room.id", index=True)

    def __repr__(self):
        return f"Image(id={self.id}, name={self.name}, created_at={self.created_at}, url={self.url})"