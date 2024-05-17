import { createRouter, createWebHistory } from "vue-router";
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import ProductDetailView from '../views/ProductDetailView.vue'
import ExchangeRateView from '../views/ExchangeRateView.vue'
import MapView from '../views/MapView.vue'
import CommunityView from '../views/CommunityView.vue'
import CommunityDetailView from '../views/CommunityDetailView.vue'
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
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/product/:product_id',
      name: 'productDetail',
      component: ProductDetailView
    },
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
      path: '/community/:article_id',
      name: 'communityDetail',
      component: CommunityDetailView
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
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ],
});

export default router;
