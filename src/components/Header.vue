<template>
  <header>
    <nav class="flex py-3 px-5 bg-blue-400 text-white justify-between">
      <RouterLink to="/" class="logo">
        <h2 class="font-bold text-xl">Vue Project</h2>
      </RouterLink>
      <div class="menu hidden md:block">
        <span class="menu-item">
          <RouterLink to="/">Home</RouterLink>
        </span>
        <span class="menu-item">
          <RouterLink to="/about">About</RouterLink>
        </span>
        <button v-on:click="handleLogout" v-if="loggedIn" class="menu-item">
          Logout
        </button>
        <span v-else>
          <RouterLink class="menu-item" to="/login">Login</RouterLink>
          <RouterLink class="menu-item" to="/signup">Signup</RouterLink>
        </span>
        <span class="menu-item">
          <RouterLink to="/cart">Cart ({{ cartTotalLength }})</RouterLink>
        </span>
      </div>
    </nav>
  </header>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      cart: {
        items: [],
      },
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
