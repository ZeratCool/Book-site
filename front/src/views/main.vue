<script setup>
import { ref, onMounted, computed } from 'vue';
import myHeader from '@/components/myHeader.vue'
import search from '@/components/search.vue'
import slider from '@/components/slider.vue'
import BookItem from "@/components/BookItem.vue";
import { storeToRefs } from 'pinia'
import { useMainStore } from "@/stores/mainStore.js";
import MyFooter from "@/components/myFooter.vue";
import router from "@/router/index.js";


const {
  swiperSlides,
  rec,
  classic,
  bookClassic,
  bookHorror,
  bookFairyTale,
  bookFantasy,
  bookDetective,
  currentGenre,
  searchQuery
} = storeToRefs(useMainStore())

const {
  fetching,
  moreFetch,
  fetchingBook,
  filterGenre,
  fetchingSwiperBooks
} = useMainStore()

onMounted(() => {
  fetchingBook()
  fetchingSwiperBooks()
})


const seeMore = (genre) => {
  searchQuery.value = ''
  router.push({ name: 'catalog', query: { genre } }).then(() => {
    window.scrollTo({ top: 0});
  });
}
</script>

<template class="">
  <div class="flex flex-col min-h-screen overflow-hidden text-black  ">
    <my-header ></my-header>
    <search></search>
    <slider :slides="swiperSlides" ></slider>


    <main class="  flex-auto">
      <section class=" bg-[#FFFCDD]  pt-[90px] ">
          <div class="max-w-[1240px] mx-auto  ">
            <div class="bg-[#B089CD] z-10 rounded-r-full flex h-[62px] items-center justify-center w-[250px] ">
              <div class="  ">
                <span class="text-4xl font-bold text-white ">Classic</span>
              </div>
            </div>
            <div class="max-w-[1240px] xl:max-w-[550px] md:max-w-[280px] mx-auto bg-[#73C4D6] mt-[32px] min-h-[592px] rounded-[10px]  ">
              <div class="flex justify-center  flex-wrap gap-[32px] pt-[32px]">

              <ul v-for="book in bookClassic" :key="book.id"  >
            <BookItem :book="book" >

            </BookItem>
              </ul>
              </div>
              <div class="flex justify-center pt-[56px] pb-[32px]">
                <button @click="seeMore('klassicheskaja-zarubezhnaja-proza')"  class="hover:bg-[#000159] hover:text-white font-semibold text-xl  rounded-full  bg-[#FFFCDD] w-[240px] h-[52px]">See more</button>
              </div>

            </div>
          </div>

      </section>
      <section class=" bg-[#FFFCDD]  pt-[90px] ">
        <div class="max-w-[1240px] mx-auto  ">
          <div class="bg-[#B089CD] z-10 rounded-r-full flex h-[62px] items-center justify-center w-[250px] ">
            <div class="  ">
              <span class="text-4xl font-bold text-white ">Horror</span>
            </div>
          </div>
          <div class="max-w-[1240px] xl:max-w-[550px] md:max-w-[280px] mx-auto bg-[#73C4D6] mt-[32px] min-h-[592px] rounded-[10px]  ">
            <div class="flex justify-center  flex-wrap gap-[32px] pt-[32px]">

              <ul v-for="book in bookHorror" :key="book.id"  >
                <BookItem :book="book" >

                </BookItem>
              </ul>
            </div>
            <div class="flex justify-center pt-[56px] pb-[32px]">
              <button @click="seeMore('uzhasy-i-mistika')"   class="hover:bg-[#000159] hover:text-white font-semibold text-xl  rounded-full  bg-[#FFFCDD] w-[240px] h-[52px]">See more</button>
            </div>

          </div>
        </div>

      </section>
      <section class=" bg-[#FFFCDD]  pt-[90px] ">
        <div class="max-w-[1240px] mx-auto  ">
          <div class="bg-[#B089CD] z-10 rounded-r-full flex h-[62px] items-center justify-center w-[250px] ">
            <div class="  ">
              <span class="text-4xl font-bold text-white ">Fairy tale</span>
            </div>
          </div>
          <div class="max-w-[1240px] xl:max-w-[550px] md:max-w-[280px] mx-auto bg-[#73C4D6] mt-[32px] min-h-[592px] rounded-[10px]  ">
            <div class="flex justify-center  flex-wrap gap-[32px] pt-[32px]">

              <ul v-for="book in bookFairyTale" :key="book.id"  >
                <BookItem :book="book" >

                </BookItem>
              </ul>
            </div>
            <div class="flex justify-center pt-[56px] pb-[32px]">
              <button @click="seeMore('detskaja-literatura')"  class="hover:bg-[#000159] hover:text-white font-semibold text-xl  rounded-full  bg-[#FFFCDD] w-[240px] h-[52px]">See more</button>
            </div>

          </div>
        </div>

      </section>
      <section class=" bg-[#FFFCDD]  pt-[90px] ">
        <div class="max-w-[1240px] mx-auto  ">
          <div class="bg-[#B089CD] z-10 rounded-r-full flex h-[62px] items-center justify-center w-[250px] ">
            <div class="  ">
              <span class="text-4xl font-bold text-white ">Fantasy</span>
            </div>
          </div>
          <div class="max-w-[1240px] xl:max-w-[550px] md:max-w-[280px] mx-auto bg-[#73C4D6] mt-[32px] min-h-[592px] rounded-[10px]  ">
            <div class="flex justify-center  flex-wrap gap-[32px] pt-[32px]">

              <ul v-for="book in bookFantasy" :key="book.id"  >
                <BookItem :book="book" >

                </BookItem>
              </ul>
            </div>
            <div class="flex justify-center pt-[56px] pb-[32px]">
              <button  @click="seeMore('fentezi')"  class="hover:bg-[#000159] hover:text-white font-semibold text-xl  rounded-full  bg-[#FFFCDD] w-[240px] h-[52px]">See more</button>
            </div>

          </div>
        </div>

      </section>
      <section class=" bg-[#FFFCDD]  pt-[90px] pb-[100px]">
        <div class="max-w-[1240px] mx-auto  ">
          <div class="bg-[#B089CD] z-10 rounded-r-full flex h-[62px] items-center justify-center w-[250px] ">
            <div class="  ">
              <span class="text-4xl font-bold text-white ">Detective</span>
            </div>
          </div>
          <div class="max-w-[1240px] xl:max-w-[550px] md:max-w-[280px] mx-auto bg-[#73C4D6] mt-[32px] min-h-[592px] rounded-[10px]  ">
            <div class="flex justify-center  flex-wrap gap-[32px] pt-[32px]">

              <ul v-for="book in bookDetective" :key="book.id"  >
                <BookItem :book="book" >

                </BookItem>
              </ul>
            </div>
            <div class="flex justify-center pt-[56px] pb-[32px]">
              <button @click="seeMore('detektivy-i-trillery')"   class="hover:bg-[#000159] hover:text-white font-semibold text-xl  rounded-full  bg-[#FFFCDD] w-[240px] h-[52px]">See more</button>
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