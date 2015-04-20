# from __future__ import absolute_import, print_function
import tweepy
import csv
import itertools
import json
import requests
from urlparse import urljoin

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="MHqDKLsyQLNra2I2nRwJhfH2S"
consumer_secret="N0DscV54WO2nVESnOQg5xT1NDpE1Q4CMn7bDUF2q3Ar7I9E0ep"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="242308086-m9enGvld76237u5H1TJmi1UXLnv4yMWNOckPjRS5"
access_token_secret="qTBgisi94bSGKBaq805b2nxzUCAo6m91xguNV4ujingro"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
# 	print tweet.text

user = api.me()
# print user.screen_name

# with open('test.csv', 'wb') as csvfile:
# 	spamwriter = csv.writer(csvfile, delimiter=' ',
# 		quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
# 	spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# saved_searches = api.saved_searches()
# for search in saved_searches:
# 	print search

# article_search = api.get_saved_search(342872172)
# print article_search

# for tweet in tweepy.Cursor(api.search,
#                            q="http://www.theatlantic.com/technology/archive/2015/01/why-i-am-not-a-maker/384767/",
#                            rpp=100,
#                            result_type="recent",
#                            include_entities=True,
#                            lang="en").items():
#     print tweet.created_at, tweet.text

search_results = tweepy.Cursor(api.search, q="http://www.buzzfeed.com/mjs538/i-followed-my-stolen-iphone-across-the-world-became-a-celebr", rpp=100, result_type="recent", include_entities=True, lang="en").items(1000)

tweets = []

for result in search_results:
	tweet = {}
	tweet["tweet"] = result.text
	tweet["user"] = result.user.screen_name
	tweet["retweeted"] = result.retweeted
	tweet["retweet_count"] = result.retweet_count
	tweet["favorited"] = result.favorited
	tweet["user_mentions"] = result.entities.get('user_mentions')
	tweet["hashtags"] = result.entities.get('hashtags')
	tweet["urls"] = result.entities.get('urls')[0]['url']
	tweet["source"] = result.source
	tweets.append(tweet)

	print "Tweet:", result.text
	print "User:", result.user.screen_name
	print "Retweeted:", result.retweeted
	print "Favorited:", result.favorited
	print "User Mentions:", result.entities.get('user_mentions')
	print "Hashtags:", result.entities.get('hashtags')
	print "URL:", result.entities.get('urls')[0]['url']
	print "Source:", result.source

subjects_file = open("articles/brotherorange.json", "w")
print >> json.dump(tweets, subjects_file, indent=4)
# If the authentication was successful, you should
# see the name of the account print out
# print(api.me().name)


# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
# api.update_status('Updating using OAuth authentication via Tweepy!')