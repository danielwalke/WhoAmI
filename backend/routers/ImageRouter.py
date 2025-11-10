import bcrypt
from typing import List
from fastapi import APIRouter, HTTPException
from constants.Router import SERVER_PREFIX, IMAGE_ROUTE, DELETE_IMAGE_ROUTE
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

@router.delete(DELETE_IMAGE_ROUTE)
def delete_image(image:Image, room:Room, session: SessionDep):  
    fetched_room = session.get(Room, room.id)
    verify_room_auth(room.password, fetched_room)
    fetched_image = session.get(Image, image.id)
    if not fetched_image or fetched_image.room_id != fetched_room.id:
        raise HTTPException(status_code=404, detail="Image not found in the specified room")
    session.delete(fetched_image)
    session.commit()
    return {"detail": "Image deleted successfully"}