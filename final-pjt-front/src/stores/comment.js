import axios from 'axios';
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from './auth.js';
import { defineStore } from 'pinia';

export const useCommentStore = defineStore(
  // 호출을 하면 리턴으로 딕셔너리
  'comment', // 스토어 고유값
  () => {
    const token = useAuthStore().token;
    const commentPlus = function (fin_prdt_cd, comment, userId) {
      console.log(fin_prdt_cd, comment, userId);
      axios({
        // 댓글 전송
        method: 'post',
        url: `http://127.0.0.1:8000/finance/product/${fin_prdt_cd}/comments/`,
        headers: {
          Authorization: `Token ${token}`,
        },
        data: {
          content: comment,
        },
      }).then((res) => {
        listComment.value.push(res.data);
      });
    };

    // 댓글 리스트 불러오기
    const listComment = ref([]);

    const getCommentList = function (productId) {
      console.log(token);
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/finance/get-comment-list/${productId}/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res) => (listComment.value = res.data))
        .catch((err) => console.log(err));
    };

    // 실시간 불러오기
    const computedComment = computed(() => {
      return listComment.value;
    });
    return { commentPlus, listComment, getCommentList, computedComment };
  },
  { persist: true }
);
