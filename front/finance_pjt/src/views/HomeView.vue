<template>
  <div>
    <h1>Home</h1>
    <!-- <b-button variant="danger">Button</b-button> -->
    <v-btn prepend-icon="mdi-check-circle"> Button </v-btn>
    <form @submit.prevent="queryGPT">
      <input type="textarea" placeholder="입력하시오." v-model="query">
      <input type="submit">
    </form>
    <p>{{ answer }}</p>
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { RouterLink, RouterView } from "vue-router";
import axios from "axios"

import { useFinanceStore } from '@/stores/finance'
import { useCommunityStore } from '@/stores/community'

const financeStore = useFinanceStore()
const communityStore = useCommunityStore()

const query = ref('')
const answer = ref('무엇이든 물어보세요')

const queryGPT = function () {
  axios({
    method: 'get',
    url: `${financeStore.BASE_URL}/finance/products/gpt/`,
    params: {
      query: query.value
    },
    // headers: {
    //   Authorization: `Token ${communityStore.token}`
    // }
  })
    .then(res => {
      answer.value = res.data.response
    })
    .catch(err => console.log(err))
}
</script>

<style scoped></style>
