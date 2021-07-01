#正则表达式的练习
import re
import os

html_path=''

def find_link(htmltext):
    links=re.findall('[hftps]+://([\S]+)+',htmltext)


    return links

if __name__ == '__main__':
    with open(html_path,'r') as html:
        text = html.read()
        links=find_link(text)
        for i in links:
            print(i,'\n')
