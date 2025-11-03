<template>
  <div class="flex flex-col h-screen w-full">
    <main class="flex-1 overflow-hidden">
      <RouterView />
    </main>

    <footer class="h-16 w-full  ">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/input">Input</RouterLink>
      <RouterLink to="/game">Game</RouterLink>
      <RouterLink to="/room">Room</RouterLink>
      <RouterLink to="/chat">Chat</RouterLink>
    </footer>
  </div>
</template>

<style scoped>
footer {
  @apply w-full bg-black/90 p-4 flex justify-center items-center gap-16;
}

footer a {
  @apply font-semibold text-lg cursor-pointer hover:scale-110 transition-transform ease-in-out text-white; 
}
</style>
