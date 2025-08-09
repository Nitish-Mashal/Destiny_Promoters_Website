<template>
    <div class="pt-4">
        <!-- Heading -->
        <div class="flex flex-col items-center justify-center pt-4 text-center">
            <div class="font-semibold text-3xl md:text-5xl lg:text-7xl">
                Featured Categories
            </div>
        </div>

        <!-- Image Cards -->
        <div class="row justify-content-center pt-4 g-4">
            <div v-for="(item, index) in propertyList" :key="index" class="col-12 col-sm-6 col-md-4 col-lg-2 pb-3">
                <div class="position-relative text-center rounded-xl overflow-hidden">
                    <!-- Title & Properties count -->
                    <div class="position-absolute top-0 start-0 text-start p-4 text-[#1A1A1A] z-10">
                        <div class="fw-semibold text-lg md:text-xl">{{ item.title }}</div>
                        <div class="text-sm text-gray-600">
                            {{ item.properties }} Properties
                        </div>
                    </div>

                    <!-- Image -->
                    <img :src="item.image" alt="Category" class="w-100 h-60 object-cover rounded-xl" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const propertyList = [
    {
        title: "Town House",
        properties: 2,
        image: new URL("../assets/images/fc_img_1.png", import.meta.url).href
    },
    {
        title: "Modern Villa",
        properties: 10,
        image: new URL("../assets/images/fc_img_2.png", import.meta.url).href
    },
    {
        title: "Apartment",
        properties: 3,
        image: new URL("../assets/images/fc_img_3.png", import.meta.url).href
    },
    {
        title: "Single Family",
        properties: 5,
        image: new URL("../assets/images/fc_img_4.png", import.meta.url).href
    },
    {
        title: "Office",
        properties: 3,
        image: new URL("../assets/images/fc_img_5.png", import.meta.url).href
    }
]
</script>
  
