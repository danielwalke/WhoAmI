import { createWebHistory, createRouter } from 'vue-router'
import { routes } from './Routes.js'

export const router = createRouter({
  history: createWebHistory(),
  routes,
})