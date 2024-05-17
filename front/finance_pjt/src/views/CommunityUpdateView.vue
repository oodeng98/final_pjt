<script setup>
import { ref, onMounted } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import { useRoute, useRouter } from "vue-router";

import axios from "axios";

const store = useCommunityStore();
const route = useRoute();
const router = useRouter();

const article = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/articles/${route.params.article_id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  }).then((res) => {
    article.value = res.data;
  });
});

const updateArticle = function () {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/`,
    data: {
      title: article.value.title,
      content: article.value.content,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.push({ name: "community" });
    })
    .catch((err) => console.log(err));
};
</script>

<template>
  <h1>게시글 수정</h1>
  <div class="container" v-if="article">
    <p>{{ article }}</p>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="article.title" />

      <label for="content">내용 : </label>
      <input type="text" id="content" v-model="article.content" />

      <button type="submit">update</button>
    </form>
  </div>
</template>

<style scoped></style>
