<script setup>
import { ref, onMounted, computed } from 'vue';
import MyHeader from "@/components/myHeader.vue";
import search from '@/components/search.vue'
import slider from '@/components/slider.vue'
import { useMainStore } from "@/stores/mainStore.js";
import { storeToRefs } from 'pinia'
import Main from "@/views/main.vue";
import MyFooter from "@/components/myFooter.vue";
import BookItem from "@/components/BookItem.vue";
import { useRouter } from 'vue-router';

const {
  swiperSlides,
  searchQuery,
  bookCatalog,
  catalog,
  category,

} = storeToRefs(useMainStore())
const router = useRouter();
const {

  fetchingGenre,
  fetchMore,
  fetchingSwiperBooks,
  filterGenre
} = useMainStore()



onMounted(() => {
  fetchingGenre();
  filterGenre(router.currentRoute.value.query.genre, searchQuery.value);
  fetchingSwiperBooks()
});



</script>


<template>
  <div class="flex flex-col min-h-screen overflow-hidden text-black bg-blue-100">

    <my-header ></my-header>
    <search></search>
    <slider :slides="swiperSlides" ></slider>

  <main>
  <section class="bg-[#FFFCDD] pb-[100px] px-[5px] ">
    <div class="max-w-[1240px] mx-auto flex justify-between pt-[60px]">
   <aside>
     <div class="">
       <h2 class="text-3xl font-bold pb-[20px]">Genre</h2>
       <div v-for="category in category" :key="category.id" class="flex items-center pb-2">

         <input :id="category.id" type="radio" @click="filterGenre(category.slug, searchQuery = '')" name="category" class="mr-2 cursor-pointer"/>
         <label :for="category.id" class="text-[18px] cursor-pointer">{{ category.name }}</label>
       </div>
     </div>

   </aside>
    <div class="xl:mx-auto mx-auto">
      <div class="max-w-[953px]   bg-[#73C4D6]   rounded-[10px]  ">
        <div class="flex flex-wrap justify-center xl:w-[550px] md:max-w-[280px]  gap-[32px] pt-[32px]">
          <ul v-for="book in bookCatalog" :key="book.id" >
            <BookItem :book="book" >

            </BookItem>
          </ul>
        </div>
        <div class="flex justify-center py-[56px]">
          <button @click="fetchMore()"  class="hover:bg-[#000159] hover:text-white font-semibold text-xl  rounded-full  bg-[#FFFCDD] w-[240px] h-[52px]">See more</button>
        </div>

      </div>
    </div>

    </div>







  </section>












  </main>






    <my-footer></my-footer>











  </div>
</template>

<style scoped>

</style>