<template>
    <div class="container mx-auto px-4 py-8">
        <!-- Section Heading -->
        <div class="text-center">
            <div class="font-semibold text-7xl">Featured Properties</div>
            <p class="text-xs">Lorem ipsum dolor sit amet</p>
        </div>

        <!-- Cards Grid -->
        <div class="row g-4">
            <div v-for="(property,) in properties" :key="property.id" class="col-12 col-sm-6 col-lg-3">
                <!-- Wrap card with RouterLink -->
                <router-link :to="`/listing/${property.id}`" class="text-decoration-none">
                    <div class="card h-100 shadow-sm border-0 rounded-3 border-5">
                        <!-- Image Section -->
                        <div class="relative p-2 pb-0">
                            <img :src="property.thumbnail" class="card-img-top rounded-3" alt="Property" />
                            <!-- Badges -->
                            <div class="absolute top-6 left-6 flex gap-2">
                                <span v-for="(badge, idx) in property.badges" :key="idx"
                                    class="px-3 py-1 text-xs font-bold rounded-full" :class="badgeColors(badge)">
                                    {{ badge }}
                                </span>
                            </div>
                        </div>

                        <!-- Card Body -->
                        <div class="card-body">
                            <h6 class="text-red-400 font-semibold text-[13px]">
                                {{ property.project_name }}
                            </h6>
                            <div class="card-title fw-semibold mb-1 text-[13px]">
                                {{ property.builder }}
                            </div>
                            <div class="text-xs mb-2 d-flex align-items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                                    stroke="currentColor" class="h-4 w-4 me-1">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                                </svg>
                                {{ property.full_location }}
                            </div>

                            <!-- Features -->
                            <div class="d-flex flex-wrap gap-3 text-sm text-secondary">
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Bed.png" alt="" class="h-3" />
                                    {{ property.bhk }}
                                </span>
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Bath.png" alt="" class="h-3" />
                                    {{ property.bath }}
                                </span>
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Sqft.png" alt="" class="h-3" />
                                    {{ property.super_built_up_area }}
                                </span>
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

const properties = ref([])

const badgeColors = (badge) => {
    switch (badge) {
        case "FOR RENT":
            return "bg-black text-white"
        case "FEATURED":
            return "bg-yellow-200 text-black"
        case "SOLD OUT":   // 👈 added this case
            return "bg-[#1a1a1a] text-white"
        default:
            return "bg-black text-white"
    }
}

onMounted(async () => {
    try {
        const response = await fetch(
            "/api/method/destiny_promoters_website.api.project_api.get_projects"
        )
        if (!response.ok) throw new Error("Failed to fetch projects")
        const data = await response.json()

        const allProjects = data.message.map((project) => ({
            id: project.name,
            project_name: project.project_name,
            builder: project.builder,
            full_location: project.full_location,
            bhk: project.bhk,
            bath: project.bath,
            super_built_up_area: project.super_built_up_area,
            thumbnail: project.thumbnail,
            // 👇 Replace FOR SALE with SOLD OUT
            badges: project.featured ? ["FEATURED"] : ["SOLD OUT"],
        }))

        properties.value = allProjects
            .filter((p) => p.badges.includes("FEATURED"))
            .slice(0, 4)

        if (properties.value.length === 0) {
            properties.value = allProjects.slice(0, 4)
        }
    } catch (err) {
        console.error("Error loading projects:", err)
    }
})
</script>
