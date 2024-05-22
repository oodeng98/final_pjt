<template>
  <v-container>
    <!-- Carousel Section -->
    <v-carousel>
      <v-carousel-item
        src="https://www.ciokorea.com/files/itworld/ITW_202304_01/GettyImages-1273700255.jpg"
        cover
      ></v-carousel-item>
      <v-carousel-item
        src="https://live.lge.co.kr/wp-content/uploads/2020/06/AI%EC%9A%A9%EC%96%B4%EC%82%AC%EC%A0%84_00.jpg"
        cover
      ></v-carousel-item>
      <v-carousel-item
        src="https://www.hellot.net/data/photos/20231252/art_17039301013143_a3d6ec.jpg"
        cover
      ></v-carousel-item>
    </v-carousel>

    <!-- Recommendation Section -->
    <div class="text-h3 text-center">
      <br />
      최고의 금융 AI 추천 서비스를 체험하세요
    </div>
    <v-card class="pa-5 my-5 text-center">
      <v-card-title class="headline text-h4"
        >필요한 상품을 알려주세요</v-card-title
      >
      <v-card-text>
        <v-btn-toggle
          v-model="preference.type"
          color="deep-purple-accent-3"
          rounded="0"
          group
        >
          <v-btn value="예금상품"> 예금 </v-btn>
          <v-btn value="적금상품"> 적금 </v-btn>
          <v-btn value=""> 상관없음 </v-btn>
        </v-btn-toggle>
        <br />
        <v-btn-toggle
          v-model="preference.bank"
          color="deep-purple-accent-3"
          rounded="0"
          group
        >
          <v-btn value="국민은행"> 국민은행 </v-btn>
          <v-btn value="신한은행"> 신한은행 </v-btn>
          <v-btn value="NH농협은행"> NH농협은행 </v-btn>
          <v-btn value="우리은행"> 우리은행 </v-btn>
          <v-btn value=""> 상관없음 </v-btn>
        </v-btn-toggle>
        <br />
        <v-btn-toggle
          v-model="preference.month"
          color="deep-purple-accent-3"
          rounded="0"
          group
        >
          <v-btn value="1개월"> 1개월 </v-btn>
          <v-btn value="3개월"> 3개월 </v-btn>
          <v-btn value="6개월"> 6개월 </v-btn>
          <v-btn value="12개월"> 12개월 </v-btn>
          <v-btn value="24개월"> 24개월 </v-btn>
          <v-btn value="36개월"> 36개월 </v-btn>
        </v-btn-toggle>
        <br />
        <v-btn-toggle
          v-model="preference.join"
          color="deep-purple-accent-3"
          rounded="0"
          group
        >
          <v-btn value="인터넷"> 인터넷 </v-btn>
          <v-btn value="스마트폰"> 스마트폰 </v-btn>
          <v-btn value="영업점"> 영업점 </v-btn>
          <v-btn value="상관없음"> 상관없음 </v-btn>
        </v-btn-toggle>
      </v-card-text>
      <v-card-actions>
        <v-btn
          @click="surveyDone"
          :loading="gptLoading"
          color="deep-purple-accent-3"
          class="mx-auto border pa-3"
          size="x-large"
        >
          추천받기
        </v-btn>
      </v-card-actions>
    </v-card>

    <!-- Answer Section -->
    <v-card class="pa-5 text-center">
      <v-card-title class="headline text-h4">당신을 위한 상품은~?</v-card-title>
      <v-card-text>
        <p>{{ answer }}</p>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useFinanceStore } from "@/stores/finance";
import { useCommunityStore } from "@/stores/community";
import Dialog from "@/components/Dialog.vue";
const financeStore = useFinanceStore();
const communityStore = useCommunityStore();

const preference = ref({
  bank: "",
  join: "",
  month: "",
  type: "예금상품",
});
const gptLoading = ref(false);

const query = ref("");
const answer = ref("추천받기를 눌러보세요");

const conversation = ref([]);

const surveyDone = () => {
  gptLoading.value = true;
  const { bank, join, month, type } = preference.value;
  query.value =
    bank +
    " " +
    type +
    " 중 가입 방식은 " +
    join +
    ", 기간은 " +
    month +
    "인 상품 중에 가장 높은 금리 상품을 찾아줘";
  queryGPT();
};

const queryGPT = function () {
  conversation.value.push(query.value);
  axios({
    method: "get",
    url: `${financeStore.BASE_URL}/finance/products/gpt/`,
    params: {
      query: query.value,
    },
  })
    .then((res) => {
      answer.value = res.data.response;
      // console.log(answer.value);
      conversation.value.push(answer.value);
      gptLoading.value = false;
    })
    .catch((err) => console.log(err));
};
</script>

<style scoped>
.container {
  margin-top: 20px;
}
</style>
