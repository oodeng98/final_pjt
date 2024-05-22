<template>
  <v-container>
    <h1>Home</h1>
    <v-form @submit.prevent="queryGPT">
      <v-text-field v-model="query" label="입력하시오."></v-text-field>
      <v-btn color="primary" type="submit">전송</v-btn>
    </v-form>
    <!-- <p>{{ answer }}</p> -->
    <template v-for="chat in conversation" :key="chat">
      <Dialog :chat="chat" />
    </template>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useFinanceStore } from "@/stores/finance";
import { useCommunityStore } from "@/stores/community";
import Dialog from "@/components/Dialog.vue";
const financeStore = useFinanceStore();
const communityStore = useCommunityStore();

const query = ref("");
const answer = ref("무엇이든 물어보세요");

const conversation = ref([]);

const queryGPT = function () {
  conversation.value.push(query.value);
  axios({
    method: "get",
    url: `${financeStore.BASE_URL}/finance/products/gpt/`,
    params: {
      query: query.value,
    },
  })
    .then((res) => {
      answer.value = res.data.response;
      // console.log(answer.value);
      conversation.value.push(answer.value);
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
.container {
  margin-top: 20px;
}
</style>
