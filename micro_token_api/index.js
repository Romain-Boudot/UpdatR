var Keycloak = require('keycloak-connect');
var hogan = require('hogan-express');
var express = require('express');
var session = require('express-session');
global.atob = require("atob");


var app = express();

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Serveur en écoute sur http://%s:%s', host, port);
});

const USERS_TOKEN = [] // variable globale chargée de contenir les token des utilisateurs

app.get('/', function (req, res) {
  console.log(req.query)
  res.sendFile(__dirname + '/view/index.html');
});

var memoryStore = new session.MemoryStore();

app.use(session({
  secret: 'mySecret',
  resave: false,
  saveUninitialized: true,
  store: memoryStore
}));

var keycloak = new Keycloak({
  store: memoryStore
});



app.use(keycloak.middleware({
  logout: '/logout',
  admin: '/',
  protected: '/protected/resource'
}));

app.get('/auth/login', keycloak.protect(), function (req, res) {
  res.write(JSON.stringify(loginPrint(JSON.parse(req.session['keycloak-token']), null, 4)))
  res.end()
});

app.get('/verify/', keycloak.protect(), function (req, res) {
  res.render('index', {
    result: JSON.stringify(loginPrint(JSON.parse(req.session['keycloak-token']), null, 4)),
    event: '1. Authentication\n2. Login'
  });
});

function loginPrint(token) {
  const access_token = token.access_token
  analyseToken(access_token)
  return token
}

/* ici nous allons analyser le token,
 * afin de récuperer les données du token
 */

function analyseToken(access_token) {
  let user = parseJwt(access_token)
  const is_registered = hasUserRegistered(user)
  if (is_registered === -1) {
    USERS_TOKEN.push(user)
  } else {
    USERS_TOKEN[is_registered] = user
  }
}

function parseJwt (token) {
  var base64Url = token.split('.')[1];
  var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  return JSON.parse(jsonPayload);
};

function hasUserRegistered(u) {
  let i = 0
  for (const user of USERS_TOKEN) {
    if (user.preferred_username === u.preferred_username) {
      return i
    }
    i++
  }
  return -1
}
