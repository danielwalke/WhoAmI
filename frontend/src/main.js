import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createPinia } from 'pinia'
import { router } from './router/Router.js'
import Vue3Lottie from 'vue3-lottie'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia).use(router).use(Vue3Lottie)
app.mount('#app')
