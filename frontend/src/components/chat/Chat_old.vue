<template>
  <div class="w-full flex flex-col bg-black/70">
    
    <div class="basis-11/12 overflow-y-auto">
      <div class=" max-h-full">
        <div class="bg-green-600 h-96">Test</div>
        <div class="bg-green-600 h-96">Test</div>
        <div class="bg-green-600 h-96">Test</div>
        <div class="bg-green-600 h-96">Test</div>
      </div>
      
      <!-- <div class="flex flex-col gap-2 p-4">
        <div v-for="(msg_obj, index) in message_obj" :key="index" class="shadow-sm flex flex-col rounded-md p-2" :class="msg_obj['clientId'] === clientId ? 'items-end bg-green-700/60' : 'items-start bg-gray-800/80'">
          <span v-if="msg_obj['clientId'] !== clientId" :style="{ color: clientColors[msg_obj['clientId'] % clientColors.length] }">
            {{ msg_obj["clientId"] }}:
          </span>
          <div class="text-white font-semibold rounded-md">
            {{ msg_obj["message"] }}
          </div>
        </div>
      </div> -->
    </div>

    <div class="basis-1/12 flex w-full bg-gray-600 items-center border-t-2 border-t-gray-600 rounded-lg flex-shrink-0">
      <form @submit.prevent="sendMessage" class="w-full flex gap-2">
        <input class="p-4 rounded-md w-4/5 text-white bg-gray-600 active:border-none border-none" v-model="newMessage" placeholder="Message" />
        <button type="submit" class="p-2 flex-1 font-semibold text-white" >
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