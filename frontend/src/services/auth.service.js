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

  setToken(value) {
    if (value) { 
      localStorage.setItem('authToken', value)
    } else {
      localStorage.clear()
    }
    this._token = value
    console.warn(value, this._token)
  }

  logout() {
    localStorage.clear()
    this._token = null
  }

}