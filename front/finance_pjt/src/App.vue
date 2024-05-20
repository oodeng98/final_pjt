<template>
  <div>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink> |
    <RouterLink :to="{ name: 'community' }">Community</RouterLink> |
    <RouterLink :to="{ name: 'logIn' }">logIn</RouterLink> |
    <button @click="logOut">logOut</button> |
    <RouterLink :to="{ name: 'signUp' }">signUp</RouterLink> |
    <RouterLink :to="{ name: 'exchangeRate' }">환율 계산기</RouterLink> |
    <RouterLink :to="{ name: 'products' }">Product</RouterLink> |
    <RouterLink :to="{ name: 'profile', params: { user_id: 1 } }"
      >My Page</RouterLink
    >
    | <RouterLink :to="{ name: 'map' }">Map</RouterLink> |
    <span v-if="user">{{ user }}</span>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useCommunityStore } from "./stores/community.js";
import { ref, onMounted, computed } from "vue";

const store = useCommunityStore();
const user = computed(() => store.userInfo);
const logOut = () => {
  store.logOut();
};
</script>

<style scoped></style>
