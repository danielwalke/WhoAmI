<template>
<div v-if="hasImages" class="p-2">
    <button @click="removeAll">
        Remove all
        <TrashIcon/>
    </button>
</div>
</template>

<script setup>
import {computed} from "vue"
import { useFieldStore } from '@/stores/FieldStore.js'
import TrashIcon from '@/components/icons/TrashIcon.vue'

const fieldStore = useFieldStore()
const hasImages = computed(()=> fieldStore.getCards.length > 0)
function removeAll(){
    fieldStore.removeAllFiles()
}
</script>

<style scoped>
button{
    @apply bg-sky-600
}
</style>