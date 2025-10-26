<template>
    <div
        class="grid grid-cols-6 gap-8"
        >
        <template v-for="card in cards" :key="card.idx">
            <Card
            class="w-full"
            :title="card.title"
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

</script>

<style scoped>
</style>