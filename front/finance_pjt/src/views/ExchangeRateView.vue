<template>
  <div>
    <h1>환율 계산기</h1>
    <p>
      비영업일의 데이터, 혹은 영업당일 11시 이전에는 환율 계산기가 제대로
      작동하지 않습니다.
    </p>
    <select name="country" v-model="selectCountry" @change="change">
      <option v-for="country in countries" :value="country">
        {{ country.cur_nm }}
      </option>
    </select>
    <input type="text" v-model="foreignCurrency" @input="input1" />
    <br />
    <input type="text" v-model="koreaCurrency" @input="input2" />
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community";

const countries = ref([]);
const selectCountry = ref("");
const foreignCurrency = ref("");
const koreaCurrency = ref("");
let changeRate = 1;
let userTarget = "input1";

onMounted(() => {
  const store = useCommunityStore();
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/finance/exchange_rate/",
    headers: {
      Authorization: store.token,
    },
  })
    .then((res) => {
      for (const data of res.data) {
        countries.value.push(data);
      }
    })
    .catch((err) => {
      console.log(err);
    });
});

const change = function () {
  const target = countries.value.find((ele) => {
    return ele.cur_nm === selectCountry.value.cur_nm;
  });
  changeRate = target.kftc_deal_bas_r;
  if (userTarget == "input1") {
    input1();
  } else {
    input2();
  }
};

const input1 = function () {
  koreaCurrency.value = (foreignCurrency.value * changeRate).toFixed(2);
  userTarget = "input1";
};

const input2 = function () {
  foreignCurrency.value = (koreaCurrency.value / changeRate).toFixed(2);
  userTarget = "input2";
};
</script>

<style scoped></style>
