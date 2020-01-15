<template>
  <div id="app">
    <updatr-nav v-if="!isLogin"></updatr-nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLogin: function() {
      return !!this.$route.path.match(/^\/login/)
    }
  }
}
</script>

<style lang="scss">
@import url('https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css');

body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
