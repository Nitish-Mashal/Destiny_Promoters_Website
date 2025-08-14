import { createRouter, createWebHistory } from 'vue-router'
import Listing from './pages/Listing.vue'
import Home from './pages/Home.vue'
import AboutUs from './pages/AboutUs.vue'
import Construction from './pages/Construction.vue'
import Interiors from './pages/Interiors.vue'
import ListingDetails from './pages/ListingDetails.vue'
import ContactUs from './pages/ContactUs.vue'

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
  {
    path: '/ListingDetails/:id',
    name: 'ListingDetails',
    component: ListingDetails,
    props: true
  },
  {
    path: '/ContactUs',
    name: 'ContactUs',
    component: ContactUs,
  },
]

let router = createRouter({
  history: createWebHistory(
    process.env.NODE_ENV === 'production'
      ? '/destinypromoters/'
      : '/'
  ),
  routes,
})

export default router
