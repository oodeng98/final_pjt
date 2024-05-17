<template>
    <div>
        <button @click="getDepoist">정기예금</button>
        <button @click="getSaving">정기적금</button>
        <ProductListVue
          :category="category"
          :products="products"
        />
    </div>
  </template>
  
<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import ProductListVue from '@/components/ProductListVue.vue';

const store = useFinanceStore()
const category = ref(0)
const products = ref(store.deposits)

const getDepoist = function () {
    category.value = 0
    products.value = store.deposits
}

const getSaving = function () {
    category.value = 1
    products.value = store.savings
}

onMounted(() => {
  if (store.deposits.length === 0 && store.savings.length == 0) {
    store.getProducts()
  }
})

</script>
  
<style scoped>
  
</style>