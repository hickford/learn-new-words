#!python
import nltk

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

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Find novel words in text")
    parser.add_argument('book', help="Path to utf-8 text document")
    args = parser.parse_args()

    found = set()

    text = open(args.book, encoding="utf-8").read()
    for sentence in nltk.tokenize.sent_tokenize(text):
        for word in nltk.tokenize.wordpunct_tokenize(sentence):
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
            example = next(line for line in nltk.tokenize.line_tokenize(sentence) if word in line)
            print("{0}: {1}".format(word, example))