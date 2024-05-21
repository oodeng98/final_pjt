<template>
  <div>
    <h1>
      {{ info?.nickname ? info.nickname : info.username }}님의 프로필 페이지
    </h1>
    <h3>기본 정보 수정</h3>
    <p>회원 번호: {{ info.id }}</p>
    <p>ID: {{ info.username }}</p>
    <form @submit.prevent="update">
      <v-text-field label="Email" v-model="email"></v-text-field>
      <v-text-field label="First Name" v-model="first_name"></v-text-field>
      <v-text-field label="Last Name" v-model="last_name"></v-text-field>
      <v-text-field label="닉네임" v-model="nickname"></v-text-field>
      <v-btn type="submit">업데이트</v-btn>
    </form>
    <p>가입한 상품들</p>
    <ol>
      <li v-for="subscribe in subscribes" :key="subscribes.id">
        <RouterLink
          :to="{ name: 'detail', params: { product_id: subscribe.product } }"
        >
          {{ subscribe }}
        </RouterLink>
      </li>
    </ol>
    <!-- https://noanomal.tistory.com/3를 참고하여 그래프를 그려보자 -->
    <!-- <p>{{ info }}</p> -->
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { useCommunityStore } from "@/stores/community";
import { useFinanceStore } from "@/stores/finance";

import axios from "axios";

const subscribes = ref([]);
const route = useRoute();
const communityStore = useCommunityStore();
const financeStore = useFinanceStore();
const info = communityStore.userInfo;
const email = ref(null);
const nickname = ref(null);
const first_name = ref(null);
const last_name = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/finance/products/subscribe_list/",
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      subscribes.value = res.data;
      console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
  email.value = communityStore.userInfo.email;
  nickname.value = communityStore.userInfo.nickname;
});

const update = () => {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/accounts/${communityStore.userInfo.id}/`,
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
    data: {
      email: email.value,
      nickname: nickname.value,
      first_name: first_name.value,
      last_name: last_name.value,
    },
  })
    .then((res) => {
      communityStore.userInfo = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
