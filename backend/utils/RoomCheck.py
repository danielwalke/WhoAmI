import bcrypt
from database.database_classes.Room import Room
from fastapi import HTTPException
def verify_room_auth(room_password, room: Room):
    if not bcrypt.checkpw(room_password.encode('utf-8'), room.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    if room is None:
        raise HTTPException(status_code=404, detail=f"Room with ID {room_id} not found")
    return True