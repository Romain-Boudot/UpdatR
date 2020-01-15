<template>
  <div class="main-container">
    <div v-bind:class="isExpended ? 'pt-5 pb-5 expended' : 'sided'" class="side-nav">
      <div class="list-container">
        <ul class="list-group list-group-flush">
          <li v-for="repo in repos" v-bind:key="repo.repo_link" class="list-group-item d-flex align-items-center">
            <div>
              <router-link class="link" v-bind:to="btoa(repo.repo_link)">{{ repo.repo_name }}</router-link>
              <a target="_blank" class="badge badge-secondary little ml-2" v-bind:href="repo.repo_link">github</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <div class="details p-5">
      <div class="container mt-5">
        <h1>{{ targetedRepo.repo_name }}</h1>

        <div class="form-group">
          <label for="discord">Alerte Discord (vide pour ne rien envoyer)</label>
          <input v-model="targetedRepo.Discord_alert" type="text" class="form-control" id="discord" placeholder="https://...">
        </div>

        <div class="form-group">
          <label for="slack">Alerte Slack (vide pour ne rien envoyer)</label>
          <input v-model="targetedRepo.Slack_alert" type="text" class="form-control" id="slack" placeholder="https://...">
        </div>

        <button v-on:click="createRapport" type="button" class="btn btn-primary">Demander un rapport</button>

        <ul class="list-group">
          <li v-for="rapport in rapports" v-bind:key="rapport.date" class="list-group-item rapport">
            <h5>{{ rapport.date }}</h5>
            <ul class="list-group list-group-flush w-100">
              <li v-if="filteredRapport(rapport).length === 0" class="list-group-item d-flex align-items-center">Rien à signaler</li>
              <li v-for="dep in filteredRapport(rapport)" v-bind:key="dep.packageName" class="list-group-item d-flex align-items-center">
                <span class="mr-3">{{ dep.packageName }}</span>
                <span class="ml-3 mr-3 text-danger">{{ dep.packageVersion }}</span>
                <span class="ml-3 text-success">{{ dep.lastVersion }}</span>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      isExpended: true,
      repos: [],
      targetedRepo: {},
      rapports: []
    }
  },
  mounted() {
    const repoId = this.$route.params.repo
    if (repoId) this.isExpended = false
    this.$repo.getAllRepo().then(repos => {
      this.repos = repos
      if (repoId) {
        this.targetedRepo = repos.find(repo => btoa(repo.repo_link) === repoId)
        this.$repo.getRapport(this.targetedRepo).then(rapports => {
          this.rapports = rapports
        })
      }
    })
  },
  watch: {
    $route(to, from) {
      if (to.params.repo) {
        this.isExpended = false
        this.targetedRepo = this.repos.find(repo => btoa(repo.repo_link) === to.params.repo)
        this.$repo.getRapport(this.targetedRepo).then(rapports => {
          this.rapports = rapports
        })
      } else {
        this.isExpended = true
        this.targetedRepo = {}
      }
    }
  },
  methods: {
    btoa(string) { return btoa(string) },
    filteredRapport(rapport) {
      return Object.keys(rapport).map(depName => ({...rapport[depName], packageName: depName})).filter(dep => dep.outdated)
    },
    createRapport() {
      this.$repo.createRapport(this.targetedRepo)
    }
  }
}
</script>

<style lang="scss">
.little { font-size: .65em }
.link { font-size: 1.5em; color: inherit }
.link:hover { text-decoration: none; color: inherit }

.main-container {
  position: relative;
  display: flex;
  flex: 1;
  .side-nav {
    position: absolute;
    z-index: 10000;
    display: flex;
    justify-content: center;
    width: calc(100%);
    height: 100%;
    box-shadow: 8px 0px 6px -6px rgb(207, 207, 207);
    transition: .5s all ease;
    background: white;
  }
  .side-nav>.list-container {
    width: 900px;
    max-width: 100%;
  }
  .side-nav.sided {
    width: calc(300px);
  }
  .list-container ul li {
    display: flex;
    >* { flex: 1 }
    >*:nth-child(1) { flex: 2 !important }
  }
  .details {
    width: 100%;
    padding-left: calc(300px + 3rem) !important;
  }
}
</style>
