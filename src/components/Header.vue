<template>
  <header class="fixed top-0 w-full z-20">
    <nav
      class="md:flex shadow-md py-3 px-5 bg-blue-400 text-white items-center md:justify-between"
    >
      <div class="flex flex-row items-center justify-between gap-2">
        <button :class="{'hidden': isOpen}" class="md:hidden" @click="isOpen = true" ><i class="fa-solid text-white text-xl fa-bars"></i></button>
        <button :class="{'hidden': !isOpen}" class="md:hidden" @click="isOpen = false" ><i class="fa-solid fa-xmark text-xl"></i></button>
        <RouterLink to="/" class="logo">
          <h2 class="font-bold text-xl">Vue Project</h2>
        </RouterLink>
        <RouterLink class="md:hidden" to="/cart"><i class="fa-solid fa-cart-shopping"></i> ({{ cartTotalLength }})</RouterLink>
      </div>
      <div 
      :class="{'hidden md:block': !isOpen }"
      class="menu text-center mt-2 transition-all duration-300">
        <ul class="md:flex items-center">
          <li class="menu-item">
            <RouterLink to="/">Home</RouterLink>
          </li>
          <li class="menu-item">
            <RouterLink to="/about">About</RouterLink>
          </li>
          <button v-on:click="handleLogout" v-if="loggedIn" class="menu-item">
            Logout
          </button>
          <li class="menu-item" v-if="!loggedIn">
            <RouterLink to="/login">Login</RouterLink>
          </li>
          <li class="menu-item" v-if="!loggedIn">
            <RouterLink to="/signup">Signup</RouterLink>
          </li>
          <li class="menu-item">
            <RouterLink to="/cart">Cart ({{ cartTotalLength }})</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      cart: {
        items: [],
      },
      isOpen: false,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.isAuthenticated;
    },
    cartTotalLength() {
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }
      return totalLength;
    },
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  methods: {
    handleLogout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      this.$store.commit("removeToken");
      this.$router.push("/login/");
    },
  },
};
</script>
