<template>
  <div class="auth-form-container">
    <form @submit.prevent="handleFormSubmit">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" v-model="username" />
      <br />
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" v-model="password1" />
      <br />
      <div v-if="isSignUpRoute">
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" v-model="email" />
        <br />
        <label for="nickname">Nickname:</label>
        <input type="nickname" id="nickname" name="nickname" v-model="nickname" />
        <br />
        <label for="password2">Confirm Password:</label>
        <input type="password" id="password2" name="password2" v-model="password2" />
      </div>
      <button class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useRoute } from 'vue-router';

const route = useRoute();
const store = useAuthStore();
const email = ref('');
const nickname = ref('');
const username = ref('');
const password1 = ref('');
const password2 = ref('');

const isSignUpRoute = route.name === 'signup';

const handleFormSubmit = () => {
  console.log(username.value, password1.value);
  if (isSignUpRoute) {
    store.signUp(
      email.value,
      nickname.value,
      username.value,
      password1.value,
      password2.value
    );
  } else {
    store.logIn(username.value, password.value);
  }
};
</script>
<style scoped></style>
