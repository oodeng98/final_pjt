<template>
  <div class="articleDetail" v-if="article">
    <button @click="router.go(-1)">뒤로가기</button>
    <h2>{{ article.title }}</h2>
    <p>article_id : {{ article.id }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성자 : {{ article.user.username }}</p>
    <p>작성일자 : {{ article.created_at }}</p>
    <p>수정일자 : {{ article.updated_at }}</p>
    <p v-if="likes">좋아요 : {{ likes.length }}</p>
    <p>
      <button v-if="!hasLiked" @click="likeArticle">좋아요</button>
      <button v-else @click="likeArticle">좋아요 취소</button>
      <button @click="deleteArticle">글 삭제</button>
      <button @click="updateArticle">글 수정</button>
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
import { onMounted, ref, computed } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import axios from "axios";
import Comment from "@/components/Comment.vue";

const route = useRoute();
const router = useRouter();
const store = useCommunityStore();
const article = ref(null);
const content = ref(""); // 댓글 작성시 사용
const likes = ref(null); // 좋아요 정보
const hasLiked = ref(null); // 좋아요 정보

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/articles/${route.params.article_id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => console.log(err))
    .then((res) => {
      axios({
        // 좋아요 했는지 검사
        method: "GET",
        url: `http://127.0.0.1:8000/articles/${article.value.id}/like/`,
        headers: {
          Authorization: `Token ${store.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data);
          // like.value = res.data;
          likes.value = res.data.likes;
          hasLiked.value = res.data.hasLiked;
        })
        .catch((err) => console.log(err));
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

const updateArticle = () => {
  router.push({
    name: "communityUpdate",
    params: { article_id: article.value.id },
  });
};

const likeArticle = () => {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/articles/${article.value.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      likes.value = res.data.likes;
      hasLiked.value = res.data.hasLiked;
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
