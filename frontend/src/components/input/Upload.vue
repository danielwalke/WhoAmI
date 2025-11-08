<template>
    <div class="p-2">
        <button :disabled="!hasImages || !hasConnection" @click="upload">Upload</button>
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

const hasConnection = computed(() => roomStore.getConnection !== undefined);

function upload() {
    console.log(fieldStore.getRawFiles);
    fieldStore.uploadFiles();
}
</script>

<style scoped>
/* button{
    @apply 
} */
</style>

