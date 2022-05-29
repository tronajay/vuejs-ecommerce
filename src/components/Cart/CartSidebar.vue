<script>
export default {
    name:"cart-sidebar",
    data(){
        return {
            cart: {
                items: []
            }
        }
    },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    totalItems() {
      return this.cart.items.length;
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.selling_price * curVal.quantity);
      }, 0);
    },
  },
};
</script>

<template>
  <div class="rounded-lg border p-3 shadow-md">
    <div class="header font-bold text-xl my-2">Price Details</div>
    <div class="content my-2">
      <div class="price flex my-2 justify-between">
        <span class="font-bold text-gray-500">
          Price ({{ totalItems }})Items
        </span>
        <span> ₹{{ cartTotalPrice }} </span>
      </div>
      <div class="discount my-2 flex justify-between">
        <span class="font-bold text-gray-500"> Discount </span>
        <span class="text-green-500"> ₹200 </span>
      </div>
      <div class="delivery my-2 flex justify-between">
        <span class="font-bold text-gray-500"> Delivery </span>
        <span class="text-green-500"> FREE </span>
      </div>
      <hr />
      <div class="total my-3 flex justify-between">
        <span class="font-bold"> Total </span>
        <span> ₹{{ cartTotalPrice }} </span>
      </div>
    </div>
    <hr />
  </div>
</template>
