const express = require('express');
const mongodb = require('mongodb');

const router = express.Router();

var TweetsJson = require('../../../tweets.json');

router.get('/', (req, res) => {
  const tweets = loadTweets()
  res.send(tweets); 
});

function loadTweets () {
      return TweetsJson
    }

module.exports = router;