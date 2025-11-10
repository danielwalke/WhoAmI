<template>
    <div v-if="!hasRooms" class="p-2 lg:p-4 flex justify-center w-full">
        <div class="warning">Warning: No rooms available.</div>
    </div>    
</template>

<script setup>
import { computed } from 'vue';
import { useRoomStore } from '../../stores/RoomStore';
const roomStore = useRoomStore();
const hasRooms = computed(() => roomStore.getRooms.length !== 0);
</script>

<style scoped>
</style>