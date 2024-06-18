import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/main.vue"),
    },
    {
      path: "/catalog",
      name: "catalog",
      component: () => import("../views/catalog.vue"),
      props: (route) => ({ genre: route.query.genre }),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/about.vue"),
    },

    {
      path: "/bookPage/:name",
      name: "bookPage",
      component: () => import("../views/bookPage.vue"),

    },
  ],
})

export default router
