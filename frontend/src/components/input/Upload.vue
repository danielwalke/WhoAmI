<template>
    <div v-if="hasImages" class="p-2">
        <button @click="upload">Upload</button>
    </div>
</template>

<script setup>  
import { useFieldStore } from '@/stores/FieldStore.js'
import { computed } from 'vue'  

const fieldStore = useFieldStore()
const hasImages = computed(()=> fieldStore.getCards.length > 0)
const uploadStatus = computed(() => fieldStore.getUploadStatus);

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

