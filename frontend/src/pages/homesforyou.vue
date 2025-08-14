<template>
    <div class="px-4">
        <div class="container-fluid bg-gray-50 rounded-2xl mx-auto py-4 px-4">
            <div class="flex flex-col items-center relative">
                <div class="font-semibold text-5xl text-center">Homes For You</div>
                <div class="w-full flex justify-center mt-1">
                    <div class="relative w-full max-w-6xl">
                        <p class="text-sm text-center">Based on your view history</p>
                        <router-link to="/Listing">
                            <div
                                class="absolute right-0 top-0 flex items-center text-sm cursor-pointer underline text-black">
                                View All
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                                    stroke="currentColor" class="w-4 h-3 ml-1">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="m4.5 19.5 15-15m0 0H8.25m11.25 0v11.25" />
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
                                        <span class="position-absolute top-0 start-0 m-3 p-2 badge bg-dark">
                                            {{ home.type === 'ready' ? 'READY TO OCCUPY' : home.type.toUpperCase() }}
                                        </span>
                                    </div>
                                    <div class="card-body">
                                        <div class="card-title fw-semibold mb-1">{{ home.title }}</div>
                                        <p class="text-xs mb-2 d-flex align-items-center">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                                stroke-width="2" stroke="currentColor" class="h-4 w-4 me-1">
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
</template>

<script setup>
import { computed } from 'vue'

const homes = [
    {
        title: 'Birla Apple Spire',
        location: 'Nayanda Halli, Bangalore',
        beds: '2 & 3 Beds',
        baths: '2 Baths',
        area: '1241 - 1847 sqft',
        type: 'ready',
        image: '/assets/images/hfy_img_1.png'
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

// Function to chunk homes array into groups of 3
const chunkedHomes = computed(() => {
    const chunkSize = 3
    const chunks = []
    for (let i = 0; i < homes.length; i += chunkSize) {
        chunks.push(homes.slice(i, i + chunkSize))
    }
    return chunks
})
</script>