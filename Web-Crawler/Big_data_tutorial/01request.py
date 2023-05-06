import requests

url="https://world.taobao.com/?"
res=requests.get(url)
print(res.text)