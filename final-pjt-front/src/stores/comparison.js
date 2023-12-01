import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { defineStore } from 'pinia';

export const useCompStore = defineStore( // 호출을 하면 리턴으로 딕셔너리
  'comparison', // 스토어 고유값
  () => {
    const selectedProducts = ref([]);
    return { selectedProducts, };
  },
  { persist: true }
);
