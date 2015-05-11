# List of words that we should disregard when getting the tweet-paragraph scores

stopWords = ["a", "able", "about", "after", "all", "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be", "but", "by", "can", "cannot", "could", "did", "do", "does", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his", "how", "i", "if", "in", "into", "is", "it", "its", "just", "least", "let", "like", "may", "me", "might", "most", "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or", "other", "our", "own", "rather", "said","say", "says", "she", "should", "since", "so", "some", "than", "that", "the","their", "them", "then", "there", "these", "they", "this", "to", "too", "twas", "us", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you", "your"]

print stopWords[0]
print len(stopWords)


# fullWords = re.findall(r'\w+', allText)
# d = defaultdict(int)
# for word in fullWords:
#     if word not in stopWords:
#         d[word] += 1
# finalFreq = sorted(d.iteritems(), key=lambda t: t[1], reverse=True)
# self.response.out.write(finalFreq)S