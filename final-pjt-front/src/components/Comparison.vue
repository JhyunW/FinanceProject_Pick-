<template>
  <div class="comparison-container">
    <div class="left-card card card-40">
      <div class="card__content">
        <p
          class="co_nm ptag"
          @mouseenter="toggleHoverEffect('co_nm', true)"
          @mouseleave="toggleHoverEffect('co_nm', false)"
        >
          {{ selectedProducts.right.kor_co_nm }}
        </p>
        <p
          class="prdt_nm ptag"
          @mouseenter="toggleHoverEffect('prdt_nm', true)"
          @mouseleave="toggleHoverEffect('prdt_nm', false)"
        >
          {{ selectedProducts.right.fin_prdt_nm }}
        </p>
                <!--여기서부터 추가-->
                <div v-for="l_detail in leftDetail">
          <p class="detail ptag"
          @mouseenter="toggleHoverEffect('detail', true)"
          @mouseleave="toggleHoverEffect('detail', false)">{{ l_detail.intr_rate_type_nm }} / {{ l_detail.save_trm }}개월 / {{ l_detail.intr_rate }}% / {{ l_detail.intr_rate2 }}%</p> 
        </div>
        <!---->
        <p
          class="etc ptag"
          @mouseenter="toggleHoverEffect('etc', true)"
          @mouseleave="toggleHoverEffect('etc', false)"
        >
          {{ selectedProducts.right.etc_note }}
        </p>
        <p
          class="join_deny ptag"
          @mouseenter="toggleHoverEffect('join_deny', true)"
          @mouseleave="toggleHoverEffect('join_deny', false)"
        >
          {{ selectedProducts.right.join_deny }}
        </p>
        <p
          class="join_member ptag"
          @mouseenter="toggleHoverEffect('join_member', true)"
          @mouseleave="toggleHoverEffect('join_member', false)"
        >
          {{ selectedProducts.right.join_member }}
        </p>
        <p
          class="spcl_cnd ptag"
          @mouseenter="toggleHoverEffect('spcl_cnd', true)"
          @mouseleave="toggleHoverEffect('spcl_cnd', false)"
        >
          {{ selectedProducts.right.spcl_cnd }}
        </p>
        <p
          class="like ptag"
          @mouseenter="toggleHoverEffect('like', true)"
          @mouseleave="toggleHoverEffect('like', false)"
        >
          {{ selectedProducts.right.like_users }}
        </p>
      </div>
    </div>
    <div class="left-card card card-20">
      <div class="card__content">
        <p
          class="co_nm ptag"
          @mouseenter="toggleHoverEffect('co_nm', true)"
          @mouseleave="toggleHoverEffect('co_nm', false)"
        >
          금융 회사
        </p>
        <p
          class="prdt_nm ptag"
          @mouseenter="toggleHoverEffect('prdt_nm', true)"
          @mouseleave="toggleHoverEffect('prdt_nm', false)"
        >
          상품명
        </p>
        <!--여기서부터 추가-->
        <p class="detail ptag"
          @mouseenter="toggleHoverEffect('detail', true)"
          @mouseleave="toggleHoverEffect('detail', false)">유형 / 기간 / 저축금리 / 최고 우대 금리</p> 
        <p
          class="etc ptag"
          @mouseenter="toggleHoverEffect('etc', true)"
          @mouseleave="toggleHoverEffect('etc', false)"
        >
          유의사항
        </p>
        <p
          class="join_deny ptag"
          @mouseenter="toggleHoverEffect('join_deny', true)"
          @mouseleave="toggleHoverEffect('join_deny', false)"
        >
          가입제한
        </p>
        <p
          class="join_member ptag"
          @mouseenter="toggleHoverEffect('join_member', true)"
          @mouseleave="toggleHoverEffect('join_member', false)"
        >
          가입대상
        </p>
        <p
          class="spcl_cnd ptag"
          @mouseenter="toggleHoverEffect('spcl_cnd', true)"
          @mouseleave="toggleHoverEffect('spcl_cnd', false)"
        >
          우대조건
        </p>
        <p
          class="like ptag"
          @mouseenter="toggleHoverEffect('like', true)"
          @mouseleave="toggleHoverEffect('like', false)"
        >
          - Pick'$ -
        </p>
      </div>
    </div>
    <div class="right-card card card-40">
      <div class="card__content">
        <p
          class="co_nm ptag"
          @mouseenter="toggleHoverEffect('co_nm', true)"
          @mouseleave="toggleHoverEffect('co_nm', false)"
        >
          {{ selectedProducts.left.kor_co_nm }}
        </p>
        <p
          class="prdt_nm ptag"
          @mouseenter="toggleHoverEffect('prdt_nm', true)"
          @mouseleave="toggleHoverEffect('prdt_nm', false)"
        >
          {{ selectedProducts.left.fin_prdt_nm }}
        </p>
         <!--여기서부터 추가-->
         <div v-for="r_detail in leftDetail">
          <p class="detail ptag"
          @mouseenter="toggleHoverEffect('detail', true)"
          @mouseleave="toggleHoverEffect('detail', false)">{{ r_detail.intr_rate_type_nm }} / {{ r_detail.save_trm }}개월 / {{ r_detail.intr_rate }}% / {{ r_detail.intr_rate2 }}%</p> 
        </div>
        <!---->
        <p
          class="etc ptag"
          @mouseenter="toggleHoverEffect('etc', true)"
          @mouseleave="toggleHoverEffect('etc', false)"
        >
          {{ selectedProducts.left.etc_note }}
        </p>
        <p
          class="join_deny ptag"
          @mouseenter="toggleHoverEffect('join_deny', true)"
          @mouseleave="toggleHoverEffect('join_deny', false)"
        >
          {{ selectedProducts.left.join_deny }}
        </p>
        <p
          class="join_member ptag"
          @mouseenter="toggleHoverEffect('join_member', true)"
          @mouseleave="toggleHoverEffect('join_member', false)"
        >
          {{ selectedProducts.left.join_member }}
        </p>
        <p
          class="spcl_cnd ptag"
          @mouseenter="toggleHoverEffect('spcl_cnd', true)"
          @mouseleave="toggleHoverEffect('spcl_cnd', false)"
        >
          {{ selectedProducts.left.spcl_cnd }}
        </p>
        <p
          class="like ptag"
          @mouseenter="toggleHoverEffect('like', true)"
          @mouseleave="toggleHoverEffect('like', false)"
        >
          {{ selectedProducts.left.like_users }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
import { useCompStore } from '@/stores/comparison.js';
import axios from 'axios';

const URL = 'http://127.0.0.1:8000/';
const store = useCompStore();
const selectedProducts = ref({
  left: store.selectedProducts[0],
  right: store.selectedProducts[1],
});
const leftDetail = ref({})
const rightDetail = ref({})

const toggleHoverEffect = (className, isHovering) => {
  const elements = document.querySelectorAll(`.${className}`);
  elements.forEach((element) => {
    if (isHovering) {
      element.classList.add('ptag2');
    } else {
      element.classList.remove('ptag2');
    }
  });
};
/* 온마운트 왼쪽 오른쪽이 반대로 나옴 어째서...? */
onMounted(() => {
  axios({
    method: 'get',
    url: `${URL}finance/deposit-product-options/${store.selectedProducts[0].fin_prdt_cd}/`,
  })
    .then((res) => {
      console.log(res);
      rightDetail.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });

    axios({
    method: 'get',
    url: `${URL}finance/deposit-product-options/${store.selectedProducts[1].fin_prdt_cd}/`,
  })
    .then((res) => {
      console.log(res);
      leftDetail.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });

})

onBeforeUnmount(() => {
  store.selectedProducts = [];
});
</script>

<style scoped>
.comparison-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5%;
}
.card {
  width: 30%;
  height: 100%;
  border-radius: 20px;
  padding: 5px;
  box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
  background-image: linear-gradient(
    144deg,
    rgba(122, 122, 137, 0),
    rgba(145, 145, 212, 0.483) 50%,
    rgba(88, 88, 97, 0.825)
  );
}

.left-card {
  margin-right: 20px;
}
.card__content {
  background: rgba(31, 31, 32, 0.825);
  border-radius: 15px;
  width: 100%;
  height: 100%;
  color: #b85c62;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 1.1rem;
}
.card-40 {
  width: 40%; /* 왼쪽 또는 오른쪽 카드의 너비 조정 */
  margin-right: 20px;
}

.card-20 {
  width: 20%; /* 비교설명 카드의 너비 조정 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.card__content p {
  margin: 10px 0;
}
.ptag {
  position: relative;
  display: block;
  cursor: pointer;
}

.ptag::before,
.ptag::after {
  content: '';
  position: absolute;
  width: 0%;
  height: 4px;
  bottom: -2px;
  margin-top: -0.5px;
  background: #ffffff;
}

.ptag::before {
  left: -2.5px;
}

.ptag::after {
  right: 2.5px;
  background: #ffffff;
  transition: width 0.8s cubic-bezier(0.22, 0.61, 0.36, 1);
}

.ptag2::before {
  background: rgb(255, 255, 255);
  width: 100%;
  transition: width 0.5s cubic-bezier(0.22, 0.61, 0.36, 1);
}

.ptag2::after {
  background: transparent;
  width: 100%;
  transition: 0s;
}
</style>
