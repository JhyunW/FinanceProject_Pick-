import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore('exchange', () => {
    const exchangeInfo = ref([])
    const URL = 'http://127.0.0.1:8000/'


    axios({
        method: 'get',
        url: `${URL}exchange/get-exchange/`
    }).then((res) => {
        exchangeInfo.value = res.data
        console.log(res)
    }).catch((err) => {
        console.log(err)
    })

    const GetExchange = function() {
        axios({
            method: 'get',
            url: `${URL}exchange/get-exchange/`
        }).then((res) => {
            exchangeInfo.value = res.data
            console.log(res)
        }).catch((err) => {
            console.log(err)
        })
    }
    return { exchangeInfo, GetExchange };
},
    { persist: true }
)
