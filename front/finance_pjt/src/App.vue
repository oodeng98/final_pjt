<template>
  <div>test</div>
  <RouterLink :to="{ name: 'community' }">Community</RouterLink> |
  <RouterLink :to="{ name: 'logIn' }">logIn</RouterLink> |
  <RouterLink :to="{ name: 'signUp' }">signUp</RouterLink> |
  <RouterView />
</template>

<script setup></script>

<style scoped></style>
