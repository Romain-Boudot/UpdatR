var express = require('express');
var session = require('express-session');
const tokenAnalyse = require('./tokenAnalyse')
const apiAuth = require('./api_auth')

global.atob = require("atob");
global.fetch = require("node-fetch")
global.FormData = require("form-data")
global.URLSearchParams = require("url").URLSearchParams

var app = express();

const REDIRECTION_URL = 'https://app.updatr.tech/login/';

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Serveur en écoute sur http://%s:%s', host, port);
});

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/view/index.html');
});

var memoryStore = new session.MemoryStore();

app.use(session({
  secret: 'mySecret',
  resave: false,
  saveUninitialized: true,
  store: memoryStore
}));

// app.get('/auth/login', function (req, res) {
//   redirectToLoginRoute(res, dispathNewToken(JSON.parse(req.session['keycloak-token']), null, 4));
// });

app.get('/auth/callback', function(req, res) {
  wretch("https://github.com/login/oauth/access_token").json({
    client_id: "a79cafc41411d723ff50",
    client_secret: "d28491002fe5dab1da00763309e83fbd20174bb7",
    code: code
  }).post().then()
})

app.get('/api*', function (req, res) {
  printJson(res, apiAuth.setApi(req))
});

function redirectToLoginRoute(res, obj) {
  res.write('<script>window.location.href = "' + REDIRECTION_URL + obj.access_token + '";</script>');
  res.end();
}

function printJson(res, obj) {
  res.setHeader('Content-Type', 'application/json');
  res.write(JSON.stringify(obj))
  res.end()
}

function dispathNewToken(token) {
  tokenAnalyse.onLogin(token);
  return token;
}
