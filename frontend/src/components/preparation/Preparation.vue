<template>
    <div class="flex justify-center h-full">
        <div class="w-full lg:w-2/3 bg-black/70 rounded-md lg:p-4 p-2 h-full overflow-y-auto">
        <h2>Preparation</h2>
        <div class="w-full">
            <div class="flex justify-center items-center flex-col w-full pb-2 lg:pb-4">
                <h3>Create a room</h3>
                <CreateRoom />
            </div>
            <div class="flex flex-col justify-center items-center pb-2 lg:pb-4">
                <h3>Join a room</h3>
                <div v-if="hasRooms && !hasConnection">
                    <JoinRoom />
                </div>
            </div>
            
            <div class="flex flex-col justify-center items-center">
                <h3>Create your own cards</h3>
                <Input/>
            </div>
                
            <div class="flex justify-center items-center flex-col">
                <h3>Upload your own cards in your room</h3>
                <Upload/>
            </div>
        </div>
        
    </div>
    </div>
    
</template>

<script setup>
import CreateRoom from "@/components/room/CreateRoom.vue"
import JoinRoom from '@/components/room/JoinRoom.vue';
import Input from '@/components/input/Input.vue';
import { useRoomStore } from '../../stores/roomStore';  
import { computed, onMounted } from 'vue';
import Upload from '@/components/input/Upload.vue'
const roomStore = useRoomStore();
const hasRooms = computed(() => roomStore.getRooms && roomStore.getRooms.length > 0);
const hasConnection = computed(() => roomStore.getConnection !== undefined);

onMounted(() => {
    console.log("Fetching rooms on Room component mount");
    roomStore.fetchRooms();
});
</script>

<style scoped>
h2{
    @apply text-2xl font-bold flex justify-center items-center lg:p-4 p-2 text-white
}

h3{
    @apply font-semibold text-xl text-white
}
</style>