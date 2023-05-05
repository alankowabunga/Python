'''
HTTP 狀態代碼
可以使用「status_code」讀取網頁的回應

200	網頁正常。
301	網頁搬家，重新導向到新的網址。
400	錯誤的要求。
401	未授權，需要憑證。
403	沒有權限。
404	找不到網頁。
500	伺服器錯誤。
503	伺服器暫時無法處理請求 ( 附載過大 )。
504	伺服器沒有回應。
'''

import requests

web=requests.get("https://data.kcg.gov.tw/12345")
if web.status_code== 404:
    print("Can't find the page")