<template>
    <div class="mt-5 relative lg:mx-10 lg:grid lg:grid-cols-3 pb-5 lg:pl-36 gap-4 w-1120px md:w-85vw overflow-x-auto border border-white rounded-lg p-3 flex flex-wrap">
        <div class="max-w-xs border-2 border-rgreen-100 rounded-lg overflow-hidden mt-5 shadow-lg hover:shadow-2xl transform hover:scale-105 transition-transform duration-300 ease-in-out">
            <img class="w-full" src="../img/amala.png" alt="Card Image">
            <div>
                <div class="px-2 py-4 bg-white flex items-center justify-between">
                    <span class="font-bold lg:text-xl mb-2 w-auto mt-3">Amala and Ewedu</span>
                    <div class="flex items-center gap-3">
                        <button class="text-xl">+</button>
                        <div class="rounded-full bg-[#DAEBDD] w-10 h-10 flex justify-center items-center">
                            <span>2</span>
                        </div>
                        <button class="text-2xl">-</button>
                    </div>
                </div>
            </div>
            <div class="flex justify-end px-3 pb-2">
                <span class="text-rgreen-100">Price - N200</span>
            </div>
            
        </div>
    </div>
    <div class="flex justify-end mx-5">
        <button class="bg-white hover:text-ryellow text-rgreen-100 font-semibold p-2 rounded transform hover:scale-105 transition-transform duration-300 ease-in-out mt-5" >
            View More
        </button>
    </div>

</template>