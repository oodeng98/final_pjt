<template>
    <div>
        <h1>정기예금</h1>
        <ProductList
          :products-props="store.deposits"
          :bank-name-props="store.depositBanks"
        />
    </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'

import ProductList from '@/components/ProdouctList.vue'

const store = useFinanceStore()
</script>

<style scoped></style>