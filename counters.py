import urllib.request
import collections

ulr = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = urllib.request.urlopen(ulr)
words = response.read().decode().split()
print(len(words))

word_counter = collections.Counter(words)

for word, count in word_counter.most_common(5):
    print(word, "-", count)

print("QUESTION", "-", word_counter["QUESTION"])
print("CIRCUMFLEX", "-", word_counter["CIRCUMFLEX"])
print("DIGIT", "-", word_counter["DIGIT"])
print("PYTHON", "-", word_counter["PYTHON"])

# With this i can get the texts from urls and throw them into a tensorflow
# model or something.