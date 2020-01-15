import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import { authService } from '../services/auth.service'

Vue.use(VueRouter)

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/login', name: 'login', component: Login },
  { path: '/login/:token', name: 'token', component: Login },
  { path: '/:repo', name: 'repoDetails', component: Home }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const auth = authService.getService();
  if (to.name !== 'login' && to.name !== 'token' && !auth.token) {
    next('/login');
  }
  if (to.name === 'login' && !!auth.token) {
    next('/');
  }
  if (to.name === 'token') {
    auth.token = from.params.token
    console.log(auth.token)
    next('/');
  }
  next();
})

export default router
