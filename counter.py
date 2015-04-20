import collections
import json
from pprint import pprint

with open('articles/brotherorange.json') as data_file:
	data = json.load(data_file)

tweet = data[0]['tweet'].split()
c = collections.Counter(tweet)

pprint(tweet)
# print len(data)

for word in tweet:
	print '%s : %d' % (word, c[word])