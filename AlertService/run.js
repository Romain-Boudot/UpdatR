const amqp = require('amqplib/callback_api')
const wretch = require('wretch')
const sample = require('./test.json')

global.fetch = require("node-fetch")
global.FormData = require("form-data")
global.URLSearchParams = require("url").URLSearchParams

const QUEUE = "alert"

amqp.connect('amqp://guest:Romain01@app.updatr.tech', function(error0, connection) {
  if (error0) throw error0

  connection.createChannel(function(error1, channel) {

    channel.assertQueue(QUEUE, { durable: true })

    // channel.sendToQueue(queue, Buffer.from(JSON.stringify(sample)))

    channel.consume(QUEUE, msg => {
        const message = JSON.parse(msg.content.toString())
        const headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

        if (message.DiscordAlert) {
            const payload = JSON.stringify({
                content: "```md\n" + Object.keys(message.report).map(key => {
                    dep = message.report[key]
                    return `${key}   used : ${dep.packageVersion}   latest : ${dep.lastVersion}`
                }).join("\n") + "\n```"
            })
            wretch().url(message.DiscordWebHook).headers(headers).body(payload).post()
        }

        if (message.SlackAlert) {
            const payload = JSON.stringify({
                text: Object.keys(message.report).map(key => {
                    dep = message.report[key]
                    return `${key}   used : ${dep.packageVersion}   latest : ${dep.lastVersion}\n`
                }).join("\n")
            })
            wretch().url(message.SlackWebHook).headers(headers).body(payload).post()
        }

    }, {
        noAck: true
    })

  })
})