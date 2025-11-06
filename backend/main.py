from constants.Router import SERVER_PREFIX
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from utils.DatabaseUtils import create_db_and_tables
from utils.DatabaseUtils import engine
from constants.Upload import UPLOAD_DIR
from constants.Router import STATIC_FILES_ROUTE
from routers.HealthRouter import router as HealthRouter
from routers.RoomRouter import router as RoomRouter
from routers.UploadRouter import router as UploadRouter
from routers.ChatRouter import router as ChatRouter
from routers.ImageRouter import router as ImageRouter

app = FastAPI(redirect_slashes=False)
app.mount(
    STATIC_FILES_ROUTE,  # The URL path
    StaticFiles(directory=UPLOAD_DIR), # The directory to serve
    name="static"
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
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