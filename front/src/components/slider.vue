<template>
  <section class="bg-[#73C4D6] flex flex-col">
    <div class="max-w-[1240px] bg-[#73C4D6] mx-auto relative">
      <swiper
          :spaceBetween="50"
          :slidesPerView="1"
          :pagination="{ clickable: true, el: '.swiper-pagination' }"
          :history="{ key: 'slide' }"
          :modules="modules"
          class="mySwiper max-w-[1100px] h-[400px] xl:w-[700px] md:w-[400px] sm:w-[370px] "
      >
        <swiper-slide v-for="(slide, index) in slides" :key="index" :data-history="index + 1">
          <div class="flex xl:flex-col  ">
            <div class="flex flex-col pt-[100px] xl:pt-0 xl:mx-auto w-[620px] xl:text-center md:w-[400px] ">
              <span class="text-4xl font-bold text-[#000159]">
                {{truncatedName(slide.name)}}
              </span>
              <span class="w-[533px] leading-[36px] text-[24px] mt-[16px] text-white xl:hidden">
                {{truncatedBody(slide.description)}}
              </span>
            </div>

            <div class="relative pl-[8%] xl:pl-0 xl:mx-auto xl:pt-[25px] ">
              <img :src="slide.image" alt="" class="w-[328px] h-[445px]  transform rotate-[19deg] translate-y-10 hover:bg-black">
            </div>
          </div>
        </swiper-slide>
      </swiper>
      <div class="swiper-pagination !absolute !bottom-[-22px] !left-1/2 !transform !-translate-x-1/2 ">

      </div>
    </div>
  </section>
</template>


<script setup>
import { ref } from 'vue';
import { Swiper, SwiperSlide,  } from 'swiper/vue';
import {  Pagination } from 'swiper/modules';

import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';


const modules = ref([ Pagination]);
const truncatedName = (name) => {
  const words = name.split(' ');
  if (words.length > 4) {
    return words.slice(0, 4).join(' ') + '...';
  }
  return name;
};
const truncatedBody = (body) => {
  const words = body.split(' ');
  if (words.length > 4) {
    return words.slice(0, 19).join(' ') + '...';
  }
  return body;
};

const props = defineProps({
  title: String,
  slides: Array
});
</script>