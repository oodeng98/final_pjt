<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <p>
        <label for="username">username : </label>
        <input type="text" v-model="username" />
      </p>
      <p>
        <label for="password1">password1 : </label>
        <input type="text" v-model="password1" />
      </p>
      <p>
        <label for="password2">password2 : </label>
        <input type="text" v-model="password2" />
      </p>
      <p>
        <label for="email">email : </label>
        <input type="email" v-model="email" />
      </p>
      <p>
        <label for="first_name">first_name : </label>
        <input type="text" v-model="first_name" />
      </p>
      <p>
        <label for="last_name">last_name : </label>
        <input type="text" v-model="last_name" />
      </p>
      <input type="submit" value="SIGN UP" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCommunityStore } from "../stores/community";
import { useRouter } from "vue-router";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const first_name = ref(null);
const last_name = ref(null);
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
  };
  store.signUp(payload);
  // console.log("signed up!!");
  // router.push({ name: "home" });
};
</script>

<style scoped></style>
