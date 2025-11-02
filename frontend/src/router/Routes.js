import Field from '@/components/Field.vue'
import Input from '@/components/Input.vue'  
import Home from '@/components/Home.vue'
import Chat from '@/components/chat/Chat.vue'
import Room from '@/components/room/Room.vue'
export const routes = [
  { path: '/', component: Home },
  { path: '/input', component: Input },
  { path: '/game', component: Field },
  { path: '/room', component: Room },
  { path: '/chat', component: Chat },
]