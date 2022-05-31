<template>
  <div class="container p-3">
    <div
      id="product-form"
      class="p-3 mx-auto md:w-2/3 mt-5 rounded-lg border shadow-md border-gray-300"
    >
      <div class="heading">
        <h2 class="font-bold text-center text-xl mb-5">Add Product</h2>
      </div>
      <form class="" @submit.prevent="submitData">
        <div class="relative z-0 w-full mb-6 group">
          <input
            type="text"
            name="name"
            required
            v-model="input.name"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" "
          />
          <label
            for="name"
            class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
            >Product Name</label
          >
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div class="relative z-0 w-full mb-6 group">
            <input
              type="text"
              name="price"
              required
              v-model="input.price"
              class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
              placeholder=" "
            />
            <label
              for="price"
              class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
              >Original Price</label
            >
          </div>
          <div class="relative z-0 w-full mb-6 group">
            <input
              type="text"
              name="selling_price"
              required
              v-model="input.selling_price"
              class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
              placeholder=" "
            />
            <label
              for="selling_price"
              class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
              >Selling Price</label
            >
          </div>
        </div>
        <div class="relative z-0 w-full mb-6 group">
          <input
            type="text"
            name="feature_img"
            required
            v-model="input.feature_img"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" "
          />
          <label
            for="feature_img"
            class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
            >Product Feature Image</label
          >
        </div>
        <div class="w-full mb-6">
          <textarea
            name="desc"
            id="desc"
            rows="4"
            required
            v-model="input.desc"
            class="block p-2.5 w-full text-sm text-gray-900 border-b-2 border-0 border-gray-300 outline-none"
            placeholder="Enter Description"
          ></textarea>
        </div>
        <button
          type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Submit
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import Product from "../../models/product";
import APIService from "../../services/api-call";
export default {
  data() {
    return {
      input: new Product("", "", "", "", ""),
      resp: "",
      error: "",
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.isAuthenticated;
    },
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push(`/login?next=${this.$route.path}`);
    }
  },
  methods: {
    async submitData() {
      var response = await new APIService("/api/product/", this.input).post();
      if (response.status) {
        this.$router.push({
          name: "home",
          params: {
            message: "Product Added Successfully",
          },
        });
      }
    },
  },
};
</script>
