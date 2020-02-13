import Vue from 'vue'
import App from './App.vue'
import VueGoogleCharts from 'vue-google-charts'
import LoadScript from 'vue-plugin-load-script';

Vue.config.productionTip = false
Vue.use(VueGoogleCharts)
Vue.use(LoadScript);

new Vue({
  render: h => h(App),
}).$mount('#app')
