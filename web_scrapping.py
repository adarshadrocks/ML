#!/usr/bin/python3
import nltk
from bs4 import BeautifulSoup
import urllib.request as urlreq
from nltk.corpus import stopwords
#reading data from url
web = urlreq.urlopen('https://php.net')
#print html tagged data
web_data=web.read()
#applying soup
souped=BeautifulSoup(web_data,'html5lib')
#library use for remove all the tags from primary page, 'html parser'
#print(souped)
#only text extraction
text_data=souped.get_text()
#print(text_data)
#tokenized=[i for i in text_data.split()]
#print(tokenized)
#stopwords.words('english')
tokenized1=[i for i in text_data.split() if i.lower() not in stopwords.words('english')]
print(len(tokenized1))
#applying frequency counter
word_count = nltk.FreqDist(tokenized1)
#dictionary
word_count.plot(15)

