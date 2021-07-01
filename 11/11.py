
filename='filtered_words.txt'
outstr='human rights'
words=[]
#load filtered_word.txt
with open(filename, 'r', encoding='utf8') as file:
    wordlist= file.readlines()
    for word in wordlist:
        word=word.strip()       #去除尾部的换行符
        words.append(word)
    print(words)

#input
iptword=input('please input something:')

#search
for word in words:
    if iptword.find(word)!=-1:
        outstr = 'freedom'
        break

print(outstr)
