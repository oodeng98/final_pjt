<template>
  <div>
    <h1>Community</h1>
    <Article
      v-for="article in store.articles"
      :article="article"
      :key="article.title"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import Article from "../components/Article.vue";
const store = useCommunityStore();
onMounted(() => {
  store.getArticles();
});
</script>

<style scoped></style>
