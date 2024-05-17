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
      <li v-for="product in info.products" :product="product">{{}}</li>
    </ol>
    <!-- https://noanomal.tistory.com/3를 참고하여 그래프를 그려보자 -->
    <!-- <p>{{ info }}</p> -->
  </div>
</template>

<script setup>
import { useCommunityStore } from "@/stores/community";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

const info = ref({});

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
});
</script>

<style scoped></style>
