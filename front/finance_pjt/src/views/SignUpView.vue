<template>
  <v-container class="d-flex justify-center align-center fill-height">
    <v-card class="pa-5" min-width="600">
      <v-card-title class="text-center">
        <span class="text-h3">회원가입</span>
      </v-card-title>
      <v-spacer></v-spacer>
      <v-card-text>
        <v-form @submit.prevent="signUp">
          <v-text-field
            variant="outlined"
            v-model="username"
            label="Username"
            prepend-icon="mdi-account"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="password1"
            label="Password"
            type="password"
            prepend-icon="mdi-lock"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="password2"
            label="Confirm Password"
            type="password"
            prepend-icon="mdi-lock"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="email"
            label="Email"
            type="email"
            prepend-icon="mdi-email"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="nickname"
            label="Nickname"
            prepend-icon="mdi-account-circle"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="first_name"
            label="First Name"
            prepend-icon="mdi-account-box"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="last_name"
            label="Last Name"
            prepend-icon="mdi-account-box-outline"
            required
          ></v-text-field>
          <v-btn color="primary" type="submit" class="mt-4" block>
            회원가입
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useCommunityStore } from "../stores/community";
import { useRouter } from "vue-router";

const username = ref("");
const password1 = ref("");
const password2 = ref("");
const email = ref("");
const first_name = ref("");
const last_name = ref("");
const nickname = ref("");

const store = useCommunityStore();
const router = useRouter();

const signUp = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    first_name: first_name.value,
    last_name: last_name.value,
    nickname: nickname.value,
  };

  store
    .signUp(payload)
    .then(() => {
      router.push({ name: "home" }); // 회원가입 성공 시 홈 페이지로 이동
    })
    .catch((err) => {
      console.error(err);
      alert("회원가입에 실패했습니다.");
    });
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
</style>
