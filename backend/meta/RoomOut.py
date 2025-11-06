from pydantic import BaseModel
import datetime

class RoomOut(BaseModel):
    id: str 
    name: str 
    created_at: datetime.datetime