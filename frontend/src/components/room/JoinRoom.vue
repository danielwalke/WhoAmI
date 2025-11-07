<template>
    <div>
        <div class="flex flex-col gap-2" v-if="!triggerAnimation">
            <h3>Join room</h3>
            <Autocomplete :items="rooms" :onSubmit="submitRoom" key_field="name"/>
            <input
                    class="border-2 p-2 rounded-md"
                    v-if="roomId"
                    type="text"
                    v-model="clientName"
                    placeholder="Username"
                />
                <input
                    class="border-2 p-2 rounded-md"
                    v-if="roomId"
                    type="password"
                    v-model="roomPassword"
                    placeholder="Room Password"
                />
            <button class="bg-sky-600 p-2 text-white font-semibold rounded-md" type="submit" @click="joinRoom">Join</button>
        </div>
        <div v-if="triggerAnimation">
            <Vue3Lottie :animationData="JoinJSON"  />
        </div>
    </div>    
</template>

<script setup>
import { Vue3Lottie } from 'vue3-lottie'
import { computed, ref } from 'vue';
import Autocomplete from '../utils/Autocomplete.vue';
import { useRoomStore } from '../../stores/roomStore';
import { useRouter } from 'vue-router';
import JoinJSON from "@/assets/lottie_files/Join.json"
import { nextTick } from 'vue'

const roomStore = useRoomStore();

const rooms = computed(() => roomStore.rooms);

const roomPassword = ref("test");
const roomId = ref(undefined);
const clientName = ref("Peter");
const triggerAnimation = ref(false)

function submitRoom(submittedRoom) {
    roomId.value = submittedRoom.id;
}

async function joinRoom(e) {
    e.preventDefault()
    triggerAnimation.value = true
    await nextTick()
    
    roomStore.joinRoom(roomId.value, roomPassword.value, clientName.value);
    setTimeout(()=>{
        triggerAnimation.value = false
        roomStore.setPage(3)
    }, 3000)
}


</script>

<style scoped>
</style>