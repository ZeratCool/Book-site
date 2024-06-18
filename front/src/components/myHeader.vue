<template>
  <section class="bg-[#FFFCDD]">
    <div class="max-w-[1240px] bg-[#FFFCDD] mx-auto relative px-[5px]">
      <header class="flex items-center justify-between h-[100px]">
        <div class="flex ">
        <picture>
          <img src="@/assets/img/Letter.png" alt="">
        </picture>
        <div>
          <button @click="toggleMenu" class="text-[#2F2F2F] hidden sm:block md:block pl-[20px] ">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
            </svg>
          </button>
        </div>

          <div class="pl-[64px] w-[240px] sm:hidden md:hidden">
            <nav class="flex items-center gap-x-[24px] font-poppins ">
              <RouterLink to="/" class="hover:text-gray-500">Home</RouterLink>
              <RouterLink to="/catalog" class="hover:text-gray-500">Categories</RouterLink>
<!--              <RouterLink to="/about" class="hover:text-gray-500">About</RouterLink>-->
            </nav>
          </div>
        </div>
<!--        <div class="flex gap-2 pl-[5px]">-->
<!--          <button class="w-[164px] sm:w-[90px] md:w-[90px] h-[52px] border-[2px] rounded-full border-[#73C4D6] font-bold hover:bg-[#000159] hover:text-white hover:border-[#000159]">Log In</button>-->
<!--          <button class=" hover:bg-[#FFFCDD] hover:text-black hover:border-[2px] hover:border-[#73C4D6] w-[164px] sm:w-[90px] md:w-[90px] h-[52px] bg-[#000159] font-bold text-white rounded-full ">Sign up</button>-->
<!--        </div>-->
      </header>
      <div v-if="isMenuOpen" class=" bg-[#FFFCDD] h-[300px]  flex justify-center items-center z-30">
        <nav class="flex flex-col items-center text-[#2F2F2F] gap-y-[16px] font-poppins">
          <RouterLink to="/" class="hover:font-semibold">Home</RouterLink>
          <RouterLink to="/catalog" class="hover:font-semibold">Categories</RouterLink>
          <RouterLink to="/about" class="hover:font-semibold">About</RouterLink>
        </nav>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const isMenuOpen = ref(false);

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<style scoped>

</style>
