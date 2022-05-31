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
    <div v-if="$store.state.isLoading" class="text-center mt-10">
      <div
        class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full border-x-gray-500 border-t-gray-500"
        role="status"
      ></div>
    </div>

  <div class="wrapper mt-16"></div>
  <div v-if="$store.state.httpError" :class="{'bg-red-500':$store.state.httpError,'bg-green-500':$store.state.httpSuccess}" class="fixed alert z-20 shadow-md text-white px-5 py-2 bottom-5 right-5 rounded-lg">
    {{$store.state.httpMessage}}
  </div>
  <div class="w-full">
    <RouterView />
  </div>
</template>
