<template>
    <div class="p-5">
        <footer class="bg-gray-50 rounded-2xl shadow-sm">
            <!-- Top -->
            <div class="flex flex-col md:flex-row items-center justify-between px-8 py-6">
                <!-- Logo -->
                <div class="flex items-center">
                    <img src="../assets/images/DP_Logo.png" alt="Destiny Promoters"
                        class="h-[60px] ml-4 md:ml-10 mt-2" />
                </div>

                <!-- Social -->
                <div class="flex items-center space-x-4 mt-4 md:mt-0">
                    <span class="font-medium text-sm">Follow Us</span>
                    <i class="fab fa-facebook-f text-sm cursor-pointer hover:text-gray-500"></i>
                    <i class="fab fa-twitter text-sm cursor-pointer hover:text-gray-500"></i>
                    <i class="fab fa-instagram text-sm cursor-pointer hover:text-gray-500"></i>
                    <i class="fab fa-linkedin-in text-sm cursor-pointer hover:text-gray-500"></i>
                </div>
            </div>

            <hr class="border-gray-400" />

            <!-- Main Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-6 gap-8 px-8 py-6">
                <!-- Subscribe -->
                <div class="col-span-1">
                    <h4 class="font-semibold mb-3 text-sm">Subscribe</h4>
                    <div class="flex items-center mb-3">
                        <input type="email" placeholder="Your e-mail"
                            class="w-10/12 md:w-28 lg:w-24 xl:w-24 h-10 px-3 text-sm border border-gray-300 rounded-l-full outline-none focus:outline-none focus:ring-0" />
                        <button
                            class="bg-black text-white px-4 h-10 text-sm rounded-r-full flex items-center justify-center space-x-1">
                            <span>Send</span>
                            <span>→</span>
                        </button>
                    </div>
                    <p class="text-sm text-gray-500 pb-2">
                        Subscribe to our newsletter to receive our weekly feed.
                    </p>
                </div>

                <!-- Discover -->
                <div>
                    <h4 class="font-semibold mb-3 text-sm ml-8">Discover</h4>
                    <ul class="space-y-2 text-sm text-black">
                        <li>Miami</li>
                        <li>New York</li>
                        <li>Chicago</li>
                        <li>Florida</li>
                        <li>Los Angeles</li>
                        <li>San Diego</li>
                    </ul>
                </div>

                <!-- Quick Links -->
                <div>
                    <h4 class="font-semibold mb-3 text-sm ml-8">Quick Links</h4>
                    <ul class="space-y-2 text-sm text-black">
                        <li>About</li>
                        <li>Contact</li>
                        <li>FAQ's</li>
                        <li>Blog</li>
                        <li>Pricing Plans</li>
                        <li>Privacy Policy</li>
                        <li>Terms & Conditions</li>
                    </ul>
                </div>

                <!-- Contact Us -->
                <div>
                    <h4 class="font-semibold mb-3 text-sm">Contact Us</h4>
                    <p class="text-sm text-black">hi@justhome.com</p>
                    <p class="text-sm text-black">(123) 456-7890</p>
                </div>

                <!-- Our Address -->
                <div>
                    <h4 class="font-semibold mb-3 text-sm">Our Address</h4>
                    <p class="text-sm text-black leading-snug">
                        99 Fifth Avenue, 3rd Floor<br />
                        San Francisco, CA 1980
                    </p>
                </div>

                <!-- Get the App -->
                <div>
                    <h4 class="font-semibold mb-3 text-sm">Get the app</h4>
                    <div class="space-y-3">
                        <button
                            class="bg-black text-white px-4 py-2 rounded-lg flex items-center space-x-2 w-full text-sm">
                            <i class="fab fa-apple text-lg"></i>
                            <span class="text-left">
                                <span class="block leading-none">Download on the</span>
                                <span class="font-semibold">Apple Store</span>
                            </span>
                        </button>
                        <button
                            class="bg-black text-white px-4 py-2 rounded-lg flex items-center space-x-2 w-full text-sm">
                            <i class="fab fa-google-play text-lg"></i>
                            <span class="text-left">
                                <span class="block leading-none">Get it on</span>
                                <span class="font-semibold">Google Play</span>
                            </span>
                        </button>
                    </div>
                </div>
            </div>

            <hr class="border-gray-200" />

            <!-- Bottom -->
            <div
                class="flex flex-col md:flex-row items-center px-8 py-4 text-sm text-black gap-10 md:gap-40">
                <span>Copyright © 2025. Destiny Promoters</span>
                <span>Powered By: Quantumberg Technologies Pvt Ltd</span>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: "FooterSection",
};
</script>

<style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css");
</style>