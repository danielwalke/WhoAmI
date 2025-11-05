from fastapi import APIRouter
from constants.Router import SERVER_PREFIX, HEALTH_ROUTE, HELLO_ROUTE

router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)

@router.get(HELLO_ROUTE)
def read_root():
    return {"Hello": "World"}

@router.get(HEALTH_ROUTE)
def read_root():
    return {"Status": "Healthy"}