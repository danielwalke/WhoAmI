<template>
    <div
        class="grid grid-cols-6 gap-x-8 gap-y-4 p-4"
        >
        <template v-for="card in cards" :key="card.id">
            <Card
            @click="() => changeState(card.id)"
            class="w-full"
            :card="card"
            />
        </template>
    </div>
</template>

<script setup>
import Card from './Card.vue'
import { useFieldStore } from '../stores/FieldStore.js'
import { computed } from 'vue'


const fieldStore = useFieldStore()
const cards = computed(() => fieldStore.getCards)
console.log(cards.value);

function changeState(cardId){
    console.log(cardId);
    
    fieldStore.changeCardState(cardId)    
}
</script>

<style scoped>
</style>