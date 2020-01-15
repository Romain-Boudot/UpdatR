<template>
  <div class="container mt-5">
    <h1>Connexion via github</h1>
    {{ $route.params.token }}
    <a href="https://github.com/login/oauth/authorize?client_id=a79cafc41411d723ff50">Se connecter</a>
    <!-- <button v-on:click="login" type="button" class="btn btn-primary">Se connecter</button> -->
  </div>
</template>

<script>
export default {
  name: 'Login',
  mounted() {
    const token = $route.params.token
    if (!token) {
      return
    }
    this.$auth.token = token
    this.$router.push('/')
  },
  methods: {
    login() {
      this.$auth.token = 'oui'
      this.$router.push('/')
    }
  }
}
</script>

<style>

</style>