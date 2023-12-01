<template>
  <div>
    <h1>사용자 설정</h1>
    <!-- store에 등록한 chagneUser함수 사용로직 자세히 알아야할듯; 그리고 chagne유저 로직에 주소 흔오한테 물어보자 -->
    <label for="newUserName">새로운 사용자 이름: </label>
    <input v-model="newUserName" type="text" id="newUserName" name="newUserName" />

    <label for="newUserEmail">새로운 이메일: </label>
    <input v-model="newUserEmail" type="email" id="newUserEmail" name="newUserEmail" />

    <button @click="store.changeUserInfo()">사용자 정보 변경</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useAuthStore } from '@/stores/auth.js';
import { ref } from 'vue';

const store = useAuthStore();
const newUserName = ref('');
const newUserEmail = ref('');

store.changeUserInfo(newUserName.value, newUserEmail.value);
// 가능하면 밑에 함수 store에 넣고 사용해보기
// const changeUserInfo = () => {
//   axios({
//     method: 'patch',
//     // url: `${URL}dj-rest-auth/` => 이거 다음 주소를 모르겠엉..
//     // url: `${URL}path/to/update/user/info/`,
//     headers: {
//       Authorization: `token ${token}`,
//     },
//     data: {
//       newUserName: newUserName.value,
//       newUserEmail: newUserEmail.value,
//     },
//   })
//     .then((res) => {
//       console.log(res);
//       // 성공 시 처리 (예를 들어 성공 메시지 표시) => 완료 alert같은거 호출하기?
//     })
//     .catch((err) => {
//       console.error(err);
//       // 에러 처리 (예를 들어 에러 메시지 표시) => 실패 alert같은거
//     });
// };
</script>

<style scoped>
</style>
