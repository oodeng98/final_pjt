<template>
  <div>
    <h1 v-if="category === 'deposit'">정기예금 상세</h1>
    <h1 v-else>정기적금 상세</h1>
    <button>가입하기</button>
    <div v-for="info in product">
      {{ info }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import { useFinanceStore } from '@/stores/finance'

const route = useRoute()
const { category, product_id } = route.params

const store = useFinanceStore()
const product = ref([])

onMounted(() => {
  if (category === 'deposit') {
    product.value = store.deposits.filter((element) => element.id == product_id)
  } else {
    product.value = store.savings.filter((element) => element.id == product_id)
  }
})
</script>

<style scoped>

</style>