import {cards} from '../utils/init/Cards.js'
import { defineStore } from 'pinia'
import axios from 'axios'
import { SERVER_URL, SERVER_PREFIX } from '../constants/Server.js'


export const useFieldStore = defineStore('field', {
  state: () => ({ cards: cards, rawFiles: [], uploadStatus: '' }),
  getters: {
    getCards: (state) => state.cards,
    getRawFiles: (state) => state.rawFiles,
    getUploadStatus: (state) => state.uploadStatus
  },
  actions: {
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
    uploadFiles() {
        console.log('Uploading files:', this.rawFiles);
        console.log(`${SERVER_URL}/${SERVER_PREFIX}/upload/single`)
        const formData = new FormData();
        for(const file of this.rawFiles) {
            formData.append("files", file);
        }
        axios.post(`${SERVER_URL}/${SERVER_PREFIX}/upload/multiple`, formData, {          
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            this.uploadStatus = `Uploading: ${percentCompleted}%`;
          }
        })
        .then(response => {
            console.log('Files uploaded successfully:', response.data);
            this.uploadStatus = `Upload successful! File: ${response.data.filename}`;
        })
        .catch(error => {
            console.error('Error uploading files:', error);
            this.uploadStatus = `Error: ${error.response.data.detail || 'Upload failed'}`;
        });
    },
    removeAllFiles(){
      this.rawFiles = []
      this.cards = []
    }
}
})