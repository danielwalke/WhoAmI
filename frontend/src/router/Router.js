import { createMemoryHistory, createRouter } from 'vue-router'
import { routes } from './Routes.js'

export const router = createRouter({
  history: createMemoryHistory(),
  routes,
})