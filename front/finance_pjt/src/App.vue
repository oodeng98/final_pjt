<template>
  <div>
    <RouterLink :to="{ name: 'exchangeRate' }">환율 계산기</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
