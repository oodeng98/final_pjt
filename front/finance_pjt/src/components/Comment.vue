<script setup>
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";
import { onMounted, ref, computed } from "vue";
import axios from "axios";

const store = useCommunityStore();
const router = useRouter();
const likes = ref(null); // 좋아요 정보
const hasLiked = ref(null); // 좋아요 했는지

onMounted(() => {
  axios({
    // 좋아요 했는지 검사
    method: "GET",
    url: `http://127.0.0.1:8000/articles/${props.comment.article}/comments/${props.comment.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      likes.value = res.data.likes;
      hasLiked.value = res.data.hasLiked;
    })
    .catch((err) => console.log(err));
});

const props = defineProps({
  comment: Object,
  idx: Number,
});
const deleteComment = () => {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/articles/${props.comment.article}/comments/${props.comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      router.go(0);
    })
    .catch((err) => console.log(err));
};

const likeComment = () => {
  axios({
    method: "POST",
    url: `http://127.0.0.1:8000/articles/${props.comment.article}/comments/${props.comment.id}/like/`,
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

<template>
  <div class="commentDetail">
    <p>{{ idx + 1 }}번째 댓글</p>
    <p>댓글 id: {{ comment.id }}</p>
    <p>댓글 작성자: {{ comment.user.username }}</p>
    <p>댓글 내용: {{ comment.content }}</p>
    <p>댓글 작성일: {{ comment.created_at }}</p>
    <p v-if="likes">좋아요 : {{ likes.length }}</p>
    <button v-if="!hasLiked" @click="likeComment">좋아요</button>
    <button v-else @click="likeComment">좋아요 취소</button>
    <button v-if="comment.user.id === store.userInfo.id" @click="deleteComment">
      댓글 삭제
    </button>
  </div>
</template>

<style scoped></style>
