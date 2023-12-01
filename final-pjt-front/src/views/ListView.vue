<template>
  <h1 style="color: white;">All List</h1>
  <ListCard />
  <!--맵 버튼-->
  <button2 class="fab-button" @click="openMap">Map</button2>
  <Locations 
  v-if="mapOpen"
  @close-map="closeMap"
  />
</template>

<script setup>
import { ref } from 'vue'
import ListCard from '@/components/ListCard.vue';
import Locations from '@/components/Locations.vue';
// const openMap = () => {
//   // 버튼이 클릭되었을 때 수행할 로직을 추가하세요.
//   console.log("Button Clicked!");
// };
const mapOpen = ref(false);  // 맵 온오프

function openMap() {
  console.log("Map Opened!"); // 맵이 열렸는지 확인할 콘솔
  mapOpen.value = true;
}

function closeMap() {
  mapOpen.value = false;
}

</script>

<style scoped>
/* 맵 버튼 스타일링 */.fab-button {
  position: fixed;
  right: 20px;
  bottom: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #3b546d; /* 어두운 톤의 색상으로 변경 */
  color: #ecf0f1; /* 밝은 톤의 글자색으로 변경 */
  font-size: 24px;
  border: none;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s; /* 마우스 호버 효과를 위한 전환 효과 추가 */
}

.fab-button:hover {
  background-color: #3498db; /* 호버 시 밝은 푸른색으로 변경 */
}
.listback {
  background-color: rgb(159, 154, 154)
}
</style>
