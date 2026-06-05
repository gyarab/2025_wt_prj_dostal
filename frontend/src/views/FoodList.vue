<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const foods = ref([]);

async function load() {
  const url = new URL("/api/food", window.location.origin);
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP returned ${res.status}`);
  const data = await res.json();
  foods.value = data.results;
}

function selectFood(food) {
  router.push(`/food/${food.id}`);
}

onMounted(load);
</script>

<template>
  <h2>Food List</h2>

  <div v-for="food in foods" @click="selectFood(food)">
    <h3>{{ food.name }}</h3>
    <p>{{ food.calories }}</p>
  </div>
</template>
