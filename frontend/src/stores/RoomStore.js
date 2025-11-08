import { defineStore } from 'pinia'
import { SERVER_PREFIX } from '../constants/Server'
import { SERVER_URL, WEBSOCKET_URL } from '../constants/Server'
import axios from 'axios'
import { useFieldStore } from './FieldStore'
import { GET_GET_ROOMS_EP, POST_CREATE_ROOM_EP, POST_GET_ROOM_EP } from '../constants/Endpoints'

export const useRoomStore = defineStore('room', {
  state: () => ({ rooms: [], connection: undefined, messages: [], joinedRoom: undefined, clientId: 0, roomId: undefined, roomPassword: undefined, page: 1 }),
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
    getPage: (state) => state.page
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
      console.log('Creating room with data:', data)
      axios.post(POST_CREATE_ROOM_EP, data).then(response => {
        console.log('Room created:', response.data)
        this.fetchRooms();
      }).catch(error => {
        console.error('Error creating room:', error)
      })    
    },
    joinRoom(roomId, roomPassword, clientName){
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
            console.log(roomId, roomPassword)
            
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
      }).catch(error => {
        console.error('Error joining room:', error)
          alert('Error joining room: ' + error.response.data["detail"]);
      })      
    },
    leaveRoom(){
      if (this.connection) {
        this.joinedRoom = undefined;
        this.connection.close();
        this.connection = undefined;
        this.messages = []
        this.roomId = undefined
        this.roomPassword = undefined
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
    }
}
})