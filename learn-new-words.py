#!python
import sys
import fileinput
import nltk

def words():
    tokenizer = nltk.tokenize.WordPunctTokenizer()
    for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
        for word in tokenizer.tokenize(line):
            yield word

dictionary = set(open('dictionary.txt').read().split())
commons = set(open('common.txt').read().split())

# lemmatizers
porter = nltk.stem.PorterStemmer()
lancaster = nltk.stem.LancasterStemmer()
snowball = nltk.stem.snowball.EnglishStemmer()
wordnet = nltk.stem.WordNetLemmatizer() # slow

def is_common(word):
    if word in commons:
        return True
    if porter.stem(word) in commons:
        return True
    if lancaster.stem(word) in commons:
        return True
    if snowball.stem(word) in commons:
        return True
    if wordnet.lemmatize(word) in commons:
        return True
    if wordnet.lemmatize(word, 'v') in commons:
        return True

found = set()

for word in words():
    if not word.isalpha():
        continue

    if not word.islower():
        continue

    if word not in dictionary:
        # probably a name
        continue

    if word in found:
        continue

    if is_common(word):
        continue

    found.add(word)
    print(word)