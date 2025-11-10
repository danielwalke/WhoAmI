import { SERVER_PREFIX, SERVER_URL } from "./Server"
export const POST_GET_IMAGES_EP = `${SERVER_URL}/${SERVER_PREFIX}/get_images`
export const GET_GET_ROOMS_EP = `${SERVER_URL}/${SERVER_PREFIX}/rooms`
export const POST_GET_ROOM_EP = `${SERVER_URL}/${SERVER_PREFIX}/room`
export const POST_CREATE_ROOM_EP = `${SERVER_URL}/${SERVER_PREFIX}/create_room`
export const POST_UPLOAD_IMAGES = `${SERVER_URL}/${SERVER_PREFIX}/upload/multiple`
export const DELETE_IMAGE_EP = `${SERVER_URL}/${SERVER_PREFIX}/delete_image`
export const DELETE_ALL_IMAGES_IN_ROOM_EP = `${SERVER_URL}/${SERVER_PREFIX}/delete_all_images_in_room`