import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import VueSession from 'vue-session' // 발급받은 token을 sessionstorage에 저장하는 것을 도와줌. 

import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false;
Vue.use(VueSession);
Vue.use(BootstrapVue);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
