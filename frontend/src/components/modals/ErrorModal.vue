<template>
    <div>
        <button @click="store.closeModal()">&times;</button>
        <h2>Error</h2>
        <p>An error has occurred.</p>
    </div>
</template>

<script setup>
import { useModalStore } from '@/stores/ModalStore.js';
const store = useModalStore();


</script>

<style scoped>
</style>