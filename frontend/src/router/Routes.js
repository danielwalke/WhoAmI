import Field from '@/components/Field.vue'
import Home from '@/components/Home.vue'
import Chat from '@/components/chat/Chat.vue'
import Preparation from '@/components/preparation/Preparation.vue'
import Invitation from '@/components/invitation/Invitation.vue'

export const ROUTE_PREFIX = "/whoisit"

export const routes = [
  { path: '/', redirect: ROUTE_PREFIX + '/' },
  { path: ROUTE_PREFIX+'/', component: Home },
  { path: ROUTE_PREFIX+'/game', component: Field },
  { path: ROUTE_PREFIX+'/chat', component: Chat },
  { path: ROUTE_PREFIX+'/prepare', component: Preparation },
  { path: ROUTE_PREFIX+'/invite/:room_id/:room_password/:client_name', component: Invitation },
]