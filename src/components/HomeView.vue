<script>
import ProductCard from "./product/ProductCard.vue";
import APIService from "../services/api-call";

export default {
    components: {
        ProductCard
    },
  data() {
    return {
      products: [],
      errors: [],
      quantity: 1,
    };
  },

  async created() {
    var response = await new APIService('/api/product/',{}).get();
    this.products = response.data;
  },
  methods: {},
};
</script>

<template>
  <div class="px-5 py-10">
    <div
      v-if="this.$route.params.message"
      class="message mx-5 my-2 bg-green-200 rounded-lg border py-2 px-5"
    >
      {{ this.$route.params.message }}
    </div>
    <div class="header flex justify-between">
      <h2 class="font-bold text-2xl">List of Products</h2>
      <RouterLink
        to="/add-product/"
        class="px-5 py-2 bg-blue-500 text-white rounded-lg"
        >Add Product
      </RouterLink>
    </div>
    <div
      class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 p-3 mt-5"
    >
      <div
        v-for="product in products"
        :key="product.id"
        class="rounded-lg shadow-md border"
      >
       <product-card :product="product">
       </product-card>
      </div>
    </div>
  </div>
</template>
