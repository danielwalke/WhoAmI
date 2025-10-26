<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-sky-600 opacity-80 text-white p-6">
    
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
        Welcome to "Who is it?", the classic two-player mystery-face game! It's a race of logic and deduction. You and your opponent each have a board full of quirky characters. Your goal: Ask smart yes-or-no questions to eliminate the wrong faces and be the first to guess your opponent's secret character!
      </p>

      <h2 class="text-2xl font-semibold text-sky-700 mb-4">
        How to Play:
      </h2>
      <ol class="list-decimal list-inside space-y-2 mb-8">
        <li>Each player secretly selects one character from their board.</li>
        <li>Take turns asking one yes-or-no question (e.g., "Does your person have glasses?").</li>
        <li>Based on the answer, flip down the characters on your board that don't match the clue.</li>
        <li>The first player to correctly guess their opponent's mystery person wins!</li>
      </ol>

      <div class="text-center">
        <p class="text-xl font-semibold mb-4">
          Ready to put your logic to the test?
        </p>
        <button class="bg-sky-600 text-white font-bold py-3 px-8 rounded-full hover:bg-sky-700 transition duration-300 shadow-lg text-lg" @click="$router.push('/input')">
          PLAY NOW
        </button>
      </div>
      
    </div>
  </div>
</template>

<script setup>
// No script logic is needed for this static introduction page.
</script>

<style scoped>
/* Scoped styles can be added here, but Tailwind classes 
   are handling all the styling for this component. */
</style>