<template>
  <v-app>
    <v-toolbar app class="bg-grey-darken-1">
      <v-toolbar-title>
        <v-btn icon>
          <v-icon @click="router.push({ name: 'home' })"
            >mdi-home-variant</v-icon
          >
        </v-btn>
        <v-btn :to="{ name: 'profile' }" v-if="user">
          <span v-if="user?.nickname" @click="router.push({ name: 'profile' })">
            안녕하세요, {{ user.nickname }}님
          </span>
          <span v-else-if="user" @click="router.push({ name: 'profile' })">
            안녕하세요, {{ user.username }}님
          </span>
        </v-btn>
      </v-toolbar-title>
      <v-toolbar-items class="hidden-xs">
        <v-btn :to="{ name: 'community' }">커뮤니티</v-btn>
        <v-btn :to="{ name: 'products' }">금융상품</v-btn>
        <v-btn :to="{ name: 'exchangeRate' }">환율계산기</v-btn>
        <v-btn :to="{ name: 'map' }">지도</v-btn>
        <template v-if="user">
          <v-btn class="bg-grey-darken-3" @click="logOut">logOut</v-btn>
          <v-btn class="bg-grey-darken-3" :to="{ name: 'profile' }">
            My Page
          </v-btn>
        </template>
        <template v-else>
          <v-btn :to="{ name: 'logIn' }">logIn</v-btn>
          <v-btn :to="{ name: 'signUp' }">signUp</v-btn>
        </template>
      </v-toolbar-items>
    </v-toolbar>
    <v-container>
      <RouterView />
    </v-container>
  </v-app>
</template>

<script setup>
import { RouterView } from "vue-router";
import { useCommunityStore } from "./stores/community.js";
import { ref, onMounted, computed } from "vue";
import router from "./router";

const store = useCommunityStore();
const user = computed(() => store.userInfo);
const logOut = () => {
  store.logOut();
};
</script>

<style scoped>
.v-toolbar-title > span {
  margin: auto;
  font-size: 100px;
}

.v-container {
  padding: 3rem;
}
</style>
