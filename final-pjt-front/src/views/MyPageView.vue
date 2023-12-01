<template>
  <div class="font-controller">
    <div class="top-text">
      <p>MY PAGE</p>
    </div>
    <div class="box-cont">
      <div class="left-box">
        <button @click="goModify()">Modify Info</button>
        <div class="card">
          <span class="card__hover">WELECOME <br> {{ userNickname }}</span>
          <figure class="card__figure">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
              style="fill: rgba(255, 255, 255, 1);transform: ;msFilter:;">
              <path
                d="M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm0 18c-4.411 0-8-3.589-8-8 0-1.168.258-2.275.709-3.276.154.09.308.182.456.276.396.25.791.5 1.286.688.494.187 1.088.312 1.879.312.792 0 1.386-.125 1.881-.313s.891-.437 1.287-.687.792-.5 1.287-.688c.494-.187 1.088-.312 1.88-.312s1.386.125 1.88.313c.495.187.891.437 1.287.687s.792.5 1.287.688c.178.067.374.122.581.171.191.682.3 1.398.3 2.141 0 4.411-3.589 8-8 8z">
              </path>
              <circle cx="8.5" cy="12.5" r="1.5"></circle>
              <circle cx="15.5" cy="12.5" r="1.5"></circle>
            </svg>
          </figure>
          <div class="card__info">
            <span class="card__name"> {{ userNickname }} </span>
            <span class="card__ocupation"> {{ userEmail }} </span>
            <div class="card__links">
            </div>
          </div>
        </div>
        <!-- 사용자 설정으로 이동하는 버튼 추가 -->
      </div>
      <div class="right-box">
        <h1>{{ userNickname }}님이 관심있는 예금상품</h1>
        <div v-for="product in likeStore.constProduct " class="liked-product" @click="showOptions(product)">
          <p>{{ product.kor_co_nm }}</p>
          <p>{{ product.fin_prdt_nm }}</p>
        </div>
      </div>
      <ListDetailModal v-if="modalOpen" :product="selectedProduct" @close-modal="closeModal" />
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth.js'
import { useLikeProductStore } from '@/stores/LikeProduct.js'
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import UserSetting from '@/components/UserSetting.vue'
import ListDetailModal from '@/components/ListDetailModal.vue';
import axios from 'axios';

const router = useRouter()
const store = useAuthStore()
const likeStore = useLikeProductStore()
const URL = 'http://127.0.0.1:8000/'
const modalOpen = ref(false);

const token = store.token
const products = likeStore.constProduct // 좋아요 누른 상품들
const selectedProduct = ref([])
const userName = store.user.username
const userNickname = store.user.nickname
const userEmail = store.user.email

const goModify = () => {
  router.push({ name: 'modify' })
}

const showOptions = (product) => {
  axios({
    method: 'get',
    url: `${URL}finance/deposit-product-options/${product.fin_prdt_cd}`,
  }).then((res) => {
    console.log(res)
  }).catch((err) => {
    console.log(err)
  })
  selectedProduct.value = product;
  modalOpen.value = true;
};

const test = computed(() => {
  return likeStore.likeProducts
})

function closeModal() {
  modalOpen.value = false;
}
onMounted(() => {
  likeStore.getLikeProduct(token)
})
</script>

<style scoped>
.top-text {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.top-text p {
  height: 150px;
  font-size: 65px;
  margin: 0;
  padding: 0;
  text-align: center;
  line-height: 2.5;
}

/* left, right box */
.box-cont {
  display: flex;
  flex-flow: wrap;
  justify-content: center;
}


.left-box {
  flex-direction: column;
  width: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.left-box button {
  margin: 30px;
  cursor: pointer;
  font-size: 20px;
}


.right-box {
  width: 45%;
  display: flex;
  text-align: center;
  flex-flow: wrap;
  justify-content: center;
}

.right-box h1 {
  width: 100%;
  margin: 10px;
  font-size: 40px;
}

.liked-product {
  background-color: rgba(113, 113, 113, 0.6);
  text-align: center;
  border: 1px solid yellow;
  width: 250px;
  border-radius: 12px;
  margin: 20px;
  cursor: pointer;
  font-size: 18px;
}

.font-controller {
  color: yellow
}

a {
  text-decoration: none;
  font-family: 'PFStardust';
  color: yellow;
}

/* card style */
.card {
  width: 300px;
  height: 400px;
  padding: 15px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: rgba(113, 113, 113, 0.6);
  backdrop-filter: blur(20px);
  text-align: center;
  border: 1px solid #fff;
  /* Transform Propertys */
  --rotate-animation: rotate(45deg);
  --scale-animation: scale(0);
  /* Backgrounds - Social Media Hover */
  --bg-facebook: blue;
  --bg-instagram: linear-gradient(to right, #8a2387, #e94057, #f27121);
  --bg-twitter: rgb(25, 173, 206);
  --bg-linkedin: rgb(30, 48, 131);
}

.card::before {
  content: '';
  height: 110%;
  width: 110%;
  position: absolute;
  top: -5%;
  left: -5%;
  z-index: -1;
  background: linear-gradient(to right,
      #0f0c29,
      #302b63,
      #24243e);
  filter: blur(30px);
}

.card__hover {
  color: #fff;
  width: 100%;
  margin: 0;
  font-size: 40px;
  font-weight: 600;
  position: absolute;
  top: 50%;
  left: 0;
  text-align: center;
  letter-spacing: 2px;
  pointer-events: none;
  transform: scale(1) translateY(-50%);
  font-family: var(--font-mulish);
  transition: transform 500ms;
}

.card:hover .card__hover {
  transform: scale(0);
}

.card__figure {
  width: 100%;
  height: 65%;
  border-radius: 10px;
  overflow: hidden;
  transform: var(--rotate-animation) var(--scale-animation);
  transition: transform 600ms ease 100ms;
}

.card:hover .card__figure {
  --rotate-animation: rotate(0);
  --scale-animation: scale(1);
}

.card__figure svg {
  height: 100%;
  width: 100%;
  object-fit: cover;
  filter: drop-shadow(0 0 2px #0f0c29);
}

.card__info {
  display: flex;
  flex-direction: column;
  transform: var(--scale-animation);
  transition: transform 600ms ease 100ms;
}

.card:hover .card__info {
  --scale-animation: scale(1);
}

.card__name {
  color: #fff;
  font-size: 28px;
  letter-spacing: 1px;
  font-family: var(--font-AR-One-Sans);
}

.card__ocupation {
  color: aliceblue;
  font-family: var(--font-mulish);
  text-transform: uppercase;
  font-size: 18px;
  letter-spacing: 2px;
}

.card__links {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-top: 1rem;
  --transform-animation: translateY(-10px);
}

.card__links svg {
  height: 55px;
  width: 55px;
  padding: 10px;
  background-color: rgba(128, 128, 128, 0.211);
  border-radius: 15px;
  cursor: pointer;
  transition: background .3s ease, transform .2s ease;
}

.card__links svg:hover {
  transform: var(--transform-animation);
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, .5);
}

/* button */
button {
  --glow-color: rgb(217, 176, 255);
  --glow-spread-color: rgba(191, 123, 255, 0.781);
  --enhanced-glow-color: rgb(231, 206, 255);
  --btn-color: rgb(100, 61, 136);
  border: .25em solid var(--glow-color);
  padding: 1em 3em;
  color: var(--glow-color);
  font-size: 15px;
  font-weight: bold;
  background-color: var(--btn-color);
  border-radius: 1em;
  outline: none;
  box-shadow: 0 0 1em .25em var(--glow-color),
    0 0 4em 1em var(--glow-spread-color),
    inset 0 0 .75em .25em var(--glow-color);
  text-shadow: 0 0 .5em var(--glow-color);
  position: relative;
  transition: all 0.3s;
}

button::after {
  pointer-events: none;
  content: "";
  position: absolute;
  top: 120%;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: var(--glow-spread-color);
  filter: blur(2em);
  opacity: .7;
  transform: perspective(1.5em) rotateX(35deg) scale(1, .6);
}

button:hover {
  color: var(--btn-color);
  background-color: var(--glow-color);
  box-shadow: 0 0 1em .25em var(--glow-color),
    0 0 4em 2em var(--glow-spread-color),
    inset 0 0 .75em .25em var(--glow-color);
}

button:active {
  box-shadow: 0 0 0.6em .25em var(--glow-color),
    0 0 2.5em 2em var(--glow-spread-color),
    inset 0 0 .5em .25em var(--glow-color);
}
</style>
