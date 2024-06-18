<script setup>
import {ref, onMounted, computed, onUnmounted} from 'vue';
import { useMainStore } from "@/stores/mainStore.js";
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router';
import axios from "axios";
import search from '@/components/search.vue'
import MyHeader from "@/components/myHeader.vue";
import MyFooter from "@/components/myFooter.vue";
const book = ref('')

const {
  bookCatalog,
  searchQuery,
  currentGenre,
} = storeToRefs(useMainStore())
const router = useRouter();
const {

  filterGenre
} = useMainStore()




onMounted(() => {
  filterGenre('', router.currentRoute.value.params.name)


});




onUnmounted(() => {
  if (searchQuery.value) {
    router.currentRoute.value.query.genre = '';
  } else {
    router.currentRoute.value.query.genre = bookCatalog.value[0].category.slug;
  }

})
</script>

<template>
  <div class="flex flex-col min-h-screen overflow-hidden text-black ">
  <my-header ></my-header>
  <search></search>
  <main class="flex-auto">

  <div v-for="book in bookCatalog">
    <section class="bg-[#FFFCDD] pt-[34px]">
      <div class="max-w-[1240px] bg-[#FFFCDD] mx-auto px-[5px]">
        <div class="flex md:flex-col">
          <div class="md:mx-auto">
            <img class=" w-[488px] h-[586px] rounded-[30px] sm:w-[320px] sm:h-[420px]" :src="book.image" alt="">
          </div>
          <div class="flex flex-col pl-[90px] lg:pl-[40px] md:pt-[20px] md:pl-[10px]">
            <span class="text-4xl text-[#000159] font-bold">{{book.name}}</span>
            <div class="pt-[40px]">
              <span class="text-2xl font-semibold">Author</span>
              <span class="ml-[15px] text-[18px] font-normal"> {{book.author}}</span>
            </div>
            <div class="pt-[20px]">
              <span class="text-2xl font-semibold">Year</span>
              <span class="ml-[15px] text-[18px] font-normal">{{Math.round(book.date)}}</span>
            </div>
            <div class="pt-[20px]">
              <span class="text-2xl font-semibold">Genre</span>
              <span class="ml-[15px] text-[18px] font-normal">{{book.category.name}}</span>
            </div>
            <div class="pt-[64px]">
            <a :href="book.file" class="w-[222px] h-[52px] bg-[#000159] text-white rounded-full font-bold flex items-center justify-center hover:bg-[#FFFCDD] hover:text-black hover:border-[2px] hover:border-[#73C4D6]">
              Download
            </a>
            </div>
          </div>
        </div>
        <div class="pt-[64px]">
          <span class="text-2xl font-semibold">Description</span>
        <p class="pt-[36px] pb-[200px] font-normal text-[24px] leading-[36px] sm:text-[18px]">{{book.description}}</p>
        </div>
      </div>
    </section>

  </div>
  </main>
  <my-footer></my-footer>
  </div>
</template>

<style scoped>

</style>