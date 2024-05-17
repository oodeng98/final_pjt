<script setup>
import { ref } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useCommunityStore();
const router = useRouter();

const title = ref("");
const content = ref("");

const createArticle = function () {
  axios({
    method: "post",
    url: "http://127.0.0.1:8000/articles/",
    data: {
      title: title.value,
      content: content.value,
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
  <h1>게시글 작성</h1>
  <form @submit.prevent="createArticle">
    <label for="title">제목 : </label>
    <input type="text" id="title" v-model="title" />

    <label for="content">내용 : </label>
    <input type="text" id="content" v-model="content" />

    <button type="submit">create</button>
  </form>
</template>

<style scoped></style>
