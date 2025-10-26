import Field from '@/components/Field.vue'
import Input from '@/components/Input.vue'  
import Home from '@/components/Home.vue'
export const routes = [
  { path: '/', component: Home },
  { path: '/input', component: Input },
  { path: '/game', component: Field },
]