from difflib import SequenceMatcher

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

print similar("Apple", "Mango")
print similar("Apple", "Apples")