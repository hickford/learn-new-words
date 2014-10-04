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

def is_rare(word):
    return word in dictionary and word not in commons


found = set()

for word in words():
    word = word.lower()

    if word in found:
        continue

    if is_rare(word):
        found.add(word)
        print(word)