<template>
    <div class="flex flex-col">
        <h2 class="text-black">Delete all images</h2>
        <p class="p-2 lg:p-4">Do you also want to delete all images from the server?</p>
        <div class="modal-actions p-2">
            <button @click="store.closeModal">Cancel</button>
            <button class="danger" @click="confirmDelete">Delete</button>
        </div>
    </div>
</template>
<script setup>

import { useModalStore } from '@/stores/modalStore';
import { useRoomStore } from '@/stores/RoomStore.js';

const store = useModalStore();
const roomStore = useRoomStore();
const confirmDelete = async () => {
    await roomStore.deleteAllImagesInRoom();
    store.closeModal();
};
</script>