import wretch from 'wretch'
import { authService } from './auth.service'

export class apiService {

  static _service

  static getService() {
    if (!this._service) 
      this._service = new apiService()
    return this._service
  }

  _auth

  constructor() {
    this._auth = authService.getService()
  }

  getAllRepo() {
    console.log(this._auth.token)
    return wretch().url('https://app.updatr.tech/api/rapportinfo/').headers({
      authorization: this._auth.token
    }).get().json()
  }

  getRapports(repo) {
    console.log(this._auth.token)
    return wretch().url('https://app.updatr.tech/api/rapport/?repo_link=' + repo.repo_link).headers({
      authorization: this._auth.token
    }).get().json()
  }

  createRapport(repo) {
    console.log(this._auth.token)
    return wretch().url('https://app.updatr.tech/api/rapport/askfor/').headers({
      authorization: this._auth.token
    }).put({ repo_link: repo.repo_link, Discord_alert: repo.Discord_alert, Slack_alert: repo.Slack_alert }).json()
  }

}