<script setup>
    import Logo2 from "../components/Logo2.vue"
</script>

<template>
    <div class="flex justify-between items-center">
        <div>
            <Logo2/>
        </div>
        <div class="flex gap-10 items-center">
            <RouterLink to="/Dashboard/1" class="text-white hover:text-ryellow transition duration-300 ease-in-out relative group text-lg md:text-2xl font-semibold">
                Dashboard
                <div class="absolute w-full h-1 bg-ryellow bottom-0 left-0 transform scale-x-0 transition-transform origin-left group-hover:scale-x-100 duration-300 ease-in-out"></div>
            </RouterLink>
            <button>
                <img src="../img/icons/Ellipse 4.png" alt="">
            </button>
            <button>
                <img class="pb-2" src="../img/icons/garden_cart.png" alt="">
            </button>
        </div>
    </div>
</template>