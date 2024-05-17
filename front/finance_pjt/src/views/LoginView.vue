<template>
  <div>
    <h1>SignIn Page</h1>
    <form @submit.prevent="logIn">
      <p>
        <label for="username">username : </label>
        <input type="text" v-model="username" />
      </p>
      <p>
        <label for="password">password : </label>
        <input type="text" v-model="password" />
      </p>
      <input type="submit" value="SIGN IN" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCommunityStore } from "../stores/community";
import { useRouter } from "vue-router";

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
  // router.push({ name: "home" });
};
</script>

<style scoped></style>
