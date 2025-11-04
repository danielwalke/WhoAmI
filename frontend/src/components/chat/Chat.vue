<template>
  <div class="flex flex-col h-full bg-black/90 lg:p-4">
    <div class="flex-1 overflow-y-auto">
        <div class="flex flex-col gap-2 p-4">
        <div v-for="(msg_obj, index) in message_obj" :key="index" class="shadow-sm flex flex-col rounded-md p-2 w-4/5 lg:w-2/3" :class="msg_obj['clientId'] === clientId ? 'items-end bg-green-700/60 self-end' : 'items-start bg-gray-800 self-start'">
            <span class="text-lg" >
             <span :style="{ color: clientColorsMap[msg_obj['clientId']] }" v-if="msg_obj['clientId'] !== clientId">{{ msg_obj["clientName"] }}</span>
             <span class="text-white" v-else>You</span>
            </span>
            <div class="text-white font-semibold rounded-md text-xl">
              {{ msg_obj["message"] }}
            </div>
          
        </div>
      </div>
    </div>

    <div class="h-16 flex w-full bg-black/20 items-center border-t-gray-200 border-gray-700 flex-shrink-0 p-2 rounded-lg">
      <form @submit.prevent="sendMessage" class="w-full flex gap-2">
        <input class="p-4 rounded-md w-4/5 text-white bg-gray-800 active:border-none border-none" v-model="newMessage" placeholder="Message" />
        <button type="submit" class="p-2 flex-1 font-semibold text-white hover:scale-110" >
          <div>Send</div>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import { useRoomStore } from '../../stores/roomStore';

const roomStore = useRoomStore();
const message_obj = computed(() => roomStore.messages);
const clientId = computed(() => roomStore.getClientId);
const newMessage = ref('');
const connection = computed(() => roomStore.connection);
const clientColors = computed(() => generateClientColors(roomStore.getClientCount));
const clientColorsMap = computed(() => {
  const clientIds = new Set();
      message_obj.value.forEach(msg => {
        if (msg.clientId !== undefined) {
          clientIds.add(msg.clientId);
        } });

  const clientColorsObj = {}  
  const ids = Array.from(clientIds);
  for(const id of ids){
    const index = ids.indexOf(id);
    clientColorsObj[id] = clientColors.value[index];
  }
  return clientColorsObj;
});




const sendMessage = () => {
  if (newMessage.value.trim() && connection.value) {
    connection.value.send(newMessage.value);
    newMessage.value = '';
  }
};

function hslToHex(h, s, l) {
    s /= 100;
    l /= 100;

    const c = (1 - Math.abs(2 * l - 1)) * s;
    const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
    const m = l - c / 2;
    let r = 0,
        g = 0,
        b = 0;

    if (0 <= h && h < 60) {
        r = c;
        g = x;
        b = 0;
    } else if (60 <= h && h < 120) {
        r = x;
        g = c;
        b = 0;
    } else if (120 <= h && h < 180) {
        r = 0;
        g = c;
        b = x;
    } else if (180 <= h && h < 240) {
        r = 0;
        g = x;
        b = c;
    } else if (240 <= h && h < 300) {
        r = x;
        g = 0;
        b = c;
    } else if (300 <= h && h < 360) {
        r = c;
        g = 0;
        b = x;
    }

    // Convert to 0-255 and then to hex
    const toHex = (c) => {
        const hex = Math.round((c + m) * 255).toString(16);
        return hex.length === 1 ? "0" + hex : hex;
    };

    return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

function generateClientColors(clientCount, saturation = 70, lightness = 50) {
    const colors = [];
    const clientLimit = Math.max(2, Math.min(clientCount, 20)); // Clamp between 2 and 20
    const hueStep = 360 / clientLimit;

    for (let i = 0; i < clientLimit; i++) {
        const hue = i * hueStep;
        colors.push(hslToHex(hue, saturation, lightness));
    }
    return colors;
}
</script>

<style scoped>
</style>