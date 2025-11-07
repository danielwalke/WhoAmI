
import bcrypt
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from constants.Router import SERVER_PREFIX, WEBSOCKET_ROUTE
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from connection_management.ConnectionManager import ConnectionManager

router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)

manager = ConnectionManager()

@router.websocket(WEBSOCKET_ROUTE)
async def websocket_endpoint(websocket: WebSocket, room_id:str, room_password:str, client_id: str, client_name:str, session: SessionDep):
    ## TODO Make this mor esecure with session cookie
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