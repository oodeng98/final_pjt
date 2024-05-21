<template>
  <v-app>
    <v-navigation-drawer v-model="sidebar" app location="end">
      <v-list>
        <p>hi</p>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app class="bg-grey-darken-1">
      <v-toolbar-title>
        <v-btn flat :to="{ name: 'home' }">HOME</v-btn>
      </v-toolbar-title>
      <v-toolbar-items class="hidden-xs">
        <v-btn flat :to="{ name: 'community' }">Community</v-btn>
        <v-btn :to="{ name: 'exchangeRate' }">환율 계산기</v-btn>
        <v-btn :to="{ name: 'products' }">Product</v-btn>
        <v-btn :to="{ name: 'map' }">Map</v-btn>
        <template v-if="user">
          <v-btn class="bg-grey-darken-3" @click="logOut">logOut</v-btn>
          <v-btn
            class="bg-grey-darken-3"
            :to="{ name: 'profile', params: { user_id: 1 } }"
            >My Page</v-btn
          >
        </template>
        <template v-else>
          <v-btn :to="{ name: 'logIn' }">logIn</v-btn>
          <v-btn :to="{ name: 'signUp' }">signUp</v-btn>
        </template>
      </v-toolbar-items>
      <v-app-bar-nav-icon
        @click="sidebar = !sidebar"
        class="hidden-sm-and-up"
      ></v-app-bar-nav-icon>
    </v-toolbar>
    <v-content>
      <div class="userInfo text-center">
        <h2 v-if="user?.nickname">Welcome, {{ user.nickname }}</h2>
        <h2 v-else-if="user">Welcome, {{ user.username }}</h2>
      </div>
      <RouterView />
    </v-content>
  </v-app>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useCommunityStore } from "./stores/community.js";
import { ref, onMounted, computed } from "vue";

const store = useCommunityStore();
const user = computed(() => store.userInfo);
const logOut = () => {
  store.logOut();
};
const sidebar = ref(false);
</script>

<style scoped></style>
