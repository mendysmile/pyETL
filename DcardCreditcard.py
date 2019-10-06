import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent
import os

def random_header():
    ua = UserAgent()
    random_header = json.loads(r'''{
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.dogforum.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent":"%s"
    }'''%ua.random)
    return random_header
########################################################
resource_path = r'./DCTRY'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

headers = {'User-Agent':str(random_header())}

url = 'https://www.dcard.tw/f/creditcard/'

req = requests.get(url,headers=headers)
soup = BeautifulSoup(req.text,'html.parser')
nalr = soup.select('div[class="PostList_entry_1rq5Lf"] a[class="PostEntry_root_V6g0rd"]')

for i in nalr:
    # print(i['href'])
    titurl = 'https://www.dcard.tw' + i['href']
    # print(titurl)
    req2 = requests.get(titurl, headers=headers)
    soup2 = BeautifulSoup(req2.text, 'html.parser')
    bookna = soup2.select('div.Post_content_NKEl9d')
    titname = soup2.select('h1[class="Post_title_2O-1el"]')
    print(titname)
    for t in titname:
        for n in bookna:
            try:
                with open(r'./DCTRY/%s.txt'%(t.text), 'a', encoding='utf-8') as f:
                    f.write(n.text+'\n')
            except:
                with open(r'./DCTRY/article%s.txt' % (len(n)), 'a', encoding='utf-8') as f:
                    f.write(n.text+'\n')
