import {cards} from '../utils/init/Cards.js'
import { defineStore } from 'pinia'
import axios from 'axios'
import { SERVER_URL, SERVER_PREFIX } from '../constants/Server.js'
import { useRoomStore } from './RoomStore.js'
import {POST_GET_IMAGES_EP, POST_UPLOAD_IMAGES} from "../constants/Endpoints.js"


export const useFieldStore = defineStore('field', {
  state: () => ({ cards: cards, rawFiles: [], uploadStatus: '', triggerUploadAnimation: false }),
  getters: {
    getCards: (state) => state.cards,
    getRawFiles: (state) => state.rawFiles,
    getUploadStatus: (state) => state.uploadStatus,
    getTriggerUploadAnimation: (state) => state.triggerUploadAnimation
  },
  actions: {
    toggleTriggerUploadAnimation(){
      this.triggerUploadAnimation = !this.triggerUploadAnimation
    },
    changeCardState(cardId) {
      const card = this.cards.find(c => c.id === cardId);
      if (card) {
        card.isActive = !card.isActive;
      }

    },
    addCard(card) {
      this.cards.push(card)
    },
    deleteCard(cardId) {
      this.cards = this.cards.filter(c => c.id !== cardId);
    },
    setRawFiles(files) {
      this.rawFiles = files;
    },
    fetchRoomImages(room_id, room_password){
      const data = {
        id: room_id,
        password: room_password
      }  
      axios.post(POST_GET_IMAGES_EP, data).then(
          response => {
            console.log(response.data)
            if(response.data && response.data.length == 0) return
            this.cards = response.data.map(image => {
              return {
                    id: image.id,
                    title: image.name,
                    url: image.url,
                    isActive: true,
                  }
            })
          }).catch(error => console.error(error))
    },
    uploadFiles() {
        this.toggleTriggerUploadAnimation()
        console.log('Uploading files:', this.rawFiles);
        const formData = new FormData();
        const roomStore = useRoomStore()
        const roomId = roomStore.getRoomId
        const roomPassword = roomStore.getRoomPassword
        formData.append("room_id", roomId);
        formData.append("room_password", roomPassword);
        for(const file of this.rawFiles) {
            formData.append("files", file);
        }
        axios.post(POST_UPLOAD_IMAGES, formData, {             
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            this.uploadStatus = `Uploading: ${percentCompleted}%`;
          }
        })
        .then(response => {
            console.log('Files uploaded successfully:', response.data);
            setTimeout(()=>{
              this.toggleTriggerUploadAnimation()
            }, 1000)
            
            this.fetchRoomImages(roomId, roomPassword)
        })
        .catch(error => {
            console.error('Error uploading files:', error);
            this.uploadStatus = `Error: ${error.response.data.detail || 'Upload failed'}`;
        });
    },
    removeAllCards(){
      this.cards = []
    },
    removeAllFiles(){
      this.rawFiles = []
      this.cards = []
    },
    resetDefaultCards(){
      this.cards = cards
    },
    pickRoomCards(){
      const roomStore = useRoomStore()
      const roomId = roomStore.getRoomId
      const roomPassword = roomStore.getRoomPassword
      this.fetchRoomImages(roomId, roomPassword)
    }
}
})