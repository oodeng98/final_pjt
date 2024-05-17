<script setup>
const props = defineProps({
  article: Object,
});
import Comment from "./Comment.vue";
</script>

<template>
  <h2>{{ article.title }}</h2>
  <p>내용 : {{ article.content }}</p>
  <p>작성자 : {{ article.user.username }}</p>
  <p>작성일자 : {{ article.created_at }}</p>
  <p>수정일자 : {{ article.updated_at }}</p>
  <!-- <p>{{ article }}</p> -->
  <Comment
    v-for="(comment, idx) in article.comment_set"
    :key="comment.id"
    :comment="comment"
    :idx="idx"
  />
</template>

<style scoped></style>
