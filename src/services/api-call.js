import axios from "axios";
import store from "../store/index";

export default class APIService {
  constructor(url, data,e_msg="") {
    this.data = data;
    this.url = url;
    this.resp = {};
    this.e_msg = e_msg;
    this.status = false;
    store.commit("setIsLoading", true);
    store.commit("clearHttpAlert");
  }

  async post() {
    await axios
      .post(this.url, this.data)
      .then((response) => {
        this.resp = response;
        console.log(response)
      })
      .catch((error) => {
        this.resp = error.response;
      });
    if ((this.resp.status >= 200) & (this.resp.status < 400)) {
      this.status = true;
    } else {
      console.log(this.resp);
      if (this.resp.data.error) {
        store.commit("setHttpError", this.resp.data.error);
      } else {
        if(this.e_msg){
          store.commit("setHttpError", this.e_msg);
        }else{
          store.commit("setHttpError", "Something Went Wrong");
        }
      }
    }
    store.commit("setIsLoading", false);
    return {
      "status":this.status,
      "data":this.resp.data,
    };
  }

  async get() {
    await axios
      .get(this.url)
      .then((response) => {
        this.resp = response;
      })
      .catch((error) => {
        this.error = error.response;
      });
    store.commit("setIsLoading", false);
    return {
      "data":this.resp.data,
    };
  }

  async patch() {
    await axios
      .patch(this.url, this.data)
      .then((response) => {
        this.resp = response;
      })
      .catch((error) => {
        this.resp = error.response;
      });
    if ((this.resp.status >= 200) & (this.resp.status < 400)) {
      this.status = true;
    } else {
      if (this.resp.data.error) {
        store.commit("setHttpError", this.resp.data.error);
      } else {
        store.commit("setHttpError", "Something Went Wrong");
      }
    }
    store.commit("setIsLoading", false);
    return {
      "status":this.status,
      "data":this.resp.data,
    };
  }
}
