<script setup>
import { RouterView } from "vue-router";
import HeaderView from "./components/Header.vue";
</script>

<script>
import axios from "axios";
export default {
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {},
};
</script>

<template>
  <HeaderView />
  <div class="wrapper"></div>

  <div class="w-full">
    <RouterView />
  </div>
</template>
