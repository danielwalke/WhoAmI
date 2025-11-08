import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createPinia } from 'pinia'
import { router } from './router/Router.js'
import Vue3Lottie from 'vue3-lottie'
import Particles from "@tsparticles/vue3";
import { loadFull } from "tsparticles";

const pinia = createPinia()
const app = createApp(App)

app.use(pinia).use(router).use(Vue3Lottie).use(Particles, {
  init: async engine => {
    await loadFull(engine);
  },
})
app.mount('#app')
