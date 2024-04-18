<script setup>
    import Logo from "../components/Logo.vue"
    import axios from "axios";
    import { onMounted, ref } from "vue";
    import { useRoute } from "vue-router";

    const currentPath = ref("")
    const routeParams = ref("")
    const restaurantId = ref("")
    const restaurant = ref({})
    const restoItems = ref([])
    const route = useRoute()
    const orders = ref([])


    currentPath.value = route.path
    routeParams.value = route.params


    // get Restaurant ID
    const getRestaurantId = async () => {
        try {
            const result = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1${currentPath.value}`);
            restaurantId.value = result.data.id
            restaurant.value = result.data

        } catch(error) {
            alert("No Restaurant Available\n\nCreate a New Resaturant")
            console.log(error)
        }
    }

    // Delete Restaurant
    const deleteRestaurant = async () => {
        try {
            const result = await axios.delete(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}`);
            alert("Restaurant Deleted Successfully!")

        } catch(error) {
            alert("No Resatuarant Exist")
            console.log(error)
        }
    }


    // Submit form for Restaurant
    const restaurantData = ref({
        name: '',
        address: '',
    });

    const restoImage = ref();
   
    const restoHandleFileChange = (event) => {
      restoImage.value = event.target.files[0];
    };

    const submitRestoForm = async () => {
        try {
            const formData = new FormData();
            formData.append('name', restaurantData.value.name)
            formData.append('address', restaurantData.value.address)
            formData.append('image', restoImage.value)

            const response = await axios.post(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1${currentPath.value}`, formData);
            alert("upload successful")

        } catch (error) {
            alert(error)
            console.error('Upload Failed:', error);
        }
    };

    // Submit form for Items
    const itemData = ref({
        name: '',
        price: '',
    });

    const itemImage = ref();

    const itemHandleFileChange = (event) => {
      itemImage.value = event.target.files[0];
    };
    const submitItemForm = async () => {
        try {
            const formData = new FormData();
            formData.append('name', itemData.value.name)
            formData.append('price', itemData.value.price)
            formData.append('image', itemImage.value)

            const response = await axios.post(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}/items`, formData);
            alert("upload successful")
            getRestoItems();

        } catch (error) {
            console.error('Upload Failed:', error);
        }
    };

    // update Restaurant Name
    const updateRestoName = async () => {
        try {
            const formData = new FormData();
            formData.append('name', restaurantData.value.name)

            const response = await axios.put(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}`, formData);
            alert("update successful")

        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };
     // update Restaurant Address
     const updateRestoAddress = async () => {
        try {
            const formData = new FormData();
            formData.append('address', restaurantData.value.address)

            const response = await axios.put(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}`, formData);
            alert("update successful")

        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };

     // update Restaurant Address
     const updateRestoImage= async () => {
        try {
            const formData = new FormData();
            formData.append('image', restoImage.value)

            const response = await axios.put(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}/image`, formData);
            alert("update successful")

        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };

    // get Restaurant items
    const getRestoItems = async () => {
        try {
            console.log(restaurantId.value)
            const response = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}/items`);
            restoItems.value = response.data

        } catch (error) {
            alert("No Item Available")
            console.error('Failed to get items:', error);
        }
    };


    // update item Name
    const updateItemName = async (itemId) => {
        try {
            const formData = new FormData();
            formData.append('name', itemData.value.name)

            const response = await axios.put(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/items/${itemId}`, formData);
            alert("update successful")
            getRestoItems();

        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };
     // update Item Price
     const updateItemPrice = async (itemId) => {
        try {
            const formData = new FormData();
            formData.append('price', itemData.value.price)

            const response = await axios.put(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/items/${itemId}`, formData);
            alert("update successful")
            getRestoItems();


        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };

     // update Item Image
     const updateItemImage= async (itemId) => {
        try {
            const formData = new FormData();
            formData.append('image', itemImage.value)

            const response = await axios.put(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/items/${itemId}/image`, formData);
            alert("update successful")
            getRestoItems();

        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };

    // Deletes an item
    const deleteItem= async (itemId) => {
        try {
            const response = await axios.delete(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/items/${itemId}`);
            alert("Deleted successfully")
            getRestoItems();

        } catch (error) {
            alert(error)
            console.error('Update Failed:', error);
        }
    };

    // gets orders of a particular restaurant
    const getOrders = async () => {
        try {
            const response = await axios.get(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/restaurants/${restaurantId.value}/orders`);
            orders.value = response.data
        } catch(error) {
            console.log(error)
            alert(error)
        }
    }

    // deletes a particular order
    const deleteOrder = async (orderId) => {
        try {
            const response = await axios.delete(`https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/orders/${orderId}`);
            getOrders()            

        } catch(error) {
            console.log(error)
            alert(error)
        }
    }

    onMounted(async () => {
        await getRestaurantId();
        getRestoItems();
        getOrders()
    });

</script>

<template>
    <section class="bg-[#F2FCF2] lg:p-16 p-2">
        <div>
            <Logo/>
        </div>
        <div class="lg:grid lg:grid-cols-2 justify-between ">
            <div>
                <div class="my-10">
                    <h1 class="text-3xl font-bold">Your Restaurant</h1>
                    <span>Fill in your resturant details</span>
                </div>
                <div class="flex justify-center">
                    <form @submit.prevent="submitRestoForm" action="" class=" w-4/5">
                        <div class="">
                            <label for="name" class="block text-xl font-semibold">Name of Restaurant</label>
                            <input v-model="restaurantData.name" type="text" name="name" id="name" class="w-full border-2 rounded p-3" :placeholder="restaurant.name" required>
                            <div class="flex justify-end">
                                <button @click="updateRestoName()" class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
                                    Update
                                </button>
                            </div>
                        </div>
                        <div class="">
                            <label for="image" class="block text-xl font-semibold">Restaurant Wallpaper</label>
                            <input v-bind="restoImage" @change="restoHandleFileChange" type="file" name="image" id="image" class="w-full border-2 rounded p-3" required>
                            <div class="flex justify-end">
                                <button @click="updateRestoImage" class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
                                    Update
                                </button>
                            </div>
                        </div>
                        <div class="">
                            <label for="address" class="block text-xl font-semibold">Restaurant Address</label>
                            <input v-model="restaurantData.address" type="text" name="address" id="address" class="w-full border-2 rounded p-3" :placeholder="restaurant.address" required>
                            <div class="flex justify-end">
                                <button @click="updateRestoAddress()" class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
                                    Update
                                </button>
                            </div>
                        </div>
                        <button type="submit" class="w-full text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center mt-5">Upload</button>
                    </form>
                </div>
                <button @click="deleteRestaurant()" class="bg-rgreen-100 hover:bg-ryellow text-white font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
                    Delete Restaurant
                </button>
            </div>
            <div>
                <div class="my-10">
                    <h1 class="text-3xl font-bold">Your Menu</h1>
                    <span>Upload images of your meals and add a description.</span>
                </div>
                <div class="flex justify-center">
                    <form @submit.prevent="submitItemForm" action="" class=" w-4/5">
                        <div class=" mb-5">
                            <label for="itemName" class="block text-xl font-semibold">Name of Food</label>
                            <input v-model="itemData.name" type="text" name="itemName" id="itemName" class="w-full border-2 rounded p-3" placeholder="Name of Item" required>
                        </div>
                        <div class=" mb-5">
                            <label for="itemImage" class="block text-xl font-semibold">Image of Food</label>
                            <input @change="itemHandleFileChange" type="file" name="itemImage" id="itemImage" class="w-full border-2 rounded p-3" required> 
                        </div>
                        <div class=" mb-5">
                            <label for="price" class="block text-xl font-semibold">Price</label>
                            <input v-model="itemData.price" type="text" name="price" id="price" class="w-full border-2 rounded p-3" placeholder="Item Price" required>
                        </div>
                        <button type="submit" class="w-full text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center mt-5">Upload</button>
                    </form>
                    
                </div>
            </div>
        </div>
        <div class="lg:grid lg:grid-cols-2">
            <div>
                <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words lg:ml-10 mt-10">Menu List</h2>
                <div class="lg:mt-10 mt-5 justify-center relative lg:mx-10 lg:grid lg:grid-cols-2 pb-5 w-1120px md:w-85vw overflow-x-auto rounded-lg p-3 flex flex-wrap">
                    <div v-for="item in restoItems" :key="item.id" class=" w-80 h-80 border border-rgreen-100 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl transform hover:scale-105 transition-transform duration-300 ease-in-out">
                        <img class="w-full h-1/3" :src="item.image" alt="Card Image">
                        <input @change="itemHandleFileChange" type="file" name="" id="" class="mx-2" required>
                        <button @click="updateItemImage(item.id)" class="mx-2 my-2 text-sm bg-rgreen-100 hover:bg-ryellow text-white py-1 px-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">update</button>
                        <div class="bg-white">
                            <input v-model="itemData.name" type="text" class="mx-2 border text-sm p-1" :placeholder="item.name" required>
                            <button @click="updateItemName(item.id)" class="my-2 ml-2 text-sm bg-rgreen-100 hover:bg-ryellow text-white py-1 px-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">update</button>
                            <input v-model="itemData.price" class="text-sm p-1 border mx-2" :placeholder="item.price" required>
                            <button @click="updateItemPrice(item.id)" class="my-2 ml-2 text-sm bg-rgreen-100 hover:bg-ryellow text-white py-1 px-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">update</button>
                        </div>
                        <button @click="deleteItem(item.id)" class="my-2 ml-2 text-sm bg-rgreen-100 hover:bg-ryellow text-white py-1 px-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">delete item</button>
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-rgreen-100 text-2xl lg:text-4xl font-poppins font-semibold break-words lg:ml-10 mt-10">Latest Orders</h2>
                <div v-for="order in orders" :key="order.id" class="bg-gray-100 p-4 my-4 rounded-lg shadow-md">
                    <p class="text-lg font-semibold">{{ order.customer.name }}</p>
                    <p class="text-gray-600">{{ order.customer.address }}</p>
                    <p class="text-gray-600">{{ order.customer.phone_no }}</p>
                    <ul class="list-disc ml-4 mt-2">
                        <li v-for="item in order.items" :key="item.id" class="flex justify-between">
                            <span class="font-semibold">{{ item.item_name }}</span>
                            <span class="text-gray-600">{{ item.item_price }}</span>
                        </li>
                    </ul>
                    <p class="text-lg font-semibold mt-2">Total Amount: {{ order.total_amount }}</p>
                    <button @click="deleteOrder(order.id)" class="my-2 ml-2 text-sm bg-rgreen-100 hover:bg-ryellow text-white py-1 px-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out">Delivered</button>
                </div>
            </div>
        </div>
    </section>
</template>