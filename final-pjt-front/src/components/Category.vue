<template>
    <h1>{{ bankname }}의 예금 상품</h1>
    <div v-for="info in infos" class="card-list">
        <div v-for="i in info" class="card-list">
            <div class="card" @click=openModal(i)>
                <p class="card-p">{{ i.fin_prdt_nm }}</p>
                <div class="card-countent">
                    <p>{{ i.etc_note }}</p>
                    <p>가입 제한 : {{ i.join_member }}</p>
                </div>
            </div>
        </div>
    </div>
    <ListDetailModal
    v-if="modalOpen"
    :product="selectedProduct"
    @close-modal="closeModal"
  />
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { useBankStore } from '@/stores/bank.js'
import { ref, onMounted } from 'vue';
import ListDetailModal from '@/components/ListDetailModal.vue';

import axios from 'axios';

const store = useBankStore()
const router = useRouter()
const route = useRoute()
const URL = 'http://127.0.0.1:8000/'
const infos = ref([])
const selectedProduct = ref(null);
const modalOpen = ref(false)
const bankname = route.params.categoryName
const bank = store.banks
const imgName = store.imgName

const obj = bank.find((element) => {
    return element.name === bankname
})

function openModal(product) {
  console.log('Modal opened');
  selectedProduct.value = product;
  modalOpen.value = true;
}

function closeModal() {
  modalOpen.value = false;
}

onMounted(() => {
    for (let o of obj.kor_co_nm) {
        axios({
            method: 'get',
            url: `${URL}finance/deposit-products/${o}/`
        }).then((res) => {
            infos.value.push(res.data)
        }).catch((err) => {
            console.log(err)
        })
    }
})
</script>

<style scoped>
.font-controller {
    font-family: PFStardust;
    color : white;
}
.card-list {
  display: flex;
  flex-wrap: wrap;
  margin: 20px;
  justify-content: center;
}

.card {
  font-family: 'PFStardust';
  position: relative;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 300px;
  height: 350px;
  border-radius: 6px;
  transition: .3s;
  background-color: #000;
  margin: 35px;
  cursor: pointer;
}

.card-p {
  position: absolute;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  padding: 0;
}

.card::after {
  content: "";
  position: absolute;
  z-index: -6;
  border-radius: 6px;
  width: 320px;
  height: 370px;
  background-color: #ffff3f;
  transition: .7s;
  background-image: linear-gradient(62deg, rgba(7, 108, 151, 0.548) 0%, #ffff3f 100%);
}

.card-countent {
  text-align: center;
  color: transparent;
  transition: all .7s;
  opacity: 0;
  line-height: 110%;
  font-size: 18px;
}

.card:hover {
  transition: .7s;
  transform: rotate(180deg);
}

.card:hover > .card-p {
  color: transparent;
}

.card:hover > .card-countent {
  opacity: 1;
  color: #000;
  transform: rotate(-180deg);
}

</style>