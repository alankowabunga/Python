'''
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

print(r.url) #查看傳送的 URL

print(r.text) #列出文字

print(r.encoding) #列出編碼

print(r.status_code) #列出 HTTP 狀態碼

print(r.headers) #列出 HTTP Response Headers

print(r.headers['Content-Type']) #印出 Header 中的 Content-Type
'''
# https://blog.gtwang.org/programming/python-requests-module-tutorial/

import requests
url="https://water.taiwanstat.com/"

web=requests.get(url)
web.encoding="utf-8"
print(web.text) #讀取並印出 text屬性

