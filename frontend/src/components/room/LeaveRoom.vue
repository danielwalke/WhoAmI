<template>
    <div class="flex flex-col gap-2 justify-center items-center">
        <button class="bg-sky-600 p-2 rounded-md text-white text-lg font-semibold" @click="leaveRoom">Leave Room</button>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoomStore } from '../../stores/roomStore';

const roomStore = useRoomStore()

const joinedRoom = computed(() => roomStore.getJoinedRoom);
function leaveRoom() {
    roomStore.leaveRoom()
}
</script>