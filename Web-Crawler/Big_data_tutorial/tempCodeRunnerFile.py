import requests
from bs4 import BeautifulSoup

url="https://world.taobao.com/?"
res=requests.get(url)
soup=BeautifulSoup(res.text)