<script setup>
import Logo from "../components/Logo.vue";
import axios from "axios";
import { ref, computed } from 'vue';
import { useRouter } from "vue-router";


const vendorSignUpData = ref({
    firstName: '',
    lastName: '',
    phone_no: '',
    email: '',
    password: '',
    confirmPassword: '',
    address: '',
});

const router = useRouter()

const passwordsMatch = computed(() => vendorSignUpData.value.password === vendorSignUpData.value.confirmPassword);

// submits a registarion form and creates a new customer
const submitForm = async () => {
    try {
        const formData = new FormData();
        formData.append('first_name', vendorSignUpData.value.firstName)
        formData.append('last_name', vendorSignUpData.value.lastName)
        formData.append('phone_no', vendorSignUpData.value.phone_no)
        formData.append('email', vendorSignUpData.value.email)
        formData.append('password', vendorSignUpData.value.password)
        formData.append('address', vendorSignUpData.value.address)

        const response = await axios.post('https://restokonnectapi-8d0b7b86e6bb.herokuapp.com/api/v1/vendors/register', formData);
        alert("Account successfully created!")
        router.push('/vendorSignIn')
        alert("Check Email for Verification link")

    } catch (error) {
        alert(error.response.data.message)
        console.error('Registration Failed:', error);
    }

};
</script>

<template>
    <section class="min-h-screen bg-rgreen-100">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0">
                <RouterLink to="/" class="flex pt-8 justify-center">
                    <Logo />
                </RouterLink>
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2x">
                        Create Account
                    </h1>
                    <form @submit.prevent="submitForm" class="space-y-4 md:space-y-6">
                        <div class="grid gap-3 md:grid-cols-2">
                            <div>
                                <label for="name" class="block mb-2 text-sm font-medium text-gray-900"> First Name </label>
                                <input v-model="vendorSignUpData.firstName" type="text" name="first name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5" placeholder="Enter your name" required>

                            </div>
                            <div>
                                <label for="name" class="block mb-2 text-sm font-medium text-gray-900"> Last Name </label>
                                <input v-model="vendorSignUpData.lastName" type="text" name="name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5" placeholder="Enter your name" required>

                            </div>
                        </div>
                        <div>
                            <label for="phone_no" class="block mb-2 text-sm font-medium text-gray-900">Phone
                                Number</label>
                            <input v-model="vendorSignUpData.phone_no" type="tel" name="phone_no" id="phone_no"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5"
                                placeholder="Enter your phone number" required>
                        </div>
                        <div>
                            <label for="address" class="block mb-2 text-sm font-medium text-gray-900">Address</label>
                            <input v-model="vendorSignUpData.address" type="text" name="address" id="address"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5"
                                placeholder="Enter your address" required>
                        </div>
                        <div>
                            <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
                            <input v-model="vendorSignUpData.email" type="email" name="email" id="email"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5"
                                placeholder="Enter your email" required>
                        </div>
                        <div>
                            <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Password</label>
                            <input v-model="vendorSignUpData.password" type="password" name="password" id="password"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5"
                                placeholder="********" required>
                        </div>
                        <div>
                            <label for="confirmPassword" class="block mb-2 text-sm font-medium text-gray-900">Confirm Password</label>
                            <input v-model="vendorSignUpData.confirmPassword" type="password" name="confirmPassword" id="confirmPassword"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-ryellow focus:border-ryellow block w-full p-2.5"
                                placeholder="********" required>
                        </div>
                        <p v-if="!passwordsMatch" class="text-red-500">Passwords do not match</p>
                        <div class="flex items-start">
                            <div class="flex items-center h-5">
                                <input id="terms" aria-describedby="terms" type="checkbox"
                                    class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300">
                            </div>
                            <div class="ml-3 text-sm">
                                <label for="terms" class="font-light text-gray-500">I accept the <a
                                        class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                                        href="#">Terms and Conditions</a></label>
                            </div>
                        </div>
                        <button type="submit"
                            class="w-full text-white bg-rgreen-100 hover:bg-ryellow focus:ring-4 focus:outline-none focus:ring-ryellow font-medium rounded-lg text-sm px-5 py-2.5 text-center">Create
                            an account</button>
                        <p class="text-sm font-light text-gray-500">
                            Already have an account? <RouterLink to="/vendorSignIn"
                                class="font-medium text-rgreen-100 hover:underline hover:text-ryellow">Login here
                            </RouterLink>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>