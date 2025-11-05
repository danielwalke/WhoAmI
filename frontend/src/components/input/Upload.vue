<template>
    <div>
        <div>{{ uploadStatus }}</div>
        <button @click="upload">Upload</button>
    </div>
</template>

<script setup>  
import { useFieldStore } from '@/stores/FieldStore.js'
import { computed } from 'vue'  

const fieldStore = useFieldStore()
const uploadStatus = computed(() => fieldStore.getUploadStatus);
function upload() {
    console.log(fieldStore.getRawFiles);
    fieldStore.uploadFiles();
}
</script>

