<template>

    <div class="container">
        <div class="mx-auto md:w-2/3 border border-gray-300 p-5 shadow-md mt-10 rounded-lg">
            <div v-if="http_error" class="error bg-red-200 border mb-2 rounded-lg px-3 py-1">
                {{ message }}
            </div>
            <form @submit.prevent="handleRegister">
                <div class="mb-6">
                    <label for="username" class="block mb-2 text-sm font-medium text-gray-900">Username</label>
                    <input type="text" id="username" v-model="user.username" @keyup="checkUsername"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                        placeholder="Enter username">
                    <div v-if="errors.username" class="error text-sm my-2 text-red-500">
                        {{ errors.username }}</div>
                </div>
                <div class="mb-6">
                    <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
                    <input type="text" id="email" v-model="user.email" @keyup="checkEmail"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "
                        placeholder="mail@example.com">
                    <div v-if="errors.email" class="error text-sm my-2 text-red-500">
                        {{ errors.email }}</div>
                </div>
                <div class="mb-6">
                    <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Your
                        password</label>
                    <input type="password" id="password" placeholder="Enter Password" v-model="user.password"
                        @keyup="checkPassword"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 ">
                    <div v-if="errors.password" class="error text-sm my-2 text-red-500">
                        {{ errors.password }}</div>
                </div>
                <div class="actions flex justify-between items-center">
                    <button
                        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center">Register</button>
                    <span>Already a User?
                        <RouterLink to="/login" class="text-blue-500 font-bold">Login</RouterLink>
                    </span>
                </div>

            </form>
        </div>
    </div>

</template>


<script>
import User from '../../models/user';
import { RouterLink } from 'vue-router';
export default {
    name: 'Register',
    data() {
        return {
            user: new User('', '', ''),
            submitted: false,
            successful: false,
            message: '',
            errors: {},
            http_error: false
        };
    },
    computed: {
        loggedIn() {
            return this.$store.state.isAuthenticated;
        }
    },
    mounted() {
        if (this.loggedIn) {
            this.$router.push('/');
        }
    },
    methods: {
        checkUsername() {
            if (!this.user.username) {
                this.errors["username"] = "Username is Required!";
            } else if (this.user.username.length < 8) {
                this.errors["username"] = "Username should be atleast 8 characters";
            }
            else {
                delete this.errors["username"]
            }
        },
        checkEmail() {
            var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            if (!this.user.email) {
                this.errors["email"] = "Email is Required!";

            } else if (!this.user.email.match(re)) {
                this.errors["email"] = "Enter Valid email address.";
            }
            else {
                delete this.errors["email"]
            }
        },
        checkPassword() {
            if (!this.user.password) {
                this.errors["password"] = "Password is required!";

            } else if (this.user.password.length < 8) {
                this.errors["password"] = "Password should be atleast 8 characters.";
            }
            else {
                delete this.errors["password"]
            }
        },
        handleRegister() {
            this.message = '';
            this.submitted = true;
            this.$store.dispatch('auth/register', this.user).then(
                data => {
                    this.message = data.message;
                    this.successful = true;
                    this.$router.push("/login");
                },
                error => {
                    this.message =
                        (error.response && error.response.data) ||
                        error.message ||
                        error.toString();
                    this.http_error = true;
                }
            );

        }
    }
};
</script>
