from typing import Union
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter, Request
from meta.RoomCreation import RoomCreation
from connection_management.ConnectionManager import ConnectionManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(redirect_slashes=False)
manager = ConnectionManager()
app.state.rooms = dict()

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

router = APIRouter(
    tags=["whoami"],
    redirect_slashes=False
)

@router.get("/hello")
def read_root():
    return {"Hello": "World"}

@router.post("/create_room")
def create_room(request: Request, body:RoomCreation):
    if body.room_name in request.app.state.rooms:
        return {"Error": "Room already exists"}
    app.state.rooms[body.room_name] = body.room_password
    return {"Success": f"Room {body.room_name} created"} ## TODO Return rather token?

@router.get("/rooms")
def get_rooms():
    print(app.state.rooms)
    print(list(app.state.rooms.keys()))
    return list(app.state.rooms.keys())

@router.websocket("/ws/{room_id}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, room_id:str, client_id: int):
    print(f"Client #{client_id} connected to room {room_id}")
    await manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(room_id, f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, f"Client #{client_id} left the chat")

app.include_router(
    router,
    prefix="/whoami"
)