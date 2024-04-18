<script setup>
    import { useRouter } from "vue-router";
    import { onMounted, ref } from "vue";
    import axios from "axios";
    

    const router = useRouter();
    const {currentPath} = defineProps(['currentPath'])
    console.log(currentPath)

    const cartItems = ref([])
    const customerId = ref("")
    const vendorId = ref("")
    const total_amount = ref()
    const baseUrl = ref('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1')
    

    

    customerId.value = localStorage.getItem('customer_id')
    vendorId.value = localStorage.getItem('vendor_id')
    

    const calculateTotalAmount = () => {
        total_amount.value = 0
        for (let i = 0; i < cartItems.value.length; i++) {
            total_amount.value += (cartItems.value[i].item_price * cartItems.value[i].count)
        }
        return total_amount.value
    }


    // retrieves all customer items added to a cart
    const get_cart_items = async () => {
        try {
            const queryParams = {};
            if (customerId.value != null) {
                queryParams.customer_id = customerId.value;
                const response = await axios.get(`${baseUrl.value}/${currentPath}/cart_items`, {
                    params: queryParams});
                cartItems.value = response.data
            } else if (vendorId.value != null) {
                queryParams.vendor_id = vendorId.value;
                const response = await axios.get(`${baseUrl.value}/${currentPath}/cart_items`, {
                    params: queryParams});
                cartItems.value = response.data
            }
            calculateTotalAmount()

        } catch(error) {
            alert(error)
            console.log(error)
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
            const response = await axios.post(`${baseUrl.value}${currentPath}/orders`, orderData);
            alert("Order Sent Successfully")
        }catch(error){
            alert(error)
            console.log(error)

        }
    }

    onMounted( () => {        
        get_cart_items()
    })


</script>

<template>
    <div class="bg-[#F2FCF2] py-12 sm:py-16 lg:py-20">
        <div class="mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-center">
                <h1 class="text-2xl font-semibold text-gray-900">Your Cart</h1>
            </div>
        
            <div class="mx-auto mt-8 max-w-2xl md:mt-12">
                <div class="bg-white shadow">
                    <div class="px-4 py-6 sm:px-8 sm:py-10">
                        <div class="flow-root">
                            <ul  v-for="cart_item in cartItems" class="-my-8">
                                <li class="flex flex-col space-y-3 py-6 text-left sm:flex-row sm:space-x-5 sm:space-y-0">
                                    <div class="relative flex flex-1 flex-col justify-between">
                                        <div class="sm:col-gap-5 sm:grid sm:grid-cols-2">
                                            <div class="pr-8 sm:pr-5">
                                                <p class="text-base font-semibold text-gray-900">{{ cart_item.item_name }}</p>
                                                <p class="mx-0 mt-1 mb-0 text-sm text-gray-400">{{ cart_item.item_price }}</p>
                                            </div>
                                        
                                            <div class="mt-4 flex items-end justify-between sm:mt-0 sm:items-start sm:justify-end">
                                                <div class="sm:order-1">
                                                    <div class="mx-auto flex h-8 items-stretch text-gray-600">
                                                        <button @click="cart_item.count--, calculateTotalAmount()" class="flex items-center justify-center rounded-l-md bg-gray-200 px-4 transition hover:bg-black hover:text-white">-</button>
                                                             <div class="flex w-full items-center justify-center bg-gray-100 px-4 text-xs uppercase transition">{{ cart_item.count }}</div>
                                                        <button @click="cart_item.count++, calculateTotalAmount()" class="flex items-center justify-center rounded-r-md bg-gray-200 px-4 transition hover:bg-black hover:text-white">+</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    
                                        <div class="flex justify-end sm:bottom-0 sm:top-auto">
                                            <button @click="remove_from_cart(cart_item.id)" type="button" class="flex rounded p-2 text-center text-gray-500 transition-all duration-200 ease-in-out focus:shadow hover:text-gray-900">
                                                <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class=""></path>
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    
                        <div class="mt-6 flex items-center justify-between">
                            <p class="text-sm font-medium text-gray-900">Total</p>
                            <p class="text-2xl font-semibold text-gray-900"><span class="text-xs font-normal text-gray-400">Naira</span>{{ total_amount }}</p>
                        </div>
                    
                        <div class="mt-6 text-center">
                            <button @click="place_order()" type="button" class="group inline-flex w-full items-center justify-center rounded-md bg-rgreen-100 px-6 py-4 text-lg font-semibold text-white transition-all duration-200 ease-in-out focus:shadow hover:bg-ryellow">
                                    Place Order
                                <svg xmlns="http://www.w3.org/2000/svg" class="group-hover:ml-8 ml-4 h-6 w-6 transition-all" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>