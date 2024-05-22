<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-5" min-width="500">
      <v-card-title class="text-center">
        <span class="text-h3">로그인</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="logIn">
          <v-text-field
            variant="outlined"
            v-model="username"
            label="Username"
            prepend-icon="mdi-account"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="password"
            label="Password"
            type="password"
            prepend-icon="mdi-lock"
            required
          ></v-text-field>
          <v-btn color="primary" type="submit" class="mt-4" block>
            로그인
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useCommunityStore } from "../stores/community";

const username = ref(null);
const password = ref(null);
const router = useRouter();
const store = useCommunityStore();

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
</style>
