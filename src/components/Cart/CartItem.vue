<template>
  <tr class="border-b-2">
    <td class="p-4 flex items-center whitespace-nowrap space-x-6 mr-12 lg:mr-0">
      <div class="text-sm font-normal text-gray-500">
        <div class="text-base font-semibold text-gray-900">
          {{ item.product.name }}
        </div>
      </div>
    </td>
    <td class="p-4 whitespace-nowrap text-base font-medium text-gray-900">
      <span class="px-5 py-1 bg-gray-200 rounded-full">
        {{ item.quantity }}
      </span>
    </td>
    <td class="p-4 whitespace-nowrap space-x-2">
      <button
        type="button"
        @click="removeFromCart(item)"
        class="text-white bg-red-500 rounded-lg px-5 py-1 inline-flex"
      >
        <svg
          class="mr-2 h-5 w-5"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
            clip-rule="evenodd"
          ></path>
        </svg>
        Remove
      </button>
    </td>
  </tr>
</template>
<script>
export default {
  name: "cart-item",
  props: ["item"],
  data() {
    return {};
  },
  methods: {
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },
  },
};
</script>
