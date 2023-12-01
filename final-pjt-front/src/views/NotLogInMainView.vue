<template>
  <h1 style="color: #E7B000; background-color: rgba(128, 128, 128, 0.4);">Join us and Get financial information</h1>
  <button>
    <RouterLink to="/login">
      <span>LogIn</span>
    </RouterLink> <!--컴포넌트의 로그인페이지로-->
  </button>
  <button>
    <RouterLink to="/signup">
      <span>SignUp</span>
    </RouterLink> <!--컴포넌트의 로그인페이지로-->
  </button>

  <div style="margin: 20px;">
    <img src="../assets/Logo.png" alt="">
  </div>
  <div class="introduction-box">
    <div>
      <p>Easy comparison</p>
    </div>
    <hr>
    <div>
      <p>Check today's exchange rate</p>
    </div>
    <hr>
    <div>
      <p>Register the product you are interested in</p>
    </div>
  </div>
  <div class="footer">
    <hr style="color: yellow; background-color: yellow; height: 5px;">
    <p style="color: yellow; font-size: 48px; font-weight: bold;">made by heun & hyeon</p>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
button {
  padding: 0.1em 0.25em;
  width: 13em;
  height: 4.2em;
  background-color: #24272B;
  border: 0.08em solid #fff;
  border-radius: 0.3em;
  font-size: 12px;
  margin: 30px;
  font-family: 'PFStardust';

}

h1 {
  font-family: 'PFStardust';
}

a {
  text-decoration: none;
  font-family: 'PFStardust';
}

button span {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  bottom: 0.4em;
  width: 8.25em;
  height: 2.5em;
  background-color: #212121;
  border-radius: 0.2em;
  font-size: 1.5em;
  color: #fff;
  border: 0.08em solid #fff;
  box-shadow: 0 0.4em 0.1em 0.019em #fff;
}

button span:hover {
  transition: all 0.5s;
  transform: translate(0, 0.4em);
  box-shadow: 0 0 0 0 #fff;
}

button span:not(hover) {
  transition: all 1s;
}

.introduction-box {
  margin: 20px;
  height: 10%;
  color: #E4D301;
  font-size: 42px;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(128, 128, 128, 0.4);
}


.introduction-box div {
  width: 30%;
}

.introduction-box hr {
  height: 300px;
  width: .3vw;
  border-width: 0;
  color: yellow;
  background-color: yellow;
}

.footer {
  height: 10%;
  padding: 0px;
  margin: 0px;
  background-color: rgba(128, 128, 128, 0.4);
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
}

.footer p {
  height: 10%;
  padding: 0%;
  margin: 0;
  line-height: 200%;
}

.footer hr {
  padding: 0;
  margin: 0;
}

</style>