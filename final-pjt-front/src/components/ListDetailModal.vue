<template>
  <div>
    <div class="modal-container">
      <div class="card flex-container">
        <div class="left-section">
          <p>{{ product.kor_co_nm }}</p>
          <p>{{ product.fin_prdt_nm }}</p>
          <p>{{ product.join_member }}</p>
          <div v-for="(detailOption, index) in detailOptions.slice(0, 4)">
            <span>저축 금리 유형 : {{ detailOption.intr_rate_type_nm }}</span>
            <br />
            <span>저축 금리 : {{ detailOption.intr_rate }}</span> <br />
            <span>최고 우대 금리 : {{ detailOption.intr_rate2 }}</span> <br />
            <span>저축 기간 : {{ detailOption.save_trm }} 개월 </span>
            <hr />
          </div>
          <button class="btn button" @click="closeModal">Close</button>
          <button class="btn2" @click="like(product)">
            <svg
              viewBox="0 0 17.503 15.625"
              height="20.625"
              width="20.503"
              xmlns="http://www.w3.org/2000/svg"
              class="icon"
            >
              <path
                transform="translate(0 0)"
                d="M8.752,15.625h0L1.383,8.162a4.824,4.824,0,0,1,0-6.762,4.679,4.679,0,0,1,6.674,0l.694.7.694-.7a4.678,4.678,0,0,1,6.675,0,4.825,4.825,0,0,1,0,6.762L8.752,15.624ZM4.72,1.25A3.442,3.442,0,0,0,2.277,2.275a3.562,3.562,0,0,0,0,5l6.475,6.556,6.475-6.556a3.563,3.563,0,0,0,0-5A3.443,3.443,0,0,0,12.786,1.25h-.01a3.415,3.415,0,0,0-2.443,1.038L8.752,3.9,7.164,2.275A3.442,3.442,0,0,0,4.72,1.25Z"
                id="Fill"
              ></path>
            </svg>
          </button>
        </div>
        <div class="right-section">
          <!-- 오른쪽 배치 -->
          <span>Piker'$ Talk</span>
          <comment :product="product" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useLikeProductStore } from '@/stores/LikeProduct.js';
import comment from '@/components/comment.vue';
import axios from 'axios';

const detailOptions = ref([]);
const URL = 'http://127.0.0.1:8000/';

const store = useAuthStore();
const likeStore = useLikeProductStore();

const emit = defineEmits(['close-modal']);
const { product } = defineProps(['product']);
const productCodeNumber = product.fin_prdt_cd;
const token = store.token;

function closeModal() {
  emit('close-modal');
}

const like = (product) => {
  axios({
    method: 'post',
    url: `${URL}finance/product/${product.fin_prdt_cd}/likes/`,
    headers: {
      Authorization: `token ${token}`,
    },
  })
    .then((res) => {
      console.log('=============================');
      console.log(likeStore.constProduct);
      likeStore.getLikeProduct(token);
      console.log('=============================');
    })
    .catch((err) => {});
  likeStore.getLikeProduct(token);
  console.log(likeStore.likeProducts);
};

onMounted(() => {
  axios({
    method: 'get',
    url: `${URL}finance/deposit-product-options/${productCodeNumber}/`,
  })
    .then((res) => {
      console.log(res);
      detailOptions.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped>
@font-face {
  font-family: 'PFStardust';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/PFStardust.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}

.modal-container {
  position: fixed;
  color: white;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
  line-height: 180%;
}

.card {
  width: 1000px;
  height: 800px;
  border-radius: 30px;
  background: black;
  box-shadow: 15px 15px 30px #bebebe, -15px -15px 30px #ffffff;
  text-align: center;
  /* display: flex;
  flex-direction: column;  만약 댓글창 지우고 가운데로 나오게 할려면*/
  justify-content: center;
  align-items: center;
}

.card p {
  /* 태그 글자 스타일 */
  color: yellow;
  font-family: 'PFStardust';
  margin: 0%;
  font-weight: bold;
  font-size: 1.5rem;
}

div span {
  /* 내용 글자 스타일 */
  color: yellow;
  font-family: 'PFStardust';
  padding: 0;
  margin: 10px;
  line-height: 50%;
  font-size: 1.2rem;
}

.button {
  color: yellow;
  width: 100px;
  height: 50px;
  border-radius: 50px;
  background-color: transparent;
  border: 2px solid yellow;
  overflow: hidden;
  position: relative;
  font-size: 16px;
  font-weight: 500;
  text-transform: uppercase;
  transition: 300ms ease;
}

.button::before {
  content: '';
  position: absolute;
  z-index: -1;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: yellow;
  top: 100%;
  left: 0;
  transition: 500ms ease;
}

.button:hover {
  color: yellow;
  letter-spacing: 4px;
}

.button:hover::before {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.btn {
  position: absolute;
  top: 20px;
  right: 20px;
  cursor: pointer;
}

/* 좋아요 버튼 style */
.btn2 {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  border-radius: 10px;
  border: none;
  background-color: transparent;
  position: relative;
}

.btn2::after {
  content: 'like';
  width: fit-content;
  height: fit-content;
  position: absolute;
  font-size: 15px;
  color: white;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
    'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  opacity: 0;
  visibility: hidden;
  transition: 0.2s linear;
  top: 115%;
}

.icon {
  width: 30px;
  height: 30px;
  transition: 0.2s linear;
}

.icon path {
  fill: white;
  transition: 0.2s linear;
}

.btn2:hover > .icon {
  transform: scale(1.2);
}

.btn2:hover > .icon path {
  fill: rgb(177, 139, 189);
}

.btn2:hover::after {
  visibility: visible;
  opacity: 1;
  top: 105%;
}

/* .flex-container를 flex로 설정하여 자식 요소를 나란히 배치 */
.flex-container {
  display: flex;
}

.left-section {
  flex: 1;
  /* 왼쪽 영역이 남는 공간을 모두 차지하도록 설정 */
  text-align: center;
}

.right-section {
  flex: 1;
  /* 오른쪽 영역이 남는 공간을 모두 차지하도록 설정 */
  text-align: left;
  padding: 20px;
  /* 적절한 여백 설정 */
  /* background-color: #333; */
  /* 댓글 영역에 배경색 추가 */
  color: white;
  /* 글자 색상 설정 */
}
.comments {
  margin-top: 20px;
}

.comment {
  background-color: #333;
  color: white;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input,
textarea,
button {
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 3px;
}

button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>
