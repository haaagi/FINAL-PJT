import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/moviedetail/',
    name: 'moviedetail',
    component: MovieDetail
  },
]
})


export default router
