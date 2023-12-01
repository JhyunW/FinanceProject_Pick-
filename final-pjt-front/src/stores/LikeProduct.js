import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useLikeProductStore = defineStore('likeproduct', () => {
    const likeProducts = ref({})
    const URL = 'http://127.0.0.1:8000/'

    const getLikeProduct = (token) => {
        axios({
          method : 'get',
          url : `${URL}finance/like-product/`,
          headers : {
            Authorization : `token ${token}`
          }
        }).then((res) => {
          likeProducts.value = res.data
        }).catch((err) => {
          console.log(err)
        })
      }

    const constProduct = computed(() => {
        return likeProducts.value
    })
      

    return { likeProducts, getLikeProduct, constProduct };
},
)
