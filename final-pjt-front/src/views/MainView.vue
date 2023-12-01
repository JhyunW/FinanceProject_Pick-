<template>
  <div style="text-align: center;">
    <!--유저정보 이용해서-->
    <!--if 사용해서 LoginMainView와 NotLoginMainView 다르게 렌더링-->
    <div v-if="isLogin">
      <LogInMainView />
    </div>
    <div v-else>
      <NotLogInMainView />
    </div>
  </div>
</template>

<script setup>
import LogInMainView from '@/views/LogInMainView.vue'; // 로그인이 되어있을때 보여줄 페이지
import NotLogInMainView from '@/views/NotLogInMainview.vue'; // 로그인이 안되어 있을때 보여줄 페이지
import { useAuthStore } from '@/stores/auth';
import { computed } from 'vue';

const store = useAuthStore();
const isLogin = computed(() => store.isAuthenticated);
</script>

<style scoped>
@font-face {
  font-family: 'PFStardust';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/PFStardust.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
h1 {
  font-family: 'PFStardust';
}

</style>
