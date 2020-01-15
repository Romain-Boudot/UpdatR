import Vue from 'vue'
import App from './App.vue'
import router from './router'
import nav from './components/nav.vue'
import { authService } from './services/auth.service'
import { repoService } from './services/repo.service'

Vue.config.productionTip = false

Vue.component(nav.name, nav)

Vue.prototype.$auth = authService.getService()
Vue.prototype.$repo = repoService.getService()

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
