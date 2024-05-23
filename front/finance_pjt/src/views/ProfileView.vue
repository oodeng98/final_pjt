<template>
  <div>
    <h1>
      {{ info?.nickname ? info.nickname : info.username }}님의 프로필 페이지
    </h1>

    <div class="infoView" v-show="!updateView">
      <v-card title="기본 정보" variant="outlined">
        <v-card-text>
          <p>회원 번호 : {{ info.id }}</p>
          <p>ID : {{ info.username }}</p>
          <p>닉네임 : {{ info.nickname }}</p>
          <p>email : {{ info.email }}</p>
          <p>first name : {{ info.first_name }}</p>
          <p>last name : {{ info.last_name }}</p>
          <br />
          <p>가입한 상품들</p>
          <ul>
            <li
              v-for="subscribe in subscribes"
              :key="subscribe.id"
              @click="
                router.push({
                  name: 'detail',
                  params: { product_id: subscribe.product.id },
                })
              "
            >
              {{ subscribe.product.fin_prdt_nm }}
            </li>
          </ul>
        </v-card-text>
        <v-card-actions>
          <v-btn
            @click="
              () => {
                updateView = !updateView;
              }
            "
            variant="outlined"
            >정보 수정</v-btn
          >
        </v-card-actions>
      </v-card>
    </div>
    <div class="changeView" v-show="updateView">
      <form @submit.prevent="update">
        <h4>기본 정보 수정</h4>
        <v-text-field label="Email" v-model="email"></v-text-field>
        <v-text-field label="First Name" v-model="first_name"></v-text-field>
        <v-text-field label="Last Name" v-model="last_name"></v-text-field>
        <v-text-field label="닉네임" v-model="nickname"></v-text-field>
        <v-btn
          @click="
            () => {
              updateView = !updateView;
            }
          "
          variant="outlined"
          style="margin-right: 4px"
          >돌아가기</v-btn
        >
        <v-btn type="submit" variant="outlined">업데이트</v-btn>
      </form>
    </div>
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
import router from "@/router";

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
  first_name.value = communityStore.userInfo.first_name;
  last_name.value = communityStore.userInfo.last_name;
});

const initChart = (data) => {
  const labels = [];
  const profits = [];
  data.forEach((element) => {
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

<style scoped>
.v-card-text > p {
  font-size: 18px;
  padding: 2px;
}

li {
  margin-left: 40px;
  font-size: 18px;
}
</style>
