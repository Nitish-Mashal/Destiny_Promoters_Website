<template>
  <div>
    <Navbar />
    <!-- Add top padding to account for navbar height -->
    <div class="pt-[63px]">
      <router-view />
    </div>
    <FooterSection />
  </div>
</template>

<script setup>
import Navbar from './pages/Navbar.vue'
import FooterSection from './pages/FooterSection.vue';
</script>

<style>
* {
  font-family: "Roboto", sans-serif;
}
</style>
