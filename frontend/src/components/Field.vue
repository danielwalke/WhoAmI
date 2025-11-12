<template>
  <div class="w-full h-full flex flex-col  overflow-y-auto">

    <div class="flex-1 w-full">
      <div class="header">
        <div class="w-full lg:w-1/2 flex gap-2 justify-center items-center">
          <Card :card="chosenCard" v-if="chosenCard" :smallCard="true" />
          <div class="flex flex-col gap-2 w-3/5 justify-center items-center">
            <Autocomplete :items="cards" :onSubmit="submitCard" key_field="title" placeholder="Search card" />
            <div class="lg:p-2 flex gap-2 justify-center items-center" v-if="!isDesktop">
              <Toggle v-model="showOnlyActiveCards" />
              <span class="text-sm">{{ showOnlyActiveCards ? ' Showing only active cards' : ' Showing all cards'
                }}</span>
            </div>
            <button @click="undo" class=" text-white font-bold p-4 rounded inline-flex items-center" v-if="historyStack.length > 0">
              <ReverseIcon />
            </button>
          </div>
        </div>


      </div>
      <span v-if="cards.length === 0" class="bg-red-500 text-sm text-white rounded-md p-2 m-2 animate-pulse">Set a card
        deck under "Prepare"</span>
      <div class="grid grid-cols-2 lg:grid-cols-6 gap-x-4 gap-y-2 p-2  w-full h-[85%]" :class="isExpanded ? '' : ''">
        <template v-for="card in cards" :key="card.id">
          <Card :small-card="false" @click="() => changeState(card.id)" class="w-full" :card="card" />
        </template>
      </div>
    </div>

    <div v-if="isDesktop && hasConnection"
      class="flex flex-col w-full overflow-hidden transition-all ease-in-out duration-300 bg-black/90 pb-4"
      :class="isExpanded ? 'absolute bottom-0 left-0 right-0 h-4/5' : 'h-[250px]'">
      <div @click="expand" class="flex justify-center pt-2 h-12 w-full items-center cursor-pointer bg-black/90">
        <svg v-if="!isExpanded" class="hover:scale-110 hover:cursor-pointer animate-bounce" width="96" height="24"
          viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 0L20 8H4L12 0Z" fill="rgba(255, 255, 255, 1)" />
          <path d="M12 6L20 14H4L12 6Z" fill="rgba(255, 255, 255, 1)" />
          <path d="M12 12L20 20H4L12 12Z" fill="rgba(255, 255, 255, 1)" />
        </svg>
        <svg class="hover:scale-110 hover:cursor-pointer animate-bounce" v-if="isExpanded" width="96" height="24"
          viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 12L20 4H4L12 12Z" fill="rgba(255, 255, 255, 1)" />
          <path d="M12 18L20 10H4L12 18Z" fill="rgba(255, 255, 255, 1)" />
          <path d="M12 24L20 16H4L12 24Z" fill="rgba(255, 255, 255, 1)" />
        </svg>
      </div>
      <Chat class="flex-1" />
    </div>
  </div>
</template>

<script setup>
import Card from './Card.vue'
import { useFieldStore } from '../stores/FieldStore.js'
import { useRoomStore } from '../stores/RoomStore.js'
import { computed, ref, onMounted, onUnmounted } from 'vue'
import Chat from './chat/Chat.vue'
import Autocomplete from './utils/Autocomplete.vue'
import Toggle from './utils/Toggle.vue'
import ReverseIcon from './icons/ReverseIcon.vue'

const fieldStore = useFieldStore()
const roomStore = useRoomStore()

const isDesktop = ref(false)
const hasConnection = computed(() => roomStore.getConnection !== undefined)
const isExpanded = ref(false)
const chosenCard = ref(undefined)
const showOnlyActiveCards = ref(false)
const historyStack = ref([])

const cards = computed(() => {
  if (showOnlyActiveCards.value) {
    return fieldStore.getCards.filter(card => card.isActive)
  }
  return fieldStore.getCards
})

console.log(cards.value);

function changeState(cardId) {
  console.log(cardId);
  historyStack.value.push(cardId)
  fieldStore.changeCardState(cardId)
}

function undo() {
  const lastCardId = historyStack.value.pop()
  if (lastCardId !== undefined) {
    fieldStore.changeCardState(lastCardId)
  }
}

function expand() {
  isExpanded.value = !isExpanded.value
}

const checkScreenSize = () => {
  isDesktop.value = window.innerWidth >= 1024
}

function submitCard(card) {
  chosenCard.value = card
}

onMounted(() => {
  checkScreenSize()
  window.addEventListener('resize', checkScreenSize)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkScreenSize)
})
</script>

<style scoped>
.header {
  @apply flex justify-center items-center sticky top-0 bg-white z-10 p-2 gap-1 lg:gap-4 lg:h-[15%]
}
</style>