<template>
    <div class="">
        <div v-if="!triggerAnimation" class="flex justify-center flex-col items-center gap-4 p-4">
            <h3>Create a room</h3>
            <Roomname v-model:roomName="roomName" />
            <Password v-model:roomPassword="roomPassword" />
            <button :disabled="roomPassword.length < 6 || roomName.length < 3" class="bg-sky-600 text-white p-4 rounded-md hover:scale-105" type="submit" @click="createRoom">Create Room</button>
            <span v-if="createRoomError" class="text-red-500 text-sm">{{ createRoomError }}</span>
        </div>
        <div>
            <Vue3Lottie :animationData="HomeJSON"  v-if="triggerAnimation" />
        </div>
    </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoomStore } from '../../stores/RoomStore.js'
import HomeJSON from "@/assets/lottie_files/Home.json"
import Password from '../utils/Password.vue'
import Roomname from '../utils/Roomname.vue'

const roomName = ref('')
const roomPassword = ref('')

const roomStore = useRoomStore()    
const triggerAnimation = computed(() => roomStore.getTriggerAnimation)
const createRoomError = computed(() => roomStore.getCreateRoomError)

function createRoom() {
    console.log(`Creating room: ${roomName.value} with password: ${roomPassword.value}`)
    roomStore.addRoom(roomName.value, roomPassword.value)    
}

</script>