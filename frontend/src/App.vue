<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <!-- html -->
  <h1>CalorieTracler</h1>
  <header>
    <router-link to="/">Homepage</router-link>
  </header>
  <main>
    <router-view />
  </main>
</template>
