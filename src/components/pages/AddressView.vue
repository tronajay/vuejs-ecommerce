<script>
import AddressCard from "../Address/AddressCard.vue";
import Address from "../../models/address";
import CartSidebar from "../Cart/CartSidebar.vue";
import axios from "axios";
export default {
  data() {
    return {
      saved_address: [],
      order_placed: false,
      address: new Address("", "", "", "", "", "", "", ""),
    };
  },
  components: {
    AddressCard,
    CartSidebar,
  },
  computed: {
    loggedIn() {
      return this.$store.state.isAuthenticated;
    },
  },
  created() {
    axios.get("/api/address/").then((response) => {
      this.saved_address = response.data;
    });
  },
  mounted() {
    if (!this.loggedIn) {
      this.$router.push(`/login/?next=address`);
    }
  },
  methods: {
    selectAddress(address) {
      this.$store.commit("addAddress", address);
    },
    async submitAddress() {
      await axios
        .post("/api/address/", this.address)
        .then(
          (response) => this.selectAddress(response.data),
          this.$router.go(0)
        );
    },
    orderPlaced(){
      this.order_placed = true;
      this.$store.commit("clearCart");
    }
  },
};
</script>

<template>
  <div class="container">
    <div v-if="!order_placed" class="container mx-auto">
      <div class="rounded-lg p-5 w-4/5 mx-auto mt-5 border shadow-md">
        <div class="header font-bold text-xl mb-2">Saved Address</div>
        <hr />
        <div class="saved-address mt-5">
          <AddressCard
            v-for="address in saved_address"
            :key="address.id"
            :address="address"
            v-on:selectAddress="selectAddress"
          ></AddressCard>
          <div class="my-2 flex justify-end">
            <button @click="orderPlaced" class="bg-blue-500 shadow-lg border-b-2 border-r-2 border-white px-5 py-2 rounded-lg text-white font-bold">
              Place Order
            </button>
          </div>
        </div>
      </div>
      <div class="rounded-lg w-4/5 mx-auto p-5 mt-10 border shadow-md">
        <div class="header my-2">
          <h2 class="font-bold text-xl">Add Address</h2>
        </div>
        <hr />
        <div class="mt-5">
          <form @submit.prevent="submitAddress">
            <div class="grid xl:grid-cols-2 xl:gap-6">
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="text"
                  name="floating_first_name"
                  id="first_name"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  v-model="address.first_name"
                  required=""
                />
                <label
                  for="floating_first_name"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >First name</label
                >
              </div>
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="text"
                  name="floating_last_name"
                  id="last_name"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  v-model="address.last_name"
                  required=""
                />
                <label
                  for="floating_last_name"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >Last name</label
                >
              </div>
            </div>
            <div class="relative z-0 w-full mb-6 group">
              <input
                type="text"
                name="address1"
                id="address1"
                class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                placeholder=" "
                v-model="address.address_1"
                required=""
              />
              <label
                for="address1"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Address 1</label
              >
            </div>
            <div class="relative z-0 w-full mb-6 group">
              <input
                type="text"
                name="address2"
                id="address2"
                class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                placeholder=" "
                v-model="address.address_2"
              />
              <label
                for="address2"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                >Address 2 (Optional)</label
              >
            </div>
            <div class="grid xl:grid-cols-3 xl:gap-6">
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="text"
                  name="city"
                  id="city"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  v-model="address.city"
                  required=""
                />
                <label
                  for="city"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >City</label
                >
              </div>
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="text"
                  name="state"
                  id="state"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  v-model="address.state"
                  required=""
                />
                <label
                  for="state"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >State</label
                >
              </div>
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="text"
                  name="postal_code"
                  id="postal_code"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  v-model="address.postal_code"
                  required=""
                />
                <label
                  for="postal_code"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >Postal Code</label
                >
              </div>
            </div>

            <div class="grid xl:grid-cols-2 xl:gap-6">
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="tel"
                  pattern="[0-9]{10}"
                  name="phone"
                  id="phone"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  required=""
                  v-model="address.phone"
                />
                <label
                  for="phone"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >Phone number (123-456-7890)</label
                >
              </div>
              <div class="relative z-0 w-full mb-6 group">
                <input
                  type="text"
                  name="floating_company"
                  id="floating_company"
                  class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                  placeholder=" "
                  v-model="address.company"
                  required=""
                />
                <label
                  for="floating_company"
                  class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
                  >Company (Ex. Google)</label
                >
              </div>
            </div>
            <button
              type="submit"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Add New Address
            </button>
          </form>
        </div>
      </div>
    </div>
    <div v-if="order_placed" class="w-full mt-10 text-center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/BlueFlat_tick_icon.svg/512px-BlueFlat_tick_icon.svg.png" class="w-48 mx-auto h-48" alt="">
      <p class="font-bold my-10 text-xl">
        Order Placed Successfully
      </p>
      <RouterLink to="/" class="bg-blue-500 mt-10 rounded-lg px-10 text-lg shadow-md py-2 text-white ">Go to Home</RouterLink>
    </div>
  </div>
</template>
