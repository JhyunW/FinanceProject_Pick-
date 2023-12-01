import { createRouter, createWebHistory } from 'vue-router';
import MainView from '@/views/MainView.vue';
import ListView from '@/views/ListView.vue';
import ModifyView from '@/components/UserModify.vue';
import ListDetailModalView from '@/components/ListDetailModal.vue';
import ExchangeView from '@/views/ExchangeView.vue';
import MyPageView from '@/views/MyPageView.vue';
import LogIn from '@/components/LogIn.vue';
import SignUp from '@/components/SignUp.vue';
import Category from '@/components/Category.vue';
import { useAuthStore } from '../stores/auth.js';
import Comparison from '@/components/Comparison.vue';
import UserSetting from '@/components/UserSetting.vue';
import LogOut from '@/components/LogOut.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 메인 페이지
      path: '/',
      name: 'Main',
      component: MainView,
    },
    {
      // 리스트 페이지
      path: '/list',
      name: 'List',
      component: ListView,
    },
    {
      // 디테일 모달 페이지
      path: '/:financeId',
      name: 'ListDetailModal',
      component: ListDetailModalView,
    },
    {
      // 비교 페이지
      path: '/comparison',
      name: 'Comparison',
      component: Comparison,
    },
    {
      // 환율 페이지
      path: '/exchange',
      name: 'Exchange',
      component: ExchangeView,
    },
    {
      // 마이 페이지
      path: '/mypage',
      name: 'MyPage',
      component: MyPageView,
    },
    {
      // 로그아웃 페이지
      path: '/logout',
      name: 'LogOut',
      component: LogOut,
      beforeEnter: (to, from) => {
        const store = useAuthStore();
        if (store.isAuthenticated) {
          store.logOut();
          return { name: 'Main' };
        }
      },
    },
    {
      // 회원정보 변경 페이지
      path: '/usersetting',
      name: 'UserSetting',
      component: UserSetting,
    },
    {
      // 로그인 창
      path: '/login',
      name: 'LogIn',
      component: LogIn,
      beforeEnter: (to, from) => {
        const store = useAuthStore();
        if (store.isAuthenticated) {
          store.logOut();
          return { name: 'Main' };
        }
      },
    },
    {
      // 회원가입 창
      path: '/signup',
      name: 'signup',
      component: SignUp,
      beforeEnter: (to, from) => {
        const store = useAuthStore();
        if (store.isAuthenticated) {
          return { name: 'Main' };
        }
      },
    },
    {
      path: '/modify',
      name: 'modify',
      component: ModifyView,
    },
    {
      path: '/category/:categoryName',
      name: 'category',
      component: Category,
    },
  ],
});

router.beforeEach((to, from) => {
  const store = useAuthStore();
  // if (to.name != 'login' && to.name != 'signup' && !store.isAuthenticated ) {
  //   return { name: 'login' }
  // }
});

export default router;
