<template>
	<nav class="navbar navbar-dark bg-dark">
		<router-link class="navbar-brand" to="/">UpdatR</router-link>
		<div>
			<button v-on:click="logout" type="button" class="btn btn-warning btn-sm">Se déconnecter</button>
		</div>
	</nav>
</template>

<script>
export default {
	name: 'updatr-nav',
	methods: {
		logout() {
			this.$auth.logout()
			this.$router.push('/login')
		}
	}
}
</script>

<style>

</style>