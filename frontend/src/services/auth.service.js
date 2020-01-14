export class authService {

  static _service

  static getService() {
    if (!this._service) 
      this._service = new authService()
    return this._service
  }

  _token

  constructor() {
    const token = localStorage.getItem('authToken')
    this._token = token || null
  }

  get token() {
    return this._token
  }

  set token(value) {
    localStorage.setItem('authToken', value)
    this._token = value
  }

  logout() {
    localStorage.clear()
    this.token = null
  }

}