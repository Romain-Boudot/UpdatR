const RABBIT = {
  'URL': 'amqp://guest:Romain01@app.updatr.tech',
  'QUEUE': 'url_git'
}
const that = this;
var amqp = require('amqplib/callback_api');

function send(msg) {
  amqp.connect(RABBIT['URL'], function(error0, connection) {
    if (error0) {
      throw error0;
    }
    connection.createChannel(function(error1, channel) {
      if (error1) {
        throw error1;
      }

      channel.assertQueue(RABBIT['QUEUE'], {
        durable: false
      });

      channel.sendToQueue(RABBIT['QUEUE'], Buffer.from(msg));
      console.log(" Sent %s", 'TEST');
    });
  });
}

exports.sendMessageToQueue = function (msg) {
  send(msg);
}
