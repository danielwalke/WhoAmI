<template>
    <div
        class="grid grid-cols-6 gap-x-8 gap-y-4"
        >
        <template v-for="card in cards" :key="card.idx">
            <Card
            @click="() => changeState(card.idx)"
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

function changeState(cardIdx){
    console.log(cardIdx);
    
    fieldStore.changeCardState(cardIdx)    
}
</script>

<style scoped>
</style>