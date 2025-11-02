<template>
    <div>
        <div class="p-2 gap-2 flex flex-col justify-center items-center w-full">

            <CreateRoom />
            <div v-if="hasRooms && !hasConnection">
                <JoinRoom />
            </div>
            <div v-if="hasConnection">
                <LeaveRoom />
            </div>
        </div>
    </div>
</template>

<script setup>
import CreateRoom from './CreateRoom.vue';
import JoinRoom from './JoinRoom.vue';
import { useRoomStore } from '../../stores/roomStore';  
import LeaveRoom from './LeaveRoom.vue';
import { computed, onMounted } from 'vue';

const roomStore = useRoomStore();
const hasRooms = computed(() => roomStore.getRooms && roomStore.getRooms.length > 0);
const hasConnection = computed(() => roomStore.connection !== undefined);

onMounted(() => {
    console.log("Fetching rooms on Room component mount");
    roomStore.fetchRooms();
});
</script>

<style scoped>
</style>