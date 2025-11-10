import bcrypt
from typing import List
from fastapi import APIRouter, HTTPException
from constants.Router import SERVER_PREFIX, IMAGE_ROUTE, DELETE_IMAGE_ROUTE, DELETE_ALL_IMAGES_IN_ROOM_ROUTE
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from database.database_classes.Image import Image
from sqlmodel import select
from utils.RoomCheck import verify_room_auth
from constants.Upload import UPLOAD_DIR

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
    file_path = UPLOAD_DIR / fetched_image.id
    if file_path.exists():
        file_path.unlink()
    session.commit()
    return {"detail": "Image deleted successfully"}

@router.delete(DELETE_ALL_IMAGES_IN_ROOM_ROUTE)
def remove_all_images_in_room(room:Room, session: SessionDep):
    fetched_room = session.get(Room, room.id)
    print(fetched_room)
    print(room.password)
    verify_room_auth(room.password, fetched_room)
    room_id = fetched_room.id
    statement = select(Image).where(Image.room_id == room_id)
    images = session.exec(statement).all()
    for image in images:
        file_path = UPLOAD_DIR / image.id
        if file_path.exists():
            file_path.unlink()
        session.delete(image)
    session.commit()