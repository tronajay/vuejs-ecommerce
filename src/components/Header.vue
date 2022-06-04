<template>
  <header class="fixed top-0 w-full z-20">
    <nav
      class="md:flex shadow-md py-3 px-5 bg-blue-400 text-white items-center md:justify-between"
    >
      <div class="flex flex-row items-center justify-between gap-2">
        <button
          :class="{ hidden: isOpen }"
          class="md:hidden"
          @click="isOpen = true"
        >
          <i class="fa-solid text-white text-xl fa-bars"></i>
        </button>
        <button
          :class="{ hidden: !isOpen }"
          class="md:hidden"
          @click="isOpen = false"
        >
          <i class="fa-solid fa-xmark text-xl"></i>
        </button>
        <RouterLink to="/" class="logo">
          <h2 class="font-bold text-xl">Vue Project</h2>
        </RouterLink>
        <RouterLink class="md:hidden" to="/cart"
          ><i class="fa-solid fa-cart-shopping"></i> ({{
            cartTotalLength
          }})</RouterLink
        >
      </div>
      <div
        :class="{ 'hidden md:block': !isOpen }"
        class="menu text-center mt-2 transition-all duration-300"
      >
        <ul class="md:flex items-center">
          <li class="">
            <form class="flex items-center" method="get" :action="'/search?q='+search">
              <label for="simple-search" class="sr-only">Search</label>
              <div class="relative w-full">
                <div
                  class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none"
                >
                  <svg
                    class="w-5 h-5 text-gray-500"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                </div>
                <input
                  type="text"
                  id="simple-search"
                  v-model="search"
                  name="q"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5"
                  placeholder="Search"
                  required=""
                />
              </div>
              <button
              type="submit"
               
                class="p-2.5 ml-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300"
              >
                <svg
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  ></path>
                </svg>
              </button>
            </form>
          </li>
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
import axios from 'axios';
export default {
  data() {
    return {
      cart: {
        items: [],
      },
      isOpen: false,
      search: "",
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
