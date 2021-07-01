import re
from collections import Counter

text_dir='subtitle.txt'

def count_words(text):
    words = re.findall('[a-z0-9]+', text)
    wordList = Counter(words)
    return wordList

if __name__ == '__main__':
    with open(text_dir,'r') as file:
        Text=file.read()
        file.close()

        Text.lower()
        wordlist=count_words(Text)
        print(dict(wordlist.most_common(5)))








