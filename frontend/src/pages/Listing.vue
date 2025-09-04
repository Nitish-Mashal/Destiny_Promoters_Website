<template>
    <div class="container mx-auto px-4 pt-14">
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
                <input type="text" placeholder="Search For A Property" v-model="searchQuery"
                    class="w-full px-4 py-3 pr-40 rounded-xl bg-gray-100 text-sm border-0 outline-none focus:ring-0" />

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

        <!-- Filters -->
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

        <!-- Property Cards -->
        <div class="font grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <router-link v-for="property in filteredProperties" :key="property.id"
                :to="{ name: 'ListingDetails', params: { id: property.id } }"
                class="relative rounded-xl overflow-hidden shadow-md border bg-white no-underline text-black hover:no-underline">

                <!-- Thumbnail -->
                <img :src="property.thumbnail" alt="Property Image" class="w-full h-52 p-2 rounded-4" />

                <!-- Sold Out Badge -->
                <div class="absolute top-4 left-4 bg-black text-white text-[10px] px-2 py-1 rounded-3xl">
                    SOLD OUT
                </div>

                <div class="px-3">
                    <!-- Project Name -->
                    <div class="text-[13px] font-semibold no-underline">
                        {{ property.name }}
                    </div>

                    <!-- Description + Button -->
                    <div class="flex items-center justify-between gap-2 pb-2">
                        <div class="text-xs text-gray-800 truncate max-w-[60%] no-underline">
                            {{ property.description }}
                        </div>
                        <button
                            class="bg-black text-white px-2 py-1 rounded-lg hover:bg-gray-800 text-sm whitespace-nowrap no-underline">
                            Know More
                        </button>
                    </div>
                </div>
            </router-link>
        </div>

        <!-- Animities Section -->
        <BuildingAmenities />

    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import BuildingAmenities from './BuildingAmenities.vue'

const properties = ref([])
const searchQuery = ref('')
const activeDropdown = ref(null)
const selectedOptions = ref(Array(5).fill(null))
const locations = ref([])         // dynamic locations
const propertyTypes = ref([])     // dynamic property types
const propertySizes = ref([])     // dynamic property sizes

// ✅ Utility: strip HTML tags so description can be truncated safely
function stripHtml(html) {
    const div = document.createElement('div')
    div.innerHTML = html
    return div.textContent || div.innerText || ''
}

onMounted(async () => {
    try {
        const res = await fetch("/api/method/destiny_promoters_website.api.project_api.get_projects")
        if (!res.ok) throw new Error("Failed to load properties")
        const data = await res.json()

        properties.value = data.message.map(p => ({
            id: p.name,
            name: p.project_name,
            description: stripHtml(p.description),
            thumbnail: p.thumbnail,
            fullLocation: p.full_location,
            location: p.full_location ? p.full_location.split(",")[0].trim() : "", // short location
            propertyType: p.property_type,
            superBuiltUpArea: p.super_built_up_area,  // 🔹 new field
            bhk: p.bhk,
            floors: p.floors,
            soldOut: p.status?.toLowerCase() === "sold out"
        }))

        // 🔹 Extract unique short locations
        locations.value = [...new Set(properties.value.map(p => p.location).filter(Boolean))]

        // 🔹 Extract unique property types + "All"
        const uniqueTypes = [...new Set(properties.value.map(p => p.propertyType).filter(Boolean))]
        propertyTypes.value = ["All", ...uniqueTypes]

        // 🔹 Extract unique property sizes
        propertySizes.value = [...new Set(properties.value.map(p => p.superBuiltUpArea).filter(Boolean))]
    } catch (err) {
        console.error("Error fetching properties:", err)
    }
})

const toggleDropdown = (index) => {
    activeDropdown.value = activeDropdown.value === index ? null : index
}

const selectOption = (filterIndex, option) => {
    selectedOptions.value[filterIndex] = option
    activeDropdown.value = null
}

// ✅ Filters setup (dynamic for Location + Property Type + Property Size)
const filters = computed(() => [
    { label: 'Location', icon: 'bi bi-geo-alt', options: locations.value },
    { label: 'Property Type', icon: 'bi bi-buildings', options: propertyTypes.value },
    { label: 'Pricing Range', icon: 'bi bi-cash-coin', options: ['< ₹50L', '₹50L - ₹1Cr', '₹1Cr - ₹2Cr', '> ₹2Cr'] },
    { label: 'Property Size', icon: 'bi bi-box', options: propertySizes.value }, // 🔹 dynamic
    { label: 'Build Year', icon: 'bi bi-calendar-event', options: ['2025', '2024', '2020-2023', 'Before 2020'] },
])

// ✅ Filtering logic
const filteredProperties = computed(() => {
    return properties.value.filter(p => {
        const matchesSearch = p.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        const matchesLocation = !selectedOptions.value[0] || p.location === selectedOptions.value[0]
        const matchesType =
            !selectedOptions.value[1] || selectedOptions.value[1] === "All" || p.propertyType === selectedOptions.value[1]
        const matchesSize =
            !selectedOptions.value[3] || p.superBuiltUpArea === selectedOptions.value[3] // 🔹 Property size filter

        return matchesSearch && matchesLocation && matchesType && matchesSize
    })
})
</script>
