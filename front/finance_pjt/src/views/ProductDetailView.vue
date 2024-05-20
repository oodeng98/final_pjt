<template>
  <div>
    <h1>{{ category }}</h1>
    <button @click="subscribe">{{comment}}</button>
    {{ product[0] }}
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

const route = useRoute()
const { product_id } = route.params

const product = ref([])
const category = ref(null)
const comment = ref('가입하기')

let isSubscribe = true

onMounted(() => {
  product.value = store.deposits.filter((element) => element.id == product_id)
  category.value = '정기예금 상세'
  if (product.value.length === 0) {
    product.value = store.savings.filter((element) => element.id == product_id)
    category.value = '정기적금 상세'
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