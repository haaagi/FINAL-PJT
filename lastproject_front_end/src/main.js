import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueSession from 'vue-session'

import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false;
Vue.use(VueSession);
Vue.user(BootstrapVue);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
