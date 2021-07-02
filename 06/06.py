import  os
import re
from collections import Counter

texts_dir='F:/homework/master/python_tutorial-master/python-practice/06/texts'

def count_words(text):
    words = re.findall('[a-z0-9]+', text)
    wordList = Counter(words)
    return wordList

if __name__ == '__main__':
    for name in os.listdir(texts_dir):
        path= texts_dir + '/' + name
        with open(path, 'r') as file:
            Text = file.read()
            file.close()

            Text.lower()
            wordlist = count_words(Text)
            print(dict(wordlist.most_common(10)),'\n')