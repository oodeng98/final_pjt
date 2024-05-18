<template>
  <div>
    <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink> |
    <RouterLink :to="{ name: 'saving' }">정기적금</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()

onMounted(() => {
  if (store.deposits.length === 0 && store.savings.length == 0) {
    store.getProducts()
  }
})
</script>

<style scoped></style>