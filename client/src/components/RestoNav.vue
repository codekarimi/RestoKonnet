<script setup>
    import Logo2 from "../components/Logo2.vue"
    import Cart from "./Cart.vue"
    import { useAuthStore } from '../stores/AuthStore'
    import { useRouter } from "vue-router";


    const authStore = useAuthStore()

    const {user} = defineProps(['user'])

    const router = useRouter()

    const logout = () => {
        router.push('/')
        authStore.logout()
    }


</script>

<template>
    <div class="flex md:flex-row justify-between items-center md:mx-auto max-w-screen-xl p-4">
        <div class="">
            <Logo2/>
        </div>
        <div class="flex gap-40 items-center m-10 pb-10">
            <div class="">
                <div class="absolute">
                    <input class="peer hidden" type="checkbox" name="select-1" id="select-1"/>
                    <label for="select-1" class="flex cursor-pointer select-none p-2 px-3">
                        <img class="w-7 md:w-auto" src="../img/icons/Ellipse 4.png" alt="">
                    </label>
                    <ul class="max-h-0 select-none flex-col overflow-hidden rounded-b-lg shadow-xl transition-all duration-300 peer-checked:max-h-56 peer-checked:py-3 bg-white">
                        <li class="cursor-pointer px-3 py-2 text-sm text-gray-500 hover:bg-gray-100">Username:  <span>{{ user.name }}</span></li>
                        <li class="cursor-pointer px-3 py-2 text-sm text-gray-500 hover:bg-gray-100">Address: <span>{{ user.address }}</span></li>
                        <li class="cursor-pointer px-3 py-2 text-sm text-gray-500 hover:bg-ryellow hover:text-white"><button @click.prevent="logout()">Logout</button></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>