const axios = require('axios'); 

const url = 'http://localhost:5000/api/tweets';

class TweetService {
    static getTweets(search_query) {
        return new Promise(async (resolve, reject) => {
            try {
              const res = await axios.get(url, {
                params: {
                  search_query: search_query
                }
              });
              const data = res.data;
              console.log("This is data from tweetservice ", data)
              resolve(
                data
              );
            } catch(err) { 
              reject(err);
            }
        })
    }
}

export default TweetService;