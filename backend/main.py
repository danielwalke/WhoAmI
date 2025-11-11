from constants.Router import SERVER_PREFIX
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from utils.DatabaseUtils import create_db_and_tables
from utils.DatabaseUtils import engine
from constants.Upload import UPLOAD_DIR
from constants.Router import STATIC_FILES_ROUTE
from fastapi import FastAPI
from datetime import datetime
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from routers.HealthRouter import router as HealthRouter
from routers.RoomRouter import router as RoomRouter
from routers.UploadRouter import router as UploadRouter
from routers.ChatRouter import router as ChatRouter
from routers.ImageRouter import router as ImageRouter
from utils.DatabaseUtils import get_session
from sqlmodel import select
from database.database_classes.Room import Room 
from database.database_classes.Image import Image

app = FastAPI(redirect_slashes=False)
app.mount(
    STATIC_FILES_ROUTE,  # The URL path
    StaticFiles(directory=UPLOAD_DIR), # The directory to serve
    name="static"
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def my_daily_task():
    print(f"Task is running at {datetime.now()}")
    session = get_session().__next__()
    rooms = session.exec(select(Room)).all()
    rooms_created_more_than_two_days_ago = [room for room in rooms if (datetime.now() - room.created_at).days > 2]
    for room in rooms_created_more_than_two_days_ago:
        images_to_delete = session.exec(select(Image).where(Image.room_id == room.id)).all()
        for image in images_to_delete:
            file_path = UPLOAD_DIR / image.id
            if file_path.exists():
                file_path.unlink()
            session.delete(image)
        session.delete(room)
    session.commit()
    print(f"{len(rooms_created_more_than_two_days_ago)} old rooms and their images have been deleted.")

scheduler = BackgroundScheduler()
trigger = CronTrigger(minute='0', hour='7')  # 7:00 AM every day
scheduler.add_job(my_daily_task, trigger)
scheduler.start()


origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
def on_startup():    
    create_db_and_tables(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    scheduler.shutdown()

app.include_router(
    HealthRouter,
    prefix=SERVER_PREFIX
)
app.include_router(
    RoomRouter,
    prefix=SERVER_PREFIX
)
app.include_router(
    UploadRouter, 
    prefix=SERVER_PREFIX
)
app.include_router(
    ChatRouter,
    prefix=SERVER_PREFIX
)
app.include_router(
    ImageRouter,
    prefix=SERVER_PREFIX
)