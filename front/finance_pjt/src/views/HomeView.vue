<template>
  <div>
    <h1>Home</h1>
    <b-button variant="danger">Button</b-button>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
