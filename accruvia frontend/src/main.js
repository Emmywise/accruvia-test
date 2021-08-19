/* eslint-disable */
import Vue from "vue";
import NProgress from "nprogress";
import axios from "axios";
import Toast from "vue-toastification";
import VueTailwind from "vue-tailwind";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/styles/index.css";
import "nprogress/nprogress.css";
import "vue-toastification/dist/index.css";

Vue.config.productionTip = false;
Vue.use(VueTailwind);
Vue.use(Toast, {});
axios.defaults.baseURL = "http://localhost:8000/api/";
Object.defineProperty(Vue.prototype, "$http", { value: axios, enumerable: false });
Object.defineProperty(Vue.prototype, "$nprogress", { value: NProgress, enumerable: false });
library.add(faSearch);
Vue.component("icon", FontAwesomeIcon);

Vue.mixin({
  methods: {
    formatDate(date) {
      let newDate = new Date(date);
      return `${newDate.toDateString()} at ${newDate.toLocaleTimeString()}`;
    }
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
