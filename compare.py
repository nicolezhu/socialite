from __future__ import division
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
import csv
import itertools
import collections
import json
from pprint import pprint
import requests
from urlparse import urljoin

with open('articles/dressarticle.json') as data_file:
	data = json.load(data_file)

tweet = "#Thedress = \u201cperfect meme, can never be topped: (1) Putting people on 2 teams, (2)  hint of magic (3) some science.\u201d http://t.co/qVvhdvyHfM"
# tweet = "So interesting that @ftrain compares The Dress to \u201cSnow Fall\u201d: https://t.co/SfANq5nAx9 Similarly \u201cgood\u201d in terms of traffic but otherwise?"

article = data["content"].replace("<div>", "")

paragraphs = []
tweet_frequencies = []
paragraph_frequencies = []

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def create_paragraphs():
	for item in article.split("</p>"):
		if "<p>" in item:
			cleaned_paragraph = item.replace("<p>", "")
			paragraphs.append(cleaned_paragraph)
		# print cleaned_paragraph

def get_tweet_dict(tweet):
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

def compare():
	create_paragraphs()
	get_tweet_dict(tweet)

	for index, paragraph in enumerate(paragraphs):
		print paragraph
		get_paragraph_dict(paragraph)
		count = 0;
		tweet_word_length = len(tweet_frequencies[0]["tweet"].split())
		print tweet_word_length

		tweet_freq = tweet_frequencies[0]["tweet_dict"]
		paragraph_freq = paragraph_frequencies[index]["paragraph_dict"]
		for word in tweet_freq:
			if word in paragraph_freq:
				print word
				count += 1

		print count / tweet_word_length
	
	# get_paragraph_dict(paragraphs[0])
	# count = 0;
	# tweet_word_length = len(tweet_frequencies[0]["tweet"].split())
	# print tweet_word_length

	# tweet_freq = tweet_frequencies[0]["tweet_dict"]
	# paragraph_freq = paragraph_frequencies[0]["paragraph_dict"]
	# for word in tweet_freq:
	# 	if word in paragraph_freq:
	# 		print word
	# 		count += 1

	#print paragraph_frequencies

# print paragraphs[0]

# for paragraph in paragraphs:
# 	print similar(tweet, paragraph)

if __name__ == '__main__':
	compare()