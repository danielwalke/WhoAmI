SERVER_PREFIX = "/whoami"

## Health routes
HEALTH_ROUTE = ""
HELLO_ROUTE = "/hello"


## Room routes
CREATE_ROOM_ROUTE = "/create_room"
GET_ROOMS_ROUTE = "/rooms"
GET_ROOM_ROUTE = "/room/{room_id}/{room_password}"

## Upload routes
UPLOAD_SINGLE_ROUTE = "/upload/single"
UPLOAD_MULTIPLE_ROUTE = "/upload/multiple"
STATIC_FILES_ROUTE = "/static"

## Chat routes
WEBSOCKET_ROUTE = "/ws/{room_id}/{room_password}/{client_id}/{client_name}"