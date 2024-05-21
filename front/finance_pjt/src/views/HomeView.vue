<template>
  <div>
    <h1>Home</h1>
    <!-- <b-button variant="danger">Button</b-button> -->
    <v-btn prepend-icon="mdi-check-circle"> Button </v-btn>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
