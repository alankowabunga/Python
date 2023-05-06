import requests
from bs4 import BeautifulSoup

url="https://rate.bot.com.tw/xrt?Lang=zh-TW"
res=requests.get(url).text
soup=BeautifulSoup(res,"html.parser")

print(soup.prettify())