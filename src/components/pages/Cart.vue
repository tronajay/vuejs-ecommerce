<script>
import CartItem from "../Cart/CartItem.vue";
import CartSidebar from "../Cart/CartSidebar.vue";
import { RouterLink } from "vue-router";
export default {
  data() {
    return {
      cart: {
        items: [],
      },
      address: {},
    };
  },
  components: {
    CartItem,
    CartSidebar,
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.product.id !== item.product.id
      );
    },
  },
};
</script>

<template>
  <div v-if="cart.items.length > 0" class="cart py-3 px-3 lg:px-10">
    <div class="mb-5">
      <h2 class="font-bold text-2xl">Your Shopping Cart</h2>
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-3 lg:gap-6">
      <div class="col-span-2 mb-3">
        <div
          v-if="cart.address"
          class="selected-address border mb-3 rounded-lg shadow-md p-3"
        >
          <div class="flex justify-between items-center">
            <div class="address px-2">
              <h2 class="font-bold">
                {{ cart.address.first_name }} {{ cart.address.last_name }}
              </h2>
              <p>
                {{ cart.address.address_1 }},{{ cart.address.city }},
                {{ cart.address.state }}, {{ cart.address.postal_code }}
              </p>
            </div>
            <RouterLink
              to="/address"
              class="text-blue-500 ring-1 ring-blue-500 my-3 rounded-lg px-5 py-2 hover:ring-2"
            >
              Change Address
            </RouterLink>
          </div>
        </div>
        <div v-else class="add-address border mb-3 rounded-lg shadow-md p-3">
          <div class="heading flex justify-between items-center">
            <h2 class="font-bold text-xl px-2">
              Add New Address
            </h2>
            <RouterLink
              to="/address"
              class="text-blue-500 ring-1 ring-blue-500 my-3 rounded-lg px-5 py-2 hover:ring-2"
            >
              Add Here
            </RouterLink>
          </div>
        </div>
        <div class="relative rounded-lg border shadow-md overflow-x-auto">
          <div class="cart-heading my-2 p-3 text-xl font-bold">Cart Items</div>
          <table class="w-full text-sm text-left text-gray-500">
            <thead
              class="text-xs text-gray-700 font-bold uppercase bg-gray-100 border"
            >
              <tr>
                <th scope="col" class="px-6 py-3">Product name</th>
                <th scope="col" class="px-6 py-3">quantity</th>
                <th scope="col" class="px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody>
              <cart-item
                v-for="item in cart.items"
                :key="item.product.id"
                :item="item"
                v-on:removeFromCart="removeFromCart"
              ></cart-item>
            </tbody>
          </table>
        </div>
      </div>
      <!-- Cart Sidebar: Start-->
      <div class="cart-sidebar">
        <cart-sidebar></cart-sidebar>
        <RouterLink
          to="/order"
          class="float-right text-white my-3 bg-blue-500 rounded-lg px-5 py-2 shadow-md hover:bg-blue-700"
        >
          Place Order
        </RouterLink>
      </div>
      <!-- Cart Sidebar: End -->
    </div>
  </div>
  <div v-else class="empty-cart mt-20 text-center">
    <div class="text-gray-500 text-xl w-full">
      <img
        src="http://cdn.onlinewebfonts.com/svg/img_456359.png"
        class="w-24 mx-auto"
        alt=""
      />
      <p class="my-5">Your Cart is Empty. Add Some Products Now</p>
      <RouterLink
        to="/"
        class="bg-blue-500 rounded-lg px-10 text-lg shadow-md py-2 text-white"
        >Go to Home</RouterLink
      >
    </div>
  </div>
</template>
