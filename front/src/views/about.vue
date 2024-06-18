<script setup>

import MyHeader from "@/components/myHeader.vue";
import search from '@/components/search.vue'
import slider from '@/components/slider.vue'
import { useMainStore } from "@/stores/mainStore.js";
import { storeToRefs } from 'pinia'
import {onMounted} from "vue";


const {
  swiperSlides,
  rec,
  classic,
} = storeToRefs(useMainStore())

const {
  fetching,
  fetchingSwiperBooks
} = useMainStore()

onMounted(() => {

  fetchingSwiperBooks()
});
</script>

<template>
  <div class="flex flex-col min-h-screen overflow-hidden text-black bg-blue-100">
    <my-header></my-header>
    <search></search>
    <slider :slides="swiperSlides" ></slider>



















  </div>
</template>

<style scoped>

</style>