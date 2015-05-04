from difflib import SequenceMatcher
from bs4 import BeautifulSoup
import csv
import itertools
import json
import requests
from urlparse import urljoin

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

with open('articles/dressarticle.json') as data_file:
	data = json.load(data_file)

tweet = "So interesting that @ftrain compares The Dress to \u201cSnow Fall\u201d: https://t.co/SfANq5nAx9 Similarly \u201cgood\u201d in terms of traffic but otherwise?"

article = data["content"].replace("<div>", "")

paragraphs = []

for item in article.split("</p>"):
	if "<p>" in item:
		cleaned_paragraph = item.replace("<p>", "")
		paragraphs.append(cleaned_paragraph)
		# print cleaned_paragraph

print paragraphs[0]

for paragraph in paragraphs:
	print similar(tweet, paragraph)