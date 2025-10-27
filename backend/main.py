from typing import Union
from fastapi import FastAPI, APIRouter, Request
from meta.RoomCreation import RoomCreation

app = FastAPI(redirect_slashes=False)
app.state.rooms = dict()

router = APIRouter(
    tags=["whoami"],
    redirect_slashes=False
)

@router.get("/hello")
def read_root():
    return {"Hello": "World"}

@router.post("/create_room")
def create_room(request: Request, body:RoomCreation):
    ## First proof of concept and later password in hashed forms in sqllite db
    if body.room_name in request.app.state.rooms:
        return {"Error": "Room already exists"}
    app.state.rooms[body.room_name] = body.room_password
    return {"Success": f"Room {body.room_name} created"}

app.include_router(
    router,
    prefix="/whoami"
)