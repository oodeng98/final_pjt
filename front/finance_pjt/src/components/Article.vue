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
  <v-card>
    <v-card-title>
      <v-layout class="align-center">
        <span class="article-title">
          {{ article.title }}
        </span>
        <v-spacer></v-spacer>
        <span class="font-weight-light">
          {{ article.article_likes_set.length }}
          <v-icon>mdi-thumb-up-outline</v-icon>
        </span>
      </v-layout>
    </v-card-title>
    <v-card-subtitle>{{ article.created_at.slice(0, 10) }}</v-card-subtitle>
    <v-card-text>
      <p class="article-content">내용 : {{ article.content }}</p>
      <p>작성자 : {{ article.user.username }}</p>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click="detail">자세히</v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
.article-title,
.article-content {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
