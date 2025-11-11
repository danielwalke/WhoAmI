<template>
    <div class="flex flex-col gap-2 justify-center items-center">
        <button class="bg-sky-600 p-2 rounded-md text-white text-lg font-semibold" @click="leaveRoom">Leave Room</button>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoomStore } from '../../stores/RoomStore.js';

import { useRouter } from 'vue-router';

const roomStore = useRoomStore()

const joinedRoom = computed(() => roomStore.getJoinedRoom);
const router = useRouter()
function leaveRoom() {
    roomStore.leaveRoom(router)
}
</script>