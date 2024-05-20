<template>
  <div>
    <h1 v-if="category === 'deposit'">정기예금 상세</h1>
    <h1 v-else>정기적금 상세</h1>
    <button @click="subscribe">{{comment}}</button>
    <div v-for="info in product">
      {{ info }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

import { useFinanceStore } from '@/stores/finance'
import { useCommunityStore} from '@/stores/community'
import router from '@/router'

const store = useFinanceStore()
const communityStore = useCommunityStore()
const product = ref([])
const route = useRoute()
const { category, product_id } = route.params
const comment = ref('가입하기')
let isSubscribe = true

onMounted(() => {
  if (category === 'deposit') {
    product.value = store.deposits.filter((element) => element.id == product_id)
  } else {
    product.value = store.savings.filter((element) => element.id == product_id)
  }

  axios({
    method: 'get',
    url: `${store.BASE_URL}/finance/products/subscribe/`,
    params: {
      product: product_id
    }, 
    headers:{
      Authorization: `Token ${communityStore.token}`
    }
  })
    .then(res => {
      if (0 < res.data.length){
        isSubscribe = true
      } else{
        isSubscribe = false
      }
      if (isSubscribe){
       comment.value = '해지하기'
      }
      console.log(res.data)
    })
    .catch(err => {
      console.log(err)
    })
})

const subscribe = function () {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/finance/products/subscribe/`,
    data: {
      product: product_id
    }, 
    headers:{
      Authorization: `Token ${communityStore.token}`
    }
  })
    .then(res => {
      console.log(res)
      router.go(-1)
    })
    .catch(res => {
      console.log(res)
    })
}
</script>

<style scoped>

</style>