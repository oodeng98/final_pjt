import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import router from '../router'


export const useCommunityStore = defineStore("community", () => {
  const token = ref(null)

  const signUp = (payload) => {
    const {username, password1, password2} = payload
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/signup/`,
      data:{
        username, password1, password2
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
      // console.log(res.data)
      token.value = res.data.key
      router.push({name:'community'})
    }).catch(err=> console.log(err))
  }

  const logOut = () => {
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/accounts/logout/`,
    }).then(res=>{
      console.log(res, 'log out')
      token.value = null
      router.push({name:'community'})
    }).catch(err=> console.log(err))
  }

  return { signUp, logIn, logOut, token  };
}, { persist: true });
