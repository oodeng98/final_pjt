<template>
    <div>
        <h1 v-if="category === 0">정기 예금</h1>
        <h1 v-else>정기 적금</h1>
        <div v-for="product of products">
            <RouterLink :to="{ name: 'productDetail', params: { 'category': category, 'product_id': product.id } }">{{ product }}</RouterLink>
        </div>
    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

defineProps({
    category: Number,
    products: Array
})
</script>

<style scoped>

</style>