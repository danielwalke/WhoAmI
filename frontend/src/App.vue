<template>
  <div class="flex flex-col h-screen w-full">
    <main class="flex-1 overflow-hidden flex justify-center items-center">
      <RouterView />
      <ModalContainer />
    </main>

    <footer class="h-16 w-full  ">
      <div class="flex justify-center gap-3 lg:gap-16 flex-1">
        <RouterLink :to="ROUTE_PREFIX+'/'">Home</RouterLink>
        <RouterLink :to="ROUTE_PREFIX+'/prepare'">Prepare</RouterLink>
        <RouterLink :to="ROUTE_PREFIX+'/game'">Game</RouterLink>
        <RouterLink v-if="hasConnection" :to="ROUTE_PREFIX+'/chat'">Chat</RouterLink>
      </div>
      
      <div class="text-white" >
          <LeaveRoom  v-if="hasConnection"/>
      </div>
    </footer>
  </div>
</template>

<script setup>
import LeaveRoom from '@/components/room/LeaveRoom.vue';
import { useRoomStore } from './stores/RoomStore.js';  
import { computed } from 'vue';
import ModalContainer from './components/modals/ModalContainer.vue';
import { ROUTE_PREFIX } from './router/Routes';

const roomStore = useRoomStore();
const hasConnection = computed(() => roomStore.getConnection !== undefined);
</script>
<style scoped>
footer {
  @apply w-full bg-black/90 p-4 flex justify-between items-center;
}

footer a {
  @apply lg:font-semibold lg:text-lg cursor-pointer hover:scale-110 transition-transform ease-in-out text-white hover:font-bold; 
}
</style>
