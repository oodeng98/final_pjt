<script setup>
defineProps({
  comment: Object,
  idx: Number,
});
</script>

<template>
  <!-- <p>{{ comment }}</p> -->
  <div class="comment">
    <p>{{ idx + 1 }}번째 댓글</p>
    <p>댓글 작성자: {{ comment.user.username }}</p>
    <p>댓글 내용: {{ comment.content }}</p>
    <p>댓글 작성일: {{ comment.created_at }}</p>
  </div>
</template>

<style scoped>
.comment {
  border: 1px solid black;
  padding: 1rem;
}
</style>
