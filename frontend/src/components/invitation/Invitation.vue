<template>
    <div>
        Invitation in progress...
        <div v-if="invitationError" class="error-message">{{ invitationError }}</div>
    </div>
</template>
<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useRoomStore } from '../../stores/RoomStore.js'
import { onMounted, ref } from 'vue'

const invitationError = ref(undefined);
const urlParams = useRoute().params;
const roomStore = useRoomStore();
const router = useRouter();
onMounted(async () => {
    try{
        await roomStore.joinRoom(urlParams.room_id, urlParams.room_password, urlParams.client_name)
        setTimeout(() => {
            router.push('/whoisit/game');
        }, 500);
        invitationError.value = undefined;
    } catch (error) {
        console.error('Error during joinRoom:', error);
        invitationError.value = "Invalid invitation link. Please check the link or contact the inviter.";
    }
});
//http://localhost:5173/whoisit/invite/80559d6f-c262-4a18-86e8-63e8e0f79dab/testtest/sandra
</script>

<style scoped>  
.error-message {
    color: red;
    font-weight: bold;
    margin-top: 20px;
}
</style>
