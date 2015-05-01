import collections
import json
from pprint import pprint

with open('articles/brotherorangearticle.json') as data_file:
	data = json.load(data_file)

paragraphs = []

for result in data:
	article_text = result['content']
	# separate articles into paragraphs
	split_paragraphs = article_text.split('\n')
	# splits the article up into their words and frequencies, but we want paragraphs
	# cleaned_paragraph = paragraph_text.lower().split() 

	# c = collections.Counter(cleaned_paragraph)

	# pprint(paragraph_text)

	# unique_words = list(set(cleaned_paragraph))

	# paragraph = {}
	# paragraph['paragraph'] = paragraph_text
	# freq_dict = {}

	# for word in unique_words:
	# 	freq_dict[word] = c[word]
	# 	print '%s : %d' % (word, c[word])

	# paragraph['paragraph_dict'] = freq_dict
	# print paragraph

	# paragraph_frequencies.append(paragraph)

subjects_file = open("articles/brotherorangearticle.json", "w")
print >> json.dump(tweet_frequencies, subjects_file, indent=4)