<template>
  <div class="commentSection">
    <div class="messages">
      <div
        v-for="comment in store.computedComment.slice().reverse()"
        :key="comment.id"
        class="message message-left"
      >
        <div class="message-container">
          <div class="avatar"></div>
          <div class="balloon balloon-left">
            <div>
              {{ comment.user.nickname }} <br />
              {{ comment.content }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="line"></div>
    <!-- 댓글 경계선 -->
    <form @submit.prevent="handleFormSubmit">
      <label for="comment">댓글 입력 : </label>
      <input type="text" id="comment" placeholder="comment" v-model="comment" />
      <button>댓글 작성</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useCommentStore } from '@/stores/comment.js';

const authStore = useAuthStore();
const store = useCommentStore();
const userName = authStore.user.username;
const userNickname = authStore.user.nickname;
const userEmail = authStore.user.email;
const token = authStore.token;

const comments = ref([]);
const comment = ref('');

const { product } = defineProps(['product']);
const productCodeNumber = product.fin_prdt_cd;

const handleFormSubmit = () => {
  console.log('폼 작동완료');
  store.commentPlus(productCodeNumber, comment.value, userName);
  comments.value = store.listComment;
  comment.value = ''; // 댓글 입력 값 비우기
};

onMounted(() => {
  store.getCommentList(product.id);
  comments.value = store.listComment;
});

onBeforeUnmount(() => {
  comments.value = [];
  console.log(comments);
});
</script>

<style scoped>
*,
::after,
::before {
  box-sizing: border-box;
}

body {
  font-family: 'Press Start 2P', cursive;
  line-height: 1.5;
  font-size: 16px;
  margin: 0;
  background-color: #0c0c0c; /* 어두운 배경색으로 변경 */
  color: #ffffff; /* 텍스트 색상을 밝은 색으로 변경 */
}

.avatar {
  width: 50px;
  min-width: 50px;
  height: 50px;
  background: #000;
  border-radius: 8px;
  display: inline-block;
  margin-bottom: -35px;
}

.messages {
  margin: 0 auto;
  width: 500px;
  height: 400px;
  display: flex;
  flex-direction: column;
  overflow-x: auto;
  overflow-y: auto;
  white-space: nowrap;
  max-width: calc(100% - 20px);
}

.message {
  margin: 30px 0;
  display: flex;
  width: 100%;
  white-space: normal;
}

.message-container {
  display: flex;
  align-items: flex-end;
  width: 100%;
}

@media (max-width: 520px) {
  .message-container {
    flex-direction: column;
  }

  .avatar {
    margin-top: 50px;
  }

  .message-left .message-container {
    align-items: flex-start;
    flex-direction: column-reverse;
  }
}

.message-left .message-container {
  justify-content: flex-start;
}

.message-left {
  align-self: flex-start;
}
.message-left .avatar {
  margin-right: 20px;
}

.balloon {
  width: 200px;
  max-width: 100%;
  padding: 7px;
  box-sizing: border-box;
  position: relative;
  box-shadow: 0 5px #1a1a1a, 0 10px #000, 0 -5px #1a1a1a, 0 -10px #000,
    -5px 0 #1a1a1a, -10px 0 #000, 5px 0 #1a1a1a, 10px 0 #000, 5px 5px #000,
    -5px -5px #000, -5px 5px #000, 5px -5px #000;
}

.balloon p {
  word-wrap: break-word;
}

.balloon-right:after,
.balloon-left:after {
  content: '';
  position: absolute;
  background: #000;
  width: 5px;
  height: 5px;
}

.balloon-left:after {
  bottom: -15px;
  left: 10%;
  box-shadow: 5px -5px #1a1a1a, 10px -5px #1a1a1a, 15px -5px #1a1a1a,
    20px -5px #1a1a1a, 25px -5px #1a1a1a, 0 5px #000, -5px 10px #000,
    -10px 15px #000, -10px 20px #000, -5px 20px #000, 0 20px #000, 5px 20px #000,
    10px 20px #000, 15px 20px #000, 20px 15px #000, 25px 10px #000,
    30px 5px #000, 30px 0 #000;
}
.commentSection {
  max-width: 100%;
  width: 100%;
  background-color: #1a1a1a; /* 도시 야경 컨셉의 배경색 */
  border: 1px solid #444; /* 적당히 각진 느낌의 테두리 */
  border-radius: 10px; /* 적당한 각진 정도의 모서리 각도 */
  padding: 20px; /* 내용과의 간격 조절 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 그림자 효과 추가 */
}

.line {
  border-bottom: 1px solid #ccc; /* 회색 줄 색상 및 굵기 조절 */
  margin-bottom: 10px; /* 줄 아래 여백 추가 */
  padding-bottom: 5px; /* 줄 아래에 일정한 간격을 유지하기 위해 패딩 추가 */
}
</style>
