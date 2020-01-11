const RABBIT = {
  'URL': 'amqp://localhost',
  'QUEUE': 'NEW_CONNECTION'
}
const that = this;
var amqp = require('amqplib/callback_api');
var channel = null;

function setChannel(channel) {
    that.channel = channel;
}

exports.init = function () {
  amqp.connect(RABBIT['URL'], function(error0, connection) {
    if (error0) {
      throw error0;
    }
    connection.createChannel(function(error1, channel) {
      if (error1) {
        throw error1;
      }
      setChannel(channel);
    });
  });
}

exports.sendMessageToQueue = function (msg) {
  that.channel.sendToQueue(RABBIT['QUEUE'], Buffer.from(msg));
}
