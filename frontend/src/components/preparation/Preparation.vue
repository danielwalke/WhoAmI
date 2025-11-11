<template>
    <div class="flex flex-col h-full bg-black/70 lg:p-4 lg:w-2/3 w-full rounded-md p-2">
        <div class="w-full flex-1 overflow-y-auto">
            <div class="h-full w-full">
                <h2>Preparation</h2>
                <div class="flex justify-center items-center flex-col w-full pb-2 lg:pb-4" v-if="page==1">
                    <CreateRoom />
                </div>
                <div class="flex flex-col justify-center items-center pb-2 lg:pb-4" v-if="page==2">
                    <WarningMissingRooms/>
                    <JoinRoom />
                </div>
                
                <div class="flex flex-col justify-center items-center" v-if="page==3">
                    <h3>Create your own cards</h3>
                    <WarningMissingConnection/>
                    <CardSelection/>
                    <Input/>
                    <div class="flex justify-center items-center" v-if="!triggerUploadAnimation">
                        <ClearInput/>
                        <Upload/>
                    </div>
                    <div class="h-full" v-if="triggerUploadAnimation">
                        <Vue3Lottie :animationData="UploadJSON"  />
                    </div>
                </div>
            </div>
            
        </div>
        <div class="h-12 lg:h-16">
            <div class="flex text-white justify-center  gap-6 items-center h-12 text-xl">
                <div v-for="page_idx in 3" :key="page_idx" @click="()=> page = page_idx" class="cursor-pointer" >
                    <div :class="page === page_idx ? 'h-5 w-5' : 'h-3 w-3 hover:h-5 hover:w-5'" class=" bg-white rounded-full transition-all ease-in-out"></div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script setup>
import { Vue3Lottie } from 'vue3-lottie'
import CreateRoom from "@/components/room/CreateRoom.vue"
import JoinRoom from '@/components/room/JoinRoom.vue';
import Input from '@/components/input/Input.vue';
import { useRoomStore } from '../../stores/roomStore';  
import { computed, onMounted, ref  } from 'vue';
import Upload from '@/components/input/Upload.vue'
import { useFieldStore } from "../../stores/FieldStore";
import UploadJSON from "@/assets/lottie_files/Upload.json"
import DefaultCards from '@/components/input/DefaultCards.vue';
import CardSelection from '../input/CardSelection.vue';
import WarningMissingConnection from '../room/WarningMissingConnection.vue';
import WarningMissingRooms from '../room/WarningMissingRooms.vue';
import ClearInput from '../input/ClearInput.vue';

const roomStore = useRoomStore();
const fieldStore = useFieldStore()
const hasRooms = computed(() => roomStore.getRooms && roomStore.getRooms.length > 0);
const hasConnection = computed(() => roomStore.getConnection !== undefined);
const triggerUploadAnimation = computed(()=> fieldStore.getTriggerUploadAnimation)

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