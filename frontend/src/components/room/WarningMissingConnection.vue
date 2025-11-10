<template>
    <div class="p-2 select-none lg:pt-4 w-full flex justify-center" v-if="!hasConnection">
        <div  class="warning">Warning: You are not connected to a room. </div>
    </div>
</template>
<script setup>
import { computed } from 'vue';
import { useRoomStore } from '../../stores/RoomStore';

const roomStore = useRoomStore();
const hasConnection = computed(() => roomStore.getConnection !== undefined);
</script>