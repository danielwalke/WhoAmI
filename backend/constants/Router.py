SERVER_PREFIX = "/whoami"

## Health routes
HEALTH_ROUTE = ""
HELLO_ROUTE = "/hello"


## Room routes
CREATE_ROOM_ROUTE = "/create_room"
GET_ROOMS_ROUTE = "/rooms"
GET_ROOM_ROUTE = "/room/{room_id}/{room_password}"

## Upload routes
UPLOAD_MULTIPLE_ROUTE = "/upload/multiple/{room_id}/{room_password}"
STATIC_FILES_ROUTE = "/static"

## Chat routes
WEBSOCKET_ROUTE = "/ws/{room_id}/{room_password}/{client_id}/{client_name}"

## Image routes
IMAGE_ROUTE = "/{room_id}/{room_password}/get_images"