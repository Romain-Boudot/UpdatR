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
    return wretch().url('https://app.updatr.tech/api/rapportinfo/list').headers({
      authorization: this._auth.token
    }).get()
  }

  getRapports(repo) {
    return wretch().url('https://app.updatr.tech/api/rapport/list?repo_link=' + repo.repo_link).headers({
      authorization: this._auth.token
    }).get()
  }

}