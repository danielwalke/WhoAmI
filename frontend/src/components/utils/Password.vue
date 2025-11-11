<template>
    <div class="flex flex-col gap-1 lg:gap-2 w-full">
        <div class="relative">
            <input
            class="border-2 p-2 rounded-md w-full pr-10"
            :type="showPassword ? 'text' : 'password'"
            v-model="roomPassword"
            placeholder="Enter room password"
            />
            <button
            type="button"
            class="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-500 hover:scale-100 p-2 bg-white rounded-full"
            @click="showPassword = !showPassword"
            tabindex="-1"
            >
            <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M2.458 12C3.732 7.943 7.523 5 12 5c4.477 0 8.268 2.943 9.542 7-1.274 4.057-5.065 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13.875 18.825A10.05 10.05 0 0112 19c-4.477 0-8.268-2.943-9.542-7a9.956 9.956 0 012.442-4.362M6.634 6.634A9.956 9.956 0 0112 5c4.477 0 8.268 2.943 9.542 7a9.965 9.965 0 01-4.293 5.072M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 3l18 18" />
            </svg>
            </button>
        </div>
        <span v-if="roomPassword.length < 6" class="text-red-500 text-sm">Password must be at least 6 characters long.</span>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { watch } from 'vue'

const props = defineProps({
    roomPassword: {
        type: String,
        required: true
    }
})

const emit = defineEmits(['update:roomPassword'])

const roomPassword = ref(props.roomPassword)
const showPassword = ref(false)

watch(roomPassword, (newVal) => {
    emit('update:roomPassword', newVal)
})

watch(() => props.roomPassword, (newVal) => {
    if (newVal !== roomPassword.value) {
        roomPassword.value = newVal
    }
})
</script>