<template>
  <link rel="stylesheet" href="//cdn.jsdelivr.net/gh/Dalgona/neodgm-webfont@1.510/neodgm_code/style.css">
  <div style="height:30vh; width: 70vb; margin: 20px auto;">
    <ExchangeChart :exchangeRates="exchangeRates"></ExchangeChart>
  </div>
  <div class="exchange-box">
    <h3 style="padding: 0%; margin: 0%; font-weight: bold; height: 150px;">환율 계산기</h3>
    <select v-model="selectedCurrency" class="custom-select" @change="calc()">
      <option value="">통화를 선택하세요</option>
      <option v-for="currency in exchangeRates" :value="currency.cur_unit">
        <p v-if="currency.cur_unit === 'JPY(100)'">JPY</p>
        <p v-else>{{ currency.cur_unit }}</p>
      </option>
    </select>
    <input type="number" @input="calc()" v-model="inputAmount" placeholder="금액을 입력하세요" maxlength="10">
    <div v-if="selectedCurrency && inputAmount" style="line-height:140%;">
      <span style="padding: 0%; margin: 0%;">{{ inputAmount }}</span> <span class="vertical-bar">|</span>
      <span v-if="selectedCurrency === 'CNH'">¥(위안)</span>
      <span v-if="selectedCurrency === 'EUR'">€</span>
      <span v-if="selectedCurrency === 'JPY(100)'">¥(엔)</span>
      <span v-if="selectedCurrency === 'USD'">$</span>
      <br>
      <span style="padding: 0%; margin: 0%; font-weight: bold;">{{ calculateAmount }}</span> <span>원 입니다.</span>
    </div>
  </div>
</template>

<script setup>
import ExchangeChart from '@/components/ExchangeChart.vue'
import { useExchangeStore } from '@/stores/exchange.js'
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios';


const store = useExchangeStore()
const exchangeInfo = store.exchangeInfo

const selectedCurrency = ref('')
const inputAmount = ref('')
const selectUnit = ref('')
const calculateAmount = ref('')

const inputLength = computed(() => {
  return inputAmount.value.toString().length
})

const calc = () => {
  if (inputLength.value > 10) {
    inputAmount.value = inputAmount.value.toString().substring(0, 10)
    // console.log(inputAmount.value * 3)
  }
  calculateAmount.value = Math.floor((selectUnit.value / 1000) * inputAmount.value)
}

const convertToInteger = function (value) {
  return parseInt(value.replace(/,/g, ''), 10);
}

// rate를 추가해서 int로 바꿔둔 객체
const exchangeRates = exchangeInfo.map((currency) => {
  const rate = convertToInteger(currency.kftc_bkpr);
  return { ...currency, rate };
})

console.log(exchangeInfo)
console.log(exchangeRates)

const selected = watch(selectedCurrency, (newValue, oldvalue) => {
  console.log(newValue)
  const temp = exchangeRates.find((element) => element.cur_unit === newValue);
  selectUnit.value = temp.rate
})

onMounted(() => {
  store.GetExchange()
})


</script>

<style scoped>
@font-face {
  font-family: 'PFStardust';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/PFStardust.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

.vertical-bar {
  color: #999;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.exchange-box {
  text-align: center;
  font-family: 'PFStardust';
  font-size: 64px;
  /* color: yellow; */
}

.custom-select {
  box-sizing: border-box;
  font-family: 'PFStardust';
  font-size: 32px;
  height: 100px;
  width: 400px;
  padding: 10px 16px 10px 16px;
  background-size: 10px;
  transition: border-color .1s ease-in-out, box-shadow .1s ease-in-out;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23131313%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E");
  background-repeat: no-repeat;
  background-position: right 1rem top 50%;
  background-size: 1rem auto;
  border: 1px solid black;
  border-radius: 3px;
  margin: 20px;
}

.custom-select:hover {
  border: 2px solid #999;
}

.custom-select:focus {
  border: 1px solid #999;
  box-shadow: 0 3px 5px 0 rgba(0, 0, 0, .2);
  outline: none;
}

input {
  font-size: 32px;
  box-sizing: border-box;
  font-family: 'PFStardust';
  width: 400px;
  height: 100px;
  outline: none;
  border: 1px solid black;
  padding: 10px;
  border-radius: 5px;
  transition: .3s;
  color: black;
  margin: 20px;

}

input:focus {
  border: 1px solid #3b82f6;
  box-shadow: 0 0 0 4px #3b83f65f
}

input:hover {
  border: 2px solid #999;
}
</style>
