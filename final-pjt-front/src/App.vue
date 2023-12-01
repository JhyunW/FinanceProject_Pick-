<script setup>
import { computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useAuthStore } from './stores/auth';
import Swal from 'sweetalert2'

const store = useAuthStore();
const isAuthenticated = computed(() => {
  return store.isAuthenticated;
});

const cat = () => {
  Swal.fire({
    title: "Nyan Nyan Nyan Nyan Nyan Nyan Nyan Nyan Nyan Nyan",
    width: 600,
    padding: "3em",
    color: "#716add",
    background: "#fff url(/images/trees.png)",
    confirmButtonColor :'#716add',
    confirmButtonText: 'Nyan',
    backdrop: `
    rgba(0,51,102,1)
    url("src/assets/nyan-cat.gif")
    center top
  `
  });
}
</script>

<template>
  <nav class="navbar">
    <img @click="cat" class="logo" src="@/assets/logo.png" alt="" />
    <div class="nav-links">
      <RouterLink to="/" class="nav-link">Main</RouterLink>
      <RouterLink to="/list" class="nav-link">List</RouterLink>
      <RouterLink to="/exchange" class="nav-link">Exchange</RouterLink>
      <RouterLink v-if="isAuthenticated" to="/mypage" class="nav-link"
        >Mypage</RouterLink
      >
      <RouterLink v-if="isAuthenticated" to="/logout" class="nav-link"
        >Logout</RouterLink
      >
      <!-- <div v-if="isAuthenticated" class="ifLogin" @click="store.logOut()">
        LogOut
      </div> -->
    </div>
  </nav>
  <RouterView />
</template>

<style scoped>
/* @font-face {
  font-family: 'PFStardust';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/PFStardust.woff') format('woff');
  font-weight: normal;
  font-style: normal;
} */

.navbar {
  background-color: black;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: Arial, sans-serif;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  position: relative; /* relative 포지션을 추가 */
}
.ifLogin {
  padding: 10px;
  display: flex;
  align-items: center;
  font-family: Arial, sans-serif;
}

.navbar::after {
  content: '';
  position: absolute;
  bottom: 0; /* 아래에 위치하도록 설정 */
  left: 0;
  width: 100%;
  height: 2px; /* 높이 설정 */
  background-color: yellow; /* 노란색 설정 */
}

.logo {
  /* max-width: 100px;
  max-height: 50px; */
  width: 15%; /* 이미지의 가로 크기를 최대한 활용 */
  height: auto; /* 세로 크기는 자동으로 조절 */
}

.nav-links {
  font-family: 'PFStardust';
  display: flex;
  gap: 30px;
  font-size: 1.2rem;
}

.nav-link {
  color: yellow;
  text-decoration: none;
  position: relative;
  transition: color 0.3s;
  border-radius: 20px;
  padding: 10px 20px;
}

.nav-link:hover {
  color: white;
}

.nav-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 20px;
  background-color: rgba(255, 255, 255, 0.1);
  transform: scale(0);
  transition: transform 0.5s;
}

.nav-link:hover::before,
.nav-link.active::before {
  transform: scale(1);
}

@media screen and (max-width: 768px) {
  .navbar {
    flex-direction: column;
  }

  .nav-links {
    flex-direction: column;
    align-items: center;
  }

  .nav-link {
    margin-top: 10px;
  }
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
.navbar:hover {
  background: linear-gradient(
    45deg,
    rgb(108, 103, 105),
    rgb(44, 44, 37),
    rgb(87, 88, 78),
    rgb(38, 38, 37)
  );
  background-size: 300% 300%;
  animation: gradient 4s ease infinite;
}
</style>
<style>
@font-face {
  font-family: 'PFStardust';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/PFStardust.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: 'PFStardust';
}
</style>
