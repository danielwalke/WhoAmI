<template>
    <div class="p-2 flex flex-col">
        <button :disabled="!hasImages || !hasConnection || numberOfCardsOverLimit" @click="upload">Upload</button>
        
    </div>
</template>

<script setup>  
import { useFieldStore } from '@/stores/FieldStore.js'
import { computed } from 'vue'  
import { useRoomStore } from '../../stores/RoomStore'

const fieldStore = useFieldStore()
const roomStore = useRoomStore()
const hasImages = computed(()=> fieldStore.getRawFiles.length > 0)
const uploadStatus = computed(() => fieldStore.getUploadStatus);
const numberOfCardsOverLimit = computed(() => fieldStore.getCards.length > 24);
const hasConnection = computed(() => roomStore.getConnection !== undefined);

function upload() {
    fieldStore.uploadFiles();
}
</script>

<style scoped>
/* button{
    @apply 
} */
</style>

