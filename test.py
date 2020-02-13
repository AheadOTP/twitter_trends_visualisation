import tweepy 
from textblob import TextBlob 
import json
import sys

from tokens import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = tweepy.Cursor(api.search, "christmas"+" -filter:retweets", lang='en', tweet_mode='extended', count=10).items()
public_tweets = api.search("christmas"+" -filter:retweets", lang='en', tweet_mode='extended', count=10)

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
	# print(tweet)
	for word in total_list:
		if word in my_dict:
			my_dict[word][0] += 1
			my_dict[word][1].append([tweet.id,tweet.full_text])
		else:
			my_dict[word] = [1, []]
			my_dict[word][1].append([tweet.id,tweet.full_text])



sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1][0], reverse=True)}

for topic in sorted_dict:
	# print(topic)
	list_of_tweets_for_topics = []
	for tweet in public_tweets:
		# print(word in tweet.full_text)
		# or any(word in tweet.full_text for word in topic.split())or any(word.lower() in tweet.full_text for word in topic.split())
		if (topic in tweet.full_text or topic.lower() in tweet.full_text):
			list_of_tweets_for_topics.append(tweet.full_text)
		# print(topic.split())
	tweets_for_topics[topic] = list_of_tweets_for_topics

json.dump(tweets_for_topics, open("tweets_for_topics.json", "w"))
json.dump(sorted_dict, open("tweets.json", "w"))
print(sorted_dict)