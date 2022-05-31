<template>
    <div class="container p-3">
        <div id="product-form" class="p-3 mx-auto md:w-2/3 mt-5 rounded-lg border shadow-md border-gray-300">
            <div class="heading">
                <h2 class="font-bold text-center text-xl my-2">
                    Update Product: {{ product.name }}
                </h2>
            </div>
            <form class="" @submit.prevent="updateProduct">
                <div class="relative z-0 w-full mb-6 group">
                    <input type="text" name="name" v-model="product.name"
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                        placeholder=" ">
                    <label for="name"
                        class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Product
                        Name</label>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <div class="relative z-0 w-full mb-6 group">
                        <input type="text" name="price" v-model="product.price"
                            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                            placeholder=" ">
                        <label for="price"
                            class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Original
                            Price</label>
                    </div>
                    <div class="relative z-0 w-full mb-6 group">
                        <input type="text" name="selling_price" v-model="product.selling_price"
                            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                            placeholder=" ">
                        <label for="selling_price"
                            class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Selling
                            Price</label>
                    </div>
                </div>
                 <div class="relative z-0 w-full mb-6 group">
                    <input type="text" name="name" v-model="product.feature_img"
                        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                        placeholder=" ">
                    <label for="name"
                        class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Product
                        Feature Image</label>
                </div>
                <div class="w-full mb-6">
                    <textarea name="desc" id="desc" rows="4"
                        class="block p-2.5 w-full text-sm text-gray-900 border-b-2 border-0 border-gray-300 outline-none"
                        placeholder="Enter Description">{{ product.desc }}</textarea>

                </div>
                <button type="submit"
                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center">Update</button>
            </form>

        </div>
    </div>
</template>

<script>
import axios from "axios";
import Product from "../../models/product";
import APIService from "../../services/api-call";

export default {
    data() {
        return {
            product: new Product("","","","",""),
            id: this.$route.params.id,
        }
    },
    computed: {
        loggedIn() {
            return this.$store.state.isAuthenticated;
        }
    },
    mounted() {
        if (!this.loggedIn) {
            this.$router.push(`/login?next=${this.$route.path}`);
        }
    },

    methods: {
        async updateProduct() {
            var response = await new APIService(`/api/product/${this.id}/`,this.product).patch();
            console.log(response.status);
            if (response.status) {
                this.$router.push(
                    {
                        name: 'home',
                        params: {
                            message: "Product Updated Successfully"
                        }
                    }
                )
            }
        }
    },

    created() {
        axios.get(`/api/product/${this.id}`)
            .then(response => {
                this.product = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
    },
}

</script>