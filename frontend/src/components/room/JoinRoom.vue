<template>
    <div class="join-room">
        <form class="flex flex-col p-2 gap-2">
            <label for="room">Room Name:</label>
            <Autocomplete :items="roomNames" :onSubmit="submitRoom"/>
            <input
                class="border-2 p-2 rounded-md"
                v-if="roomName"
                type="password"
                v-model="roomPassword"
                placeholder="Room Password"
            />
            <button class="bg-sky-600 p-4 text-white font-semibold rounded-md" type="submit" @click="joinRoom">Join</button>
        </form>
    </div>
</template>

<script setup>
import { computed, ref } from 'vue';
import Autocomplete from '../utils/Autocomplete.vue';
import { useRoomStore } from '../../stores/roomStore';

const roomStore = useRoomStore();

const roomNames = computed(() => roomStore.rooms);

const roomPassword = ref("test");
const roomName = ref(undefined);

function submitRoom(submittedRoomName) {
    console.log("Submitting room:", submittedRoomName);
    roomName.value = submittedRoomName;
}

function joinRoom(event) {
    event.preventDefault();
    if (!roomName.value) {
        alert("Please select a room.");
        return;
    }
    roomStore.joinRoom(roomName.value, roomPassword.value);
}


</script>

<style scoped>
.join-room {
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem;
    border: 1px solid #ddd;
    border-radius: 8px;
}
h2 {
    margin-bottom: 1rem;
}
form {
    display: flex;
    flex-direction: column;
}
label {
    margin-bottom: 0.5rem;
}
input {
    margin-bottom: 1rem;
    padding: 0.5rem;
    font-size: 1rem;
}
button {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
}
</style>