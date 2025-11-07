<template>
    <div class="">
        <div v-if="!triggerAnimation" class="flex justify-center flex-col items-center gap-4 p-4">
            <h3>Create a room</h3>
            <input class="border-2 p-2 rounded-md" v-model="roomName" type="text" placeholder="Enter room name" />
            <input class="border-2 p-2 rounded-md" v-model="roomPassword" type="password" placeholder="Enter room password" />
            <button class="bg-sky-600 text-white p-4 rounded-md hover:scale-105" type="submit" @click="createRoom">Create Room</button>
        </div>
        <div>
            <Vue3Lottie :animationData="HomeJSON"  v-if="triggerAnimation" />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoomStore } from '../../stores/RoomStore'
import HomeJSON from "@/assets/lottie_files/Home.json"

const roomName = ref('test')
const roomPassword = ref('test')

const roomStore = useRoomStore()    
const triggerAnimation = ref(false)

function createRoom() {
    console.log(`Creating room: ${roomName.value} with password: ${roomPassword.value}`)
    triggerAnimation.value = true
    setTimeout(()=>{
        triggerAnimation.value = false
        roomStore.setPage(2)
    }, 3000)
    roomStore.addRoom(roomName.value, roomPassword.value)
    
}

</script>