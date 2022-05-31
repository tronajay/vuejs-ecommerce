import { createStore } from "vuex";

export default createStore({
  modules: {
  },
  state: {
    cart: {
      items: [],
      address: "",
    },
    token: "",
    isAuthenticated: false,
    isLoading: false,
    httpError: false,
    httpSuccess: false,
    httpMessage: "",
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        state.cart = JSON.parse(localStorage.getItem("cart"));
      } else {
        localStorage.setItem("cart", JSON.stringify(state.cart));
      }
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(
        (i) => i.product.id === item.product.id
      );
      if (exists.length) {
        exists[0].quantity =
          parseInt(exists[0].quantity) + parseInt(item.quantity);
      } else {
        state.cart.items.push(item);
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    clearCart(state) {
      state.cart.items = [],

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state){
      state.token = "";
      state.isAuthenticated = false;
    },
    addAddress(state,address){
      state.cart.address = address;
      localStorage.setItem("cart",JSON.stringify(state.cart));
    },
    setIsLoading(state,value){
      state.isLoading = value;
    },
    setHttpError(state,message){
      state.httpError = true;
      state.httpMessage = message;
    },
    clearHttpAlert(state){
      state.httpError = false;
      state.httpMessage = false;
      state.httpMessage = "";
    },
    setHttpSuccess(state,message){
      state.httpSuccess = true;
      state.httpMessage = message;
    }
  },
});
