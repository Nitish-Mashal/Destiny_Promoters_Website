<template>
    <div class="container mx-auto px-4 py-14">
        <!-- Header -->
        <div class="pb-8">
            <div class="text-[35px] font-medium pb-2">Find Your Dream Property</div>
            <p class="text-black mt-2 text-[13px]">
                Welcome to <strong>Destiny Promoters</strong>, where your dream property awaits in every corner of our
                beautiful world. Explore our curated selection of properties, each offering a unique story and a chance
                to redefine your life.
            </p>
        </div>

        <!-- Search Input -->
        <div class="flex justify-center pb-4">
            <div class="relative w-[90%] max-w-3xl">
                <input type="text" placeholder="Search For A Property"
                    class="w-full px-4 py-3 pr-40 rounded-xl bg-gray-100 text-sm border-0 outline-none focus:ring-0 focus:outline-none" />

                <button
                    class="hidden md:flex absolute top-1/2 right-2 transform -translate-y-1/2 bg-black text-white px-5 py-2 rounded-lg text-sm items-center gap-2 hover:bg-gray-800">
                    <i class="bi bi-search text-base"></i>
                    Find Property
                </button>
                <div class="block md:hidden mt-4 text-center">
                    <button
                        class="bg-black text-white px-5 py-2 rounded-lg text-sm flex items-center gap-2 hover:bg-gray-800 mx-auto">
                        <i class="bi bi-search text-base"></i>
                        Find Property
                    </button>
                </div>
            </div>
        </div>

        <!-- Filters Section -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-10">
            <div v-for="(filter, index) in filters" :key="index" class="relative">
                <div @click="toggleDropdown(index)"
                    class="bg-gray-100 rounded-xl px-4 py-3 flex items-center justify-between text-sm cursor-pointer">
                    <div class="flex items-center gap-2">
                        <i :class="filter.icon"></i>
                        <span>{{ selectedOptions[index] ?? filter.label }}</span>
                    </div>
                    <i class="bi bi-chevron-down"></i>
                </div>
                <div v-if="activeDropdown === index"
                    class="absolute z-10 mt-1 w-full bg-white shadow-md rounded-xl text-sm overflow-hidden">
                    <div v-for="(option, idx) in filter.options" :key="idx" @click="selectOption(index, option)"
                        class="px-4 py-2 hover:bg-gray-100 cursor-pointer">
                        {{ option }}
                    </div>
                </div>
            </div>
        </div>

        <!-- Cards Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <div v-for="(property, index) in properties" :key="index"
                class="relative rounded-xl overflow-hidden shadow-md border bg-white">
                <img :src="property.image" alt="Property Image" class="w-full h-48 p-2 rounded" />

                <!-- SOLD OUT badge -->
                <div class="">
                    <div v-if="property.soldOut"
                        class="absolute top-2 left-2 bg-black text-white text-[10px] px-2 py-1 rounded">
                        SOLD OUT
                    </div>
                </div>

                <div class="px-3">
                    <div class="text-[13px] font-semibold">{{ property.title }}</div>
                    <div class="flex items-center justify-between gap-2 pb-2">
                        <div class="text-xs text-gray-800 truncate max-w-[60%]">
                            {{ property.description }}
                        </div>
                        <button
                            class="bg-black text-white px-2 py-1 rounded-lg hover:bg-gray-800 text-sm whitespace-nowrap">
                            Know More
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <BuildingAmenities />
    </div>
</template>

<script setup>
import BuildingAmenities from './BuildingAmenities.vue'
import { ref } from 'vue'

const activeDropdown = ref(null)
const selectedOptions = ref(Array(5).fill(null))

const toggleDropdown = (index) => {
    activeDropdown.value = activeDropdown.value === index ? null : index
}

const selectOption = (filterIndex, option) => {
    selectedOptions.value[filterIndex] = option
    activeDropdown.value = null
}

const filters = [
    { label: 'Location', icon: 'bi bi-geo-alt', options: ['Delhi', 'Mumbai', 'Bangalore', 'Chennai'] },
    { label: 'Property Type', icon: 'bi bi-buildings', options: ['Apartment', 'Villa', 'Plot', 'Commercial'] },
    { label: 'Pricing Range', icon: 'bi bi-cash-coin', options: ['< ₹50L', '₹50L - ₹1Cr', '₹1Cr - ₹2Cr', '> ₹2Cr'] },
    { label: 'Property Size', icon: 'bi bi-box', options: ['500-1000 sq ft', '1000-2000 sq ft', '2000+ sq ft'] },
    { label: 'Build Year', icon: 'bi bi-calendar-event', options: ['2025', '2024', '2020-2023', 'Before 2020'] },
]

// JSON with "soldOut"
const properties = ref([
    { title: "Avani Hills", description: "Your Dream will not...", image: new URL("../assets/images/Listing/Avani_Hills.png", import.meta.url).href, soldOut: true },
    { title: "Avani Gardens", description: "Your Dream, our passion...", image: new URL("../assets/images/Listing/Avani_Gardens.png", import.meta.url).href, soldOut: true },
    { title: "Avani Residency", description: "Stop Dreaming, Start Living...", image: new URL("../assets/images/Listing/Avani_Residency.png", import.meta.url).href, soldOut: true },
    { title: "SSB Royale", description: "Luxury you deserve...", image: new URL("../assets/images/Listing/SSB_Royale.png", import.meta.url).href, soldOut: true },
    { title: "Panchmukhi Paradise", description: "Where Diversity and...", image: new URL("../assets/images/Listing/Panchmuki.png", import.meta.url).href, soldOut: true },
    { title: "Birla Apple Spire", description: "Live Healthy, Live Well...", image: new URL("../assets/images/Listing/Birla_Apple.png", import.meta.url).href, soldOut: true },
    { title: "Reliance Trends", description: "A Commercial Project...", image: new URL("../assets/images/Listing/Reliancetrends.png", import.meta.url).href, soldOut: true },
    { title: "Suvedha Elegant", description: "An Irresistible Living...", image: new URL("../assets/images/Listing/SuvedhaElegant.png", import.meta.url).href, soldOut: true },
    { title: "Suvedha Paradise", description: "Higher Quality Of Living...", image: new URL("../assets/images/Listing/SuvedhaParadise.png", import.meta.url).href, soldOut: true },
    { title: "Suvedha Elite", description: "Quality Construction...", image: new URL("../assets/images/Listing/SuvedhaElite.png", import.meta.url).href, soldOut: true },
    { title: "Suvedha Luxuria", description: "A Rare Blend of Luxury...", image: new URL("../assets/images/Listing/SuvedhaLuxuria.png", import.meta.url).href, soldOut: true },
    { title: "Sri Sayuktha Enclave", description: "Redefining Luxury...", image: new URL("../assets/images/Listing/SriSayukthaEnclave.png", import.meta.url).href, soldOut: true },
    { title: "Bhaskara Elite", description: "Living Luxury...", image: new URL("../assets/images/Listing/BhaskaraElite.png", import.meta.url).href, soldOut: true },
    { title: "GR Galaxy", description: "A Place To Celebrate...", image: new URL("../assets/images/Listing/GRGalaxy.png", import.meta.url).href, soldOut: true },
    { title: "Suvedha Pride", description: "Higher Quality Of Living...", image: new URL("../assets/images/Listing/SuvedhaPride.png", import.meta.url).href, soldOut: true },
    { title: "Suvedha Sukriti", description: "Higher Quality Of Living...", image: new URL("../assets/images/Listing/SuvedhaSukriti.png", import.meta.url).href, soldOut: true },
    { title: "Sai Krupa Forest View", description: "Premium Apartments...", image: new URL("../assets/images/Listing/SaiKrupaForestView.png", import.meta.url).href, soldOut: true },
    { title: "Sai Krupa Elegance", description: "Peaceful Urban Life...", image: new URL("../assets/images/Listing/SaiKrupaElegance.png", import.meta.url).href, soldOut: true },
    { title: "Maitri Thimmiah Serenity", description: "A Vision for Your Future...", image: new URL("../assets/images/Listing/MuniThimmaiahSerenity.png", import.meta.url).href, soldOut: true },
])
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css";
</style>