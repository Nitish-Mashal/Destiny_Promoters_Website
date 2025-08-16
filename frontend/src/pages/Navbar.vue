<template>
    <header class="absolute top-0 left-0 w-full z-50 bg-transprent">
        <div class="max-w-7xl mx-auto">
            <nav class="flex items-center justify-between px-[30px] sm:px-[150px]  relative">
                <!-- Logo -->
                <div class="flex items-center space-x-2">
                    <router-link to="/">
                        <img src="../assets/images/DP_Logo.png" alt="Logo" class="h-12" />
                    </router-link>
                </div>

                <!-- Desktop Navigation -->
                <div
                    class="hidden md:flex items-center justify-between flex-grow font-regular mt-2 ml-4 cursor-pointer">
                    <!-- Left nav links -->
                    <ul class="flex items-center space-x-8">
                        <li>
                            <router-link to="/" class="text-gray-800  no-underline" custom v-slot="{ navigate, href }">
                                <a :href="href" @click="navigate" class="no-underline text-gray-800">
                                    Home
                                </a>
                            </router-link>
                        </li>

                        <li>
                            <router-link to="/Listing" class="text-gray-800  no-underline" custom
                                v-slot="{ navigate, href }">
                                <a :href="href" @click="navigate" class="no-underline text-gray-800">
                                    Listing
                                </a>
                            </router-link>
                        </li>
                        <li>
                            <router-link to="/AboutUs" class="text-gray-800  no-underline" custom
                                v-slot="{ navigate, href }">
                                <a :href="href" @click="navigate" class="no-underline text-gray-800">
                                    About Us
                                </a>
                            </router-link>
                        </li>
                        <li class="relative group">
                            <div href="#" class="text-gray-800  no-underline flex items-center space-x-2">
                                Services
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20"
                                    fill="currentColor">
                                    <path fill-rule="evenodd"
                                        d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                                        clip-rule="evenodd" />
                                </svg>
                            </div>
                            <ul class="absolute hidden group-hover:block bg-white border rounded shadow-md w-40 z-50">
                                <li>
                                    <router-link to="/construction" custom v-slot="{ navigate, href }">
                                        <a :href="href" @click="navigate"
                                            class="block py-2 text-gray-800  no-underline">
                                            Construction
                                        </a>
                                    </router-link>
                                </li>
                                <li>
                                    <router-link to="/Interiors" custom v-slot="{ navigate, href }">
                                        <a :href="href" @click="navigate"
                                            class="block py-2 text-gray-800  no-underline">
                                            Interiors
                                        </a>
                                    </router-link>
                                </li>
                            </ul>

                        </li>
                        <li>
                            <router-link to="/ContactUS" custom v-slot="{ navigate, href }">
                                <a :href="href" @click="navigate" class="block py-2 text-gray-800  no-underline">
                                    Contact
                                </a>
                            </router-link>
                        </li>
                    </ul>

                    <!-- Right nav icons -->
                    <ul class="flex items-center space-x-4 ml-auto">
                        <li class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                            </svg>
                            <span>+68 685 88666</span>
                        </li>
                        <li>
                            <button>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1"
                                    stroke="currentColor" class="w-5 h-5">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                </svg>
                            </button>
                        </li>
                    </ul>
                </div>

                <!-- Mobile Toggle + Menu Wrapper -->
                <div class="md:hidden relative" ref="menuWrapper">
                    <button @click.stop="toggleMenu">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>

                    <!-- Mobile Menu -->
                    <transition name="fade-slide">
                        <ul v-if="isOpen" ref="mobileMenu"
                            class="absolute right-0 mt-2 bg-white w-60 shadow-lg rounded-md px-6 py-4 space-y-2 font-regular z-50">
                            <li>
                                <router-link to="/" custom v-slot="{ navigate, href }">
                                    <a :href="href" @click="navigate" class="block text-gray-800  no-underline">
                                        Home
                                    </a>
                                </router-link>
                            </li>

                            <li>
                                <router-link to="/Listing" custom v-slot="{ navigate, href }">
                                    <a :href="href" @click="navigate" class="block text-gray-800  no-underline">
                                        Listings
                                    </a>
                                </router-link>
                            </li>

                            <li>
                                <router-link to="/AboutUs" custom v-slot="{ navigate, href }">
                                    <a :href="href" @click="navigate" class="block text-gray-800  no-underline">
                                        About Us
                                    </a>
                                </router-link>
                            </li>

                            <li>
                                <router-link to="/construction" custom v-slot="{ navigate, href }">
                                    <a :href="href" @click="navigate" class="block text-gray-800  no-underline">
                                        Construction
                                    </a>
                                </router-link>
                            </li>

                            <li>
                                <router-link to="/Interiors" custom v-slot="{ navigate, href }">
                                    <a :href="href" @click="navigate" class="block text-gray-800  no-underline">
                                        Interiors
                                    </a>
                                </router-link>
                            </li>

                            <li>
                                <router-link to="/ContactUS" custom v-slot="{ navigate, href }">
                                    <a :href="href" @click="navigate" class="block py-2 text-gray-800  no-underline">
                                        Contact
                                    </a>
                                </router-link>
                            </li>

                            <li class="flex items-center space-x-2">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                                </svg>
                                <span>+68 685 88666</span>
                            </li>
                            <li>
                                <button>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                    </svg>
                                </button>
                            </li>
                        </ul>
                    </transition>
                </div>
            </nav>
        </div>
    </header>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'

const isOpen = ref(false)
const menuWrapper = ref(null)

const toggleMenu = async () => {
    isOpen.value = !isOpen.value
    await nextTick() // wait for DOM update before attaching outside listener
}

const handleClickOutside = (event) => {
    if (isOpen.value && menuWrapper.value && !menuWrapper.value.contains(event.target)) {
        isOpen.value = false
    }
}

onMounted(() => {
    document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
    transition: all 0.3s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
    opacity: 0;
    transform: translateY(-10px);
}
</style>