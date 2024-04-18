<script setup>
    import RestoNav from "../components/RestoNav.vue"
    import Footer2 from "../components/Footer2.vue"
    import Cart from "../components/Cart.vue"
    import Cust_SignIn from "./Cust_SignIn.vue";
    import { onMounted, ref } from "vue";
    import { useAuthStore  } from "../stores/AuthStore";
    import axios from "axios";
    import { useRoute } from 'vue-router';

    const authStore = useAuthStore();


    const restaurant = ref({});
    const items = ref([]);
    const cartItems = ref([])
    const customerId = ref("")
    const vendorId = ref("")
    const route = useRoute();
    const currentPath = ref('');
    const total_amount = ref()
    const baseUrl = ref('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1')
    const currentUser = ref(authStore.currentUser)

    customerId.value = localStorage.getItem('customer_id')
    vendorId.value = localStorage.getItem('vendor_id')
    currentPath.value = route.path;    

    // calculates total amount
    const calculateTotalAmount = () => {
        total_amount.value = 0
        for (let i = 0; i < cartItems.value.length; i++) {
            total_amount.value += (cartItems.value[i].item_price * cartItems.value[i].count)
        }
        return total_amount.value
    }
      
    // retrieves a details of a particular restaurant
    const get_restaurants = async () => {
    try {
        // const token = localStorage.getItem('token');
        // const headers = { 'Authorization': `Bearer ${token}` };

        // Use axios.get to make a GET request
        const response = await axios.get(`${baseUrl.value}/${currentPath.value}`);
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

    // creates an item in the cart
    const add_to_cart = async (item_name, item_price, count=1) => {
        try {
            const formData = new FormData()
            
            formData.append("item_name", item_name)
            formData.append("item_price", item_price)
            formData.append("count", count)

            if (customerId.value != null) {
                formData.append("customer_id", customerId.value)
                const response = await axios.post(`${baseUrl.value}/${currentPath.value}/cart_items`, formData);
            } else if (vendorId.value != null) {
                formData.append("vendor_id", vendorId.value)
                const response = await axios.post(`${baseUrl.value}/${currentPath.value}/cart_items`, formData);
                console.log(response.data)
            }
            alert("added to cart sucessfully")
            get_cart_items()

        } catch(error) {
            alert(error)
        }
    }

    // retrieves all customer items added to a cart
    const get_cart_items = async () => {
        try {
            const queryParams = {};

            if (customerId.value != null) {
                queryParams.customer_id = customerId.value;
                const response = await axios.get(`${baseUrl.value}/${currentPath.value}/cart_items`, {
                    params: queryParams});
                cartItems.value = response.data
            } else if (vendorId.value != null) {
                queryParams.vendor_id = vendorId.value;
                const response = await axios.get(`${baseUrl.value}/${currentPath.value}/cart_items`, {
                    params: queryParams});
                cartItems.value = response.data
            }
            calculateTotalAmount()

        } catch(error) {
            alert(error)
        }
    }

    // deletes an item fromthe cart
    const remove_from_cart = async (cart_item_id) => {
        try {
            const response = await axios.delete(`${baseUrl.value}/cart_items/${cart_item_id}`)
            alert("deleted successfully")
            get_cart_items()
        } catch(error) {
            alert(error.response.message)
        }
    }

    // creates an order for a aprticular restaurant
    const place_order = async () =>  {
        try {
            const orderData = {
                items: cartItems.value,
                total_amount: total_amount.value,
                customer: currentUser.value,
            }
            const response = await axios.post(`${baseUrl.value}${currentPath.value}/orders`, orderData);
            alert("Order Sent Successfully")
        }catch(error){
            alert(error)
            console.log(error)

        }
    }

    onMounted( () => {
        currentPath.value = route.path;
        get_restaurants() 
        get_items()
        get_cart_items()
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
            <div class="hidden lg:block">
                <Cart :currentPath="currentPath"/>
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

        <!-- <div class="lg:mx-60 mx-5">
            <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words mt-5">All Menu</h2>
            <div class="mt-5 relative lg:grid lg:grid-cols-3 justify-center pb-5 lg:gap-32 w-1120px md:w-85vw overflow-x-auto flex flex-wrap">
                <div  v-for="item in items" class="w-96 h-96 border-2 border-rgreen-100 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl">
                    <img class="w-full h-3/4 transform hover:scale-105 transition-transform duration-300 ease-in-out" :src="item.image" alt="Card Image">
                    <div class="px-2 py-1 bg-white flex items-center justify-between">
                        <span class="font-bold lg:text-xl mb-2 w-auto mt-3">{{ item.name }}</span>
                        <div class="flex items-center gap-3">
                            <button @click="item.count++" class="text-xl">+</button>
                            <div class="rounded-full bg-[#DAEBDD] w-10 h-10 flex justify-center items-center">
                                <span>{{ item.count }}</span>
                            </div>
                            <button @click="item.count--" class="text-2xl">-</button>
                        </div>
                    </div>
                    <div class="flex justify-between items-center px-3 pb-1">
                        <span class="text-rgreen-100">Price - N{{ item.price }}</span>
                        <button @click="add_to_cart(item.name, item.price, item.count)" class="bg-rgreen-100 hover:text-ryellow text-white font-semibold p-1 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out" >
                            Add to cart
                        </button>
                    </div> 
                </div>
            </div>
           
        </div> -->
        <div class="bg-rgreen-100 border">
            <Footer2/>
        </div>
    </div>
    <div v-else="authStore.isAuthenticated">
        <Cust_SignIn/>
    </div>
</template>