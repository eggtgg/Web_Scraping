'''import re
a='hello minh tri hồ óc chó vcl'
k=re.findall('(?:hello{6})*',a)
print(k)
#how are you today?
#hello ae'''
import requests
from bs4 import BeautifulSoup
import csv
import json
r = requests.get('https://authoraditiagarwal.com/')
soup = BeautifulSoup(r.text, 'lxml')
y = json.dumps(soup.title.text)
with open('JSONFile.txt', 'wt') as outfile:
   json.dump(y, outfile)