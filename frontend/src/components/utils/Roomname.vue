<template>
    <div class="flex flex-col gap-1 lg:gap-2 w-full">
        <input class="border-2 p-2 rounded-md" v-model="roomName" type="text" placeholder="Enter room name" />
        <span v-if="roomName.length < 3" class="text-red-500 text-sm">Room name must be at least 3 characters long.</span>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { watch } from 'vue'

const props = defineProps({
    roomName: {
        type: String,
        required: true
    }
})

const emit = defineEmits(['update:roomName'])

const roomName = ref(props.roomName)

watch(roomName, (newVal) => {
    emit('update:roomName', newVal)
})

watch(() => props.roomName, (newVal) => {
    if (newVal !== roomName.value) {
        roomName.value = newVal
    }
})
</script>