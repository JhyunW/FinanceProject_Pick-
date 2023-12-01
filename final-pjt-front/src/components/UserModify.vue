<template>
  <div class="gray-opacity">
    <div style="display: flex; justify-content: center; height: 700px;">
      <form action="" class="form_main" @submit.prevent="changeUserInfo(nickname, email)">
        <p class="heading">Modify</p>
        <div class="inputContainer">
          <svg class="inputIcon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#E7B000"
            viewBox="0 0 16 16">
            <path
              d="M13.106 7.222c0-2.967-2.249-5.032-5.482-5.032-3.35 0-5.646 2.318-5.646 5.702 0 3.493 2.235 5.708 5.762 5.708.862 0 1.689-.123 2.304-.335v-.862c-.43.199-1.354.328-2.29.328-2.926 0-4.813-1.88-4.813-4.798 0-2.844 1.921-4.881 4.594-4.881 2.735 0 4.608 1.688 4.608 4.156 0 1.682-.554 2.769-1.416 2.769-.492 0-.772-.28-.772-.76V5.206H8.923v.834h-.11c-.266-.595-.881-.964-1.6-.964-1.4 0-2.378 1.162-2.378 2.823 0 1.737.957 2.906 2.379 2.906.8 0 1.415-.39 1.709-1.087h.11c.081.67.703 1.148 1.503 1.148 1.572 0 2.57-1.415 2.57-3.643zm-7.177.704c0-1.197.54-1.907 1.456-1.907.93 0 1.524.738 1.524 1.907S8.308 9.84 7.371 9.84c-.895 0-1.442-.725-1.442-1.914z">
            </path>
          </svg>
          <input type="text" class="inputField" id="nickname" placeholder="change nickname" v-model="nickname">
        </div>

        <div class="inputContainer">
          <svg class="inputIcon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#E7B000"
            viewBox="0 0 16 16">
            <path
              d="M13.106 7.222c0-2.967-2.249-5.032-5.482-5.032-3.35 0-5.646 2.318-5.646 5.702 0 3.493 2.235 5.708 5.762 5.708.862 0 1.689-.123 2.304-.335v-.862c-.43.199-1.354.328-2.29.328-2.926 0-4.813-1.88-4.813-4.798 0-2.844 1.921-4.881 4.594-4.881 2.735 0 4.608 1.688 4.608 4.156 0 1.682-.554 2.769-1.416 2.769-.492 0-.772-.28-.772-.76V5.206H8.923v.834h-.11c-.266-.595-.881-.964-1.6-.964-1.4 0-2.378 1.162-2.378 2.823 0 1.737.957 2.906 2.379 2.906.8 0 1.415-.39 1.709-1.087h.11c.081.67.703 1.148 1.503 1.148 1.572 0 2.57-1.415 2.57-3.643zm-7.177.704c0-1.197.54-1.907 1.456-1.907.93 0 1.524.738 1.524 1.907S8.308 9.84 7.371 9.84c-.895 0-1.442-.725-1.442-1.914z">
            </path>
          </svg>
          <input type="email" class="inputField" id="email" placeholder="change email" v-model="email">
        </div>
        <button id="button">Submit</button>
        <a class="forgotLink" href="#" @click="toUserPage()">back</a>
      </form>
    </div>
  </div>
</template>
  
<script setup>
import { ref, } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'


const store = useAuthStore()
const router = useRouter()
const nickname = ref('');
const email = ref('');

const token = store.token
const URL = 'http://127.0.0.1:8000/'

const changeUserInfo = (nickname, email) => {
  Swal.fire({
    title: "changes to your information",
    text: "Do you want to make changes to your information?",
    icon: "question",
    showCancelButton: true,
    confirmButtonText: 'modify',
    cancelButtonText: 'cancel',
    allowEscapeKey: true
  }).then((result) => {
    if (result.isConfirmed) {
      axios({
        method: 'put',
        url: `${URL}accounts/change-info/`,
        headers: {
          Authorization: `token ${token}`
        },
        data: {
          nickname,
          email,
        }
      }).then((res) => {
        console.log(res)
        store.user.nickname = nickname
        store.user.email = email
        router.push({ name: 'MyPage' })
      }).catch((err) => {
        console.log(err)
      })
    }
  })
};

const toUserPage = () => {
  router.push({ name: 'MyPage' })
}
</script>
  
  
<style scoped>
.gray-opacity {
    padding: 0;
    margin: 0;
    height: 100vh;
    background-color: rgba(128, 128, 128, 0.4);
    z-index: 9999;
}
.form_main {
  font-family: 'PFStardust';
  width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #060620;
  padding: 30px 30px 30px 30px;
  /* box-shadow: 0px 0px 40px rgba(0, 0, 0, 0.062); */
  position: relative;
  overflow: hidden;
}

.form_main::before {
  position: absolute;
  content: "";
  width: 400px;
  height: 400px;
  background-color: #00203F;
  transform: rotate(45deg);
  left: -200px;
  bottom: 300px;
  z-index: 1;
  border-radius: 30px;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.082);
}

.heading {
  font-size: 2em;
  color: #E7B000;
  font-weight: 700;
  margin: 5px 0 10px 0;
  z-index: 2;
}

.inputContainer {
  width: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
}

.inputIcon {
  position: absolute;
  left: 3px;
}

.inputField {
  font-family: "PFStardust";
  width: 100%;
  height: 30px;
  background-color: transparent;
  border: none;
  border-bottom: 2px solid rgb(173, 173, 173);
  margin: 10px 0;
  color: #E7B000;
  font-size: 1.2em;
  font-weight: 500;
  box-sizing: border-box;
  padding-left: 30px;
}

.inputField:focus {
  outline: none;
  border-bottom: 2px solid rgb(199, 114, 255);
}

.inputField::placeholder {
  color: #E7B000;
  font-size: 1.2em;
  font-weight: 500;
}

#button {
  font-family: "PFStardust";
  z-index: 2;
  position: relative;
  width: 100%;
  border: none;
  background-color: #0A5A7A;
  height: 40px;
  color: white;
  font-size: .8em;
  font-weight: 500;
  letter-spacing: 1px;
  margin: 10px;
  cursor: pointer;
}

#button:hover {
  background-color: rgb(126, 84, 255);
}

.forgotLink {
  z-index: 2;
  font-size: 24px;
  font-weight: 500;
  color: #E7B000;
  text-decoration: none;
  padding: 8px 15px;
  border-radius: 20px;
}
</style>