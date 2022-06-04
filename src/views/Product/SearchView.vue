<template>
  <div class="container p-3">
    <div class="heading">
      <h2>Search Results: {{query}}</h2>
    </div>
    <loading-bar/>
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

<script>
import APIService from "../../services/api-call";
import LoadingBar from "../../components/LoadingBar.vue";
import ProductCard from "../../components/product/ProductCard.vue";
export default {
  data() {
    return {
      products: [],
      query: "",
    };
  },
  components:{
      LoadingBar,
      ProductCard
  },
  async created() {
    this.query = this.$route.query.q;
    var response = await new APIService(
      `/api/product/search/?search=${this.query}`
    ).get();
    console.log(response);
    this.products = response.data;
  },
};
</script>
