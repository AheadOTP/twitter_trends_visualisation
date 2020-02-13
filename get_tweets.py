import tweepy 
from textblob import TextBlob 
import json
import sys

from tokens import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(sys.argv[1]+" -filter:retweets", lang='en', tweet_mode='extended', count=10)
total_list = []
tweets_for_topics = {}
my_dict = {}

for tweet in public_tweets:
	# print(tweet.full_text)
	analysis = TextBlob(tweet.full_text)
	# print(analysis.sentiment)
	# print(analysis.words)
	# print(analysis.noun_phrases)
	total_list += analysis.noun_phrases

	for word in total_list:
		if word in my_dict:
			my_dict[word][0] += 1
			my_dict[word][1].append([tweet.id,tweet.full_text])
		else:
			my_dict[word] = [1, []]
			my_dict[word][1].append([tweet.id,tweet.full_text])

sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}

json.dump(sorted_dict, open("tweets.json", "w"))
print(sorted_dict)