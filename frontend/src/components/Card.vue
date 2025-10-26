<template>
    <div class="card">
        <div class="image">Image Placeholder</div>
        <div class="title">{{title}}</div>
    </div>
</template>

<script setup>
defineProps({
    title: {
        type: String,
        required: true
    }
})
</script>

<style scoped>
.card{
    @apply rounded-md p-6 shadow-lg bg-white border border-gray-200;
}


.image{
    @apply bg-gray-300 h-32 mb-4 rounded-md flex items-center justify-center p-1;
}

.title{
    @apply text-lg font-semibold text-center;
}
</style>