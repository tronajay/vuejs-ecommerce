<script>
export default {
  props: ["address"],
  data(){
      return {
          selected_address: '',
      }
  },
  methods:{
      selectAddress(address){
          this.$emit("selectAddress", address);
      }
  },
  mounted(){
      this.selected_address = this.$store.state.cart.address.id;
  }
};
</script>

<template>
  <div class="flex items-center focus:bg-gray-200 mb-4">
    <input
      :id="'address-select-'+address.id"
      type="radio"
      name="countries"
      :value="address.id"
      class="w-4 h-4 border-gray-300"
      @click="selectAddress(address)"
      :checked="selected_address==address.id?true:false"
    />
    <label
      :for="'address-select-'+address.id"
      class="block ml-2 text-sm font-medium text-gray-900"
    >
      <div class="select">
          <h2 class="font-bold text-lg">{{ address.first_name }} {{ address.last_name }}</h2>
          <p>{{address.address_1}},{{address.city}}, {{address.state}}, {{address.postal_code}}</p>
      </div>
    </label>
  </div>
</template>
