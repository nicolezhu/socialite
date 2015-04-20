import tweepy
import csv
import itertools
import json
import requests
from urlparse import urljoin
from flask import Flask, jsonify, request, make_response
app = Flask(__name__)
# flask json mimetype

@app.route('/tweets', methods=['GET'])
def scrape_tweets():
	consumer_key="MHqDKLsyQLNra2I2nRwJhfH2S"
	consumer_secret="N0DscV54WO2nVESnOQg5xT1NDpE1Q4CMn7bDUF2q3Ar7I9E0ep"

	access_token="242308086-m9enGvld76237u5H1TJmi1UXLnv4yMWNOckPjRS5"
	access_token_secret="qTBgisi94bSGKBaq805b2nxzUCAo6m91xguNV4ujingro"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.secure = True
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	url = request.args.get('url')
	# "http://www.newyorker.com/magazine/2015/02/23/pain-gain"
	# catch exception - pass back to client, render error in json
	# authenticate with twiter account - log into account with our tool
	# multiple keys/values

	user = api.me()

	search_results = tweepy.Cursor(api.search, q=url, rpp=100, result_type="recent", include_entities=True, lang="en").items(1000)
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

	response = make_response(json.dumps(tweets, indent=4))
	response.headers['Access-Control-Allow-Origin'] = "*"
	return response
    # return 'Hello World!'
    # return tweets

    # use ?url="something"
    # request.qwargs.url

if __name__ == '__main__':
	app.debug = True
	app.run()