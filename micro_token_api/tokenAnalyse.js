const func_tools = require('./tools/func_tools.js');

const USERS_TOKEN = [] // variable globale chargée de contenir les token des utilisateurs

const N_COUNTDOWN = 2000000 // countdown de validité de token

exports.onLogin = function (token) { // lors d'une connexion
  const user_token = analyseToken(token)
  setTimeout(function () {
    onTokenExpiration(user_token)
  }, N_COUNTDOWN)
  return token
}

exports.getUsersToken = function () {
  return USERS_TOKEN
}

function createNewUser(token) { // permet de créer un objet 'user' qui conserve le token ET le token decodé
  const user = parseJwt(token.access_token)
  return {
    user: user,
    token: token,
    countdown_value: 0 // cette variable permet de repousser le countdown à N_COUNTDOWN minutes
  }
}

/**
 * méthode d'analyse de token, indique si un utilisateur est déjà connecté, puis
 * ajoute ou mets à jour un token (avec les nouvelles donnnées)
 */
function analyseToken(token) {
  const user_token = createNewUser(token)
  const is_registered = hasUserRegistered(user_token)
  if (is_registered === -1) { // si l'utilisateur n'est pas en mémoire, alors...
    USERS_TOKEN.push(user_token)
  } else { // sinon le mettre à jours
    user_token.countdown_value = USERS_TOKEN[is_registered].countdown_value + 1 // nous incrementons la variable de countdown
    USERS_TOKEN[is_registered] = user_token
  }
  return user_token
}
  
function parseJwt (token) { // nous récupérons le contenu d'un token
  var base64Url = token.split('.')[1];
  var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));
  
  return JSON.parse(jsonPayload);
}
  
function hasUserRegistered(user_token) { // nous vérifions la présence ou non Token parmies ceux en mémoire
  let i = 0
  for (const token of USERS_TOKEN) {
    if (user_token.user.preferred_username === token.user.preferred_username) {
      return i
    }
    i++
  }
  return -1
}
  

function onTokenExpiration(user_token) {
  if (user_token.countdown_value > 0) { // si ce n'est pas le dernier login de cette utilisateur
    user_token.countdown_value -= 1
  } else {
    const index = func_tools.getIndexObj(USERS_TOKEN, user_token) // nous obtenons l'index de l'objet
    USERS_TOKEN.splice(index, 1) // pour le retirer
  }
}
