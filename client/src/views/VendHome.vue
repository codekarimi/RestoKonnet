<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import Footer2 from "../components/Footer2.vue"
    import Cust_SignIn from "./Cust_SignIn.vue";
    import { onMounted, ref } from "vue";
    import { useAuthStore  } from "../stores/AuthStore";
    import axios from "axios";
    import { useRoute } from 'vue-router';

    const authStore = useAuthStore();


    const restaurant = ref({});
    const items = ref([]);
    const vendorId = ref("")
    const route = useRoute();
    const currentPath = ref('');
    const baseUrl = ref('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1')
    const currentUser = ref(authStore.currentUser)

    vendorId.value = localStorage.getItem('vendor_id')
    currentPath.value = route.path;    


    // retrieves a details of a particular restaurant
    const get_restaurants = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/${currentPath.value}/restaurants`);
        restaurant.value = response.data
        
        } catch (error) {
            console.error(error);
        }
    }

    // retrives all customers item
    const get_items = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/${currentPath.value}/items`);
        items.value = response.data
        
        } catch (error) {
            console.error(error);
        }
    }


    onMounted( () => {
        currentPath.value = route.path;
        get_restaurants() 
        get_items()
    });
    
</script>

<template>
    <div v-if="authStore.isAuthenticated">
        <div class="bg-rgreen-100 border">
            <RestoNav :user="currentUser" />
        </div>
        <div class="flex flex-wrap justify-center  lg:justify-between md:mx-auto max-w-screen-xl p-4">
            <div class="lg:w-1/2" >
                <div class="w-96 h-96 lg:h-96 lg:w-full rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl">
                    <img class="w-full h-full" :src="restaurant.image" alt="Card Image">
                </div>
                <div class="px-2 py-4 bg-white">
                    <h1 class="font-extrabold lg:text-4xl mb-2 w-auto mt-3">{{ restaurant.name}}</h1>
                    <p class="text-xl text-gray-600">{{ restaurant.address }}</p>
                </div>
            </div>
        </div>
        <section class="bg-white py-12 text-gray-700 sm:py-16 lg:py-20">
            <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
                <div class="mx-auto max-w-md text-center">
                    <h2 class="font-serif text-2xl font-bold sm:text-3xl">Available Delicacies</h2>
                </div>

                <div class="mt-10 grid grid-cols-2 gap-6 sm:grid-cols-4 sm:gap-4 lg:mt-16">
      
                    <article v-for="item in items" class="relative flex flex-col overflow-hidden rounded-lg border">
                        <div class="aspect-square overflow-hidden">
                            <img class="h-full w-full object-cover transition-all duration-300 group-hover:scale-125" :src="item.image" alt="item image" />
                        </div>
                        <div class="my-4 mx-auto flex w-10/12 flex-col items-start justify-between">
                            <div class="mb-2 flex">
                                <p class="mr-3 text-sm font-semibold">{{ item.price }}</p>
                            </div>
                            <h3 class="mb-2 text-sm text-gray-400">{{ item.name }}</h3>
                        </div>
                        <button @click="add_to_cart(item.name, item.price)" class="group mx-auto mb-2 flex h-10 w-10/12 items-stretch overflow-hidden rounded-md text-gray-600">
                            <div class="flex w-full items-center justify-center bg-gray-100 text-xs uppercase transition group-hover:bg-ryellow group-hover:text-white">Add</div>
                            <div class="flex items-center justify-center bg-gray-200 px-5 transition group-hover:bg-yellow-600 group-hover:text-white">+</div>
                        </button> 
                    </article>
                </div>
            </div>
        </section>

        <div class="bg-rgreen-100 border">
            <Footer2/>
        </div>
    </div>
    <div v-else="authStore.isAuthenticated">
        <Cust_SignIn/>
    </div>
</template>cd 