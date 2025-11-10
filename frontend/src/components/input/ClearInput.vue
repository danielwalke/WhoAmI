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
import { useRoomStore } from '@/stores/RoomStore.js'
import { useModalStore } from '@/stores/ModalStore.js'
import TrashIcon from '@/components/icons/TrashIcon.vue'
import DeleteAllImages from "../modals/DeleteAllImages.vue"

const fieldStore = useFieldStore()
const roomStore = useRoomStore()
const modalStore = useModalStore()
const hasImages = computed(()=> fieldStore.getCards.length > 0)
const hasConnection = computed(()=> roomStore.getConnection !== undefined)
const hasAnyServerCards = computed(()=>{
    const serverCards = fieldStore.getCards.filter(card => !card.isLocalCard)
    return serverCards.length > 0
})
function removeAll(){
    if (!hasAnyServerCards.value || !hasConnection.value){
        fieldStore.removeAllFiles()    
        return
    }
    modalStore.openModal(DeleteAllImages)
    
}
</script>

<style scoped>
button{
    @apply bg-sky-600
}
</style>