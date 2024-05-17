<template>
  <div>
    <RouterLink :to="{ name: 'product' }">[Product]</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()

onMounted(() => {
  store.getProduct()
})
</script>

<style scoped>

</style>