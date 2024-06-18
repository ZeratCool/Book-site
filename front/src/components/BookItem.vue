<template>
  <div class="">



      <div class="w-[222px]">
        <img :src="book.image" alt="" class="w-full h-[272px] rounded-[15px]" >
        <div class="flex flex-col h-[80px] ">
          <span class="font-semibold pt-[16px]  text-[#000159]">{{ truncatedName(book?.name)}}</span>
          <span class="pt-[4px] ">{{ book?.author }}</span>
        </div>
        <button @click="readBook(book.name)" class=" hover:bg-[#FFFCDD] hover:text-black  w-full bg-[#000159] text-white rounded-full h-[52px] mt-[16px]">Read</button>
      </div>


  </div>
</template>

<script setup>
import { defineProps } from 'vue';
import router from "@/router/index.js";

const props = defineProps({
  book: {
    type: Object,
    required: true,
  },
});

const truncatedName = (name) => {
  const words = name.split(' ');
  if (words.length > 4) {
    return words.slice(0, 4).join(' ') + '...';
  }
  return name;
};

const readBook = (name) =>{
  router.push({ name: 'bookPage', params: { name: name } })
}
</script>
