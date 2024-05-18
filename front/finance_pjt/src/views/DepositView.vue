<template>
    <div>
        <h1>정기예금</h1>
        <select v-model="bankName">
            <option selected>전체은행</option>
            <option v-for="bank in store.depositBanks" :key="bank">
                {{ bank }}
            </option>
        </select>
        <div v-for="product of products">
            <RouterLink :to="{ name: 'productDetail', params: { 'category': 'deposit', 'product_id': product.id } }">
                <span>{{ product.dcls_month }} </span>
                <span>{{ product.kor_co_nm }}</span>
                <span>{{ product.fin_prdt_nm }}</span>
                <span v-if="product.rates[4]">{{ product.rates[4] }}</span>
                <span v-else>-</span>
                <span v-if="product.rates[6]">{{ product.rates[6] }}</span>
                <span v-else>-</span>
                <span v-if="product.rates[8]">{{ product.rates[8] }}</span>
                <span v-else>-</span>
                <span v-if="product.rates[10]">{{ product.rates[10] }}</span>
                <span v-else>-</span>
            </RouterLink>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { RouterLink } from 'vue-router'

import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()

const products = ref(store.deposits)
const bankName = ref('전체은행')

watch(bankName, (newValue) => {
    if (bankName.value == '전체은행') {
        products.value = store.deposits
    } else {
        products.value = store.deposits.filter((element) => element.kor_co_nm === newValue)
    }
})
</script>

<style scoped></style>