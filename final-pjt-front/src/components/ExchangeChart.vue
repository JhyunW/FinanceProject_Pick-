<template>
  <Bar :data="data" :options="options" />
</template>

<script setup>
import { slotFlagsText } from '@vue/shared';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'vue-chartjs';
import { onMounted, onBeforeUnmount } from 'vue';

onMounted(() => {
  // 페이지를 들어올때
  console.log();
  const section = document.querySelector('.background');
  section.style.background = 'white';
  section.style.transition = '1.5';
});

onBeforeUnmount(() => {
  // 페이지를 떠날때
  const section = document.querySelector('.background');
  section.style = '.background';
});
const props = defineProps({
  exchangeRates: Array,
});

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const data = {
  labels: ['위안', '유로', '엔', '달러'],
  datasets: [
    {
      label: 'Daliy Exchange',
      backgroundColor: '#f87979',
      data: [
        props.exchangeRates[0].rate,
        props.exchangeRates[1].rate,
        props.exchangeRates[2].rate,
        props.exchangeRates[3].rate,
      ],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 205, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
      ],
      borderWidth: 1,
    },
  ],
};
let delayed;
const options = {
  responsive: true,
  maintainAspectRatio: false,
  animation: {
    onComplete: () => {
      delayed = true;
    },
    delay: (context) => {
      let delay = 0;
      if (context.type === 'data' && context.mode === 'default' && !delayed) {
        delay = context.dataIndex * 300 + context.datasetIndex * 100;
      }
      return delay;
    },
  },
  scales: {
    x: {
      border: {
        // color: 'yellow'
      },
      ticks: {
        font: {
          size: 28,
          family: 'PFStardust',
        },
      },
    },
    y: {
      border: {
        // color: 'yellow'
      },
      ticks: {
        font: {
          size: 28,
          family: 'PFStardust',
        },
      },
    },
  },
  plugins: {
    legend: {
      labels: {
        font: {
          family: 'PFStardust',
          size: 27,
        },
      },
    },
  },
};
</script>

<style scoped>
@font-face {
  font-family: 'PFStardust';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/PFStardust.woff')
    format('woff');
  font-weight: normal;
  font-style: normal;
}

.background {
  height: 100vh;
  overflow: auto;
  margin: 0;
  background-image: url('src/assets/background.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  padding: 0;
  margin: 0;
  background-attachment: fixed;
}
.backwhite {
  background: white;
  transition: 1.5s;
}
</style>
