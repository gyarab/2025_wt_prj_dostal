import { createRouter, createWebHistory } from "vue-router";
import FoodList from "../views/FoodList.vue";
import FoodDetail from "../views/FoodDetail.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: FoodList },
    { path: "/food/:id", name: "food-detail", component: FoodDetail },
  ],
});

export default router;
