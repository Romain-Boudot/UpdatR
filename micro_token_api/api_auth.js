const tokenAnalyse = require('./tokenAnalyse')

PATH_URLS = {
    'all': getAll, // retourne tous les tokens
    'exist': existPath, // retourne true si l'information passé en paramètre existe, faux sinon
    'get': null
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
    'exist/token/{access_token}',
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
    const access_token = path[1]
    return {
      exist: getUserByAccessToken(access_token) != null
    }
}

function existUserName(path) {
    const username = path[1]
    return {
      exist: getUserByUsername(username) != null
    }
}

function getUserByUsername(username) {
  const users_token = tokenAnalyse.getUsersToken()
  let user = null
  for (const user_token of users_token) {
    if (user_token.user.preferred_username === username) {
      user = user_token
      break
    }
  }
  return user
}

function getUserByAccessToken(access_token) {
  const users_token = tokenAnalyse.getUsersToken()
  let user = null
  for (const user_token of users_token) {
    if (user_token.token.access_token === access_token) {
      user = user_token
      break
    }
  }
  return user
}
