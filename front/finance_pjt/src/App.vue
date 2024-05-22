<template>
  <v-app>
    <v-toolbar app class="bg-grey-darken-1">
      <v-toolbar-title>
        <v-btn icon>
          <v-icon @click="router.push({ name: 'home' })"
            >mdi-home-variant</v-icon
          >
        </v-btn>
      </v-toolbar-title>
      <v-toolbar-items class="hidden-xs">
        <v-btn :to="{ name: 'community' }">Community</v-btn>
        <v-btn :to="{ name: 'exchangeRate' }">환율 계산기</v-btn>
        <v-btn :to="{ name: 'products' }">Product</v-btn>
        <v-btn :to="{ name: 'map' }">Map</v-btn>
        <template v-if="user">
          <v-btn class="bg-grey-darken-3" @click="logOut">logOut</v-btn>
          <v-btn
            class="bg-grey-darken-3"
            :to="{ name: 'profile', params: { user_id: 1 } }"
          >
            My Page
          </v-btn>
        </template>
        <template v-else>
          <v-btn :to="{ name: 'logIn' }">logIn</v-btn>
          <v-btn :to="{ name: 'signUp' }">signUp</v-btn>
        </template>
      </v-toolbar-items>
    </v-toolbar>
    <div>
      <v-col class="userInfo text-end">
        <span class="text-h4" v-if="user?.nickname">
          Welcome, {{ user.nickname }}
        </span>
        <span class="text-h4" v-else-if="user">
          Welcome, {{ user.username }}
        </span>
      </v-col>
    </div>
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

<style scoped></style>
