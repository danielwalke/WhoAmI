import { defineStore } from 'pinia'
import { SERVER_PREFIX } from '../constants/Server'
import { SERVER_URL, WEBSOCKET_URL } from '../constants/Server'
import axios from 'axios'

export const useRoomStore = defineStore('room', {
  state: () => ({ rooms: [], connection: undefined, messages: [], joinedRoom: undefined, clientId: 0 }),
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
    getClientId: (state) => state.clientId
  },
  actions: {
    addRoom(roomName, roomPassword) {
      const data = {
        room_name: roomName,
        room_password: roomPassword
      }
      console.log('Creating room with data:', data)
      axios.post(`${SERVER_URL}/${SERVER_PREFIX}/create_room`, data).then(response => {
        console.log('Room created:', response.data)
        this.fetchRooms();
      }).catch(error => {
        console.error('Error creating room:', error)
      })    
    },
    joinRoom(roomName, roomPassword){
      //TODO password verification
      this.clientId = Math.floor(Math.random() * 1000000);
      const wsUrl = `${WEBSOCKET_URL}/${roomName}/${this.clientId}`;
      this.connection = new WebSocket(wsUrl);
      this.joinedRoom = roomName;

      this.connection.onopen = (event) => {
        console.log(`Successfully connected ${this.clientId} to WebSocket server`);
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
    },
    leaveRoom(){
      if (this.connection) {
        this.joinedRoom = undefined;
        this.connection.close();
        this.connection = undefined;
      }
    },
    fetchRooms() {
      axios.get(`${SERVER_URL}/${SERVER_PREFIX}/rooms`).then(response => {
        const fetched_rooms = response.data;
        console.log(fetched_rooms)
        if (fetched_rooms === undefined) return;
        this.rooms = fetched_rooms;

      }).catch(error => {
        console.error('Error fetching rooms:', error);
      })
    }
}
})