from urllib import parse
from urllib import request
import requests

useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'User-Agent':useragent}
url='http://e2c87555.ngrok.io/weather'

post_data= {'location':'高雄'}
"""
res= request.urlopen(url)
post_data= {'username':'Mindy'}
data = bytes(pause.urlencode(post_data), encoding='utf-8')
req= request.Request(url=url, headers=headers, data=data)
"""

res = requests.post(url, headers=headers, data=post_data)
print(res.text)
