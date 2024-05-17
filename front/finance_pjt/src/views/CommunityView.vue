<template>
  <div>
    <h1>Community</h1>
    <button @click="communityCreate">게시글 작성</button>
    <div v-for="article in articles" class="article" :key="article.id">
      <Article :article="article" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community.js";
import Article from "../components/Article.vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();
const store = useCommunityStore();
const articles = ref([]);
onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/articles/",
  }).then((res) => {
    articles.value = res.data;
  });
});
const communityCreate = () => {
  router.push({ name: "communityCreate" });
};
</script>

<style scoped>
.article {
  border: 1px solid black;
  margin: 1rem 0;
  padding: 1rem;
}
</style>
