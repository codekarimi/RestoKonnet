<script setup>
    import Logo from "../components/Logo.vue"
    import Restaurants from "../components/Restaurants.vue"
    import Footer from "../components/Footer.vue";
    import { RouterLink } from "vue-router";
    import { useRouter } from "vue-router";

    const router = useRouter()
</script>

<template>
    <header class="shadow mb-2">
        <div class="relative flex max-w-screen-xl flex-col overflow-hidden px-4 py-4 md:mx-auto md:flex-row md:items-center">
            <Logo />
            <input type="checkbox" class="peer hidden" id="navbar-open" />
            <label class="absolute top-5 right-7 cursor-pointer md:hidden" for="navbar-open">
                <span class="sr-only">Toggle Navigation</span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
                </svg>
            </label>
            <nav aria-label="Header Navigation" class="peer-checked:mt-8 peer-checked:max-h-56 flex max-h-0 w-full flex-col items-center justify-between overflow-hidden transition-all md:ml-24 md:max-h-full md:flex-row md:items-start">
                <ul class="flex flex-col items-center space-y-2 md:ml-auto md:flex-row md:space-y-0">
                    <li class="text-gray-600 md:mr-12 hover:text-rgreen-100"><RouterLink to="#">Home</RouterLink></li>
                    <li class="text-gray-600 md:mr-12 hover:text-rgreen-100"><RouterLink to="#">About</RouterLink></li>
                    <li class="text-gray-600 md:mr-12 hover:text-rgreen-100"><RouterLink to="#">Support</RouterLink></li>
                    <li class="text-gray-600 md:mr-12 hover:text-rgreen-100">
                        
                        <div class="hs-dropdown relative inline-flex [--trigger:hover]">
                            <button id="hs-dropdown-hover-event" type="button" class="hs-dropdown-toggle py-3 px-4 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border bg-rgreen-100 text-white shadow-sm hover:bg-ryellow disabled:opacity-50 disabled:pointer-events-none">
                              Login
                              <svg class="hs-dropdown-open:rotate-180 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
                            </button>
                        
                            <div class="hs-dropdown-menu transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden min-w-60 bg-white shadow-md rounded-lg p-2 mt-2 after:h-4 after:absolute after:-bottom-4 after:start-0 after:w-full before:h-4 before:absolute before:-top-4 before:start-0 before:w-full" aria-labelledby="hs-dropdown-hover-event">
                              <RouterLink to="/customerSignIn" class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-gray-800 hover:bg-ryellow hover:text-white focus:outline-none focus:bg-gray-100">
                                Customer
                              </RouterLink>
                              <RouterLink to="/vendorSignIn" class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-gray-800 hover:bg-ryellow hover:text-white focus:outline-none focus:bg-gray-100">
                                Vendor
                              </RouterLink>
                              
                            </div>
                        </div>
                    </li>
                </ul>
            </nav>
        </div>
    </header>
    <div class="mt-5 gap-20 flex flex-col md:flex-row items-center justify-between md:mx-auto max-w-screen-xl p-4">
        <div class="md:w-1/2">
            <div class="text-rgreen-100 text-4xl md:text-5xl lg:text-6xl font-poppins font-extrabold">
            Connect with your favorite Restaurant meals.
            </div>
            <div class="w-full text-gray-800 text-base md:text-lg lg:text-2xl font-poppins font-medium my-5">
            Savor dishes born from passion, love, and expertise, all conveniently accessible through our seamless and intuitive platform.
            </div>
            <button class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold lg:text-2xl p-3 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">
                Get Started
            </button>
        </div>
        <div class="md:w-1/2 mt-5 md:mt-0">
            <img src="../img/image 5.png" alt="burger image" class="w-full h-auto">
        </div>
    </div>
    <div class="bg-rgreen-100 mt-3">
        <div class="md:mx-auto max-w-screen-xl p-4">
            <h2 class="text-white text-2xl lg:text-4xl font-poppins font-semibold break-words pt-5 ">Explore Restaurants</h2>
            <Restaurants/>
            
        </div>
        
    </div>
    <section class="flex flex-wrap pb-5 gap-3 justify-center md:mx-auto max-w-screen-xl p-4">
        <div class="text-rgreen-100 md:text-3xl text-xl font-bold font-helvetica break-words my-6">
            Why Choose RestoKonnect
        </div>
        <div class="border-2 rounded-lg border-rgreen-100 w-full overflow-hidden transform hover:scale-105 transition-transform duration-300 ease-in-out">
            <div class="flex justify-between my-7 lg:mx-24 items-center">
                <div class="lg:my-24 lg:mx-2 p-1 px-4">
                    <p class="lg:text-4xl font-semibold break-words text-[#244E2A]">We can get your favorite Meals delivered Right to your door step.</p>
                </div>
                <div class="p-1 px-4">
                    <img class="rounded-lg h-2/3 lg:h-full" src="../img/Frame 52.png" alt="frame1">
                </div>
            </div>
        </div>
        <div class="border-2 rounded-lg border-rgreen-100 w-full overflow-hidden transform hover:scale-105 transition-transform duration-300 ease-in-out">
            <div class="flex justify-between my-7 lg:mx-24 items-center">
                <div class="p-1">
                    <img class="rounded-lg h-2/3 lg:h-full" src="../img/Frame 52 (1).png" alt="frame1">
                </div>
                <div class="lg:my-24 lg:mx-2 p-1">
                    <p class="lg:text-4xl font-semibold break-words text-[#244E2A]">Get your to connect with the best Food Vendors in Nigeria.</p>
                </div>
            </div>
        </div>
        <div class="border-2 rounded-lg border-rgreen-100 w-full overflow-hidden transform hover:scale-105 transition-transform duration-300 ease-in-out">
            <div class="flex justify-between my-7 lg:mx-24 items-center">
                <div class="lg:my-24 lg:mx-2 p-1">
                    <p class="lg:text-4xl font-semibold break-words text-[#244E2A]">Affordable Delivery fees and 500N off on your first purchase.</p>
                </div>
                <div class="p-1">
                    <img class="rounded-lg h-2/3 lg:h-full" src="../img/image 8.png" alt="frame1">
                </div>
            </div>
        </div>
        <div class="border-2 rounded-lg border-rgreen-100 w-full overflow-hidden transform hover:scale-105 transition-transform duration-300 ease-in-out">
            <div class="flex justify-between my-7 lg:mx-24 items-center">
                <div class="p-1">
                    <img class="rounded-lg h-2/3 lg:h-full" src="../img/Frame 52 (2).png" alt="frame1">
                </div>
                <div class="lg:my-24 lg:mx-2 p-1">
                    <p class="lg:text-4xl font-semibold break-words text-[#244E2A]">Swift and timely delivery on every meal you order. </p>
                </div>
            </div>
        </div>
    </section>
    <section class="bg-rgreen-100">
        <div class="md:mx-auto max-w-screen-xl">
            <div class="flex justify-center py-8 px-2 flex-wrap items-center">
                <h2 class="text-white break-words md:text-3xl font-bold text-lg">Register to become one of RestoKonnect Team </h2>
            </div>
            <div class="flex justify-around p-2 gap-2">
                <div class="transform hover:scale-105 transition-transform duration-300 ease-in-out">
                    <img src="../img/food_vendor.png" alt="food_vendor">
                    <p class="text-white lg:text-2xl font-semibold lg:ml-20 lg:my-6 ml-10  hover:text-ryellow transition duration-300 ease-in-out">Vendor</p>
                </div>
                <div class="transform hover:scale-105 transition-transform duration-300 ease-in-out">
                    <img src="../img/Dispatch_rider.png" alt="disptch_rider">
                    <p class="text-white lg:text-2xl font-semibold lg:ml-20 lg:my-6 ml-10  hover:text-ryellow transition duration-300 ease-in-out">Delivery</p>
                </div>
            </div>  
        </div>
        
    </section>
    <footer class="md:mx-auto max-w-screen-xl p-4">
       <Footer/>
    </footer>
</template>