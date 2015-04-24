# using embedly with python
import csv
import itertools
import json
import requests
from urlparse import urljoin

# below currently works in the command line, but not sure how to translate it into this python document, run it and have it work

from embedly import Embedly

# key = 'f2f84ff5013b443ab711b204590d9aa2'

client = Embedly('f2f84ff5013b443ab711b204590d9aa2')
result = client.extract('http://www.buzzfeed.com/mjs538/i-followed-my-stolen-iphone-across-the-world-became-a-celebr')

article = {}
article["url"] = result["url"]
article["headline"] = result["title"]
article["description"] = result["description"]
article["content"] = result["content"]
# tweet["favorited"] = result.favorited
# tweet["user_mentions"] = result.entities.get('user_mentions')
# tweet["hashtags"] = result.entities.get('hashtags')
# tweet["urls"] = result.entities.get('urls')[0]['url']
# tweet["source"] = result.source

print "URL:", result["url"]
print "Headline:", result["title"]
print "Description:", result["description"]
print "Article:", result["content"]

subjects_file = open("../articles/brotherorangearticle.json", "w")
print >> json.dump(article, subjects_file, indent=4)