<template>
    <div class="container mx-auto px-4 py-8">
        <!-- Section Heading -->
        <div class="text-center">
            <div class="font-semibold text-7xl">Featured Properties</div>
            <p class="text-xs">Lorem ipsum dolor sit amet</p>
        </div>

        <!-- Cards Grid -->
        <div class="row g-4">
            <div v-for="(property, index) in properties" :key="index" class="col-12 col-sm-6 col-lg-3">
                <!-- Wrap card with RouterLink -->
                <router-link :to="`/ListingDetails/${property.id}`" class="text-decoration-none">
                    <div class="card h-100 shadow-sm border-0 rounded-3 border-5">
                        <!-- Image Section -->
                        <div class="relative p-2 pb-0">
                            <img :src="property.image" class="card-img-top rounded-3" alt="Property" />
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
                                {{ property.title }}
                            </h6>
                            <div class="card-title fw-semibold mb-1 text-[13px]">
                                {{ property.subtitle }}
                            </div>
                            <div class="text-xs mb-2 d-flex align-items-center ">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                                    stroke="currentColor" class="h-4 w-4 me-1">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                                </svg>
                                {{ property.location }}
                            </div>

                            <!-- Features -->
                            <div class="d-flex flex-wrap gap-3 text-sm text-secondary">
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Bed.png" alt="" class="h-3" />
                                    {{ property.beds }}
                                </span>
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Bath.png" alt="" class="h-3" />
                                    {{ property.baths }}
                                </span>
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Sqft.png" alt="" class="h-3" />
                                    {{ property.sizes }}
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
const properties = [
    {
        id: 6,
        title: "Live Healthy, Live Well",
        subtitle: "Birla Apple Spire",
        location: "Nayanda Halli, Bangalore",
        beds: "2 & 3",
        baths: "2",
        sizes: "1241 - 1847",
        badges: ["FOR SALE"],
        image: new URL("../assets/images/hfy_img_1.png", import.meta.url).href,
    },
    {
        id: 11,
        title: "A Rare Blend of Luxury, Necessity",
        subtitle: "Suvedha Luxuria",
        location: "Uttarahalli, Bangalore",
        beds: "3",
        baths: "2",
        sizes: "2227",
        badges: ["FOR RENT"],
        image: new URL("../assets/images/hfy_img_2.png", import.meta.url).href,
    },
    {
        id: 9,
        title: "Higher Quality Of Living",
        subtitle: "Suvedha Paradise",
        location: "Srinivasanagar, Bangalore",
        beds: "2 & 3",
        baths: "2",
        sizes: "1075 - 1300",
        badges: ["FOR SALE"],
        image: new URL("../assets/images/hfy_img_3.png", import.meta.url).href,
    },
    {
        id: 8,
        title: "An Irresistible Living Option",
        subtitle: "Suvedha Elegant",
        location: "Banashankari, Bangalore",
        beds: "2 & 3",
        baths: "2",
        sizes: "1026 - 1301",
        badges: ["FOR RENT", "FEATURED"],
        image: new URL("../assets/images/hfy_img_4.png", import.meta.url).href,
    },
];

const badgeColors = (badge) => {
    switch (badge) {
        case "FOR SALE":
            return "bg-black text-white";
        case "FOR RENT":
            return "bg-black text-white";
        case "FEATURED":
            return "bg-yellow-200 text-black";
        default:
            return "bg-black text-black";
    }
};
</script>