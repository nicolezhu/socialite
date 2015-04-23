import collections
import json
from pprint import pprint

article = ["I’ve broken this story up into three chapters. It should never have gone this far, but the internet works in mysterious ways. None of this should have ever happened. It makes absolutely no sense at all. It’s truly crazy.", "THE STORY BEGINS in early 2014 when I was in the East Village at my favorite bar, EVS. I've said this multiple times so far, but I swear it's on St. Marks and it’s not douchey. Also don't start going there, because it’s my bar and it’s impossible to find a not-crowded bar in New York City with a good happy hour. So yeah, don't go there.", ]

for result in data:
	# paragraph_text = result['paragraph']
	cleaned_paragraph = paragraph_text.split()

	c = collections.Counter(cleaned_paragraph)

	pprint(paragraph_text)

	unique_words = list(set(cleaned_paragraph))

	paragraph = {}
	paragraph['paragraph'] = paragraph_text
	freq_dict = {}

	for word in unique_words:
		freq_dict[word] = c[word]
		print '%s : %d' % (word, c[word])

	paragraph['paragraph_dict'] = freq_dict
	print paragraph

	paragraph_frequencies.append(paragraph)

subjects_file = open("articles/brotherorangearticle.json", "w")
print >> json.dump(tweet_frequencies, subjects_file, indent=4)