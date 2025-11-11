<template>
    <div class="card-scene">
        <div class="card-inner" :class="{ 'is-flipped': card.isActive }">
            <div class="card-face card-front">
                <div class="inactive-card-content">
                    <div class="image"></div>
                    <div class="title" style="color: #888; font-style: italic;"></div>
                </div>
            </div>

            <div class="card-face card-back">
                <div class="active-card-content">
                    <div class="image">
                        <img :src="card.url" alt="Card Image" class="w-full h-full object-contain rounded-md"/>
                    </div>
                    <div class="title">{{ card.title }}</div>
                </div>
            </div>

        </div>
    </div>
</template>

<script setup>
defineProps({
    card: {
        type: Object,
        required: true
    }
})
</script>
<style scoped>
.card-scene {
    @apply cursor-pointer w-full h-48 lg:h-52;
}

.card-inner {
    @apply relative w-full h-full transition-transform duration-700 ease-in-out flex justify-center items-center;
    transform-style: preserve-3d;
}

.card-inner.is-flipped {
    transform: rotateY(180deg);
}

.card-face {
    @apply absolute w-full h-full rounded-md shadow-lg border;
    backface-visibility: hidden;
}

.card-front {
    @apply bg-gray-100 border-gray-300;
}
.card-back {
    @apply bg-white border-gray-200;
    transform: rotateY(180deg);
}

.active-card-content,
.inactive-card-content {
    @apply p-4;
}

.image {
    @apply bg-gray-300 h-32 rounded-md flex items-center justify-center p-1;
}

.title {
    @apply text-lg font-semibold text-center min-h-8 pt-4;
}
</style>