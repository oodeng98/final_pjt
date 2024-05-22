<template>
  <div>
    <h1>
      {{ info?.nickname ? info.nickname : info.username }}님의 프로필 페이지
    </h1>

    <div class="infoView" v-show="!updateView">
      <v-btn
        @click="
          () => {
            updateView = !updateView;
          }
        "
        >정보 수정</v-btn
      >
      <p>회원 번호 : {{ info.id }}</p>
      <p>ID : {{ info.username }}</p>
      <p>닉네임 : {{ info.nickname }}</p>
      <p>email : {{ info.email }}</p>
      <p>first name : {{ info.first_name }}</p>
      <p>last name : {{ info.last_name }}</p>
    </div>
    <div class="changeView" v-show="updateView">
      <v-btn
        @click="
          () => {
            updateView = !updateView;
          }
        "
        >정보 보기</v-btn
      >
      <h3>기본 정보 수정</h3>
      <form @submit.prevent="update">
        <v-text-field label="Email" v-model="email"></v-text-field>
        <v-text-field label="First Name" v-model="first_name"></v-text-field>
        <v-text-field label="Last Name" v-model="last_name"></v-text-field>
        <v-text-field label="닉네임" v-model="nickname"></v-text-field>
        <v-btn type="submit">업데이트</v-btn>
      </form>
    </div>
    <p>가입한 상품들</p>
    <ul>
      <li v-for="subscribe in subscribes" :key="subscribe.id">
        <RouterLink
          :to="{ name: 'detail', params: { product_id: subscribe.product.id } }"
        >
          {{ subscribe.product.fin_prdt_nm }}
        </RouterLink>
      </li>
    </ul>
  </div>
  <div class="chart">
    <canvas ref="barChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { useCommunityStore } from "@/stores/community";
import { useFinanceStore } from "@/stores/finance";

import axios from "axios";
import { computed } from "vue";

import { Chart } from "chart.js/auto";

const subscribes = ref([]);
const route = useRoute();
const communityStore = useCommunityStore();
const financeStore = useFinanceStore();
const info = computed(() => communityStore.userInfo);
const email = ref(null);
const nickname = ref(null);
const first_name = ref(null);
const last_name = ref(null);
const updateView = ref(false);

const barChart = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/finance/products/subscribe_list/",
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      subscribes.value = res.data;
      initChart(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
  email.value = communityStore.userInfo.email;
  nickname.value = communityStore.userInfo.nickname;
});

const initChart = (data) => {
  const labels = [];
  const profits = [];
  data.forEach((element) => {
    console.log(element)
    labels.push(element.product.fin_prdt_nm);
    profits.push(element.profit);
  });

  const ctx = barChart.value.getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "수익 (대한민국 원)",
          backgroundColor: [
            "#3e95cd",
            "#8e5ea2",
            "#3cba9f",
            "#e8c3b9",
            "#c45850",
          ],
          data: profits,
        },
      ],
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: "그래프",
      },
    },
  });
};

const update = () => {
  axios({
    method: "put",
    url: `http://127.0.0.1:8000/accounts/${communityStore.userInfo.id}/`,
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
    data: {
      email: email.value,
      nickname: nickname.value,
      first_name: first_name.value,
      last_name: last_name.value,
    },
  })
    .then((res) => {
      communityStore.userInfo = res.data;
      updateView.value = false;
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
