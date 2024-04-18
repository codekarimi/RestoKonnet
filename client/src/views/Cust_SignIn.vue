<script setup>
    import Logo from "../components/Logo.vue";
    import { ref } from "vue";
    import { useRouter } from "vue-router";
    import { useAuthStore  } from "../stores/AuthStore";

    const custPhone_no = ref("");
    const router = useRouter();

    const authStore = useAuthStore()

    const login_customer = async () => {
        const response = await authStore.login_customer(custPhone_no.value)
        router.push(`/customers/${response.id}`)
    }

    
    // submit customer details to sign in


    // const submitForm = async () => {
    //     const formData = new FormData()
    //     formData.append('phone_no', custPhone_no.value)

    //     try {
    //         const response = await axios.post('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/customer_login', formData);
    //         localStorage.setItem('token', response.data.access_token);
    //         localStorage.setItem('customer_id', response.data.id)
    //         localStorage.removeItem('vendor_id');
    //         const id = response.data.id
    //         router.push(`/customers/${id}`)

    //     } catch (error) {
    //         alert(error.response.data.message)
    //         console.log("Login Failed:", error)
    //     }
    // }

</script>

<template>
    <section class="bg-rgreen-100">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <RouterLink to="/" class="flex pt-8 justify-center mb-6 ">
                    <Logo />  
                </RouterLink>
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                            Sign In
                    </h1>
                    <form @submit.prevent="login_customer" class="space-y-4 md:space-y-6" action="#">
                        <div>
                            <label for="phone" class="block mb-2 text-sm font-medium text-gray-900">Phone Number</label>
                            <input v-model="custPhone_no" type="tel" name="phone" id="phone" placeholder="Enter your phone number" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5" required>
                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input id="remember" aria-describedby="remember" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-ryellow">
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember" class="text-gray-500">Remember me</label>
                                </div>
                            </div>
                            <a href="#" class="text-sm font-medium text-primary-600 hover:underline">Forgot password?</a>
                        </div>
                        <button type="submit" class="w-full text-white bg-rgreen-100 hover:bg-ryellow font-semibold rounded-lg lg:text-lg px-5 py-2.5 text-center">Sign in</button>
                        <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                            Don’t have an account yet? <RouterLink to="/customerSignUp" class="font-medium text-rgreen-100 hover:underline hover:text-ryellow">Sign up</RouterLink>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>