
#若只是想要查看特定的路徑是否存在，不分檔案或目錄，則可使用 os.path.exists：
import os

filepath = "/etc/motd" # 要檢查的檔案路徑
# 檢查路徑是否存在
if os.path.exists(filepath):
  print("路徑存在。")
else:
  print("路徑不存在。")