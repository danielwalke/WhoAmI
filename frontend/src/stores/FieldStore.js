import {cards} from '../utils/init/Cards.js'
import { defineStore } from 'pinia'

export const useFieldStore = defineStore('field', {
  state: () => ({ cards: []}),
  getters: {
    getCards: (state) => state.cards,
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
    }
}
})