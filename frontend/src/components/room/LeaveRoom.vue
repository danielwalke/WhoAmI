<template>
    <div class="flex flex-col gap-2 justify-center items-center">
        <div class="rounded-md shadow-md text-lg p-4 flex w-64">Currently you are in room:</div>
        <div class="rounded-md shadow-md text-xl font-semibold p-4 mb-4 w-64 text-center italic">{{ joinedRoom }}</div>
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