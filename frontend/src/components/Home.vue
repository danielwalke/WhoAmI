<template>
  <div class="relative flex flex-col items-center justify-center h-full text-white p-6 w-full">
    
    <!-- Desktop particle background -->
    <div 
      v-show="isDesktop"
      class="absolute inset-0 -z-10"
    >
      <vue-particles
        id="tsparticles"
        :options="particleOptions"
      />
    </div>

    <!-- Main content box -->
    <div
  class="flex flex-col items-center justify-center"
  :class="[
    isDesktop
      ? 'lg:w-2/3 w-full bg-opacity-80  rounded-2xl p-8'
      : 'w-full  p-6'
  ]"
> 
      <div class="mb-6">
        <img 
          src="../assets/logo.png" 
          alt="Who is it? Logo" 
          class="h-64 w-auto rounded-full shadow-lg" 
        />
      </div>

      <h1 class="text-5xl font-bold mb-4 text-center">
        Welcome to Who is it?
      </h1>

      <p class="text-xl italic text-sky-100 mb-12 text-center max-w-lg">
        "One face in the crowd holds the secret. Can you find it first?"
      </p>

      <div class="bg-white text-gray-800 rounded-lg shadow-xl p-8 max-w-2xl w-full">
        <p class="text-base md:text-lg mb-6 leading-relaxed">
          Welcome to "Who is it?", the classic two-player mystery-face game! It's a race of logic and deduction.
          You and your opponent each have a board full of quirky characters. Your goal:
          Ask smart yes-or-no questions to eliminate the wrong faces and be the first to guess your opponent's secret character!
        </p>

        <h2 class="text-2xl font-semibold text-sky-700 mb-4">
          How to Play:
        </h2>
        <ol class="list-decimal list-inside space-y-2 mb-8">
          <li>Each player secretly selects one character from their board.</li>
          <li>Take turns asking one yes-or-no question (e.g., "Does your person have glasses?").</li>
          <li>Based on the answer, flip down the characters that don't match the clue.</li>
          <li>The first player to correctly guess their opponent's mystery person wins!</li>
        </ol>

        <div class="text-center">
          <p class="text-xl font-semibold mb-4">
            Ready to put your logic to the test?
          </p>
          <button
            class="bg-sky-600 text-white font-bold py-3 px-8 rounded-full hover:bg-sky-700 transition duration-300 shadow-lg text-lg"
            @click="$router.push('/whoisit/prepare')"
          >
            PLAY NOW
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'


const isDesktop = ref(false)

const checkScreenSize = () => {
  isDesktop.value = window.innerWidth >= 1024
}

onMounted(() => {
  checkScreenSize()
  //window.addEventListener('resize', checkScreenSize)
})

onUnmounted(() => {
  // window.removeEventListener('resize', checkScreenSize)
})

const particleOptions = {
  background: {
    color: { value: '#0d47a1' }
  },
  fpsLimit: 120,
  interactivity: {
    events: {
      onClick: { enable: true, mode: 'push' },
      onHover: { enable: true, mode: 'repulse' }
    },
    modes: {
      bubble: { distance: 400, duration: 2, opacity: 0.8, size: 40 },
      push: { quantity: 4 },
      repulse: { distance: 200, duration: 0.4 }
    }
  },
  particles: {
    color: { value: '#ffffff' },
    links: {
      color: '#ffffff',
      distance: 150,
      enable: true,
      opacity: 0.5,
      width: 1
    },
    move: {
      direction: 'none',
      enable: true,
      outModes: 'bounce',
      random: false,
      speed: 6,
      straight: false
    },
    number: {
      density: { enable: true },
      value: 80
    },
    opacity: { value: 0.5 },
    shape: { type: 'circle' },
    size: { value: { min: 1, max: 5 } }
  },
  detectRetina: true
}

const particlesLoaded = (container) => {
  console.log('Particles loaded:', container)
}
</script>

<style scoped>
/* Nothing special needed, Tailwind handles responsiveness and layout */
</style>
