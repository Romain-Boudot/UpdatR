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
    return wretch().url('https://app.updatr.tech/api/rapportinfo/').headers({
      authorization: this._auth.token
    }).get().json()
  }

  getRapports(repo) {
    return wretch().url('https://app.updatr.tech/api/rapport/?repo_link=' + repo.repo_link).headers({
      authorization: this._auth.token
    }).get().json()
  }

  createRapport(repo) {
    return wretch().url('https://app.updatr.tech/api/rapport/').headers({
      authorization: this._auth.token
    }).post({ repo_link: repo.repo_link, Discord_alert: repo.Discord_alert, Slack_alert: repo.Slack_alert }).json()
  }

}