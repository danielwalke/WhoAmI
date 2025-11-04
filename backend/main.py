import bcrypt
import json
from typing import Union
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter, Request, Depends, HTTPException
from meta.RoomCreation import RoomCreation
from connection_management.ConnectionManager import ConnectionManager
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from typing import Annotated
from sqlmodel import create_engine, SQLModel, Session, select
from constants.Database import SQLITE_URL
from utils.DatabaseUtils import create_db_and_tables
from database.database_classes.Room import Room


app = FastAPI(redirect_slashes=False)
manager = ConnectionManager()
app.state.rooms = dict()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    # You can also use allow_origins=["*"] for development, but be specific in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)

def get_session():
        with Session(engine) as session:
            yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():    
    create_db_and_tables(engine)

router = APIRouter(
    tags=["whoami"],
    redirect_slashes=False
)

@router.get("/hello")
def read_root():
    return {"Hello": "World"}

@router.post("/create_room")
def create_room(room:Room, session: SessionDep):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(room.password.encode('utf-8'), salt)
    room.password = hashed

    session.add(room)
    session.commit()
    session.refresh(room)
    return {"Success": f"Room {room.name} created"}

@router.get("/rooms")
def get_rooms(session: SessionDep) -> list[Room]:
    rooms = session.exec(select(Room)).all()
    for room in rooms:
        room.password = "hidden"
    return rooms

@router.get("/room/{room_id}/{room_password}", response_model=Room)
def get_room(session: SessionDep, room_id, room_password) -> Room:
    room = session.get(Room, room_id)
    if not bcrypt.checkpw(room_password.encode('utf-8'), room.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    if room is None:
        raise HTTPException(status_code=404, detail=f"Room with ID {room_id} not found")
    room.password = "hidden"
    return room

@router.websocket("/ws/{room_id}/{room_password}/{client_id}/{client_name}")
async def websocket_endpoint(websocket: WebSocket, room_id:str, room_password:str, client_id: str, client_name:str, session: SessionDep):
    print(f"Client #{client_id} ({client_name}) connected to room {room_id}")
    room = session.get(Room, room_id)
    
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    if not bcrypt.checkpw(room_password.encode('utf-8'), room.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    

    await manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_payload = {
                "clientId": client_id,
                "message": data,
                "clientName": client_name
            }
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(room_id, json.dumps(message_payload))
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, f"Client #{client_id} left the chat")

app.include_router(
    router,
    prefix="/whoami"
)