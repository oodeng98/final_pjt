<script setup>
import { useCommunityStore } from "@/stores/community.js";
import { useRouter } from "vue-router";

const store = useCommunityStore();
const router = useRouter();
const props = defineProps({
  article: Object,
});

const detail = () => {
  router.push({
    name: "communityDetail",
    params: { article_id: props.article.id },
  });
};
</script>

<template>
  <h2>{{ article.title }}</h2>
  <p>내용 : {{ article.content }}</p>
  <p>작성자 : {{ article.user.username }}</p>
  <p>작성일자 : {{ article.created_at }}</p>
  <button @click="detail">디테일</button>
</template>

<style scoped></style>
