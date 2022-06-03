import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../components/HomeView.vue'
import AboutView from '../components/pages/AboutView.vue'
import AddProductView from '../components/product/AddProductView.vue'
import UpdateProductView from '../components/product/UpdateProductView.vue'
import LoginView from '../components/pages/LoginView.vue'
import SignupView from '../components/pages/SignupView.vue'
import Cart from '../components/pages/Cart.vue';
import AddressView from '../components/pages/AddressView.vue';
import ProductView from '../views/Product/ProductView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      props: true,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/add-product',
      name: 'add_product',
      component: AddProductView
    },
    {
      path: '/product/:uuid/edit/',
      name: 'product_details',
      component: UpdateProductView
    },
    {
      path: '/product/:slug/',
      name: 'product_detail',
      component: ProductView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'register',
      component: SignupView
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    },
    {
      path: '/address',
      name: "address",
      component: AddressView
    },


  ]
})

export default router
