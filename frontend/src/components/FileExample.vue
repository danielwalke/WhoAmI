<script setup>
import { ref } from 'vue'

// Sample data
const items = ref([
  { id: 1, title: 'Item 1' },
  { id: 2, title: 'Item 2' },
  { id: 3, title: 'Item 3' },
  { id: 4, title: 'Item 4' },
  { id: 5, title: 'Item 5' },
  { id: 6, title: 'Item 6' },
])

// Use an object to track the flipped state for each card by its ID
const flippedCards = ref({})

// Function to toggle the flipped state for a specific card ID
function toggleFlip(id) {
  // This reactivity works perfectly in Vue 3
  flippedCards.value[id] = !flippedCards.value[id]
}
</script>

<template>
  <div class="p-6 bg-gray-100">
    <h1 class="text-2xl font-bold mb-4">Clickable Flip Card Grid</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      
      <div 
        v-for="item in items" 
        :key="item.id" 
        class="h-48 [perspective:1000px]"
      >
        <div 
          class="relative w-full h-full cursor-pointer transition-transform duration-700 [transform-style:preserve-3d]"
          :class="{ 'rotate-y-180': flippedCards[item.id] }"
          @click="toggleFlip(item.id)"
        >
          <div class="absolute inset-0 w-full h-full backface-hidden bg-white p-6 rounded-lg shadow-md flex flex-col justify-center items-center">
            <h2 class="text-xl font-semibold">{{ item.title }}</h2>
            <p class="text-gray-600">This is the FRONT</p>
            <p class="text-sm text-gray-400 mt-4">(Click me)</p>
          </div>

          <div class="absolute inset-0 w-full h-full backface-hidden rotate-y-180 bg-indigo-600 text-white p-6 rounded-lg shadow-md flex flex-col justify-center items-center">
            <h2 class="text-xl font-semibold">{{ item.title }}</h2>
            <p>This is the BACK</p>
            <p class="text-sm text-indigo-200 mt-4">(Click to flip back)</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
/* Tailwind's 'backface-hidden' utility handles this, 
   but this is the underlying CSS rule. */
.backface-hidden {
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}
</style>