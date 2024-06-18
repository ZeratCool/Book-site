import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMainStore = defineStore('main', () => {
  const swiperSlides = ref([])
  const rec = ref([])
  const category = ref([])
  const bookCatalog = ref([])
  const bookClassic = ref([])
  const bookHorror = ref([])
  const bookFairyTale = ref([])
  const bookFantasy = ref([])
  const bookDetective = ref([])
  const loadedBooksCount = ref(12)
  const startBookIndex = ref(0)
  let currentGenre = ref('')
  const searchQuery = ref('');


  function fetchingSwiperBooks () {
    axios.get('http://127.0.0.1:8000/api/books/?_limit=3&_random=true').then(({data}) => {
      swiperSlides.value = data
    })
  }
   function fetchingBook() {
     axios.get('http://127.0.0.1:8000/api/books/klassicheskaja-zarubezhnaja-proza/?_limit=4&_random=true').then(({data}) => {
       bookClassic.value = data
     })

     axios.get('http://127.0.0.1:8000/api/books/uzhasy-i-mistika/?_limit=4&_random=true').then(({data}) => {
       bookHorror.value = data
     })

     axios.get('http://127.0.0.1:8000/api/books/detskaja-literatura/?_limit=4&_random=true').then(({data}) => {
       bookFairyTale.value = data
     })

     axios.get('http://127.0.0.1:8000/api/books/fentezi/?_limit=4&_random=true').then(({data}) => {
       bookFantasy.value = data
     })

     axios.get('http://127.0.0.1:8000/api/books/detektivy-i-trillery/?_limit=4&_random=true').then(({data}) => {
       bookDetective.value = data
     })

   }



  async function fetchingGenre() {
    try {
      const responseGenre = await axios.get('http://127.0.0.1:8000/api/category')
      category.value = responseGenre.data
      console.log(responseGenre)
    } catch (e) {
      console.log(e)
    }
  }

  async function filterGenre(genre = '', search = '') {
    try {

      startBookIndex.value = 0
      const responseBookGenre = await axios.get(`http://127.0.0.1:8000/api/books/${genre}?_search=${search}&_limit=${loadedBooksCount.value}&_start=0`)
      bookCatalog.value = responseBookGenre.data
      currentGenre.value = genre

      console.log(responseBookGenre)
    } catch (e) {
      console.log(e)
    }
  }




  async function fetchMore() {
    try {
      startBookIndex.value += loadedBooksCount.value
      const responseBookGenre = await axios.get(`http://127.0.0.1:8000/api/books/${currentGenre.value}`, {
        params:{
          _search: searchQuery.value,
          _limit: loadedBooksCount.value,
          _start: startBookIndex.value,

        }
      })
      bookCatalog.value.push(...responseBookGenre.data)
      console.log(responseBookGenre)
    } catch (e) {
      console.log(e)
    }
  }

  return {
    swiperSlides,
    category,
    rec,
    bookClassic,
    bookHorror,
    searchQuery,
    bookFairyTale,
    bookFantasy,
    bookDetective,
    currentGenre,
    fetchingGenre,
    bookCatalog,
    fetchMore,
    filterGenre,
    fetchingSwiperBooks,
    fetchingBook,

  }
})
