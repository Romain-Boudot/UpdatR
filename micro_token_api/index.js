var Keycloak = require('keycloak-connect');
var hogan = require('hogan-express');
var express = require('express');
var session = require('express-session');
global.atob = require("atob");
const tokenAnalyse = require('./tokenAnalyse')

var app = express();

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Serveur en écoute sur http://%s:%s', host, port);
});

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
  res.write(JSON.stringify(tokenAnalyse.onLogin(JSON.parse(req.session['keycloak-token']), null, 4)))
  res.end()
});

app.get('/verify/', keycloak.protect(), function (req, res) {
  res.render('index', {
    result: JSON.stringify(loginPrint(JSON.parse(req.session['keycloak-token']), null, 4)),
    event: '1. Authentication\n2. Login'
  });
});

