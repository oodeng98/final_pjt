import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import DepositView from '../views/DepositView.vue'
import SavingView from "@/views/SavingView.vue";
import ProductDetailView from '../views/ProductDetailView.vue'
import ExchangeRateView from '../views/ExchangeRateView.vue'
import MapView from '../views/MapView.vue'
import CommunityView from '../views/CommunityView.vue'
import CommunityCreateView from '../views/CommunityCreateView.vue'
import CommunityDetailView from '../views/CommunityDetailView.vue'
import CommunityUpdateView from '../views/CommunityUpdateView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from '../views/SignUpView.vue'
import ProfileView from '../views/ProfileView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductView,
      children: [
        { path: 'deposit', name: "deposit", component: DepositView },
        { path: 'saving', name: "saving", component: SavingView },
        { path: ':category/:product_id', name: 'productDetail', component: ProductDetailView }
      ]
    },
    // {
    //   path: '/product/:category/:product_id',
    //   name: 'productDetail',
    //   component: ProductDetailView
    // },
    {
      path: '/exchange-rate',
      name: 'exchangeRate',
      component: ExchangeRateView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/community/create',
      name: 'communityCreate',
      component: CommunityCreateView
    },
    {
      path: '/community/:article_id',
      name: 'communityDetail',
      component: CommunityDetailView
    },
    {
      path: '/community/:article_id/update',
      name: 'communityUpdate',
      component: CommunityUpdateView
    },
    {
      path: '/accounts/login',
      name: 'logIn',
      component: LoginView
    },
    {
      path: '/accounts/signup',
      name: 'signUp',
      component: SignUpView
    },
    {
      path: '/accounts/:user_id',
      name: 'profile',
      component: ProfileView
    },
  ],
});

import { useCommunityStore } from '@/stores/community'


router.beforeEach((to, from) => {
  const store = useCommunityStore()
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (!(to.name === 'logIn' || to.name === 'signUp' || to.name === 'home') && store.isLogin === false) {
    return { name: 'logIn' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'logIn' || to.name === 'signUp') && (store.isLogin === true)) {
    return { name: 'home' }
  }
})

export default router;
