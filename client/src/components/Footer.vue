<script setup>
    import Logo from "../components/Logo.vue"
</script>
<template>
    <footer class="w-full max-w-[85rem] py-10 px-4 sm:px-6 lg:px-8 mx-auto">
        <!-- Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 items-center gap-5 text-center">
            <div class="flex justify-center lg:justify-start">
                <a href="#" aria-label="Brand">
                    <Logo />
                </a>
            </div>
          <!-- End Col -->
      
          <ul class="text-center">
            <li class="inline-block relative pe-8 last:pe-0 last-of-type:before:hidden before:absolute before:top-1/2 before:end-3 before:-translate-y-1/2 before:content-['*'] before:text-ryellow">
              <a class="inline-flex gap-x-2 text-md text-rgreen-100 hover:text-ryellow" href="#">
                About
              </a>
            </li>
            <li class="inline-block relative pe-8 last:pe-0 last-of-type:before:hidden before:absolute before:top-1/2 before:end-3 before:-translate-y-1/2 before:content-['*'] before:text-ryellow">
              <a class="inline-flex gap-x-2 text-md text-rgreen-100 hover:text-ryellow" href="#">
                Services
              </a>
            </li>
            <li class="inline-block relative pe-8 last:pe-0 last-of-type:before:hidden before:absolute before:top-1/2 before:end-3 before:-translate-y-1/2 before:content-['/'] before:text-ryellow">
              <a class="inline-flex gap-x-2 text-md text-rgreen-100 hover:text-ryellow" href="#">
                Blog
              </a>
            </li>
          </ul>
          <!-- End Col -->
      
          <!-- Social Brands -->
          <div class="md:text-end space-x-2">
            <a class="size-8 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-full border border-transparent text-gray-500 hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">
                <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/linkedin black.1.png" alt="">
            </a>
            <a class="size-8 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-full border border-transparent text-gray-500 hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">
                <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/facebook black.1.png" alt="">
            </a>
            <a class="size-8 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-full border border-transparent text-gray-500 hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600" href="#">
                <img class="transform hover:scale-150 transition-transform duration-300 ease-in-out" src="../img/icons/twitter black.1.png" alt="">
            </a>
          </div>
          <!-- End Social Brands -->
        </div>
        <div class="flex justify-center mt-10 text-sm text-gray-500">
            © All Rights Reserved. 2024, Restokonnet Inc.
        </div>
        <!-- End Grid -->
    </footer>
</template>