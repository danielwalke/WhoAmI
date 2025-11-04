from typing import List
from sqlmodel import Field, SQLModel

class Membership(SQLModel, table=True):
    """
    This is the "link table" that connects rooms and clients.
    """
    room_id: int | None = Field(
        default=None, foreign_key="room.id", primary_key=True, index=True
    )
    client_id: int | None = Field(
        default=None, foreign_key="client.id", primary_key=True, index=True
    )