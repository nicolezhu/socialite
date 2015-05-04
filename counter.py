import collections
import json
from pprint import pprint

with open('articles/brotherorange.json') as data_file:
	data = json.load(data_file)

tweet_frequencies = []

for result in data:
	tweet_text = result['tweet']
	cleaned_tweet = tweet_text.lower().split()

	# make function for cleaning tweet, finding frequency

	c = collections.Counter(cleaned_tweet)

	pprint(tweet_text)

	unique_words = list(set(cleaned_tweet))

	tweet = {}
	tweet['tweet'] = tweet_text
	freq_dict = {}

	for word in unique_words:
		# case sensitive!
		freq_dict[word] = c[word]
		print '%s : %d' % (word, c[word])

	tweet['tweet_dict'] = freq_dict
	print tweet

	tweet_frequencies.append(tweet)

subjects_file = open("articles/brotherorangedict.json", "w")
print >> json.dump(tweet_frequencies, subjects_file, indent=4)