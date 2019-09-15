from urllib import request
from bs4 import BeautifulSoup
# res = request.urlopen(url)
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'User-Agent':useragent}
url = 'https://www.ptt.cc/bbs/index.html'
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

soup = BeautifulSoup(res.read().decode('utf-8'),'html.parser')
#print(soup)
"""
temp = soup.findAll('div',{'id':'topbar'})
print(temp[0])
print(temp[0].a.text)
print(temp[0].a['href'])
"""
title = soup.findAll('a', class_ ='board')
for href_title in title:
    print(href_title.div.text)
    print('https://www.ptt.cc'+href_title['href'])
    print()
