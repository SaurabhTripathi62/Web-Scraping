import requests
from lxml import html

url='https://www.imdb.com/chart/top?sort=us,desc&mode=simple&page=1'
path='.//td[@class="titleColumn"]/a/text()'
response=requests.get(url)
bitcode=html.fromstring(response.content)

result=bitcode.xpath(path)
rates=bitcode.xpath('.//td[@class="ratingColumn imdbRating"]/strong/text()')
print('result',result)
print('rates',rates)
final=[result,rates]
for a in zip(*final):
    print(a)


'''list_of_lists = [list_a, list_b, list_c]

for a in zip(*list_of_lists):
    print(*a)
'''



'''import requests 
from lxml import html
#import lxml.html..............we have tu use lxml.html every where
url='https://gaana.com/artist/sia'
path='/html/head/title/text()'
response=requests.get(url)
raw=response.content
bitcode=html.fromstring(raw)
source= bitcode.xpath(path)
print(source)


import requests
from lxml import html
link='https://en.wikipedia.org / wiki / Web_scraping'
path='//*[@id="p-tb"]/div/ul'
respon=requests.get(link)
raw=respon.content
sourcecode=html.fromstring(raw)
tree=sourcecode.xpath(path)
print(tree[0].text_content())

import requests 
from lxml import html 
  
# url to scrape data from 
link = 'https://en.wikipedia.org / wiki / Web_scraping'
  
# path to particular element 
path = '//*[@id ="mw-content-text"]/div / p[1]'
  
response = requests.get(link) 
byte_string = response.content 
  
# get filtered source code 
source_code = html.fromstring(byte_string) 
  
# jump to preferred html element 
tree = source_code.xpath(path) 
  
# print texts in first element in list 
print(tree[0].text_content())



from lxml import html 
import urllib
import requests
url="https://lxml.de/"
response = requests.get(url)
byte_data=response.content
sourceCode=html.fromstring(byte_data)
print(sourceCode)
inspect=sourceCode.xpath('//*[@id="introduction"]/p/text()')
print(inspect)




def sum(a):
    r=a+5
    return r
a=[1,2]
#map(fun, iter)  ,iterable (list, tuple etc.)
z=list(map(sum,a))
print(z)

l=list(map(lambda x:x+5,a))
print(l)

f=list(filter(lambda x:x%2==0,a))
print(f)

from bs4 import BeautifulSoup
import requests
import re

session = requests.Session()

sp500 = 'https://www.reuters.com/finance/markets/index/.SPX'

page = 1
regex = re.compile(r'/finance/stocks/overview/.*')
symbols = []

while True:
  print('Scraping page:', page)
  params = params={'sortBy': '', 'sortDir' :'', 'pn': page}
  html = session.get(sp500, params=params).text
  soup = BeautifulSoup(html, "html.parser")
  pagenav = soup.find(class_='pageNavigation')
  if not pagenav:
    break
  companies = pagenav.find_next('table', class_='dataTable')
  for link in companies.find_all('a', href=regex):
    symbols.append(link.get('href').split('/')[-1])
  page += 1

print(symbols)
'''
