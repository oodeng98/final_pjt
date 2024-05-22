<template>
  <div>
    <v-menu>
      <template v-slot:activator="{ props }">
        <v-btn variant="outlined" v-bind="props">상품 종류</v-btn>
      </template>
      <v-list>
        <v-list-item>
          <v-list-item-title @click="router.push({ name: 'deposit' })"
            >정기 예금</v-list-item-title
          >
        </v-list-item>
        <v-list-item>
          <v-list-item-title @click="router.push({ name: 'saving' })"
            >정기 적금</v-list-item-title
          >
        </v-list-item>
      </v-list>
    </v-menu>
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { RouterView, useRouter } from "vue-router";
import { useFinanceStore } from "@/stores/finance";

const store = useFinanceStore();
const router = useRouter();

onMounted(() => {
  if (store.deposits.length === 0 && store.savings.length == 0) {
    store.getProducts();
  }
  // router.push({ name: "deposit" });
});
</script>

<style scoped></style>
