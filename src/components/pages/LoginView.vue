<template>
  <div class="container p-3">
    <div
      class="mx-auto relative md:w-2/3 border border-gray-300 p-5 shadow-md mt-10 rounded-lg"
    >
    <loading-bar-contain/>
    <div class="header text-center my-2">
      <h2 class="font-bold text-2xl">
        Login
      </h2>
    </div>
      <form @submit.prevent="handleLogin">
        <div class="mb-6">
          <label
            for="username"
            class="block mb-2 text-sm font-medium text-gray-900"
            >Username</label
          >
          <input
            type="text"
            id="username"
            v-model="user.username"
            class="bg-gray-50 border focus:ring-1 focus:outline-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            placeholder="Enter Username"
          />
        </div>
        <div class="mb-6">
          <label
            for="password"
            class="block mb-2 text-sm font-medium text-gray-900"
            >Your password</label
          >
          <input
            type="password"
            id="password"
            placeholder="Enter Password"
            v-model="user.password"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-1 focus:outline-none focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          />
        </div>
        <button
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import User from "../../models/user";
import axios from "axios";
import APIService from "../../services/api-call";
import LoadingBarContain from "../Loading/LoadingBarContain.vue";
export default {
  name: "LoginView",
  data() {
    return {
      user: new User("", ""),
      loading: false,
      message: "",
    };
  },
  components: {
    LoadingBarContain,
  },
  computed: {
    loggedIn() {
      return this.$store.state.isAuthenticated;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/");
    }
  },
  methods: {
    async handleLogin() {
      axios.defaults.headers.common["Authorization"] = "";
      const error_message  = "Invalid Username or Password"
      var response = await new APIService('/api/login/',this.user,error_message).post();
      if (response.status){
        const token = response.data.access;
          this.$store.commit("setToken", token);

          axios.defaults.headers.common["Authorization"] = "Bearer " + token;
          localStorage.setItem("token", token);
          const url = this.$route.query.to || "/";
          this.$router.push(url);
      }else{

      }
      // await axios
      //   .post("/api/login/", this.user)
      //   .then((response) => {
      //     const token = response.data.access;
      //     this.$store.commit("setToken", token);

      //     axios.defaults.headers.common["Authorization"] = "Bearer " + token;
      //     localStorage.setItem("token", token);
      //     const url = this.$route.query.to || "/";
      //     this.$router.push(url);
      //   })
      //   .catch((error) => {
      //     {
      //       this.errors.push("Something went wrong. Please try again");
      //     }
      //   });
    },
  },
};
</script>
