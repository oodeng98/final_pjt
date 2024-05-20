<template>
  <div>
    <h1>{{ info.username }}님의 프로필 페이지</h1>
    <h3>기본 정보 수정</h3>
    <p>회원 번호: {{}}</p>
    <p>ID: {{ info.username }}</p>
    <form action="">
      <label for="email">Email: </label>
      <input type="text" id="email" />
      <input type="submit" />
    </form>
    <form action="">
      <label for="nickname">Nickname: </label>
      <input type="text" id="nickname" />
      <input type="submit" />
    </form>
    <form action="">
      <label for="age">나이: : </label>
      <input type="text" id="age" />
      <input type="submit" />
    </form>
    <form action="">
      <label for="balance">현재 가진 금액: </label>
      <input type="text" id="balance" />
      <input type="submit" />
    </form>
    <form action="">
      <label for="salary">연봉: </label>
      <input type="text" id="salary" />
      <input type="submit" />
    </form>
    <p>가입한 상품들</p>
    <ol>
      <li v-for="subscribe in subscribes" :key="subscribes.id">
        <RouterLink :to="{ name: 'detail', params: { 'product_id': subscribe.product } }">
          {{ subscribe }}
        </RouterLink>
      </li>
    </ol>
    <!-- https://noanomal.tistory.com/3를 참고하여 그래프를 그려보자 -->
    <!-- <p>{{ info }}</p> -->
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { useRoute, RouterLink } from "vue-router"
import { useCommunityStore } from "@/stores/community"

import axios from "axios";

const info = ref({});
const subscribes = ref([])

onMounted(() => {
  const route = useRoute();
  const store = useCommunityStore();

  axios({
    method: "get",
    url: `http://127.0.0.1:8000/accounts/${route.params.user_id}/`,
    headers: {
      Authorization: store.token,
    },
  })
    .then((res) => {
      console.log(res);
      info.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
  
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/finance/products/subscribe_list/',
    headers:{
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      subscribes.value = res.data
      console.log(res.data)
    })
    .catch(err => {
      console.log(err)
    })
});
</script>

<style scoped></style>
