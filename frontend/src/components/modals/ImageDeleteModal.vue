<template>
    <div class="flex flex-col">
        <h2 class="text-black">Delete Image</h2>
        <p class="p-2 lg:p-4">Do you also want to delete the image on the server?</p>
        <div class="modal-actions p-2">
            <button @click="store.closeModal">Cancel</button>
            <button class="danger" @click="confirmDelete">Delete</button>
        </div>
    </div>
</template>

<script setup>
import { useModalStore } from '@/stores/ModalStore.js';
import { useRoomStore } from '@/stores/RoomStore.js';
const store = useModalStore();
const roomStore = useRoomStore();

const props = defineProps({
    callbackFun: {
        type: Function,
        required: true
    }
});

function confirmDelete() {
    
    props.callbackFun();
    roomStore.deleteSelectedImage();
    store.closeModal();
}
</script>

<style scoped>
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.danger {
  background-color: red;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
}
</style>