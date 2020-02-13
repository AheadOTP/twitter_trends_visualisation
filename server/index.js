const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
var fs = require('fs');

// Middleware
app.use(bodyParser.json());
app.use(cors());

app.get('/api/tweets', async function (req, res) {
  runPy(req.query.search_query).then(function(fromRunpy) {
      // wait(200).then(function() {
      //   let TweetsJson = JSON.parse(fs.readFileSync('tweets.json', 'utf8'));
      //   console.log("Hello from index.js, search_query ", req.query.search_query)
      //   res.send(TweetsJson);
      // }).catch(
      //   (reason) => {
      //     console.log('Handle rejected promise ('+reason+') here.');
      //   }
      // )
      let TweetsJson = JSON.parse(fs.readFileSync('tweets.json', 'utf8'));
      console.log("Hello from index.js, search_query ", req.query.search_query)
      res.send(TweetsJson);
  }).catch(
    (reason) => {
      console.log('Handle rejected promise ('+reason+') here.');
    }
  );
})

let runPy = function(search_query) {
  return new Promise(function(success, nosuccess) {
  console.log("runPy search_query ", search_query)
  const { spawn } = require('child_process');
  const pyprog = spawn('python3', ['get_tweets.py', search_query]);

  pyprog.stdout.on('data', function(data) {
      success(data);
  });

  pyprog.stderr.on('data', (data) => {
      nosuccess(data);
  });
})};

async function wait(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server started on port ${port}`));