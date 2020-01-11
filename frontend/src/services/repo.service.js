import { apiService } from './api.service'

export class repoService {

  static _service

  static getService() {
    if (!this._service) 
      this._service = new repoService()
    return this._service
  }

  _base

  constructor() {
    this._api = apiService.getService()
  }

  getAllRepo() {
    return this._api.getAllRepo()
  }

  getRapport(repo) {
    return this._api.getRapports(repo)
  }

}