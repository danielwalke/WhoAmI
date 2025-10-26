<script setup>
import Field from './components/Field.vue'
</script>

<template>
  <div class="w-full h-full">
    <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>
    
    <main>
      <RouterView />
    </main>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/game">Game</RouterLink>
    </nav>
  </div>
</template>

<style scoped>
nav {
  @apply fixed bottom-0 left-0 w-full bg-gray-200 p-4 border-t flex justify-center items-center gap-16;
}

nav a {
  @apply font-semibold text-lg cursor-pointer hover:scale-105 transition-transform ease-in-out; 
}
</style>
