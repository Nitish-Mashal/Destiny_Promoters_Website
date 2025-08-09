<template>
  <div>
    <div class="container-fluid">
      <!-- First Section -->
      <div class="relative max-w-[1300px] mx-auto rounded-3xl overflow-hidden">
        <!-- Background Image -->
        <img :src="bgImage" alt="Hero Banner" class="w-full h-[300px] sm:h-auto object-cover" />

        <!-- Overlay Content -->
        <div
          class="absolute inset-0 flex flex-col items-center justify-center text-white text-center px-2 sm:px-4 animate-slide-up">

          <!-- Heading -->
          <div
            class="text-[10px] sm:text-xs border border-white px-3 sm:px-4 py-1 sm:py-2 rounded-full tracking-wide mb-1 sm:mb-2">
            LET US GUIDE YOUR HOME
          </div>
          <div class="text-lg sm:text-3xl md:text-[45px] font-semibold mb-1 sm:mb-2">
            Enjoy The Finest Homes
          </div>
          <p class="text-[10px] sm:text-xs md:text-sm mb-4 sm:mb-8">
            From as low as $10 per day with limited time offer discounts
          </p>

          <!-- Filter Tabs -->
          <div
            class="flex items-center justify-center space-x-1 sm:space-x-2 bg-white text-black rounded-t-lg w-[130px] sm:w-[160px] md:w-[200px]">
            <button @click="setFilter('all')" :class="[
              'flex-1 py-1 sm:py-2 px-2 sm:px-3 text-[10px] sm:text-sm font-semibold rounded-tl-lg',
              selectedFilter === 'all' ? 'bg-black text-white' : 'hover:bg-gray-200'
            ]">All</button>

            <button @click="setFilter('sale')" :class="[
              'flex-1 py-1 sm:py-2 px-2 sm:px-3 text-[10px] sm:text-sm rounded-t-lg',
              selectedFilter === 'sale' ? 'bg-black text-white' : 'hover:bg-gray-200'
            ]">Sale</button>

            <button @click="setFilter('rent')" :class="[
              'flex-1 py-1 sm:py-2 px-2 sm:px-3 text-[10px] sm:text-sm rounded-t-lg',
              selectedFilter === 'rent' ? 'bg-black text-white' : 'hover:bg-gray-200'
            ]">Rent</button>
          </div>

          <!-- Search Bar -->
          <div
            class="bg-white rounded-2xl sm:rounded-3xl p-1 sm:p-2 shadow-lg w-[70%] sm:w-full sm:max-w-2xl flex flex-col sm:flex-row items-stretch sm:items-center overflow-hidden">

            <!-- Keyword -->
            <div class="flex-1 border-b sm:border-b-0 sm:border-r pr-3 sm:pr-6 mb-2 sm:mb-0">
              <label class="text-[10px] sm:text-xs text-gray-500 block text-left ml-2 sm:ml-3">Keyword</label>
              <input type="text" placeholder="Enter Keyword"
                class="w-full text-[10px] sm:text-sm border-0 outline-none focus:ring-0 text-black placeholder:text-black placeholder:text-[10px] sm:placeholder:text-xs" />
            </div>

            <!-- Type -->
            <div class="flex-1 border-b sm:border-b-0 sm:border-r px-2 sm:px-3 mb-2 sm:mb-0">
              <label class="text-[10px] sm:text-xs text-gray-500 block text-left ml-2 sm:ml-3">Type</label>
              <select class="w-full text-[10px] sm:text-sm border-0 outline-none focus:ring-0 text-black">
                <option>All Type</option>
                <option>House</option>
                <option>Apartment</option>
              </select>
            </div>

            <!-- Buttons -->
            <div class="flex gap-1 sm:gap-2 mt-2 sm:mt-0 sm:ml-2 justify-center">
              <!-- Filter Button -->
              <button
                class="flex items-center gap-1 px-2 sm:px-3 py-1 sm:py-2 text-[10px] sm:text-sm rounded-lg bg-white text-black border hover:bg-gray-100">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                  stroke="currentColor" class="w-3 h-3 sm:w-4 sm:h-4">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M10.5 6h9.75M10.5 6a1.5 1.5 0 1 1-3 0m3 0a1.5 1.5 0 1 0-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-9.75 0h9.75" />
                </svg>
                Filter
              </button>

              <!-- Search Button -->
              <button
                class="px-3 sm:px-4 py-1 sm:py-2 text-[10px] sm:text-sm rounded-lg bg-black text-white hover:bg-gray-800">
                Search
              </button>
            </div>
          </div>
        </div>

      </div>

      <!-- Second Section -->
      <div class="pt-10">
        <div class="container-fluid bg-gray-100 rounded-2xl mx-auto py-4 px-4">
          <div class="flex flex-col items-center relative">
            <div class="font-semibold text-5xl text-center">Homes For You</div>
            <div class="w-full flex justify-center mt-1">
              <div class="relative w-full max-w-6xl">
                <p class="text-sm text-center">Based on your view history</p>
                <router-link to="/Listing">
                  <div class="absolute right-0 top-0 flex items-center text-sm cursor-pointer underline text-black">
                    View All
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                      stroke="currentColor" class="w-4 h-3 ml-1">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 19.5 15-15m0 0H8.25m11.25 0v11.25" />
                    </svg>
                  </div>
                </router-link>
              </div>
            </div>
          </div>

          <!-- Carousel -->
          <el-carousel :interval="5000" arrow="always" height="350px" indicator-position="none">
            <el-carousel-item v-for="(chunk, index) in chunkedHomes" :key="'chunk-' + index">
              <div class="container">
                <div class="row justify-content-center g-4">
                  <div class="col-md-4" v-for="(home, idx) in chunk" :key="'home-' + idx">
                    <div class="card h-100 shadow-sm border-0 rounded-3">
                      <div class="position-relative">
                        <img :src="home.image" class="card-img-top p-2 rounded-4" alt="Property Image"
                          style="height: 220px; object-fit: cover" />
                        <span class="position-absolute top-0 start-0 m-4 p-2 badge bg-dark rounded-5">
                          {{ home.type === 'ready' ? 'READY TO OCCUPY' : home.type.toUpperCase() }}
                        </span>
                      </div>
                      <div class="card-body">
                        <div class="card-title fw-semibold mb-1">{{ home.title }}</div>
                        <p class="text-xs mb-3 d-flex align-items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                            stroke="currentColor" class="h-4 w-4 me-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                              d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                            <path stroke-linecap="round" stroke-linejoin="round"
                              d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                          </svg>
                          {{ home.location }}
                        </p>
                        <div class="d-flex flex-wrap gap-3 text-xs text-secondary">
                          <span class="d-flex align-items-center gap-1">
                            <img src="../assets/images/Bed.png" alt="" class="h-3"> {{ home.beds }}
                          </span>
                          <span class="d-flex align-items-center gap-1">
                            <img src="../assets/images/Bath.png" alt="" class="h-3"> {{ home.baths
                            }}
                          </span>
                          <span class="d-flex align-items-center gap-1">
                            <img src="../assets/images/Sqft.png" alt="" class="h-3"> {{ home.area }}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </el-carousel-item>
          </el-carousel>
        </div>
      </div>

      <!-- Stats: Show on small screens only -->
      <div
        class="block md:hidden bg-white p-4 w-[95%] mx-auto mt-4 grid grid-cols-1 text-center gap-4 rounded-xl shadow">
        <div>
          <div class="text-xl font-bold">5+</div>
          <div class="text-gray-500 text-sm">Completed Projects</div>
        </div>
        <div>
          <div class="text-xl font-bold">8+</div>
          <div class="text-gray-500 text-sm">Upcoming Projects</div>
        </div>
        <div>
          <div class="text-xl font-bold">25+</div>
          <div class="text-gray-500 text-sm">Trained Professionals</div>
        </div>
      </div>

      <!-- third Section -->
      <FeaturedCategories />

      <!-- Fourth Section -->
      <dreamhome />

      <!-- Fifth Section -->
      <FeaturedProperties />

      <!-- Sixth Section -->
      <CustomerTestimonials />

      <!-- seventh Section -->
      <HomeIntroSection />

      <!-- Eighth Section -->
      <BuildingAmenities />

    </div>
  </div>
</template>

<script setup>
import bgImage from '../assets/images/Home_Img_1.png'
import { ref, computed } from 'vue'
import { ElCarousel, ElCarouselItem } from 'element-plus'
import FeaturedProperties from './FeaturedProperties.vue'
import CustomerTestimonials from './CustomerTestimonials.vue'
import dreamhome from './dreamhome.vue'
import FeaturedCategories from './FeaturedCategories.vue'
import HomeIntroSection from './HomeIntroSection.vue'
import BuildingAmenities from './BuildingAmenities.vue'

const homes = [
  {
    title: 'Birla Apple Spire',
    location: 'Nayanda Halli, Bangalore',
    beds: '2 & 3 Beds',
    baths: '2 Baths',
    area: '1241 - 1847 sqft',
    type: 'ready',
    image: new URL('../assets/images/hfy_img_1.png', import.meta.url).href
  },
  {
    title: 'Suvedha Luxuria',
    location: 'Uttarahalli, Bangalore',
    beds: '3 Beds',
    baths: '2 Baths',
    area: '2227 sqft',
    type: 'sale',
    image: new URL('../assets/images/hfy_img_2.png', import.meta.url).href
  },
  {
    title: 'Suvedha Paradise',
    location: 'Srinivasnagar, Bangalore',
    beds: '2 & 3 Beds',
    baths: '2 Baths',
    area: '1075 - 1300 sqft',
    type: 'rent',
    image: new URL('../assets/images/hfy_img_3.png', import.meta.url).href
  }
]

const selectedFilter = ref('all')

const filteredHomes = computed(() => {
  return selectedFilter.value === 'all'
    ? homes
    : homes.filter(h => h.type === selectedFilter.value)
})

const chunkedHomes = computed(() => {
  const chunkSize = 3
  const chunks = []
  for (let i = 0; i < filteredHomes.value.length; i += chunkSize) {
    chunks.push(filteredHomes.value.slice(i, i + chunkSize))
  }
  return chunks
})

const setFilter = filter => {
  selectedFilter.value = filter
}
</script>

<style scoped>
.custom-clip {
  clip-path: polygon(70px 0%, 100% 0%, 100% 100%, 0% 100%, 0% 100px);
}

@keyframes slideUp {
  0% {
    transform: translateY(50px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

.animate-slide-up {
  animation: slideUp 0.8s ease-out forwards;
}
</style>