<template>
    <div class="flex justify-center h-full">
        <div class="w-full lg:w-2/3 bg-black/70 rounded-md lg:p-4 p-2 h-full overflow-y-auto">
            <h2>Preparation</h2>
            <div class="w-full  ">
                <div class="flex justify-center items-center flex-col w-full pb-2 lg:pb-4" v-if="page==1">
                    <CreateRoom />
                </div>
                <div class="flex flex-col justify-center items-center pb-2 lg:pb-4" v-if="page==2">
                    <JoinRoom />
                </div>
                
                <div class="flex flex-col justify-center items-center" v-if="page==3">
                    <h3>Create your own cards</h3>
                    <Input/>
                </div>
                    
                <div class="flex justify-center items-center flex-col" v-if="page==4">
                    <h3>Upload your own cards in your room</h3>
                    <Upload/>
                </div>
                
                <div class="flex text-white justify-center  gap-6 items-center h-12 text-xl">
                    <div v-for="page_idx in 4" :key="page_idx" @click="()=> page = page_idx" class="cursor-pointer" >
                        <div :class="page === page_idx ? 'h-5 w-5' : 'h-3 w-3 hover:h-5 hover:w-5'" class=" bg-white rounded-full transition-all ease-in-out"></div>
                    </div>
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
import { computed, onMounted, ref  } from 'vue';
import Upload from '@/components/input/Upload.vue'



const roomStore = useRoomStore();
const hasRooms = computed(() => roomStore.getRooms && roomStore.getRooms.length > 0);
const hasConnection = computed(() => roomStore.getConnection !== undefined);
const page = computed({
  get() {
    return roomStore.getPage;
  },  
  set(newValue) {
    roomStore.setPage(newValue)
  }
})
onMounted(() => {
    console.log("Fetching rooms on Room component mount");
    roomStore.fetchRooms();
});
</script>

<style scoped>

</style>