<template>
  <div>
    <h1 v-if="category === '0'">정기예금 상세</h1>
    <h1 v-else>정기적금 상세</h1>
    <div v-for="p in product">
    {{ p }}</div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import { ref, onMounted } from 'vue';

const route = useRoute()
const { category, product_id } = route.params

const store = useFinanceStore()
const product = ref([])

onMounted(() => {
  if (category === '0') {
    product.value = store.deposits.filter((element) => element.id == product_id)
  } else {
    product.value = store.savings.filter((element) => element.id == product_id)
  }
})
</script>

<style scoped>

</style>