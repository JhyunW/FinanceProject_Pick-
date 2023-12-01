<template>
  <div>
    <h1 style="color: white; font-family: PFStardust">Select bank category</h1>
  </div>
  <div class="card-list">
    <div class="body" v-for="bank in banks" @click="goCategoryList(bank)">
      <a class="card credentialing" href="#">
        <div class="overlay"></div>
        <div class="circle">
          <img :src="`/${bank.imgName}.png`" style="z-index: 1" />
        </div>
        <p>{{ bank.name }}</p>
      </a>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useBankStore } from '@/stores/bank.js';
import { ref } from 'vue';

const store = useBankStore();
const banks = store.banks;
const router = useRouter();

const goCategoryList = (bank) => {
  router.push({ name: 'category', params: { categoryName: bank.name } });
};
</script>

<style scoped>
/* --bg-color 건드리면 색 바뀜 */
.credentialing {
  --bg-color: #fefae0;
  --bg-color-light: #e2fced;
  --text-color-hover: #4c5656;
  --box-shadow-color: rgba(184, 249, 211, 0.48);
}
.card-list {
  display: flex;
  flex-wrap: wrap;
  margin: 20px;
  justify-content: center;
}

.card {
  width: 220px;
  height: 321px;
  background: rgba(0, 0, 0, 0.46);
  border-top-right-radius: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  border: 0.5rem outset #4c5656;
  box-shadow: 0 14px 26px rgba(0, 0, 0, 0.04);
  transition: all 0.3s ease-out;
  text-decoration: none;
  margin: 20px;
  font-weight: bold;
}

.card:hover {
  transform: translateY(-5px) scale(1.005) translateZ(0);
  box-shadow: 0 24px 36px rgba(0, 0, 0, 0.11),
    0 24px 46px var(--box-shadow-color);
}

.card:hover .overlay {
  transform: scale(4) translateZ(0);
}

.card:hover .circle {
  border-color: var(--bg-color-light);
  background: var(--bg-color);
}

.card:hover .circle:after {
  background: var(--bg-color-light);
}

.card:hover p {
  color: var(--text-color-hover);
}

.card:active {
  transform: scale(1) translateZ(0);
  box-shadow: 0 15px 24px rgba(0, 0, 0, 0.11),
    0 15px 24px var(--box-shadow-color);
}

.card p {
  font-size: 32px;
  color: #4c5656;
  margin-top: 30px;
  margin: 0;
  padding: 0;
  z-index: 1000;
  transition: color 0.3s ease-out;
}

.circle {
  width: 131px;
  height: 131px;
  border-radius: 50%;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  z-index: 1;
  transition: all 0.3s ease-out;
}

.circle:after {
  content: '';
  width: 118px;
  height: 118px;
  display: block;
  position: absolute;
  background: var(--bg-color);
  border-radius: 50%;
  transition: opacity 0.3s ease-out;
}

.circle svg {
  z-index: 10000;
  transform: translateZ(0);
}

.overlay {
  width: 118px;
  position: absolute;
  height: 118px;
  border-radius: 50%;
  background: var(--bg-color);
  top: 55px;
  left: 50px;
  z-index: 0;
  transition: transform 0.3s ease-out;
}
</style>
