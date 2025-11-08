import Field from '@/components/Field.vue'
import Home from '@/components/Home.vue'
import Chat from '@/components/chat/Chat.vue'
import Preparation from '@/components/preparation/Preparation.vue'
export const routes = [
  { path: '/', component: Home },
  { path: '/game', component: Field },
  { path: '/chat', component: Chat },
  { path: '/prepare', component: Preparation },
]