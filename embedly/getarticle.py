# using embedly with python
import json

# below currently works in the command line, but not sure how to translate it into this python document, run it and have it work

from embedly import Embedly

key = 'f2f84ff5013b443ab711b204590d9aa2'

client = Embedly(key)
search_results = client.extract('http://www.buzzfeed.com/mjs538/i-followed-my-stolen-iphone-across-the-world-became-a-celebr#.ks6v5YNoA')

# storing data in json file?
articles = []

for result in search_results:
	article = {}
	article["url"] = result.provider_url
	article["headline"] = result.title
	article["description"] = result.description
	article["content"] = result.content
	# tweet["favorited"] = result.favorited
	# tweet["user_mentions"] = result.entities.get('user_mentions')
	# tweet["hashtags"] = result.entities.get('hashtags')
	# tweet["urls"] = result.entities.get('urls')[0]['url']
	# tweet["source"] = result.source
	tweets.append(tweet)

	print "Url:", result.provider_url
	print "Headline:", result.title
	print "Dek:", result.description
	print "Article:", result.content
	# print "User Mentions:", result.entities.get('user_mentions')
	# print "Hashtags:", result.entities.get('hashtags')
	# print "URL:", result.entities.get('urls')[0]['url']
	# print "Source:", result.source

subjects_file = open("articles/brotherorangearticle.json", "w")
print >> json.dump(tweets, subjects_file, indent=4)