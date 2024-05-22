<template>
  <v-container class="border-double">
    <v-col class="articleDetail" v-if="article">
      <v-btn class="bg-red" @click="router.go(-1)">뒤로가기</v-btn>
      <div class="text-h2">{{ article.title }}</div>
      <div class="text-h4">{{ article.user.username }}</div>
      <div class="content">
        <p>{{ article.content }}</p>
      </div>
      <p>작성일자 : {{ article.created_at.slice(0, 10) }}</p>
      <p>수정일자 : {{ article.updated_at.slice(0, 10) }}</p>
      <p v-if="likes">좋아요 : {{ likes.length }}</p>
      <br />
      <p>
        <v-btn v-if="!hasLiked" @click="likeArticle" class="bg-red"
          >좋아요</v-btn
        >
        <v-btn v-else @click="likeArticle" class="bg-red">좋아요 취소</v-btn>
        <span v-if="article.user.id === store.userInfo.id">
          <v-btn @click="deleteArticle">글 삭제</v-btn>
          <v-btn @click="updateArticle">글 수정</v-btn>
        </span>
      </p>
      <v-row class="align-center justify-center">
        <v-col cols="10">
          <form @submit.prevent="createComment">
            <br />
            <v-text-field
              label="댓글 작성"
              type="text"
              id="content"
              v-model="content"
            />
          </form>
        </v-col>
        <v-col cols="2">
          <v-btn @click="createComment" size="x-large">댓글달기</v-btn>
        </v-col>
      </v-row>
      <div
        class="comment"
        v-for="(comment, idx) in article.comment_set"
        :key="comment.id"
      >
        <Comment :comment="comment" :idx="idx" />
      </div>
    </v-col>
  </v-container>
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
.articleDetail {
  padding: 1rem;
}

.text-h2 {
  margin: 1rem 0;
  font-size: 24px;
  font-weight: bold;
}

.text-h4 {
  margin: 1rem 0;
  font-size: 18px;
}

.content {
  margin: 1rem 0;
}

.comment {
  border: 1px solid #ccc;
  padding: 1rem;
  margin: 1rem 0;
}

.v-btn {
  margin-right: 1rem;
}
/* .v-container {
  border: 1px solid black;
  border-radius: 3%;
} */
</style>
