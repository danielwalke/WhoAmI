import bcrypt
from typing import List
from fastapi import APIRouter, HTTPException
from constants.Router import SERVER_PREFIX, IMAGE_ROUTE
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from database.database_classes.Image import Image
from sqlmodel import select
from utils.RoomCheck import verify_room_auth

router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)

@router.post(IMAGE_ROUTE)
def read_images(room:Room, session: SessionDep) -> list[Image]:
    fetched_room = session.get(Room, room.id)
    verify_room_auth(room.password, fetched_room)
    statement = select(Image).where(Image.room_id == fetched_room.id)
    return session.exec(statement).all()