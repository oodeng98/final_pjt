<script setup>
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useCommunityStore();
const router = useRouter();

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
</script>

<template>
  <div class="commentDetail">
    <p>{{ idx + 1 }}번째 댓글</p>
    <p>댓글 작성자: {{ comment.user.username }}</p>
    <p>댓글 내용: {{ comment.content }}</p>
    <p>댓글 작성일: {{ comment.created_at }}</p>
    <button @click="deleteComment">댓글 삭제</button>
  </div>
</template>

<style scoped></style>
