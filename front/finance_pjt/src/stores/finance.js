import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from 'axios'

export const useFinanceStore = defineStore("finance", () => {
  const BASE_URL = 'http://127.0.0.1:8000'

  const deposits = ref([])
  const savings = ref([])
  const getProducts = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/finance/products/get_product/`,
    })
      .then(res => {
        for (const data of res.data) {
          if (data.category === 0) {
            deposits.value.push(data)
          } else {
            savings.value.push(data)
          }
        }
      })
      .catch(err => console.log(err))
  }
  return { getProducts, deposits, savings };
}, { persist: true });
