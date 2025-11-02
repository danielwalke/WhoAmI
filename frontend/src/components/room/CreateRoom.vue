<template>
    <div class="flex justify-center flex-col items-center gap-4 p-4 border rounded-lg shadow-sm">
        <div class="text-lg font-semibold">
            Room Creation
        </div>
        <input class="border-2 p-2 rounded-md" v-model="roomName" type="text" placeholder="Enter room name" />
        <input class="border-2 p-2 rounded-md" v-model="roomPassword" type="password" placeholder="Enter room password" />
        <button class="bg-sky-600 text-white p-4 rounded-md hover:scale-105" type="submit" @click="createRoom">Create Room</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoomStore } from '../../stores/RoomStore'

const roomName = ref('test')
const roomPassword = ref('test')

const roomStore = useRoomStore()    

function createRoom() {
    console.log(`Creating room: ${roomName.value} with password: ${roomPassword.value}`)
    roomStore.addRoom(roomName.value, roomPassword.value)
}

</script>