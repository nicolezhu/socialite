from __future__ import division
from bs4 import BeautifulSoup
import operator
import csv
import itertools
import collections
import json
import sys
from pprint import pprint
import requests
from urlparse import urljoin

with open('articles/dressarticle.json') as data_file:
	data = json.load(data_file)

# tweet = "Yes to The Dress: \"BuzzFeed garnered 25MM views (&amp; climbing) for its article about the dress,\" article examines why\nhttps://t.co/Nz1JUQlOuh"

# tweet = "#Thedress = \u201cperfect meme, can never be topped: (1) Putting people on 2 teams, (2)  hint of magic (3) some science.\u201d http://t.co/qVvhdvyHfM"
# tweet = "So interesting that @ftrain compares The Dress to \u201cSnow Fall\u201d: https://t.co/SfANq5nAx9 Similarly \u201cgood\u201d in terms of traffic but otherwise?"

article = data["content"].replace("<div>", "")

paragraphs = []
# tweet_frequencies = []
paragraph_frequencies = []

def create_paragraphs():
	for item in article.split("</p>"):
		if "<p>" in item:
			cleaned_paragraph = item.replace("<p>", "")
			paragraphs.append(cleaned_paragraph)
		# print cleaned_paragraph

def get_tweet_dict(tweet):
	tweet_frequencies = []
	cleaned_tweet = tweet.lower().split()
	c = collections.Counter(cleaned_tweet)

	unique_words = list(set(cleaned_tweet))

	tweet_text = {}
	tweet_text['tweet'] = tweet
	freq_dict = {}

	for word in unique_words:
		freq_dict[word] = c[word]
		# print '%s : %d' % (word, c[word])

	tweet_text['tweet_dict'] = freq_dict
	# print tweet_text

	tweet_frequencies.append(tweet_text)
	return tweet_frequencies


def get_paragraph_dict(paragraph):
	cleaned_paragraph = paragraph.lower().split()
	c = collections.Counter(cleaned_paragraph)

	unique_words = list(set(cleaned_paragraph))

	paragraph_text = {}
	paragraph_text['paragraph'] = paragraph
	freq_dict = {}

	for word in unique_words:
		freq_dict[word] = c[word]
		# print '%s : %d' % (word, c[word])

	paragraph_text['paragraph_dict'] = freq_dict
	# print paragraph_text

	paragraph_frequencies.append(paragraph_text)

def compare(tweet):
	tweet_frequencies = get_tweet_dict(tweet)

	similarity_scores = {}

	for index, paragraph in enumerate(paragraphs):
		get_paragraph_dict(paragraph)
		count = 0;
		tweet_word_length = len(tweet_frequencies[0]["tweet"].split())

		tweet_freq = tweet_frequencies[0]["tweet_dict"]
		paragraph_freq = paragraph_frequencies[index]["paragraph_dict"]
		for word in tweet_freq:
			if word in paragraph_freq:
				# print word
				count += 1

		similarity_scores[index] = (count / tweet_word_length)

	# print similarity_scores

	highest_score = max(similarity_scores.iteritems(), key=operator.itemgetter(1))[1]
	highest_score_paragraph = max(similarity_scores.iteritems(), key=operator.itemgetter(1))[0]

	print paragraphs[highest_score_paragraph], highest_score


def stop_words():
	stopWords = ["a", "able", "about", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "but", "by", "can", "cannot", "could", "did", "do", "does", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said","say", "says", "she", "should", "since", "so", "some", "than", "that", "the","their", "them", "then", "there", "these", "they", "this", "to", "too", "twas", "us", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"]

	# return similarity_scores

# for paragraph in paragraphs:
# 	print similar(tweet, paragraph)

if __name__ == '__main__':
	create_paragraphs()

	with open('articles/dresstweets.json') as data_file:
		dress_tweets = json.load(data_file)

	demo_tweets = dress_tweets["tweets"]
	tweet_len = len(demo_tweets)

	def analyze_tweet(tweet_num):
		tweet = int(tweet_num) - 1
		print demo_tweets[tweet]
		compare(demo_tweets[tweet])
		# for tweet in demo_tweets:
		# 	print tweet
		# 	compare(tweet)

	tweet_num = raw_input('Enter the number of a tweet to be analyzed: ')
	if (tweet_num > 0) and (int(tweet_num) < tweet_len):
		print ("tweet " + tweet_num)
		analyze_tweet(tweet_num)
	else:
		print ("Please enter a number between 1 and " + str(tweet_len))

	# tweet = dress_tweets["tweets"][0]
	# accessing a dictionary in a dictionary
	# print dress_tweets["tweet_dict"]["terms"]q