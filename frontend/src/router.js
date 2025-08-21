import { createRouter, createWebHistory } from 'vue-router'
import Listing from './pages/Listing.vue'
import Home from './pages/Home.vue'
import AboutUs from './pages/AboutUs.vue'
import Construction from './pages/Construction.vue'
import Interiors from './pages/Interiors.vue'
import ListingDetails from './pages/ListingDetails.vue'
import ContactUs from './pages/ContactUs.vue'
import PrivacyPolicy from './pages/PrivacyPolicy.vue'
import TermsAndConditions from './pages/TermsAndConditions.vue'

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
  {
    path: '/PrivacyPolicy',
    name: 'PrivacyPolicy',
    component: PrivacyPolicy,
  },
  {
    path: '/TermsAndConditions',
    name: 'TermsAndConditions',
    component: TermsAndConditions,
  },
]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return { top: 0 }
  }
})

export default router
