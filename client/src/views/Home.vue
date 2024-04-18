<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import Footer2 from "../components/Footer2.vue"
    import Restaurants from "../components/Restaurants.vue"
    import { useAuthStore  } from "../stores/AuthStore";
    import { ref } from "vue";

    const currentUser = ref({})

    const authStore = useAuthStore();
    currentUser.value = authStore.currentUser
    
</script>

<template>
    <section class="">
        <div class="bg-rgreen-100 border">
            <RestoNav :user="currentUser"/>
            <div class="my-24">
                <div class="flex justify-center mb-5">
                    <p class="text-4xl text-white font-extrabold break-words">Welcome! {{ currentUser.name }}</p>
                </div>
                <div class="flex justify-center">
                    <div class="flex gap-2 bg-white p-3 rounded-3xl w-96">
                        <button>
                            <img src="../img/icons/search.png" alt="">
                        </button>
                        <input type="text" name="search" id="search" class="p-1" placeholder="search">
                    </div>
                </div>
            </div>     
        </div>
        <div class="md:mx-auto max-w-screen-xl p-4">
            <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words">Explore Restaurants</h2>
            <Restaurants/>
            
        </div>
        <div class="bg-rgreen-100 border">
            <Footer2/>
        </div>
    </section>
</template>