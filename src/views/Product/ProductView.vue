<template>
  <div class="container w-full px-5">
    <div class="md:flex gap-3 space-y-3">
      <div class="p-3 md:w-4/5 grid grid-cols-1 md:grid-cols-2">
        <div class="p-10 rounded-lg image-gallery">
          <img
            src="https://m.media-amazon.com/images/I/71HcZHyEsTL._SL1500_.jpg"
            alt=""
          />
        </div>
        <div class="class p-3 md:mt-10 product-detail">
          <h2 class="font-bold text-xl">
            {{product.name}}
          </h2>
          <div class="flex rating items-center mt-2.5 mb-5">
            <svg
              class="w-5 h-5 text-yellow-300"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              ></path>
            </svg>
            <svg
              class="w-5 h-5 text-yellow-300"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              ></path>
            </svg>
            <svg
              class="w-5 h-5 text-yellow-300"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              ></path>
            </svg>
            <svg
              class="w-5 h-5 text-yellow-300"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              ></path>
            </svg>
            <svg
              class="w-5 h-5 text-yellow-300"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
              ></path>
            </svg>
            <span
              class="bg-blue-100 text-blue-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded dark:bg-blue-200 dark:text-blue-800 ml-3"
              >5.0</span
            >
          </div>
          <div class="pricing">
            <p class="text-lg space-x-2">
              <span class="font-bold">₹{{product.selling_price}}</span>
              <span class="line-through text-gray-500">₹{{product.price}}</span>
            </p>
          </div>
          <div class="actions flex mt-5 space-x-3">
            <button
            @click="addToCart()"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2 text-center"
            >
              Add to cart
            </button>
            <button
            @click="buyNow()"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2 text-center"
            >
              Buy Now
            </button>
          </div>
          <div
            class="bank-offers flex gap-3 items-center p-3 mt-5 border-b-4 border-green-600 rounded-lg bg-green-100"
          >
            <img
              class="w-8"
              src="https://pic.onlinewebfonts.com/svg/img_85955.png"
              alt=""
            />
            <div>Rs.1000 Cashback on Amazon Pay ICICI Credit Card.</div>
          </div>
          <div class="description mt-5">
            <h3 class="font-bold text-lg mb-2">Description</h3>
            <hr />
            <p class="desc-content">
              {{product.desc}}
            </p>
          </div>
        </div>
      </div>
      <div class="md:w-1/5">
        <cart-sidebar />
        <div class="justify-end flex">
          <RouterLink
            to="/cart"
            class="text-white mt-3 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2 text-center"
          >
            View Cart
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CartSidebar from "../../components/Cart/CartSidebar.vue";
import Product from "../../models/product";
import APIService from "../../services/api-call";
export default {
  data() {
    return {
      product: new Product("", "", "", "", ""),
      slug: this.$route.params.slug,
      quantity: 1,
    };
  },
  components: {
    CartSidebar,
  },
    async created() {
    var response = await new APIService(`/api/product/${this.slug}/view/`).get();
    this.product = response.data;
    console.log(this.product);
  },
    methods: {
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
          this.quantity = 1
      }
      const item = {
          product: this.product,
          quantity: this.quantity
      }
      this.$store.commit('addToCart', item)
    },
    buyNow(){
        this.addToCart();
        this.$router.push("/cart");
    }
  },
};
</script>
