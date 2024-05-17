<template>
  <div class="articleDetail" v-if="article">
    <button @click="router.go(-1)">뒤로가기</button>
    <h2>{{ article.title }}</h2>
    <p>article_id : {{ article.id }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성자 : {{ article.user.username }}</p>
    <p>작성일자 : {{ article.created_at }}</p>
    <p>수정일자 : {{ article.updated_at }}</p>
    <p>
      <button @click="deleteArticle">글 삭제</button>
    </p>
    <form @submit.prevent="createComment">
      <label for="content">댓글 작성 : </label>
      <input type="text" id="content" v-model="content" />
      <button type="submit">댓글달기</button>
    </form>
    <div
      class="comment"
      v-for="(comment, idx) in article.comment_set"
      :key="comment.id"
    >
      <Comment :comment="comment" :idx="idx" />
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import axios from "axios";
import Comment from "@/components/Comment.vue";

const route = useRoute();
const router = useRouter();
const store = useCommunityStore();
const article = ref(null);
const content = ref(""); // 댓글 작성시 사용

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

const deleteArticle = () => {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.push({ name: "community" });
    })
    .catch((err) => console.log(err));
};

const createComment = () => {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.go(0);
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
.comment {
  border: 1px solid black;
  padding: 1rem;
  margin: 1rem 0;
}
</style>
