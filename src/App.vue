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
};
</script>

<template>
  <HeaderView />

  <div class="wrapper"></div>
  <div
    v-if="$store.state.httpError"
    :class="{
      'bg-red-500': $store.state.httpError,
      'bg-green-500': $store.state.httpSuccess,
    }"
    class="fixed alert z-20 shadow-md text-white px-5 py-2 bottom-5 right-5 rounded-lg"
  >
    {{ $store.state.httpMessage }}
  </div>
  <div class="w-ful my-20">
    <RouterView />
  </div>
</template>
