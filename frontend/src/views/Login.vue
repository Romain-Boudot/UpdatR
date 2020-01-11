<template>
  <div class="container mt-5">
    <h1>Connexion via github</h1>
    <button v-on:click="login" type="button" class="btn btn-primary">Se connecter</button>
  </div>
</template>

<script>
export default {
  name: 'Login',
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