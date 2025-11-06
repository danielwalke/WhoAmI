import bcrypt
from typing import List
from fastapi import APIRouter, HTTPException
from constants.Router import SERVER_PREFIX, IMAGE_ROUTE
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from database.database_classes.Image import Image
from sqlmodel import select

router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)

@router.get(IMAGE_ROUTE)
def read_images(session: SessionDep, room_id, room_password, response_model=List[Room]) -> list[Image]:
    room = session.get(Room, room_id)
    if not bcrypt.checkpw(room_password.encode('utf-8'), room.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    if room is None:
        raise HTTPException(status_code=404, detail=f"Room with ID {room_id} not found")
    room.password = "hidden"
    statement = select(Image).where(Image.room_id == room.id)
    return session.exec(statement).all()