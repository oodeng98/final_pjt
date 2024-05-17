<template>
    <div>
        <button @click="getDepoist">정기예금</button>
        <button @click="getSaving">정기적금</button>
        <DepositVue
          :products="products"
        />
    </div>
  </template>
  
<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import DepositVue from '@/components/DepositVue.vue';

const store = useFinanceStore()
const products = ref(store.deposits)




</script>
  
<style scoped>
  
</style>