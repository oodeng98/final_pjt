<template>
    <div>
        <select v-model="bankName">
            <option selected>전체은행</option>
            <option v-for="bank in props.bankNameProps" :key="bank">
                {{ bank }}
            </option>
        </select>
        <button @click="sort6Months">6개월</button>
        <button @click="sort12Months">12개월</button>
        <button @click="sort24Months">24개월</button>
        <button @click="sort36Months">36개월</button>
        <button @click="initialize">초기화</button>
        <div v-for="product of products">
            <RouterLink
              :to="{
                name: 'productDetail',
                params: { 'category': product.category === 0?'deposit':'saving', 'product_id': product.id }
                }">
                <span>{{ product.id }} - </span>
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
import { ref, watch, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
    productsProps: Array,
    bankNameProps: Array
})

const products = ref(null)
const bankName = ref(null)

const sort6MonthsOption = ref('des')
const sort12MonthsOption = ref('des')
const sort24MonthsOption = ref('des')
const sort36MonthsOption = ref('des')

onMounted(() => {
    products.value = props.productsProps.sort(function (a, b) {
        return a.id - b.id
    })
    bankName.value = '전체은행'
})

watch(bankName, (newValue) => {
    if (bankName.value == '전체은행') {
        products.value = props.productsProps
    } else {
        products.value = props.productsProps.filter((element) => element.kor_co_nm === newValue)
    }
})

const sort6Months = function () {
    if (sort6MonthsOption.value == 'des') {
        products.value = products.value.sort(function (a, b) {
            return a.rates[4] - b.rates[4]
        })
        sort6MonthsOption.value = 'asc'
    } else {
        products.value = products.value.sort(function (a, b) {
            return b.rates[4] - a.rates[4]
        })
        sort6MonthsOption.value = 'des'
    }
}

const sort12Months = function () {
    if (sort12MonthsOption.value == 'des') {
        products.value = products.value.sort(function (a, b) {
            return a.rates[6] - b.rates[6]
        })
        sort12MonthsOption.value = 'asc'
    } else {
        products.value = products.value.sort(function (a, b) {
            return b.rates[6] - a.rates[6]
        })
        sort12MonthsOption.value = 'des'
    }
}

const sort24Months = function () {
    if (sort24MonthsOption.value == 'des') {
        products.value = products.value.sort(function (a, b) {
            return a.rates[8] - b.rates[8]
        })
        sort24MonthsOption.value = 'asc'
    } else {
        products.value = products.value.sort(function (a, b) {
            return b.rates[8] - a.rates[8]
        })
        sort24MonthsOption.value = 'des'
    }
}

const sort36Months = function () {
    if (sort36MonthsOption.value == 'des') {
        products.value = products.value.sort(function (a, b) {
            return a.rates[10] - b.rates[10]
        })
        sort36MonthsOption.value = 'asc'
    } else {
        products.value = products.value.sort(function (a, b) {
            return b.rates[10] - a.rates[10]
        })
        sort36MonthsOption.value = 'des'
    }
}

const initialize = function () {
    products.value = props.productsProps.sort(function (a, b) {
        return a.id - b.id
    })
    bankName.value = '전체은행'
}
</script>

<style scoped></style>