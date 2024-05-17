<template>
    <div>
        <h1>정기예금</h1>
        <select v-model="bankName">
            <option v-for="bank in store.depositBanks" :key="bank">
                {{ bank }}
            </option>
        </select>
        <div v-for="product of products">
            <RouterLink :to="{ name: 'productDetail', params: { 'category': 'deposit', 'product_id': product.id } }">
                {{ product.category }} - {{ product.kor_co_nm }} {{ product.fin_prdt_nm }} {{ product.rates }}
            </RouterLink>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const products = ref(store.deposits)
</script>

<style scoped>

</style>