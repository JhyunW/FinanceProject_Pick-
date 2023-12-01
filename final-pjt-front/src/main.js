import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

// app.use(createPinia())
app.use(VueSweetalert2);
pinia.use(piniaPluginPersistedstate)
app.use(router)
app.use(pinia)

app.mount('#app')
