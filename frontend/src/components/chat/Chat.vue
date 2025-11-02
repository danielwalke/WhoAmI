<template>
  <div>
    <div class="chat-box">
      <ul>
        <li v-for="(msg, index) in messages" :key="index">{{ msg }}</li>
      </ul>
    </div>
    <form @submit.prevent="sendMessage">
      <input v-model="newMessage" placeholder="Type a message..." />
      <button type="submit">Send</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import { useRoomStore } from '../../stores/roomStore';

const roomStore = useRoomStore();
const messages = computed(() => roomStore.messages);
const newMessage = ref('');
const connection = computed(() => roomStore.connection);

// onMounted(() => {
//   console.log('Connecting to WebSocket...');
  
//   const roomId = 'default_room'; 
//   const clientId = Math.floor(Math.random() * 1000000);
//   const wsUrl = `ws://localhost:8000/whoami/ws/${roomId}/${clientId}`;
//   connection.value = new WebSocket(wsUrl);

//   connection.value.onopen = (event) => {
//     console.log(`Successfully connected ${clientId} to WebSocket server`);
//   };

//   connection.value.onmessage = (event) => {
//     messages.value.push(event.data);
//   };

//   connection.value.onclose = (event) => {
//     console.log('WebSocket connection closed');
//   };

//   connection.value.onerror = (error) => {
//     console.error('WebSocket Error:', error);
//   };
// });

// onUnmounted(() => {
//   if (connection.value) {
//     connection.value.close();
//   }
// });

const sendMessage = () => {
  if (newMessage.value.trim() && connection.value) {
    connection.value.send(newMessage.value);
    newMessage.value = '';
  }
};
</script>

<style scoped>
</style>