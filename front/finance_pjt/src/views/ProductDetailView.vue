<template>
  <div>
    <div style="display: flex">
      <h2 style="margin-right: 5px">{{ category }}</h2>
    </div>
    <v-card
      :title="product[0]?.kor_co_nm + ' ' + product[0]?.fin_prdt_nm"
      variant="outlined"
    >
      <v-card-text>
        <div><strong>가입 방법: </strong>{{ product[0]?.join_way }}</div>
        <div>
          <strong>우대 조건</strong>
          <ul>
            <template v-for="condition in product[0]?.spcl_cnd.split(')')">
              <li v-if="condition.trim()" style="margin-left: 30px">
                {{ condition.trim() }})
              </li>
            </template>
          </ul>
        </div>
        <div><strong>가입 조건: </strong>{{ product[0]?.join_member }}</div>
        <div><strong>기타 유의사항: </strong>{{ product[0]?.join_member }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn
          v-if="communityStore.token"
          @click="subscribe"
          variant="outlined"
          width="70px"
          >{{ comment }}</v-btn
        >
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

import { useFinanceStore } from "@/stores/finance";
import { useCommunityStore } from "@/stores/community";
import router from "@/router";

const financeStore = useFinanceStore();
const communityStore = useCommunityStore();

const route = useRoute();
const { product_id } = route.params;

const product = ref([]);
const category = ref(null);
const comment = ref("가입하기");

let isSubscribe = true;

onMounted(() => {
  product.value = financeStore.deposits.filter(
    (element) => element.id == product_id
  );
  category.value = "정기예금 상세";
  if (product.value.length === 0) {
    product.value = financeStore.savings.filter(
      (element) => element.id == product_id
    );
    category.value = "정기적금 상세";
  }

  axios({
    method: "get",
    url: `${financeStore.BASE_URL}/finance/products/subscribe/`,
    params: {
      product: product_id,
    },
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      if (0 < res.data.length) {
        isSubscribe = true;
      } else {
        isSubscribe = false;
      }
      if (isSubscribe) {
        comment.value = "해지하기";
      }
    })
    .catch((err) => {
      console.log(err);
    });
});

const subscribe = function () {
  axios({
    method: "post",
    url: `${financeStore.BASE_URL}/finance/products/subscribe/`,
    data: {
      product: product_id,
    },
    headers: {
      Authorization: `Token ${communityStore.token}`,
    },
  })
    .then((res) => {
      router.go(-1);
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.v-card-text > div {
  padding: 2px;
}
</style>
