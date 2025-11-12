import { defineStore } from 'pinia'
import { SERVER_PREFIX } from '../constants/Server'
import { SERVER_URL, WEBSOCKET_URL } from '../constants/Server'
import axios from 'axios'
import { useFieldStore } from './FieldStore'
import { GET_GET_ROOMS_EP, POST_CREATE_ROOM_EP, POST_GET_ROOM_EP, DELETE_IMAGE_EP, DELETE_ALL_IMAGES_IN_ROOM_EP } from '../constants/Endpoints'
import { ROUTE_PREFIX } from '../router/Routes.js'

export const useRoomStore = defineStore('room', {
  state: () => ({ rooms: [], 
                connection: undefined, 
                messages: [],
                 joinedRoom: undefined,
                 clientId: 0, 
                 roomId: undefined, 
                 roomPassword: undefined, 
                 page: 1, 
                 selectedImageId: undefined,
                createRoomError: undefined,
                joinRoomError: undefined,
                triggerAnimation: false
              }),
  getters: {
    getRooms: (state) => state.rooms,
    getConnection: (state) => state.connection,
    getJoinedRoom: (state) => state.joinedRoom,
    getClientCount: (state) => {
      const clientIds = new Set();
      state.messages.forEach(msg => {
        if (msg.clientId !== undefined) {
          clientIds.add(msg.clientId);
        } });
      return clientIds.size;
    },
    getClientId: (state) => state.clientId,
    getRoomId: (state) => state.roomId,
    getRoomPassword: (state) => state.roomPassword,
    getPage: (state) => state.page,
    getSelectedImageId: (state) => state.selectedImageId,
    getCreateRoomError: (state) => state.createRoomError,
    getTriggerAnimation: (state) => state.triggerAnimation,
    getJoinRoomError: (state) => state.joinRoomError
  },
  actions: {
    setPage(newPage){
        this.page = newPage
    },
    addRoom(roomName, roomPassword) {
      const data = {
        id: crypto.randomUUID(),
        name: roomName,
        password: roomPassword
      }
      this.triggerAnimation = true
      console.log('Creating room with data:', data)
      axios.post(POST_CREATE_ROOM_EP, data).then(response => {
        console.log('Room created:', response.data)
        this.fetchRooms();
        
        this.createRoomError = undefined;
      }).catch(error => {
        console.error('Error creating room:', error)
        this.createRoomError = error.response.data["detail"];
      }).finally(() => {  
        setTimeout(() => {
          this.triggerAnimation = false
          this.setPage(2)
        }, 2000)
        
      })
    },
    joinRoom(roomId, roomPassword, clientName){
      this.triggerAnimation = true
      const fieldStore = useFieldStore()
      this.clientId = crypto.randomUUID();
      this.roomId = roomId
      this.roomPassword = roomPassword
      const wsUrl = `${WEBSOCKET_URL}/${roomId}/${roomPassword}/${this.clientId}/${clientName}`;
      this.connection = new WebSocket(wsUrl);
      axios.post(POST_GET_ROOM_EP, {
            "id": roomId,
            "password": roomPassword
      }).then(resp =>{
          this.joinedRoom = resp.data;
          console.log("fetch")
          fieldStore.fetchRoomImages(roomId, roomPassword)
          this.connection.onopen = (event) => {
            console.log(`Successfully connected ${this.clientId} to WebSocket server`);
            this.joinRoomError = undefined
            
          };

          this.connection.onmessage = (event) => {
            const data = JSON.parse(event.data);
            console.log('Message received from server:', data);
            this.messages.push(data);
          };

          this.connection.onclose = (event) => {
            console.log('WebSocket connection closed');
          };

          this.connection.onerror = (error) => {
            console.error('WebSocket Error:', error);
          };
          setTimeout(() => {
          this.triggerAnimation = false
          this.setPage(3)
        }, 2000)
      }).catch(error => {
        console.error('Error joining room:', error)
        this.joinRoomError = error.response.data["detail"];
        this.connection = undefined;
        this.roomId = undefined
        this.roomPassword = undefined
      }).finally(() => {
        
      })    
    },
    leaveRoom(router){
      if (this.connection) {
        this.joinedRoom = undefined;
        this.connection.close();
        this.connection = undefined;
        this.messages = []
        this.roomId = undefined
        this.roomPassword = undefined
        this.joinRoomError = undefined
        this.createRoomError = undefined
        this.setPage(2)
        router.push(ROUTE_PREFIX+'/prepare')
      }
    },
    fetchRooms() {
      axios.get(GET_GET_ROOMS_EP).then(response => {
        const fetched_rooms = response.data;
        console.log(fetched_rooms)
        if (fetched_rooms === undefined) return;
        this.rooms = fetched_rooms

      }).catch(error => {
        console.error('Error fetching rooms:', error);
      })
    },
    setSelectedImageId(imageId){
      this.selectedImageId = imageId
    },
    deleteSelectedImage(){
      axios.delete(DELETE_IMAGE_EP, {
        data: {
          image: { id: this.selectedImageId },
          room: { id: this.roomId, password: this.roomPassword }
        }
      }).then(response => { 
        console.log('Image deleted:', response.data)
        const fieldStore = useFieldStore()
        fieldStore.fetchRoomImages(this.roomId, this.roomPassword)
      }).catch(error => {
        console.error('Error deleting image:', error)
      })
      this.selectedImageId = undefined
    },
    async deleteAllImagesInRoom(){
      const fieldStore = useFieldStore()
      try {
        const room = {
            id: this.roomId,
            password: this.roomPassword
        }
        console.log('Deleting all images in room:', room)
        await axios.delete(DELETE_ALL_IMAGES_IN_ROOM_EP, {
            data: room
        });
        fieldStore.fetchRoomImages(this.roomId, this.roomPassword);
      } catch (error) {
          console.error('Error deleting all images:', error);
      }
    }
}
})