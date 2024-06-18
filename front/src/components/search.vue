<script setup>
import { useMainStore } from "@/stores/mainStore.js";
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'

const { searchQuery } = storeToRefs(useMainStore())
const { filterGenre } = useMainStore()
const router = useRouter()

// Функция для выполнения поиска по книгам и перехода по маршруту
const searchBooksAndNavigate =  () => {
  router.push({ name: 'catalog' })
  // Вызываем функцию из стора для фильтрации книг по жанру и поиску
  filterGenre('', searchQuery.value);
  // Переходим по маршруту 'catalog'

};
</script>

<template>
  <section class="bg-[#FFFCDD]">
    <div class="max-w-[1240px] bg-[#FFFCDD] mx-auto px-[5px]">
      <div class="flex h-[100px] items-center gap-[8px]">
        <div class="w-[460px] relative">
          <input v-model="searchQuery" type="text" placeholder="Search book..." class="w-full h-[52px] bg-white pl-20 pr-10 py-2 border-2 border-[#DBCAAD] rounded-full ">
          <div class="absolute top-[7px] left-[32px] bg-transparent border-none p-2">
            <img src="@/assets/img/lupa.png" alt="Search" class="h-6 w-6">
          </div>
        </div>
        <button @click="searchBooksAndNavigate" class="w-[164px] h-[52px] bg-[#000159] text-white rounded-full font-bold hover:bg-[#FFFCDD] hover:text-black hover:border-[2px] hover:border-[#73C4D6]">Search</button>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
