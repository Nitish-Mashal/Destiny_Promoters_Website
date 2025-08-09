import { createRouter, createWebHistory } from 'vue-router'
import Listing from './pages/Listing.vue'
import Home from './pages/Home.vue'
import AboutUs from './pages/AboutUs.vue'
import Construction from './pages/Construction.vue'
import Interiors from './pages/Interiors.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/Listing',
    name: 'Listing',
    component: Listing,
  },
  {
    path: '/AboutUs',
    name: 'AboutUs',
    component: AboutUs,
  },
  {
    path: '/Construction',
    name: 'Construction',
    component: Construction,
  },
  {
    path: '/Interiors',
    name: 'Interiors',
    component: Interiors,
  },
]

let router = createRouter({
  history: createWebHistory(''),
  routes,
})

export default router
