<template>
  <div>
    <h1>환율 계산기</h1>
    <p>
      비영업일의 데이터, 혹은 영업당일 11시 이전에는 환율 계산기가 제대로
      작동하지 않습니다.
    </p>
    <select name="country" v-model="selectCountry" @change="change">
      <option v-for="country in countries" :value="country"></option>
      <option value="USA">미국 달러</option>
    </select>
    <input type="text" v-model="foreignCurrency" />
    <br />
    <input type="text" v-model="koreaCurrency" />
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

onMounted(() => {
  axios({
    method: "get",
    url: "http://127.0.0.1:8000/finance/exchange_rate/",
    // headers: {
    //   Authorization: "",
    // },
  })
    .then((res) => {
      const countries = ref([]);
      for (data in res.data) {
        countries.value.push(data.cur_nm);
      }
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
});

const selectCountry = ref("");
const foreignCurrency = ref("");
const koreaCurrency = ref("");

const change = function () {
  console.log("change");
  console.log(country.value);
};
</script>

<style scoped></style>
