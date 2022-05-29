import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import './index.css'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://ecommerce-drf.herokuapp.com'

const app = createApp(App).use(store)

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
