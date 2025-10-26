import {cards} from '../utils/init/Cards.js'
import { defineStore } from 'pinia'

export const useFieldStore = defineStore('field', {
  state: () => ({ cards: cards}),
  getters: {
    getCards: (state) => state.cards,
  },
  actions: {
    changeCardState(cardIdx, newState) {
      this.cards[cardIdx].isActive = newState
    },
}
})