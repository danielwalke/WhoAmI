<template>
    <div class="p-2">
        <button @click="sendInvitaion">Send Invitation</button>
    </div>
</template> 

<script setup>
import { useRoomStore } from '../../stores/RoomStore.js'
const roomStore = useRoomStore();
import { CLIENT_URL } from '../../constants/Server'

async function sendInvitaion(){
    const url = `${CLIENT_URL}/whoisit/invite/${roomStore.getRoomId}/${roomStore.getRoomPassword}/guest`
    const text = `Remember the classic game ‘Who is it?’ - where you uncover the other player’s mystery character just by asking clever yes-or-no questions? Join me using this link: ${url}`
    if (navigator.share) await navigator.share({ title: `'Who is it?' Invitation Link from ${roomStore.getClientName}`, text: text, url: url })
  else {
    await navigator.clipboard.writeText(text)
    alert('Link copied to clipboard')
  }
}
</script>