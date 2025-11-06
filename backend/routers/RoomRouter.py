from fastapi import APIRouter
import bcrypt
from typing import List
from fastapi import HTTPException
from sqlmodel import Session, select
from constants.Router import SERVER_PREFIX, CREATE_ROOM_ROUTE, GET_ROOMS_ROUTE, GET_ROOM_ROUTE
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from meta.RoomOut import RoomOut

router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)


@router.post(CREATE_ROOM_ROUTE)
def create_room(room:Room, session: SessionDep):
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

@router.get(GET_ROOM_ROUTE, response_model=Room)
def get_room(session: SessionDep, room_id, room_password) -> Room:
    room = session.get(Room, room_id)
    if not bcrypt.checkpw(room_password.encode('utf-8'), room.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    if room is None:
        raise HTTPException(status_code=404, detail=f"Room with ID {room_id} not found")
    room.password = "hidden"
    return room