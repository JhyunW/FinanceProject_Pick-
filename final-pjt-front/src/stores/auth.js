import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { defineStore } from 'pinia';
import Swal from 'sweetalert2'

export const useAuthStore = defineStore(
  'auth',
  () => {
    const user = ref({});
    const router = useRouter();
    const token = ref('');
    const isAuthenticated = ref(false);
    const URL = 'http://127.0.0.1:8000/';

    const signUp = function (email, nickname, username, password1, password2) {
      console.log(username, password1);
      axios({
        method: 'post',
        // url을 dj-rest-auth로 변경
        url: `${URL}dj-rest-auth/registration/`,
        data: {
          email,
          nickname,
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          token.value = res.data.key;
          isAuthenticated.value = true;
          // user.nickname = nickname
          Swal.fire({
            title: "Good job!",
            text: "go to main page",
            icon: "success",
            confirmButtonText: '확인',
            allowEscapeKey: true
          }).then((result) => {
            if (result.isConfirmed) {
              logIn(username, password1)
            }
          })
        })
        .catch((err) => {
          if (password1 !== password2) {
            Swal.fire({
              title: 'Error!',
              text: 'password do not match',
              icon: 'error',
              confirmButtonText: 'check your password',
              allowEscapeKey: true
            })
          }
          if (!email) {
            Swal.fire({
              title: 'Error!',
              text: 'Email is empty',
              icon: 'error',
              confirmButtonText: 'check your password',
              allowEscapeKey: true
            })
          }
        });
    };

    const logIn = function (username, password) {
      axios({
        method: 'post',
        url: `${URL}dj-rest-auth/login/`,
        data: {
          username,
          password,
        },
      }).then((res) => {
        token.value = res.data.key;
        isAuthenticated.value = true;
        console.log(res.data);
        axios({
          method: 'get',
          url: `${URL}dj-rest-auth/user/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        }).then((res) => {
          axios({
            method: 'get',
            url: `${URL}accounts/get-user/${username}`,
          }).then((res) => {
            user.value = res.data
          })
          router.push({ name: 'Main' });
        });
      }).catch((err) => {
        Swal.fire({
          title: 'Error!',
          text: 'id or password is incorrect',
          icon: 'error',
          confirmButtonText: 'check your input',
          allowEscapeKey: true
        })
      });
    };

    const logOut = function () {
      Swal.fire({
        title: "<u><string>Log Out</string></u> ",
        text: "Would you like to log out?",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: 'logout',
        cancelButtonText: 'cancel',
        allowEscapeKey: true,
      }).then((result) => {
        if (result.isConfirmed) {
          isAuthenticated.value = false;
          token.value = '';
          user.value = {};
          router.push({ name: 'Main' });
        }
      })

    };

    // 개인정보 변경 함수
    const changeUserInfo = (newUserName, newUserEmail) => {
      axios({
        method: 'patch',
        // url: `${URL}dj-rest-auth/` => 이거 다음 주소를 모르겠엉..
        // url: `${URL}path/to/update/user/info/`,
        headers: {
          Authorization: `token ${token.value}`,
        },
        data: {
          newUserName,
          newUserEmail,
        },
      })
        .then((res) => {
          console.log(res);
          // 성공 시 처리 (예를 들어 성공 메시지 표시) => 완료 alert같은거 호출하기?
        })
        .catch((err) => {
          console.error(err);
          // 에러 처리 (예를 들어 에러 메시지 표시) => 실패 alert같은거
        });
    };

    return {
      signUp,
      logIn,
      logOut,
      changeUserInfo,
      token,
      isAuthenticated,
      user,
    };
  },
  { persist: true }
);
