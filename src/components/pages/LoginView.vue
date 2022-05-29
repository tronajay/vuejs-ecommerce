<template>
  <div class="container">
    <div
      class="mx-auto md:w-2/3 border border-gray-300 p-5 shadow-md mt-10 rounded-lg"
    >
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
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            placeholder="name@flowbite.com"
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
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
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
export default {
  name: "LoginView",
  data() {
    return {
      user: new User("", ""),
      loading: false,
      message: "",
    };
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
      localStorage.removeItem("token");
      await axios
        .post("/api/login/", this.user)
        .then((response) => {
          const token = response.data.access;
          this.$store.commit("setToken", token);

          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          const url = this.$route.query.to || "/";
          this.$router.push(url);
        })
        .catch((error) => {
          {
            this.errors.push("Something went wrong. Please try again");
          }
        });
    },
  },
};
</script>
