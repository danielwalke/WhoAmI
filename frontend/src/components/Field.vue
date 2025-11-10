<template>
    <div class="w-full h-full flex flex-col  overflow-y-auto">
        <div
        class="grid grid-cols-2 lg:grid-cols-6 gap-x-8 gap-y-4 p-4  w-full flex-1"
        >
            <template v-for="card in cards" :key="card.id">
                <Card
                @click="() => changeState(card.id)"
                class="w-full"
                :card="card"
                />
            </template>
        </div>
        <div v-if="isDesktop && hasConnection" class="w-full h-60 overflow-y-auto">
            <Chat/>
        </div>
    </div>
</template>

<script setup>
import Card from './Card.vue'
import { useFieldStore } from '../stores/FieldStore.js'
import { useRoomStore } from '../stores/RoomStore.js'
import { computed, ref, onMounted, onUnmounted } from 'vue'
import Chat from './chat/Chat.vue'

const fieldStore = useFieldStore()
const roomStore = useRoomStore()
const cards = computed(() => fieldStore.getCards)
const isDesktop = ref(false)
const hasConnection = computed(() => roomStore.getConnection !== undefined)
console.log(cards.value);

function changeState(cardId){
    console.log(cardId);
    
    fieldStore.changeCardState(cardId)    
}



const checkScreenSize = () => {
  isDesktop.value = window.innerWidth >= 1024
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
</style>