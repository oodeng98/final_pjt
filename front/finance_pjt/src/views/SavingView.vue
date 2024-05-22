<template>
  <div>
    <h1>정기적금</h1>
    <ProductList
      :products-props="store.savings"
      :bank-name-props="store.savingBanks"
    />
  </div>
</template>

<script setup>
import { useFinanceStore } from "@/stores/finance";

import ProductList from "@/components/ProductList.vue";

const store = useFinanceStore();
</script>

<style scoped></style>
