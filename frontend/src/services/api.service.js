import wretch from 'wretch'

const RAPPORT = {
  "discord.js":  {
    "packageVersion": "v0.0.0",
    "lastVersion": "v0.0.1",
    "url": "...",
    "doc": "..",
    "packageType": "...",
    "homepage": "...",
    "outdated": true
  },
  "ahhhhhhhhhh":  {
    "packageVersion": "v0.0.2",
    "lastVersion": "v0.0.3",
    "url": "...",
    "doc": "..",
    "packageType": "...",
    "homepage": "...",
    "outdated": true
  },
  "non":  {
    "packageVersion": "v0.0.2",
    "lastVersion": "v0.0.3",
    "url": "...",
    "doc": "..",
    "packageType": "...",
    "homepage": "...",
    "outdated": false
  }
}

export class apiService {

  static _service

  static getService() {
    if (!this._service) 
      this._service = new apiService()
    return this._service
  }

  _base

  constructor() {
    this._base = wretch().url('https://app.updatr.tech/api/')
  }

  getAllRepo() {
    return Promise.resolve([
      {
        repo_link: "https://github.com/oui",
        repo_name: "oui",
        hasAutoReport: true,
        frequence: 1,
        Discord_alert: true,
        Slack_alert: false,
        DateTimeRapport: new Date(6546546),
      },
      {
        repo_link: "https://github.com/non",
        repo_name: "non",
        hasAutoReport: true,
        frequence: 2,
        Discord_alert: false,
        Slack_alert: true,
        DateTimeRapport: new Date(6542513),
      },
      {
        repo_link: "https://github.com/pasencore",
        repo_name: "pasencore",
        hasAutoReport: false,
      }
    ])
  }

  getRapports(repo) {
    if (repo.repo_name === "oui")
      return Promise.resolve([
        {
          "non":  {
            "packageVersion": "v0.0.2",
            "lastVersion": "v0.0.3",
            "url": "...",
            "doc": "..",
            "packageType": "...",
            "homepage": "...",
            "outdated": false
          }
        }, RAPPORT
      ])
    if (repo.repo_name === "non")
      return Promise.resolve([
        RAPPORT,
        RAPPORT
      ])
    return Promise.resolve([
      RAPPORT
    ])
  }

}