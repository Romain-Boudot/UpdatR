const tokenAnalyse = require('./tokenAnalyse')

PATH_URLS = {
    'all': getAll, // retourne tous les tokens
    'exist': existPath // retourne true si le token passé en paramètre existe, faux sinon
}


exports.setApi = function (req) {
  return getOnPath(req)
}

function getOnPath(req) {
  const url = req.url
  const path = url.split('/')
  path.splice(0, 2)

  const p = path[0]

  if (p === '' || PATH_URLS[p] === undefined) { // s'il n'y a pas de paramètre
    return printPathUrls()
  }

  return PATH_URLS[p](req, path)
}

function printPathUrls() { // affiche le retour de cette fonction lors de requête inexistante
  return [
    'all',
    'exist/username/{username}',
    'exist/token/{token}'
  ]
}

function getAll(req, path) {
  return tokenAnalyse.getUsersToken()
}

/**
 * Ici, nous nous occupons de /exist
 */

EXIST_PATH = {
    'username': existUserName,
    'token': existToken
}

function existPath(req, path) {
  path.splice(0, 1)
  const p = path[0]

  if (path.length < 2 || path[1] === '' || EXIST_PATH[p] === undefined) {
    return printExistPath()
  }

  return EXIST_PATH[p](path)
}

function printExistPath() {
  return [
      'username/{username}',
      'token/{token}'
  ]
}

function existToken(path) {
    const username = path[1]
    return getUserToken(username)
}

function existUserName(path) {
    const username = path[1]
    return {
      exist: getUserToken(username) != null
    }
}

function getUserToken(username) {
  const users_token = tokenAnalyse.getUsersToken()
  let token = null
  for (const user_token of users_token) {
    if (user_token.user.preferred_username === username) {
      token = user_token 
    }
  }
  return token
}
