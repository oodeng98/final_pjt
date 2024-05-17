<template>
  <div>
    <div>test</div>
    <RouterLink :to="{ name: 'community' }">Community</RouterLink> |
    <RouterLink :to="{ name: 'logIn' }">logIn</RouterLink> |
    <RouterLink :to="{ name: 'signUp' }">signUp</RouterLink> |
    <RouterLink :to="{ name: 'exchangeRate' }">환율 계산기</RouterLink> |
    <RouterLink :to="{ name: 'profile', params: { user_id: 1 } }"
      >My Page</RouterLink
    >
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
