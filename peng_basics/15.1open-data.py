'''網路連線, 公開資料串接'''

# import urllib.request as request
# with requst.rulopen(網址)as response:
#     data=response.read()
# print(data)


'''公開資料:以台北市政府為例'''
#確認資料格式, JSON, CSV...etc

import urllib.request as request
src="https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8")
print(data)