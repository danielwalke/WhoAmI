from fastapi import APIRouter
import bcrypt
from typing import List
from fastapi import HTTPException
from sqlmodel import Session, select
from constants.Router import SERVER_PREFIX, CREATE_ROOM_ROUTE, GET_ROOMS_ROUTE, POST_GET_ROOM_ROUTE
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from meta.RoomOut import RoomOut
from utils.RoomCheck import verify_room_auth

router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)


@router.post(CREATE_ROOM_ROUTE)
def create_room(room:Room, session: SessionDep):
    if session.exec(select(Room).where(Room.name == room.name)).first():
        raise HTTPException(status_code=400, detail=f"Room with name {room.name} already exists")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(room.password.encode('utf-8'), salt)
    room.password = hashed
    session.add(room)
    session.commit()
    session.refresh(room)
    return {"Success": f"Room {room.name} created"}

@router.get(GET_ROOMS_ROUTE, response_model=List[RoomOut])
def get_rooms(session: SessionDep) -> list[RoomOut]:
    rooms = session.exec(select(Room)).all()
    out_rooms = []
    for room in rooms:
        room_out = RoomOut(id = room.id, created_at=room.created_at, name = room.name)
        out_rooms.append(room_out)
    return out_rooms

@router.post(POST_GET_ROOM_ROUTE, response_model=Room)
def get_room(room: Room, session: SessionDep) -> Room:
    fetched_room = session.get(Room, room.id)
    verify_room_auth(room_password=room.password, room=fetched_room)
    out_room = RoomOut(id = fetched_room.id, created_at=fetched_room.created_at, name = fetched_room.name)
    return out_room