const express = require('express')
const wretch = require('wretch')
const jwt = require('jsonwebtoken')

global.fetch = require('node-fetch')
global.FormData = require('form-data')
global.URLSearchParams = require('url').URLSearchParams

const app = express();

const JWT_SECRET = 'q58sXwg3%8JgZG^g!&A#'

app.get('/auth/callback', function(req, res) {
  wretch("https://github.com/login/oauth/access_token").json({
    client_id: "a79cafc41411d723ff50",
    client_secret: "d28491002fe5dab1da00763309e83fbd20174bb7",
    code: code
  }).post().then(res => {
    const token = jwt.sign({ username: '' }, JWT_SECRET, { expiresIn: '1d' })
    res.redirect('https://app.updatr.tech/login/' + token)
  })
})

app.get('/local/token/info/:token', function(res, req) {
  const token = req.params.token
  if (!token) {
    res.send(JSON.stringify({ valid: false }))
  }
  try {
    const token = jwt.verify(req.params.token, JWT_SECRET)
    res.send(JSON.stringify({ valid: true, username: token.username }))
  } catch(err) {
    res.send(JSON.stringify({ valid: false }))
  }
})

app.listen(3000)