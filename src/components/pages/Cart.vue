<script>
import CartItem from '../Cart/CartItem.vue';
import CartSidebar from '../Cart/CartSidebar.vue';
import { RouterLink } from 'vue-router';
export default {
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  components:{
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
  <div class="cart p-3">
    <div class="flex justify-between">
      <h2 class="font-bold text-2xl">Your Shopping Cart</h2>
    </div>
    <div class="flex gap-2 w-4/5 mx-auto">
      <div class="mt-5 w-4/5 border rounded-lg p-3 shadow-md">
        <div class="relative overflow-x-auto">
          <table class="w-full text-sm text-left text-gray-500">
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
        <RouterLink to="/address" class="float-right text-white my-3 bg-blue-500 rounded-lg px-5 py-2 shadow-md hover :bg-blue-700">
          Place Order
        </RouterLink>
      </div>
      <!-- Cart Sidebar: Start-->
      <div class="cart-sidebar w-2/5">
        <cart-sidebar></cart-sidebar>
      </div>
      <!-- Cart Sidebar: End -->
    </div>
  </div>
</template>