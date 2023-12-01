import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBankStore = defineStore('bank', () => {
    const banks = [
        {
          name: '신한은행',
          imgName: '001',
          kor_co_nm: ['신한저축은행', '신한은행']
        },
        {
          name: '토스뱅크',
          imgName: '토스뱅크',
          kor_co_nm: ['토스뱅크 주식회사']
        },
        {
          name: '카카오뱅크',
          imgName: '카카오뱅크',
          kor_co_nm: ['주식회사 카카오뱅크']
        },
        {
          name: 'NH농협',
          imgName: 'NH농협',
          kor_co_nm: ['농협은행주식회사']
        },
        {
          name: '국민은행',
          imgName: 'KB',
          kor_co_nm: ['국민은행']
        },
        {
          name: '하나은행',
          imgName: '하나은행',
          kor_co_nm: ['하나은행']
        },
        {
          name: '우리은행',
          imgName: '우리',
          kor_co_nm: ['우리금융저축은행', '우리은행']
        },
      ]
    const findTarget = (name) =>{
      console.log('==========================')
      console.log("IN STORE")
      console.log(name)
      console.log('==========================')

      return banks.name === name
    }

    return { banks, findTarget };
},
)
