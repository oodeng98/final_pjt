<template>
  <div>
  <div>test</div>
  <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
    <RouterLink :to="{ name: 'community' }">Community</RouterLink> |
    <RouterLink :to="{ name: 'logIn' }">logIn</RouterLink> |
    <RouterLink :to="{ name: 'signUp' }">signUp</RouterLink> |
    <RouterLink :to="{ name: 'exchangeRate' }">환율 계산기</RouterLink> |
    <RouterLink :to="{ name: 'product' }">Product</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
