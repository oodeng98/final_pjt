import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from '../router'


export const useCommunityStore = defineStore("community", () => {
  const token = ref(null)
  const userInfo = ref(null)

  const signUp = (payload) => {
    const {username, password1, password2, email ,first_name,last_name} = payload
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/signup/`,
      data:{
        username, password1, password2 , email ,first_name,last_name
      }
    }).then(res=>{
      console.log('signed up')
      const password = password1
      logIn({username, password})
    }).catch(err=> console.log(err))
  }

  const logIn = (payload) => {
    const {username, password} = payload
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/login/`,
      data:{
        username, password
      }
    }).then(res=>{
      console.log('signed In')
      token.value = res.data.key
      getUserInfo()
      router.push({name:'community'})
    }).catch(err=> {
      console.log(err)
    })
  }

  const getUserInfo = () => {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/accounts/user/',
      headers: {
        Authorization: `Token ${token.value}`,
      },
    }).then(res=>{
      userInfo.value = res.data
    })
  }

  const logOut = () => {
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/logout/`,
    }).then(res=>{
      console.log(res, 'log out')
      token.value = null
      userInfo.value =null
      router.go(0)
    }).catch(err=> console.log(err))
  }

  const isLogin = computed(() => token.value? true : false)

  return { signUp, logIn, logOut, token, isLogin, userInfo  };
}, { persist: true });
