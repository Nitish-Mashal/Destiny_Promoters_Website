<template>
    <div v-if="property">
        <!-- First Section: Carousel -->
        <el-carousel indicator-position="outside" :height="carouselHeight">
            <el-carousel-item v-for="(image, index) in property.carouselImages" :key="index">
                <img :src="image" alt="Carousel Image" class="w-full h-full" />
            </el-carousel-item>
        </el-carousel>

        <!-- Second Section -->
        <div class="px-[7%] mb-6">
            <div class="flex flex-wrap items-center gap-4 w-full md:w-3/4 lg:w-75">

                <!-- Status -->
                <span class="bg-[#E7C873] px-3 py-1 text-white rounded-3xl">
                    {{ property.status }}
                </span>

                <!-- Floors -->
                <span class="flex items-center text-sm font-bold gap-1">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-5 h-5 text-[#E7C873]">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M3.75 21h16.5M4.5 3h15M5.25 3v18m13.5-18v18M9 6.75h1.5m-1.5 3h1.5m-1.5 3h1.5m3-6H15m-1.5 3H15m-1.5 3H15M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21" />
                    </svg>
                    {{ property.floors }}
                </span>

                <!-- BHK -->
                <span class="flex items-center text-sm font-bold gap-1">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-5 h-5 text-[#E7C873]">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                    </svg>
                    {{ property.bhk }}
                </span>

                <!-- Location -->
                <span class="flex items-center text-sm font-bold gap-1">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-5 h-5 text-[#E7C873]">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    {{ property.fullLocation }}
                </span>

            </div>
        </div>

        <!-- Third Section -->
        <div class="px-[7%] mb-6">
            <div class="text-[#E7C873] font-extrabold text-4xl md:text-7xl mb-3">{{ property.name }}</div>
            <div class="row font">

                <!-- Left Column: Description -->
                <div class="col-12 col-md-6 mb-4 mb-md-0">
                    <div class="font-semibold text-7xl mb-2">Description</div>
                    <div class="text-sm">
                        {{ property.description }}
                    </div>
                </div>
                <div class="col-md-1"></div>

                <!-- Right Column: Property Detail -->
                <div class="col-12 col-md-5">
                    <div class="font-semibold text-7xl mb-2">Property Detail</div>
                    <div class="row text-sm">
                        <div class="col-6">
                            <div class="mb-2">Status: <span class="font-semibold">{{ property.status }}</span></div>
                            <div class="mb-2">Project Area: <span class="font-semibold">{{ property.projectArea
                            }}</span></div>
                            <div class="mb-2">Project By: <span class="font-semibold">{{ property.builder }}</span>
                            </div>
                            <div class="mb-2">Super Built Up Area: <span class="font-semibold">{{
                                property.superBuiltUpArea }}</span></div>
                        </div>
                        <div class="col-6">
                            <div class="mb-2">Project Type: <span class="font-semibold">{{ property.type }}</span></div>
                            <div class="mb-2">No Of Floors: <span class="font-semibold">{{ property.floors }}</span>
                            </div>
                            <div class="mb-2">Location: <span class="font-semibold">{{ property.location }}</span></div>
                            <div class="mb-2">No Of Rooms: <span class="font-semibold">{{ property.bhk }}</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Fourth Section -->
        <div class="px-[7%]">
            <div class="font font-semibold text-4xl md:text-7xl mb-3 text-center">Project Gallery</div>
            <div class="row font g-3">
                <div class="col-12 col-md-6">
                    <img v-if="property.galleryImages && property.galleryImages[0]" :src="property.galleryImages[0]"
                        alt="Project Image 1" class="img-fluid w-100 rounded">
                </div>
                <div class="col-12 col-md-6">
                    <img v-if="property.galleryImages && property.galleryImages[1]" :src="property.galleryImages[1]"
                        alt="Project Image 2" class="img-fluid w-100 rounded mb-3">
                    <img v-if="property.galleryImages && property.galleryImages[2]" :src="property.galleryImages[2]"
                        alt="Project Image 3" class="img-fluid w-100 rounded">
                </div>
            </div>
        </div>

        <!-- Fifth Section -->
        <BuildingAmenities />
    </div>

    <div v-else class="text-center py-14">
        <p>Property not found.</p>
    </div>
</template>

<script setup>
import BuildingAmenities from './BuildingAmenities.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import propertiesData from '../data/properties.json'

const route = useRoute()
const property = ref(null)
const carouselHeight = ref('550px')

const setHeight = () => {
    if (window.innerWidth < 768) {
        carouselHeight.value = '250px'
    } else if (window.innerWidth < 1024) {
        carouselHeight.value = '400px'
    } else {
        carouselHeight.value = '550px'
    }
}

onMounted(() => {
    const id = Number(route.params.id)
    property.value = propertiesData.find(p => p.id === id) || null
    setHeight()
    window.addEventListener('resize', setHeight)
})
</script>