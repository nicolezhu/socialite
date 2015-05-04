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
result = client.extract('https://medium.com/message/yes-to-the-dress-5ec06c06aca4')

article = {}
article["url"] = result["url"]
article["headline"] = result["title"]
article["description"] = result["description"]
article["content"] = result["content"]

print "URL:", result["url"]
print "Headline:", result["title"]
print "Description:", result["description"]
print "Article:", result["content"]

subjects_file = open("../articles/dressarticle.json", "w")
print >> json.dump(article, subjects_file, indent=4)