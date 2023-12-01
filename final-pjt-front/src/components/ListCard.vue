<template>
  <div class="card-list">
    <!-- <p>{{ store.selectedProducts }}</p> -->
    <div v-for="product in products" :key="product.id">
      <div class="card">
        <div class="content">
          <p class="heading">{{ product.kor_co_nm }}</p>
          <p class="para">상품명 :{{ product.fin_prdt_nm }}</p>
          <p class="para">가입 방법 : {{ product.join_way }}</p>
          <p class="para">Pick'$ : {{ product.like_users.length }}</p>
          <div class="button_check">
          <button1 class="btn" @click="openModal(product)">Detail</button1>
          <div class="checkbox">
            <input
              :id="`checkbox${product.id}`"
              class="checkbox__input"
              type="checkbox"
              :checked="store.selectedProducts.includes(product)"
              @change="handleCheckboxChange(product)"
            />
            <label :for="`checkbox${product.id}`" class="checkbox__label">
              <span class="checkbox__custom"></span>
              비교 리스트 담기
            </label>
          </div>
        </div>
        </div>
      </div>
    </div>
    <div class="fixed-buttons">
      <transition name="list-item">
        <button
          clss="list1"
          v-if="store.selectedProducts[0]"
          @click="delete1()"
        >
          <span class="text"
            >{{ store.selectedProducts[0].kor_co_nm }}
            <br />
            {{ store.selectedProducts[0].fin_prdt_nm }}</span
          ><span>Delete!</span>
        </button>
      </transition>
      <transition name="list-item">
        <button
          clss="list2"
          v-if="store.selectedProducts[1]"
          @click="delete2()"
        >
          <span class="text"
            >{{ store.selectedProducts[1].kor_co_nm }}
            <br />
            {{ store.selectedProducts[1].fin_prdt_nm }}</span
          ><span>Delete!</span>
        </button>
      </transition>
      <button2 class="compare-button" @click="startComparison()"
        >비교하기</button2
      >
    </div>
  </div>
  <ListDetailModal
    v-if="modalOpen"
    :product="selectedProduct"
    @close-modal="closeModal"
  />
</template>

<script setup>
import { ref, provide } from 'vue';
import axios from 'axios';
import ListDetailModal from '@/components/ListDetailModal.vue';
import { useRouter } from 'vue-router';
import { useCompStore } from '@/stores/comparison';

const router = useRouter(); // 라우터 초기화
const products = ref([]);
const modalOpen = ref(false);
const selectedProduct = ref(null);
const store = useCompStore();
// const selectedProducts = ref([]);

const URL = 'http://127.0.0.1:8000/';
axios
  .get(`${URL}finance/deposit-products/`)
  .then((res) => {
    console.log(res);
    products.value = res.data;
  })
  .catch((err) => {
    console.log(err);
  });

function openModal(product) {
  console.log('Modal opened');
  selectedProduct.value = product;
  modalOpen.value = true;
}

function closeModal() {
  modalOpen.value = false;
}

function handleCheckboxChange(product) {
  if (
    store.selectedProducts.length >= 2 &&
    !store.selectedProducts.includes(product)
  ) {
    alert('최대 2개까지만 선택할 수 있습니다.');
    const checkboxId = `checkbox${product.id}`;
    document.getElementById(checkboxId).checked = false;
    return;
  }

  if (store.selectedProducts.includes(product)) {
    store.selectedProducts.splice(store.selectedProducts.indexOf(product), 1); // 선택 제품 제거
  } else {
    store.selectedProducts.push(product); // 선택 제품 추가
  }
}

function startComparison() {
  if (store.selectedProducts.length < 2) {
    alert('최소 2개의 제품을 선택해야 합니다.');
    return;
  }

  // 여기서 선택한 제품들을 comparison.vue 파일로 전달하여 비교 페이지를 만듭니다.
  console.log('Selected Products:', store.selectedProducts);
  // 비교 페이지로 이동하는 코드를 추가해주세요.
  router.push({ name: 'Comparison' });
}

function delete1() {
  console.log(store.selectedProducts[0]);
  store.selectedProducts.shift();
}
function delete2() {
  store.selectedProducts.pop();
}
</script>

<style scoped>
.card {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 300px;
  height: 300px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  padding: 32px;
  margin: 20px;
  overflow: hidden;
  border-radius: 10px;
  transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  border: gray 1px solid;
  background-color: rgba(0, 0, 0, 0.6);
}

.content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0px;
  color: white;
  transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
  z-index: 2;
}

.content .heading {
  font-weight: 700;
  font-size: 32px;
}

.content .para {
  line-height: 1.5;
}

.content .btn {
  color: #e8e8e8;
  text-decoration: none;
  padding: 10px;
  font-weight: 400;
  border: none;
  cursor: pointer;
  background: linear-gradient(-45deg, rgb(47, 34, 88) 0%, #5800ff 100%);
  /* 원래 백그라운드 색조합   background: linear-gradient(-45deg, #f89b29 0%, #ff0f7b 100%);
 */
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}

.card::before {
  content: '';
  position: absolute;
  right: 0;
  bottom: 0;
  width: 5px;
  height: 100%;
  background: linear-gradient(-45deg, rgba(0, 0, 0, 0.04) 0%, #5800ff 100%);
  z-index: 1;
  transition: all 0.5s cubic-bezier(0.23, 1, 0.32, 1);
}

.card:hover::before {
  width: 100%;
}

.card:hover {
  box-shadow: none;
}

.card:hover .btn {
  outline: 2px solid #e8e8e8;
  background: transparent;
  color: #e8e8e8;
}

.content .btn:hover {
  color: #212121;
  background: rgba(108, 189, 243, 0.625);
}

.content .btn:active {
  box-shadow: none;
}

.card-list {
  display: flex;
  flex-wrap: wrap;
  margin: 20px;
}

/* 찜하기 버튼 스타일 */
.checkbox {
  display: inline-block;
  position: relative;
  cursor: pointer;
}

.checkbox__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.checkbox__label {
  display: inline-block;
  padding-left: 30px;
  margin-bottom: 10px;
  position: relative;
  font-size: 16px;
  color: #fff;
  cursor: pointer;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}

.checkbox__custom {
  position: absolute;
  top: 12px;
  left: 0;
  width: 20px;
  height: 20px;
  background: linear-gradient(#1a1a1a, #1a1a1a) padding-box,
    linear-gradient(145deg, #e81cff, #40c9ff) border-box;
  border: 2px solid transparent;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}

.checkbox__input:checked + .checkbox__label .checkbox__custom {
  background-image: linear-gradient(145deg, #e81cff, #40c9ff);
  transform: rotate(45deg) scale(0.8);
}

.checkbox__label:hover .checkbox__custom {
  transform: scale(1.2);
}
/* 비교하기 버튼 */
.compare-button {
  padding: 15px 25px;
  border: unset;
  border-radius: 15px;
  color: #212121;
  z-index: 1;
  background: rgba(40, 140, 207, 0.825);
  position: relative;
  cursor: pointer;
  font-weight: 1000;
  font-size: 17px;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms;
  overflow: hidden;
}

.compare-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0;
  border-radius: 15px;
  background-color: #212121;
  z-index: -1;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms;
}

.compare-button:hover {
  color: #e8e8e8;
}

.compare-button:hover::before {
  width: 100%;
}

/* 리스트 버튼 스타일 */
button {
  position: relative;
  overflow: hidden;
  border: 1px solid #18181a;
  color: #c9c9d3;
  display: inline-block;
  font-size: 15px;
  line-height: 15px;
  padding: 18px 18px 17px;
  border-radius: 15px;
  text-decoration: none;
  cursor: pointer;
  background: rgba(7, 31, 46, 0.825);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

button span:first-child {
  position: relative;
  transition: color 600ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 10;
}

button span:last-child {
  color: white;
  display: block;
  position: absolute;
  bottom: 0;
  transition: all 500ms cubic-bezier(0.48, 0, 0.12, 1);
  z-index: 100;
  opacity: 0;
  top: 50%;
  left: 50%;
  transform: translateY(225%) translateX(-50%);
  height: 14px;
  line-height: 13px;
}

button:after {
  content: '';
  position: absolute;
  bottom: -50%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: black;
  transform-origin: bottom center;
  transition: transform 600ms cubic-bezier(0.48, 0, 0.12, 1);
  transform: skewY(9.3deg) scaleY(0);
  z-index: 50;
}

button:hover:after {
  transform-origin: bottom center;
  transform: skewY(9.3deg) scaleY(2);
}

button:hover span:last-child {
  transform: translateX(-50%) translateY(-50%);
  opacity: 1;
  transition: all 900ms cubic-bezier(0.48, 0, 0.12, 1);
}
.fixed-buttons {
  position: fixed;
  bottom: 5%;
  right: 4%;
  /* transform: translateY(-50%); */
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: 60;
}

.list-item-enter-active,
.list-item-leave-active {
  transition: opacity 0.5s;
}
.list-item-enter,
.list-item-leave-to {
  opacity: 0;
}
.button_check {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.button_check .btn {
  margin-right: 10px; /* 필요한 만큼 여백 조절 */
}
</style>
